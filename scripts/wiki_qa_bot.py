#!/usr/bin/env python3
"""Offline bilingual evidence search across the wiki and explicitly allowed legacy notes.

Results are excerpts, NOT synthesized answers or verified truth. Search is lexical
(BM25, CJK bigrams and an editable synonym glossary), not arbitrary translation.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

try:
    from .rebuild_index import parse_frontmatter_text, page_status
except ImportError:
    from rebuild_index import parse_frontmatter_text, page_status

WIKI_SUBDIRS = ("entities", "concepts", "sources", "syntheses")
LEGACY_ROOTS = ("AWS", "Stock", "Container", "SystemDesign")
UNKNOWN_ANSWER = "未找到足夠相關的資料摘錄；無法據此回答。"
STOPWORDS = set("a an and are as at be by can do does for from how i in is it of on or that the this to was we what when where which who why with you your about explain please tell me should would could has have been being than into use using used".split())
CJK_STOP = {"什麼", "什么", "如何", "可以", "怎麼", "怎么", "為何", "为何", "的是", "哪些", "以及", "是否", "請問", "请问", "幫我", "帮我"}
TOKEN_RE = re.compile(r"[a-zA-Z0-9]+|[\u3400-\u9fff]+")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
EXCLUDED_HEADINGS = {"open questions", "follow-ups", "follow ups", "follow-up questions", "follow up questions", "related", "entities mentioned", "concepts mentioned", "aliases", "question / purpose", "待研究問題", "待研究问题", "待解問題", "待解问题", "後續問題", "后续问题", "待辦事項"}
PAGE_REF_RE = re.compile(r"(?:\b(?:p{1,2}\.?|pages?)\s*\d+(?:\s*[-–]\s*\d+)?|第\s*\d+(?:\s*[-–]\s*\d+)?\s*頁)", re.IGNORECASE)
NAVIGATION_RE = re.compile(r"^[-*>\s]*(?:相關主題|相关主题|相關連結|相关链接|相關筆記|related topics?|related links?|see also|navigation)\s*[:：]", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"^(?:[-*>\s]*)(?:TODO|TBD|待填|待整理|待分析|尚未整理|尚未分析|pending extraction|not yet reviewed|尚待|尚未選錄)(?:\b|[。:：]|$)", re.IGNORECASE)


@dataclass(frozen=True)
class Passage:
    file_path: Path
    heading: str
    text: str
    token_set: frozenset[str]
    body_tokens: frozenset[str]
    frequencies: dict[str, float]
    length: float
    line: int
    status: str
    collection: str
    citations: tuple[str, ...]
    page_refs: tuple[str, ...]
    source_path: str | None
    source_url: str | None
    coverage: str


@dataclass(frozen=True)
class Match:
    passage: Passage
    score: float
    overlap_count: int


def tokenize(text: str) -> list[str]:
    """Latin terms and overlapping CJK bigrams; no dictionary dependency."""
    terms = []
    for match in TOKEN_RE.finditer(unicodedata.normalize("NFKC", text).casefold()):
        token = match.group()
        if re.match(r"[a-z0-9]", token):
            if token not in STOPWORDS:
                terms.append(token)
        elif len(token) == 1:
            # Single generic Chinese characters create too many accidental matches.
            continue
        else:
            terms.extend(token[i:i + 2] for i in range(len(token) - 1) if token[i:i + 2] not in CJK_STOP)
    return terms


def normalize_markdown(text: str) -> str:
    text = WIKILINK_RE.sub(lambda match: match.group(2) or match.group(1), text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    return text.replace("`", "").strip()


def passages_with_lines(file_path: Path, text: str, offset=0):
    headings: list[tuple[int, str]] = []
    lines: list[str] = []
    start_line = 0
    fenced = False

    def flush():
        nonlocal lines
        chunk = " ".join(line.strip() for line in lines).strip()
        lines = []
        if not chunk or chunk.startswith("<!--") or any(title.casefold().strip() in EXCLUDED_HEADINGS for _, title in headings):
            return None
        without_links = MD_LINK_RE.sub("", WIKILINK_RE.sub("", chunk))
        if NAVIGATION_RE.search(chunk) or not re.search(r"[\w\u3400-\u9fff]", without_links):
            return None
        if PLACEHOLDER_RE.search(chunk) or re.fullmatch(r"[|:\s-]+", chunk):
            return None
        heading = " > ".join(title for _, title in headings) or file_path.stem
        return heading, chunk, start_line

    for number, raw in enumerate(text.splitlines(), 1 + offset):
        if raw.strip().startswith(("```", "~~~")):
            item = flush()
            if item:
                yield item
            fenced = not fenced
            continue
        if fenced:
            continue
        match = HEADING_RE.match(raw)
        if match:
            item = flush()
            if item:
                yield item
            level = len(match.group(1))
            headings = [(depth, title) for depth, title in headings if depth < level]
            headings.append((level, normalize_markdown(match.group(2))))
            continue
        if not raw.strip():
            item = flush()
            if item:
                yield item
            continue
        # Keep table rows intact, and avoid joining independent list items.
        if raw.lstrip().startswith(("- ", "* ", "|", "> ")) or re.match(r"\s*\d+\.\s", raw):
            item = flush()
            if item:
                yield item
        if not lines:
            start_line = number
        lines.append(raw)
    item = flush()
    if item:
        yield item


def split_passages(file_path: Path, text: str):
    return [(heading, text) for heading, text, _ in passages_with_lines(file_path, text)]


class WikiQABot:
    def __init__(self, wiki_dir: Path, include_legacy: bool = True, aliases_path: Path | None = None):
        self.wiki_dir = Path(wiki_dir).resolve()
        self.root = self.wiki_dir.parent
        self.include_legacy = include_legacy
        self.aliases_path = aliases_path or Path(__file__).resolve().parents[1] / "config/search-aliases.json"
        data = json.loads(self.aliases_path.read_text(encoding="utf-8")) if self.aliases_path.exists() else {"groups": {}}
        self.aliases = []
        for canonical, variants in data["groups"].items():
            for variant in variants:
                normalized = unicodedata.normalize("NFKC", variant).casefold()
                # Chinese phrases can occur within unsegmented sentences; Latin aliases need boundaries.
                pattern = re.escape(normalized)
                if re.search(r"[a-z0-9]", normalized):
                    pattern = r"(?<![a-z0-9])" + pattern + r"(?![a-z0-9])"
                self.aliases.append((re.compile(pattern), "alias:" + canonical))
        self.passages: list[Passage] = []
        self.idf: dict[str, float] = {}
        self.average_length = 1.0
        self.skipped_files: list[str] = []
        self._load()

    def _tokens(self, text: str) -> list[str]:
        normalized = unicodedata.normalize("NFKC", text).casefold()
        # Prefer the longest known phrase. "vector database" is one specific
        # concept, not an extra vote for every database-related passage.
        candidates = [(match.start(), match.end(), canonical) for pattern, canonical in self.aliases for match in pattern.finditer(normalized)]
        accepted = []
        occupied = set()
        for start, end, canonical in sorted(candidates, key=lambda item: (-(item[1] - item[0]), item[0], item[2])):
            positions = set(range(start, end))
            if occupied & positions:
                continue
            occupied.update(positions)
            accepted.append((start, end, canonical))
        remainder = list(normalized)
        for start, end, _ in accepted:
            remainder[start:end] = " " * (end - start)
        return tokenize("".join(remainder)) + [canonical for _, _, canonical in accepted]

    def _iter_markdown_files(self) -> list[Path]:
        roots = [self.wiki_dir / folder for folder in WIKI_SUBDIRS]
        if self.include_legacy:
            roots.extend(self.root / folder for folder in LEGACY_ROOTS)
        return sorted({path for root in roots for path in root.rglob("*.md") if path.is_file() and not path.is_symlink()})

    def _load(self):
        frequency: Counter = Counter()
        for file_path in self._iter_markdown_files():
            text = file_path.read_text(encoding="utf-8")
            collection = "wiki" if file_path.is_relative_to(self.wiki_dir) else "legacy"
            metadata: dict = {}
            body = text
            offset = 0
            if text.lstrip("\ufeff").startswith("---"):
                try:
                    metadata, body = parse_frontmatter_text(text)
                    # Original file line numbers, including frontmatter and the blank after it.
                    offset = len(text.splitlines()) - len(body.splitlines())
                except ValueError:
                    self.skipped_files.append(file_path.relative_to(self.root).as_posix())
                    continue
            try:
                status = page_status(metadata) if collection == "wiki" else str(metadata.get("status", "unknown"))
            except ValueError:
                self.skipped_files.append(file_path.relative_to(self.root).as_posix())
                continue
            # Draft/blocked cards are intake records, not usable evidence yet.
            if status in {"draft", "blocked"} or "<!-- REVIEW_REQUIRED -->" in body:
                continue
            title = next((line[2:].strip() for line in body.splitlines() if line.startswith("# ")), file_path.stem)
            extra = " ".join(str(item) for field in ("tags", "aliases") for item in (metadata.get(field, []) if isinstance(metadata.get(field, []), list) else [metadata[field]]))
            for heading, chunk, line in passages_with_lines(file_path, body, offset):
                excerpt = normalize_markdown(chunk)
                tokens = self._tokens(excerpt)
                if not tokens:
                    continue
                counts = Counter(tokens)
                for token in set(self._tokens(heading)):
                    counts[token] += 0.8
                for token in set(self._tokens(extra)):
                    counts[token] += 0.2
                citations = tuple(dict.fromkeys(match.group(1).strip() for match in WIKILINK_RE.finditer(chunk)))
                citations += tuple(match.group(2) for match in MD_LINK_RE.finditer(chunk) if match.group(2) not in citations)
                passage = Passage(file_path, heading, excerpt, frozenset(counts), frozenset(tokens), dict(counts), sum(counts.values()), line, status, collection, tuple(dict.fromkeys(citations)), tuple(dict.fromkeys(PAGE_REF_RE.findall(chunk))), metadata.get("source_path"), metadata.get("source_url"), str(metadata.get("coverage", metadata.get("transcript_coverage", "unknown"))))
                self.passages.append(passage)
                frequency.update(counts.keys())
        total = len(self.passages)
        if total:
            self.average_length = sum(p.length for p in self.passages) / total
            self.idf = {token: math.log(1 + (total - count + 0.5) / (count + 0.5)) for token, count in frequency.items()}

    def retrieve(self, question: str, top_k: int = 5) -> list[Match]:
        terms = set(self._tokens(question))
        if not terms or top_k < 1:
            return []
        alias_terms = {term for term in terms if term.startswith("alias:")}
        # Preserve the question's most distinctive known concept. Otherwise a
        # generic "database"/"AI" match can displace a specific vector/knowledge query.
        anchors = set()
        if alias_terms:
            rarest = max(self.idf.get(term, 0) for term in alias_terms)
            anchors = {term for term in alias_terms if self.idf.get(term, 0) >= rarest * 0.9}
        matches = []
        for passage in self.passages:
            overlap = terms & passage.token_set
            if not overlap or (anchors and not (anchors & passage.token_set)):
                continue
            # Unknown words stay in the denominator: a common word alone is weak evidence.
            coverage = len(overlap) / len(terms)
            alias_coverage = len(alias_terms & overlap) / len(alias_terms) if alias_terms else 0
            if coverage < 0.32 and alias_coverage < 0.5:
                continue
            score = 0.0
            for term in overlap:
                tf = passage.frequencies[term]
                length_penalty = 1.2 * (0.25 + 0.75 * passage.length / self.average_length)
                score += self.idf.get(term, 0) * tf * 2.2 / (tf + length_penalty) * (1.8 if term.startswith("alias:") else 1)
            body_coverage = len(terms & passage.body_tokens) / len(terms)
            score *= 0.35 + 0.65 * max(body_coverage, len(alias_terms & passage.body_tokens) / len(alias_terms) if alias_terms else 0)
            # A matching page label is useful for discovery but cannot make an
            # unrelated passage more relevant than one containing the evidence.
            if not (terms & passage.body_tokens):
                score *= 0.25
            # Short labels and fragments carry less explanatory evidence than
            # a definition. This counteracts BM25's preference for tiny chunks.
            content_length = len(tokenize(passage.text))
            score *= min(1.0, max(0.15, content_length / 14))
            if anchors:
                normalized_excerpt = unicodedata.normalize("NFKC", passage.text).casefold()
                positions = [match.start() for pattern, canonical in self.aliases if canonical in anchors for match in pattern.finditer(normalized_excerpt)]
                if positions and min(positions) <= max(20, len(normalized_excerpt) * 0.2):
                    score *= 1.3
            # Answer-choice fragments require their missing question context.
            if re.match(r"^[\s*>-]*(?:this|that|it) is (?:in)?correct\b", passage.text, re.IGNORECASE):
                score *= 0.6
            section = passage.heading.split(" > ")[-1].casefold()
            if section in {"definition", "identity", "summary", "answer / analysis", "定義", "摘要"}:
                score *= 1.8
            matches.append(Match(passage, score, len(overlap)))
        # Metadata-only hits are a fallback for finding a page by tag/alias.
        # If actual excerpt matches exist, do not mix unrelated bodies into them.
        if any(terms & match.passage.body_tokens for match in matches):
            matches = [match for match in matches if terms & match.passage.body_tokens]
        matches.sort(key=lambda match: (-match.score, match.passage.file_path.as_posix(), match.passage.line))
        # Offer different documents instead of five near-identical chunks from one page.
        selected = []
        paths = set()
        for match in matches:
            if match.passage.file_path not in paths:
                selected.append(match)
                paths.add(match.passage.file_path)
            if len(selected) >= top_k:
                break
        return selected

    def search(self, question: str, top_k: int = 5) -> dict:
        results = []
        for match in self.retrieve(question, top_k):
            p = match.passage
            results.append({"file": p.file_path.relative_to(self.root).as_posix(), "heading": p.heading, "line": p.line, "excerpt": p.text, "score": round(match.score, 4), "status": p.status, "collection": p.collection, "citations": list(p.citations), "page_refs": list(p.page_refs), "source_path": p.source_path, "source_url": p.source_url, "coverage": p.coverage})
        return {"mode": "evidence-search", "query": question, "matched": bool(results), "notice": "以下為資料摘錄，未生成答案；引用代表可追溯，不代表已驗證正確。", "results": results, "skipped_files": self.skipped_files}

    def answer(self, question: str, top_k: int = 5) -> str:
        result = self.search(question, top_k)
        if not result["matched"]:
            return UNKNOWN_ANSWER
        lines = [result["notice"], ""]
        for index, item in enumerate(result["results"], 1):
            lines.extend([f"{index}. {item['file']}:{item['line']} — {item['heading']} [{item['status']}; coverage={item['coverage']}]", f"   {item['excerpt']}"])
            if item["page_refs"]:
                lines.append("   頁碼：" + ", ".join(item["page_refs"]))
            if item["citations"]:
                lines.append("   引用：" + ", ".join(item["citations"]))
        if result["skipped_files"]:
            lines.append("略過格式錯誤的檔案：" + ", ".join(result["skipped_files"]))
        return "\n".join(lines)


def build_arg_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-w", "--wiki-dir", default="wiki")
    parser.add_argument("-q", "--question")
    parser.add_argument("-k", "--top-k", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="Emit structured evidence results; requires --question")
    parser.add_argument("--no-legacy", action="store_true", help="Search only wiki pages")
    parser.add_argument("--aliases", type=Path, help="Alternative bilingual glossary JSON")
    return parser


def run_interactive(bot, top_k):
    print("Notes evidence search — 資料摘錄模式。輸入 exit 結束。")
    while True:
        try:
            question = input("\n> ").strip()
        except EOFError:
            print()
            return 0
        if question.casefold() in {"exit", "quit"}:
            return 0
        if question:
            print(bot.answer(question, top_k))


def main():
    parser = build_arg_parser()
    args = parser.parse_args()
    wiki_dir = Path(args.wiki_dir).resolve()
    if not wiki_dir.is_dir():
        parser.error(f"wiki directory not found: {wiki_dir}")
    if args.json and args.question is None:
        parser.error("--json requires --question")
    try:
        bot = WikiQABot(wiki_dir, not args.no_legacy, args.aliases)
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.question is not None:
        result = bot.search(args.question, max(1, args.top_k)) if args.json else bot.answer(args.question, max(1, args.top_k))
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else result)
        return 0
    return run_interactive(bot, max(1, args.top_k))


if __name__ == "__main__":
    raise SystemExit(main())
