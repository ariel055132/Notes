#!/usr/bin/env python3
"""Schema lint checker for LLM Wiki pages."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    from .rebuild_index import parse_frontmatter_text, load_pages, STATUSES, validate_date
except ImportError:
    from rebuild_index import parse_frontmatter_text, load_pages, STATUSES, validate_date

REQUIRED_FRONTMATTER = {
    "entity": ["type", "aliases", "tags", "created", "updated"],
    "concept": ["type", "aliases", "tags", "created", "updated"],
    "source": ["type", "source_path", "title", "author", "date", "tags", "created"],
    "synthesis": ["type", "question", "tags", "created", "updated"],
}

REQUIRED_SECTIONS = {
    "entity": [
        "## Identity",
        "## Aliases",
        "## Key Attributes",
        "## Evidence",
        "## Related",
        "## Open Questions",
    ],
    "concept": [
        "## Definition",
        "## Scope",
        "## Contrasts",
        "## Evidence",
        "## Related",
        "## Open Questions",
    ],
    "source": [
        "## Summary",
        "## Key Claims",
        "## Notable Quotes",
        "## Entities Mentioned",
        "## Concepts Mentioned",
        "## Follow-ups",
    ],
    "synthesis": [
        "## Question / Purpose",
        "## Answer / Analysis",
        "## Citations",
        "## Implications",
        "## Follow-up Questions",
    ],
}

INDEX_SECTION_TO_DIR = {
    "Entities": "entities",
    "Concepts": "concepts",
    "Sources": "sources",
    "Syntheses": "syntheses",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


@dataclass
class Issue:
    code: str
    severity: str
    file: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "severity": self.severity,
            "file": self.file,
            "message": self.message,
        }


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    try:
        return parse_frontmatter_text(text)
    except ValueError:
        return {}, text


def page_name(md_file: Path) -> str:
    return md_file.stem


def wiki_content_files(root: Path) -> list[Path]:
    allowed = {"entities", "concepts", "sources", "syntheses"}
    files = []
    for path in root.rglob("*.md"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.parts and rel.parts[0] in allowed:
            files.append(path)
    return files


def build_page_index(root: Path) -> set[str]:
    return {page_name(path) for path in wiki_content_files(root)}


def first_h1_from_body(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def build_link_target_index(root: Path) -> set[str]:
    targets: set[str] = set()
    for path in wiki_content_files(root):
        text = path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)

        targets.add(path.stem)
        targets.add(path.relative_to(root).with_suffix("").as_posix())
        targets.add("wiki/" + path.relative_to(root).with_suffix("").as_posix())

        title = first_h1_from_body(body)
        if title:
            targets.add(title)

        aliases = frontmatter.get("aliases", [])
        if isinstance(aliases, list):
            for alias in aliases:
                if isinstance(alias, str) and alias.strip():
                    targets.add(alias.strip())

    return targets


def build_page_index_by_dir(root: Path) -> dict[str, set[str]]:
    by_dir: dict[str, set[str]] = {}
    for folder in INDEX_SECTION_TO_DIR.values():
        by_dir[folder] = {target for path in (root / folder).rglob("*.md") for target in (path.stem, path.relative_to(root).with_suffix("").as_posix())}
    return by_dir


def split_markdown_row(row: str) -> list[str]:
    text = row.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]

    cells: list[str] = []
    chunk: list[str] = []
    escaped = False
    for char in text:
        if escaped:
            chunk.append(char)
            escaped = False
            continue
        if char == "\\":
            chunk.append(char)
            escaped = True
            continue
        if char == "|":
            cells.append("".join(chunk).strip())
            chunk = []
            continue
        chunk.append(char)

    cells.append("".join(chunk).strip())
    return cells


def section_table_lines(text: str, section: str) -> tuple[bool, list[str]]:
    lines = text.splitlines()
    in_section = False
    found_section = False
    table_lines: list[str] = []

    for line in lines:
        if line.startswith("## "):
            heading = line[3:].strip()
            if heading == section:
                in_section = True
                found_section = True
                continue
            if in_section:
                break

        if in_section and line.strip().startswith("|"):
            table_lines.append(line)

    return found_section, table_lines


def check_index(index_path: Path, wiki_root: Path, known_pages_by_dir: dict[str, set[str]]) -> list[Issue]:
    issues: list[Issue] = []
    rel = index_path.relative_to(wiki_root.parent).as_posix()
    if not index_path.exists():
        issues.append(Issue("missing_index", "high", rel, "Missing `wiki/index.md`."))
        return issues

    text = index_path.read_text(encoding="utf-8")
    expected_header = ["Page", "Summary", "Sources", "Status", "Updated"]
    try:
        derived_pages = load_pages("name", wiki_root)
    except ValueError as exc:
        issues.append(Issue("invalid_catalog_metadata", "high", rel, str(exc)))
        return issues
    expected_rows = {folder: {page.link_target: page for page in derived_pages if page.category == folder} for folder in INDEX_SECTION_TO_DIR.values()}

    for section, folder in INDEX_SECTION_TO_DIR.items():
        found_section, rows = section_table_lines(text, section)
        if not found_section:
            issues.append(Issue("missing_index_section", "high", rel, f"Missing `## {section}` section in index."))
            continue
        if len(rows) < 2:
            issues.append(Issue("malformed_index_table", "high", rel, f"`## {section}` must include table header and separator rows."))
            continue

        header_cells = split_markdown_row(rows[0])
        if header_cells != expected_header:
            issues.append(Issue("invalid_index_header", "high", rel, f"`## {section}` table header must be `{expected_header}`."))

        seen: set[str] = set()
        for row in rows[2:]:
            cells = split_markdown_row(row)
            if len(cells) != 5:
                issues.append(Issue("malformed_index_row", "high", rel, f"Malformed row in `## {section}` table: `{row.strip()}`"))
                continue

            page_cell = cells[0]
            match = re.fullmatch(r"\[\[([^\]|#\\]+)\]\]", page_cell)
            if not match:
                if "\\|" in page_cell or "|" in page_cell:
                    issues.append(Issue("index_alias_wikilink", "medium", rel, f"Use stem-only wikilinks in index tables (no aliases): `{page_cell}`"))
                else:
                    issues.append(Issue("invalid_index_page_cell", "high", rel, f"Page cell must be a single stem-only wikilink: `{page_cell}`"))
                continue

            target = match.group(1).strip()
            if target not in known_pages_by_dir.get(folder, set()):
                issues.append(Issue("broken_index_page_link", "medium", rel, f"Index link `[[{target}]]` in `## {section}` does not resolve to `wiki/{folder}/`."))

            if target in seen:
                issues.append(Issue("duplicate_index_page", "high", rel, f"Duplicate index entry: {target}"))
            seen.add(target)
            expected = expected_rows[folder].get(target)
            if expected is not None:
                if cells[2] != str(expected.source_count):
                    issues.append(Issue("incorrect_source_count", "high", rel, f"{target}: expected {expected.source_count} distinct direct sources, got {cells[2]}."))
                if cells[3] != expected.status:
                    issues.append(Issue("incorrect_index_status", "high", rel, f"{target}: expected status {expected.status}, got {cells[3]}."))
        for target in sorted(set(expected_rows[folder]) - seen):
            issues.append(Issue("missing_index_page", "high", rel, f"Missing catalog entry for wiki/{folder}/{target}."))

    return issues


def related_section_links(body: str) -> list[str]:
    lines = body.splitlines()
    in_related = False
    chunk: list[str] = []
    for line in lines:
        if line.startswith("## "):
            if line.strip() == "## Related":
                in_related = True
                continue
            if in_related:
                break
        if in_related:
            chunk.append(line)
    text = "\n".join(chunk)
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]


def check_file(md_file: Path, wiki_root: Path, known_link_targets: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    rel = md_file.relative_to(wiki_root.parent).as_posix()
    text = md_file.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)

    page_type = frontmatter.get("type")
    if not page_type:
        issues.append(Issue("missing_frontmatter", "high", rel, "Missing frontmatter or `type` key."))
        return issues

    if page_type not in REQUIRED_FRONTMATTER:
        issues.append(Issue("invalid_type", "high", rel, f"Unsupported type `{page_type}`."))
        return issues

    for key in REQUIRED_FRONTMATTER[page_type]:
        if key not in frontmatter:
            issues.append(Issue("missing_frontmatter_key", "high", rel, f"Missing required frontmatter key `{key}` for type `{page_type}`."))

    for section in REQUIRED_SECTIONS[page_type]:
        if section not in body:
            issues.append(Issue("missing_section", "high", rel, f"Missing required section heading `{section}` for type `{page_type}`."))

    expected_type = {"entities": "entity", "concepts": "concept", "sources": "source", "syntheses": "synthesis"}.get(md_file.relative_to(wiki_root).parts[0])
    if page_type != expected_type:
        issues.append(Issue("type_path_mismatch", "high", rel, f"Expected type {expected_type} for this folder."))
    for field in ("tags", "aliases"):
        if field in frontmatter and (not isinstance(frontmatter[field], list) or any(not isinstance(item, str) for item in frontmatter[field])):
            issues.append(Issue("invalid_list", "high", rel, f"{field} must be a list of strings."))
    for field in ("created", "updated"):
        if field in frontmatter:
            try:
                validate_date(md_file, field, frontmatter[field])
            except ValueError as exc:
                issues.append(Issue("invalid_date", "high", rel, str(exc)))
    for field in ("status", "processing_status"):
        if field in frontmatter and frontmatter[field] not in STATUSES:
            issues.append(Issue("invalid_processing_status", "high", rel, f"{field} must be one of {sorted(STATUSES)}."))

    if page_type == "source":
        source_path = str(frontmatter.get("source_path", ""))
        parts = Path(source_path).parts
        if not parts or parts[0] != "raw" or len(parts) < 2 or ".." in parts or Path(source_path).is_absolute():
            issues.append(Issue("invalid_source_path", "high", rel, "source_path must be a relative path inside raw/ without traversal."))
        metadata_enums = {
            "source_type": {"pdf", "article", "video-report", "video_report", "web", "note", "document"},
            "coverage": {"none", "partial", "full", "unknown"},
            "confidence": {"low", "medium", "high", "unknown"},
            "evidence_level": {"original-document", "secondary-summary", "source-notes"},
            "analysis_level": {"quick-screen", "full-transcript"},
            "transcript_coverage": {"none", "partial", "full", "unknown"},
        }
        for key, accepted in metadata_enums.items():
            if key in frontmatter and frontmatter[key] not in accepted:
                issues.append(Issue("invalid_source_metadata", "high", rel, f"{key} must be one of {sorted(accepted)}."))
        for key in ("source_id", "source_type", "processing_status"):
            if "source_id" in frontmatter and not frontmatter.get(key):
                issues.append(Issue("missing_source_metadata", "high", rel, f"Registered sources require {key}."))
        source_url = frontmatter.get("source_url")
        if source_url and (not isinstance(source_url, str) or urlparse(source_url).scheme not in {"http", "https"} or not urlparse(source_url).netloc):
            issues.append(Issue("invalid_source_url", "high", rel, "source_url must be HTTP(S) or empty when unknown."))

    if "## Related" in body:
        links = related_section_links(body)
        if not links:
            issues.append(Issue("missing_related_links", "medium", rel, "`## Related` section has no wikilinks."))
        else:
            for link in links:
                if link not in known_link_targets:
                    issues.append(Issue("broken_related_link", "medium", rel, f"Related link `[[{link}]]` does not resolve to an existing page."))
    elif page_type in {"entity", "concept"}:
        issues.append(Issue("missing_related_links", "medium", rel, "Page requires a `## Related` section with at least one wikilink."))

    return issues


def lint_wiki(wiki_root: Path) -> dict[str, Any]:
    files = wiki_content_files(wiki_root)
    known_link_targets = build_link_target_index(wiki_root)
    known_pages_by_dir = build_page_index_by_dir(wiki_root)
    issues: list[Issue] = []

    for md_file in sorted(files):
        issues.extend(check_file(md_file, wiki_root, known_link_targets))

    issues.extend(check_index(wiki_root / "index.md", wiki_root, known_pages_by_dir))

    summary = {
        "files_scanned": len(files) + 1,
        "issues_total": len(issues),
        "high": sum(i.severity == "high" for i in issues),
        "medium": sum(i.severity == "medium" for i in issues),
        "low": sum(i.severity == "low" for i in issues),
    }

    return {"summary": summary, "issues": [i.to_dict() for i in issues]}


def print_human_report(result: dict[str, Any]) -> None:
    summary = result["summary"]
    print("Schema Lint Report")
    print("=" * 18)
    print(f"Files scanned: {summary['files_scanned']}")
    print(f"Total issues: {summary['issues_total']} (high={summary['high']}, medium={summary['medium']}, low={summary['low']})")
    print()

    if not result["issues"]:
        print("No schema issues found.")
        return

    by_file: dict[str, list[dict[str, str]]] = {}
    for issue in result["issues"]:
        by_file.setdefault(issue["file"], []).append(issue)

    for file, file_issues in by_file.items():
        print(f"- {file}")
        for issue in file_issues:
            print(f"  [{issue['severity'].upper()}] {issue['code']}: {issue['message']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate wiki schema and produce lint reports.")
    parser.add_argument("--wiki-root", default="wiki", help="Path to wiki root directory (default: wiki)")
    parser.add_argument("--json-out", help="Write machine-readable JSON report to this path")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when any issue is found")
    args = parser.parse_args()

    wiki_root = Path(args.wiki_root)
    if not wiki_root.exists() or not wiki_root.is_dir():
        print(f"wiki root not found: {wiki_root}")
        return 2

    result = lint_wiki(wiki_root)
    print_human_report(result)

    if args.json_out:
        out = Path(args.json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    if args.strict and result["summary"]["issues_total"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())