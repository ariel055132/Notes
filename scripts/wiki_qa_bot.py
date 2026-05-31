#!/usr/bin/env python3
"""Local wiki-only QA bot.

Answers are generated only from markdown files under the wiki directory.
If no relevant wiki evidence is found, the bot returns:
"cannot answer as nothing is found in wiki."
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

WIKI_SUBDIRS = ("entities", "concepts", "sources", "syntheses")
UNKNOWN_ANSWER = "cannot answer as nothing is found in wiki."

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "was",
    "we",
    "what",
    "when",
    "where",
    "which",
    "who",
    "why",
    "with",
    "you",
    "your",
}

TOKEN_RE = re.compile(r"[a-zA-Z0-9]+")
WIKILINK_WITH_LABEL_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?\|([^\]]+)\]\]")
WIKILINK_PLAIN_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?\]\]")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^\)]+\)")
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


@dataclass(frozen=True)
class Passage:
    file_path: Path
    heading: str
    text: str
    token_set: frozenset[str]
    vector: dict[str, float]
    norm: float


@dataclass(frozen=True)
class Match:
    passage: Passage
    score: float
    overlap_count: int


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def normalize_markdown(text: str) -> str:
    text = FRONTMATTER_RE.sub("", text)
    text = WIKILINK_WITH_LABEL_RE.sub(r"\2", text)
    text = WIKILINK_PLAIN_RE.sub(r"\1", text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = text.replace("`", "")
    return text


def split_passages(file_path: Path, text: str) -> list[tuple[str, str]]:
    passages: list[tuple[str, str]] = []
    heading_stack: list[str] = []
    paragraph_lines: list[str] = []

    def flush_paragraph() -> None:
        if not paragraph_lines:
            return
        paragraph = " ".join(line.strip() for line in paragraph_lines).strip()
        paragraph_lines.clear()
        if not paragraph:
            return
        heading = " > ".join(heading_stack) if heading_stack else file_path.stem
        passages.append((heading, paragraph))

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        heading_match = HEADING_RE.match(line)
        if heading_match:
            flush_paragraph()
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            if title:
                while len(heading_stack) >= level:
                    heading_stack.pop()
                heading_stack.append(title)
            continue

        if not line.strip():
            flush_paragraph()
            continue

        if line.lstrip().startswith(("-", "*", "|", ">")):
            flush_paragraph()
            cleaned = line.lstrip("-*|> ").strip()
            if cleaned:
                heading = " > ".join(heading_stack) if heading_stack else file_path.stem
                passages.append((heading, cleaned))
            continue

        paragraph_lines.append(line)

    flush_paragraph()
    return passages


def sentence_split(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


class WikiQABot:
    def __init__(self, wiki_dir: Path):
        self.wiki_dir = wiki_dir
        self.passages: list[Passage] = []
        self.idf: dict[str, float] = {}
        self._load()

    def _iter_markdown_files(self) -> list[Path]:
        files: list[Path] = []
        for subdir in WIKI_SUBDIRS:
            directory = self.wiki_dir / subdir
            if not directory.exists():
                continue
            files.extend(sorted(directory.glob("*.md")))
        return files

    def _load(self) -> None:
        raw_chunks: list[tuple[Path, str, str, list[str]]] = []
        doc_freq: dict[str, int] = {}

        for file_path in self._iter_markdown_files():
            text = file_path.read_text(encoding="utf-8")
            normalized = normalize_markdown(text)

            for heading, chunk_text in split_passages(file_path, normalized):
                tokens = [t for t in tokenize(chunk_text) if t not in STOPWORDS]
                if len(tokens) < 3:
                    continue

                token_set = set(tokens)
                for token in token_set:
                    doc_freq[token] = doc_freq.get(token, 0) + 1

                raw_chunks.append((file_path, heading, chunk_text, tokens))

        total_docs = len(raw_chunks)
        if total_docs == 0:
            return

        for token, freq in doc_freq.items():
            self.idf[token] = math.log((total_docs + 1) / (freq + 1)) + 1.0

        for file_path, heading, chunk_text, tokens in raw_chunks:
            tf: dict[str, int] = {}
            for token in tokens:
                tf[token] = tf.get(token, 0) + 1

            vec: dict[str, float] = {}
            max_tf = max(tf.values())
            for token, count in tf.items():
                idf = self.idf.get(token, 0.0)
                tf_weight = 0.5 + 0.5 * (count / max_tf)
                vec[token] = tf_weight * idf

            norm = math.sqrt(sum(v * v for v in vec.values()))
            if norm == 0:
                continue

            self.passages.append(
                Passage(
                    file_path=file_path,
                    heading=heading,
                    text=chunk_text,
                    token_set=frozenset(tf.keys()),
                    vector=vec,
                    norm=norm,
                )
            )

    def _query_vector(self, question: str) -> tuple[dict[str, float], float, set[str]]:
        tokens = [t for t in tokenize(question) if t not in STOPWORDS]
        if not tokens:
            tokens = tokenize(question)

        tf: dict[str, int] = {}
        for token in tokens:
            tf[token] = tf.get(token, 0) + 1

        if not tf:
            return {}, 0.0, set()

        max_tf = max(tf.values())
        vec: dict[str, float] = {}
        for token, count in tf.items():
            idf = self.idf.get(token, 0.0)
            tf_weight = 0.5 + 0.5 * (count / max_tf)
            vec[token] = tf_weight * idf

        norm = math.sqrt(sum(v * v for v in vec.values()))
        return vec, norm, set(tf.keys())

    def retrieve(self, question: str, top_k: int = 5) -> list[Match]:
        q_vec, q_norm, q_terms = self._query_vector(question)
        if not q_vec or q_norm == 0.0 or not q_terms:
            return []

        matches: list[Match] = []
        for passage in self.passages:
            overlap_count = len(q_terms & passage.token_set)
            if overlap_count == 0:
                continue

            dot = 0.0
            for token, q_weight in q_vec.items():
                dot += q_weight * passage.vector.get(token, 0.0)

            cosine = dot / (q_norm * passage.norm)
            overlap_ratio = overlap_count / max(len(q_terms), 1)
            score = 0.8 * cosine + 0.2 * overlap_ratio

            if score > 0:
                matches.append(Match(passage=passage, score=score, overlap_count=overlap_count))

        matches.sort(key=lambda m: (m.score, m.overlap_count), reverse=True)
        return matches[:top_k]

    def _has_evidence(self, question: str, matches: list[Match]) -> bool:
        if not matches:
            return False

        q_terms = [t for t in tokenize(question) if t not in STOPWORDS]
        term_count = len(q_terms)
        best = matches[0]

        if term_count >= 4:
            return best.overlap_count >= 2 and best.score >= 0.12
        if term_count >= 2:
            return best.overlap_count >= 1 and best.score >= 0.1
        return best.score >= 0.08

    def answer(self, question: str, top_k: int = 5) -> str:
        matches = self.retrieve(question, top_k=top_k)
        if not self._has_evidence(question, matches):
            return UNKNOWN_ANSWER

        q_terms = set(tokenize(question))
        lines: list[str] = []
        used_signatures: set[str] = set()
        evidence: list[str] = []

        for match in matches:
            sentences = sentence_split(match.passage.text)
            if not sentences:
                continue

            ranked = sorted(
                sentences,
                key=lambda s: len(q_terms & set(tokenize(s))),
                reverse=True,
            )
            best_sentence = ranked[0]
            signature = best_sentence.lower()
            if signature in used_signatures:
                continue

            used_signatures.add(signature)
            lines.append(f"- {best_sentence}")

            rel_path = match.passage.file_path.as_posix()
            evidence.append(f"- {rel_path} ({match.passage.heading})")

            if len(lines) >= 3:
                break

        if not lines:
            return UNKNOWN_ANSWER

        answer_lines = ["Answer (wiki-only):", *lines, "", "Evidence:", *evidence]
        return "\n".join(answer_lines)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ask questions against local wiki markdown pages.")
    parser.add_argument(
        "-w",
        "--wiki-dir",
        default="wiki",
        help="Path to wiki directory (default: wiki)",
    )
    parser.add_argument(
        "-q",
        "--question",
        help="Single question to answer. If omitted, starts interactive mode.",
    )
    parser.add_argument(
        "-k",
        "--top-k",
        type=int,
        default=5,
        help="Maximum retrieved passages to inspect (default: 5)",
    )
    return parser


def run_interactive(bot: WikiQABot, top_k: int) -> int:
    print("Wiki QA bot ready. Ask a question, or type 'exit' to quit.")
    while True:
        try:
            question = input("\n> ").strip()
        except EOFError:
            print()
            return 0

        if not question:
            continue
        if question.lower() in {"exit", "quit"}:
            return 0

        print(bot.answer(question, top_k=top_k))


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    wiki_dir = Path(args.wiki_dir).resolve()
    if not wiki_dir.exists() or not wiki_dir.is_dir():
        print(f"ERROR: wiki directory not found: {wiki_dir}", file=sys.stderr)
        return 1

    bot = WikiQABot(wiki_dir)
    if not bot.passages:
        print(UNKNOWN_ANSWER)
        return 0

    if args.question:
        print(bot.answer(args.question, top_k=max(1, args.top_k)))
        return 0

    return run_interactive(bot, top_k=max(1, args.top_k))


if __name__ == "__main__":
    raise SystemExit(main())