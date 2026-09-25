#!/usr/bin/env python3
"""Generate the catalog from every wiki page; source counts are derived citations.

The flat YAML subset used by Notes accepts scalars, inline lists and block lists.
Nested mappings and multiline scalars are intentionally rejected rather than guessed.
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
INDEX_PATH = WIKI_DIR / "index.md"
SECTIONS = {"entities": "entity", "concepts": "concept", "sources": "source", "syntheses": "synthesis"}
STATUSES = {"ready", "draft", "needs-review", "blocked", "unknown"}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class Page:
    path: Path
    category: str
    link_target: str
    updated: str
    source_count: int
    summary: str
    status: str = "needs-review"


def parse_value(value: str):
    value = value.strip()
    if value.startswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid quoted scalar: {value}") from exc
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    if value.startswith("[") and value.endswith("]"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            try:
                return ast.literal_eval(value)
            except (ValueError, SyntaxError):
                return [parse_value(part.strip()) for part in value[1:-1].split(",") if part.strip()]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value in {"true", "false"}:
        return value == "true"
    if value in {"null", "~"}:
        return None
    return re.split(r"\s+#", value, maxsplit=1)[0].strip()


def parse_frontmatter_text(text: str) -> tuple[dict, str]:
    lines = text.lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter opening '---'")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError("missing YAML frontmatter closing '---'")
    data: dict = {}
    pending_key = None
    for raw in lines[1:end]:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and pending_key:
            if data[pending_key] == "":
                data[pending_key] = []
            if not isinstance(data[pending_key], list):
                raise ValueError(f"invalid list: {raw}")
            data[pending_key].append(parse_value(stripped[2:]))
            continue
        if raw[0].isspace() or ":" not in stripped:
            raise ValueError(f"unsupported frontmatter structure: {raw}")
        key, value = stripped.split(":", 1)
        if value.strip() in {"|", ">", "|-", ">-"}:
            raise ValueError(f"multiline YAML scalar unsupported: {key}")
        if key in data:
            raise ValueError(f"duplicate frontmatter key: {key}")
        data[key] = parse_value(value)
        pending_key = key if not value.strip() else None
    return data, "\n".join(lines[end + 1 :])


def parse_frontmatter(path: Path) -> dict:
    try:
        return parse_frontmatter_text(path.read_text(encoding="utf-8"))[0]
    except ValueError as exc:
        raise ValueError(f"{path}: {exc}") from exc


def validate_date(path, key, value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"{path}: frontmatter '{key}' must be YYYY-MM-DD, got {value!r}")
    try:
        dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{path}: invalid calendar date for '{key}': {value}") from exc


def first_h1(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def summary_line(path: Path) -> str:
    _, body = parse_frontmatter_text(path.read_text(encoding="utf-8"))
    for line in body.splitlines():
        text = line.strip()
        if text and not text.startswith(("#", ">", "<!--")):
            return text.replace("|", "\\|")
    return "—"


def page_status(metadata: dict) -> str:
    status = metadata.get("processing_status", metadata.get("status", "needs-review"))
    if status not in STATUSES:
        raise ValueError(f"unsupported page status: {status!r}")
    return status


def source_lookup(wiki_root: Path) -> dict[str, set[str]]:
    """Resolve citation aliases to stable source identities, not mention frequency."""
    lookup: dict[str, set[str]] = {}
    for path in sorted((wiki_root / "sources").rglob("*.md")):
        metadata = parse_frontmatter(path)
        # Multiple cards for versions of one source count only once when source_id agrees.
        identity = str(metadata.get("source_id") or path.relative_to(wiki_root).as_posix())
        rel = path.relative_to(wiki_root).as_posix()
        keys = {path.stem, path.name, rel, rel.removesuffix(".md"), first_h1(path)}
        keys.update({"wiki/" + rel, "wiki/" + rel.removesuffix(".md")})
        aliases = metadata.get("aliases", [])
        if isinstance(aliases, list):
            keys.update(str(alias) for alias in aliases)
        for key in keys:
            lookup.setdefault(key.strip().casefold(), set()).add(identity)
    return lookup


def cited_source_ids(path: Path, wiki_root: Path, lookup: dict[str, set[str]]) -> set[str]:
    metadata, body = parse_frontmatter_text(path.read_text(encoding="utf-8"))
    if metadata.get("type") == "source":
        return {str(metadata.get("source_id") or path.relative_to(wiki_root).as_posix())}
    result: set[str] = set()
    for match in WIKILINK_RE.finditer(body):
        # An ambiguous title/alias is not proof of either source.
        identities = lookup.get(match.group(1).strip().removesuffix(".md").casefold(), set())
        if len(identities) == 1:
            result.update(identities)
    for match in MD_LINK_RE.finditer(body):
        target = unquote(match.group(1).strip().strip("<>").split("#", 1)[0])
        if re.match(r"[a-zA-Z]+://", target):
            continue
        absolute = (path.parent / target).resolve()
        try:
            key = absolute.relative_to(wiki_root.resolve()).as_posix()
        except ValueError:
            continue
        identities = lookup.get(key.casefold(), set())
        if len(identities) == 1:
            result.update(identities)
    return result


def load_pages(sort_by="name", wiki_root: Path | None = None):
    wiki_root = Path(wiki_root or WIKI_DIR)
    lookup = source_lookup(wiki_root)
    pages = []
    paths = [p for folder in SECTIONS for p in (wiki_root / folder).rglob("*.md")]
    stems: dict[str, int] = {}
    for path in paths:
        stems[path.stem.casefold()] = stems.get(path.stem.casefold(), 0) + 1
    for path in sorted(paths):
        folder = path.relative_to(wiki_root).parts[0]
        metadata = parse_frontmatter(path)
        if metadata.get("type") != SECTIONS[folder]:
            raise ValueError(f"{path}: type/path mismatch (expected {SECTIONS[folder]})")
        created = metadata.get("created", "")
        validate_date(path, "created", created)
        updated = metadata.get("updated", created)
        validate_date(path, "updated", updated)
        # Ignore manually maintained source_count; the generated value is authoritative.
        count = len(cited_source_ids(path, wiki_root, lookup))
        target = path.stem if stems[path.stem.casefold()] == 1 else path.relative_to(wiki_root).with_suffix("").as_posix()
        pages.append(Page(path, folder, target, updated, count, summary_line(path), page_status(metadata)))
    pages.sort(key=(lambda p: (p.category, p.updated, p.link_target.casefold())) if sort_by == "updated" else (lambda p: (p.category, p.link_target.casefold())))
    return pages


def table(rows):
    return ["| Page | Summary | Sources | Status | Updated |", "|------|---------|---------|--------|---------|", *[
        f"| [[{page.link_target}]] | {page.summary} | {page.source_count} | {page.status} | {page.updated} |" for page in rows
    ]]


def render(pages):
    groups = {folder: [] for folder in SECTIONS}
    for page in pages:
        groups[page.category].append(page)
    lines = ["# Wiki Index", "", "> Generated by scripts/rebuild_index.py. Sources count distinct direct source references (a source card counts itself); counts are not quality scores. Unreviewed legacy pages default to needs-review.", ""]
    for folder, rows in groups.items():
        lines.extend([f"## {folder.title()}", "", *table(rows), ""])
    last = max((page.updated for page in pages), default="—")
    lines.extend(["## Statistics", "", f"- **Total pages**: {len(pages)}", f"- **Total sources**: {len(groups['sources'])}", f"- **Last updated**: {last}", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sort-by", choices=["name", "updated"], default="name")
    parser.add_argument("--wiki-root", type=Path, default=WIKI_DIR)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.wiki_root.is_dir():
        parser.error(f"wiki root not found: {args.wiki_root}")
    index_path = args.wiki_root / "index.md"
    try:
        output = render(load_pages(args.sort_by, args.wiki_root))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.check:
        current = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
        if current != output:
            print("ERROR: wiki/index.md is out of date. Run scripts/rebuild_index.py", file=sys.stderr)
            return 1
        print("wiki/index.md is up to date.")
        return 0
    index_path.write_text(output, encoding="utf-8")
    print(f"Rebuilt {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
