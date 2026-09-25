#!/usr/bin/env python3
"""Import local evidence into Notes; no network, LLM, publication or source moves.

Immutable snapshots and extraction output stay local. A tracked registry and
source card carry provenance, revisions and explicit review state.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import sys
from contextlib import contextmanager
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = "<!-- REVIEW_REQUIRED -->"
STATUSES = ("draft", "needs-review", "ready", "blocked")
COVERAGES = ("unknown", "none", "partial", "full")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def scalar(value: str):
    value = value.strip()
    try:
        return json.loads(value)
    except (ValueError, TypeError):
        if value.startswith("[") and value.endswith("]"):
            return [s.strip().strip("\"'") for s in next(csv.reader([value[1:-1]], skipinitialspace=True))]
        return value.strip("\"'")


def frontmatter(text: str) -> tuple[dict, str]:
    """Read the flat metadata contract, without evaluating YAML objects."""
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        return {}, text
    fields = {}
    list_key = None
    for line in match.group(1).splitlines():
        if list_key and re.match(r"^\s+-\s+", line):
            fields[list_key].append(scalar(re.sub(r"^\s+-\s+", "", line)))
            continue
        if line.strip() and not line.lstrip().startswith("#") and ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = scalar(value)
            list_key = key.strip() if not value.strip() else None
            if list_key:
                fields[list_key] = []
    return fields, text[match.end():]


def document(fields: dict, body: str) -> str:
    return "---\n" + "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items()) + "\n---\n\n" + body.lstrip()


def canonical_url(url: str) -> str:
    if not url:
        return ""
    parts = urlsplit(url.strip())
    if parts.scheme not in ("http", "https") or not parts.netloc or parts.username or parts.password:
        raise ValueError("source URL must be an http(s) URL without credentials")
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if not k.lower().startswith("utm_") and k.lower() not in ("fbclid", "gclid")]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path or "/", urlencode(sorted(query)), ""))


def inside(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"path escapes Notes root: {relative}")
    return path


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    # This only writes our metadata; raw snapshots use exclusive creation below.
    with temporary.open("xb") as handle:
        handle.write(data)
    os.replace(temporary, path)


def snapshot(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise ValueError(f"immutable snapshot collision: {path}")
        return
    with path.open("xb") as handle:
        handle.write(data)


@contextmanager
def locked(root: Path):
    lock = inside(root, ".notes-import.lock")
    with lock.open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def registry(root: Path) -> dict:
    path = inside(root, "inbox/sources.json")
    data = json.loads(path.read_text()) if path.exists() else {"schema_version": 1, "sources": {}}
    if data.get("schema_version") != 1 or not isinstance(data.get("sources"), dict):
        raise ValueError("unsupported or malformed source registry")
    return data


def save_registry(root: Path, data: dict) -> None:
    atomic_write(inside(root, "inbox/sources.json"), (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode())


def log(root: Path, action: str, title: str, page: str, note: str) -> None:
    path = inside(root, "wiki/log.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    # Prevent source titles/notes injecting extra log sections.
    title, note = " ".join(title.split()), " ".join(note.split())
    entry = f"\n## [{dt.date.today().isoformat()}] {action} | {title}\n\n- **Action**: {note}\n- **Pages touched**: `{page}`, `inbox/sources.json`, `wiki/index.md`\n- **Notes**: Original files retained; local snapshot and provenance recorded.\n- **Open questions**: Review extraction limitations and source claims before relying on them.\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)


def refresh_index(root: Path) -> None:
    # Use the same index implementation for CLI and imports.
    import rebuild_index
    previous = (rebuild_index.ROOT, rebuild_index.WIKI_DIR, rebuild_index.INDEX_PATH)
    try:
        rebuild_index.ROOT, rebuild_index.WIKI_DIR, rebuild_index.INDEX_PATH = root, root / "wiki", root / "wiki/index.md"
        output = rebuild_index.render(rebuild_index.load_pages("name"))
        atomic_write(root / "wiki/index.md", output.encode())
    finally:
        rebuild_index.ROOT, rebuild_index.WIKI_DIR, rebuild_index.INDEX_PATH = previous


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.main_parts = [], []
        self.skip = 0
        self.main = 0
        self.title = []
        self.in_title = False
        self.url = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self.skip += 1
        if tag in ("main", "article"):
            self.main += 1
        if tag == "title":
            self.in_title = True
        if tag == "link" and attrs.get("rel") == "canonical":
            self.url = attrs.get("href", "")
        if tag in ("p", "div", "br", "li", "h1", "h2", "h3", "tr"):
            self.parts.append("\n")
            if self.main:
                self.main_parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.skip = max(0, self.skip - 1)
        if tag in ("main", "article"):
            self.main = max(0, self.main - 1)
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.skip:
            return
        if self.in_title:
            self.title.append(data)
        self.parts.append(data)
        if self.main:
            self.main_parts.append(data)


def extract(path: Path, kind: str, text: str) -> dict:
    if kind == "pdf":
        from pdf_extract import extract_pdf
        return extract_pdf(path)
    if path.suffix.lower() in (".html", ".htm"):
        parser = ArticleParser()
        parser.feed(text)
        body = re.sub(r"[ \t]+", " ", "".join(parser.main_parts or parser.parts)).strip()
        return {"status": "needs-review", "method": "html-parser", "page_count": 1, "pages": [{"page": 1, "text": body, "warnings": [], "tables": []}], "warnings": ["HTML extraction does not verify image content, complex tables or source completeness."], "title": "".join(parser.title), "source_url": parser.url}
    _, body = frontmatter(text)
    return {"status": "ready" if body.strip() else "blocked", "method": "utf8-text", "page_count": 1, "pages": [{"page": 1, "text": body, "warnings": [], "tables": []}], "warnings": [] if body.strip() else ["No text content."]}


def source_stub(title: str, extraction: dict) -> str:
    warnings = "\n".join(f"- {warning}" for warning in extraction.get("warnings", [])) or "- No machine-detected extraction warnings; semantic accuracy is unverified."
    return f"# {title}\n\n{PLACEHOLDER}\n\n## Summary\n\n尚待閱讀來源並撰寫摘要。\n\n## Key Claims\n\n尚待核對；不從檔名或擷取成功推定結論。\n\n## Notable Quotes\n\n尚未選錄；逐字引文須附頁碼或段落，翻譯另作標示。\n\n## Entities Mentioned\n\n尚未整理。\n\n## Concepts Mentioned\n\n尚未整理。\n\n## Follow-ups\n\n{warnings}\n"


def add_source(root: Path, path: Path, *, kind="auto", url="", title="", author="", published_date="", coverage=None, confidence=None, evidence_level="", source_id="", existing_page="", reextract=False) -> dict:
    root, path = root.resolve(), path.resolve()
    if coverage is not None and coverage not in COVERAGES or confidence is not None and confidence not in ("low", "medium", "high"):
        raise ValueError("invalid coverage or confidence")
    payload = path.read_bytes()
    text = "" if path.suffix.lower() == ".pdf" else payload.decode("utf-8-sig")
    upstream, _ = frontmatter(text)
    if kind == "auto":
        kind = "pdf" if path.suffix.lower() == ".pdf" else "video-report" if upstream.get("document_type") == "video-summary" or "analysis_level" in upstream else "article"
    if kind not in ("pdf", "article", "video-report"):
        raise ValueError("unsupported source type")
    extracted = extract(path, kind, text)
    source_hint = str(upstream.get("source") or "")
    url = canonical_url(url or str(upstream.get("url") or (source_hint if source_hint.startswith(("http://", "https://")) else "") or extracted.get("source_url") or ""))
    checksum = digest(payload)
    video_id = str(upstream.get("video_id") or "") if kind == "video-report" else ""
    identity = f"video:{video_id}" if video_id else url or path.as_uri()
    sid = source_id or f"{kind}-{digest(identity.encode())[:16]}"
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,95}", sid):
        raise ValueError("source ID must contain lowercase ASCII letters, digits, _ or -")
    title = title or str(upstream.get("title") or extracted.get("title") or path.stem)
    title = " ".join(title.split())
    today = dt.date.today().isoformat()
    snap = f"raw/imports/{sid}/{checksum}{path.suffix.lower() or '.txt'}"
    extraction_bytes = (json.dumps(extracted, ensure_ascii=False, indent=2) + "\n").encode()
    extraction_hash = digest(extraction_bytes)
    derived = f"derived/{sid}/{checksum}-{extraction_hash[:16]}.json"
    fields = {"type": "source", "source_id": sid, "source_type": kind, "source_path": snap, "source_url": url, "title": title, "author": author or upstream.get("author") or upstream.get("creator") or "Unknown", "date": published_date or upstream.get("published_at") or upstream.get("published") or "unknown", "published_date": published_date or upstream.get("published_at") or upstream.get("published") or None, "tags": upstream.get("tags") if isinstance(upstream.get("tags"), list) else [], "created": today, "updated": today, "processing_status": "blocked" if extracted["status"] == "blocked" else "needs-review" if extracted["status"] == "needs-review" else "draft", "coverage": coverage, "confidence": confidence, "evidence_level": "secondary-summary" if kind == "video-report" else "original-document", "extraction_path": derived, "upstream_sha256": checksum}
    fields["coverage"] = coverage or upstream.get("coverage") or "unknown"
    fields["confidence"] = confidence or upstream.get("confidence") or "low"
    fields["evidence_level"] = evidence_level or upstream.get("evidence_level") or fields["evidence_level"]
    fields["captured_at"] = upstream.get("created") or today
    if fields["coverage"] not in COVERAGES or fields["confidence"] not in ("low", "medium", "high") or fields["evidence_level"] not in ("original-document", "secondary-summary", "source-notes"):
        raise ValueError("invalid evidence metadata in source")
    if kind == "video-report":
        for key in ("video_id", "analysis_level", "transcript_coverage", "confidence", "recommendation", "recommendation_score", "quality_score"):
            if key in upstream:
                fields[key] = upstream[key]
        fields["coverage"] = upstream.get("transcript_coverage", coverage)
        # A saved report is evidence about its source, not the original transcript.
        if fields["coverage"] not in COVERAGES:
            fields["coverage"] = "unknown"
    with locked(root):
        data = registry(root)
        # Canonical URLs prevent duplicate sources even if a custom ID is supplied.
        for known_id, known in data["sources"].items():
            if (url and known.get("source_url") == url or video_id and known.get("video_id") == video_id) and known_id != sid:
                raise ValueError(f"source already registered as {known_id}; reuse that source ID")
        old = data["sources"].get(sid)
        if old and old.get("source_url") != url and not (video_id and old.get("video_id") == video_id):
            raise ValueError("source ID already belongs to a different source URL")
        if old and old["current_sha256"] == checksum and not reextract:
            last = old["versions"][-1]
            for rel, expected in ((old["source_path"], checksum), (last["extraction_path"], last["extraction_sha256"])):
                target = inside(root, rel)
                if not target.is_file() or digest(target.read_bytes()) != expected:
                    raise ValueError("registered source integrity/missing-file error; restore evidence or explicitly --reextract")
            if not inside(root, old["source_page"]).is_file():
                raise ValueError("registered source card is missing")
            return {"changed": False, **old}
        page_rel = old["source_page"] if old else existing_page or f"wiki/sources/{today}--{sid}.md"
        if not page_rel.startswith("wiki/sources/") or not page_rel.endswith(".md"):
            raise ValueError("source page must be under wiki/sources/ and end with .md")
        page = inside(root, page_rel)
        if old or existing_page:
            if not page.is_file():
                raise ValueError("existing source page does not exist")
            previous, body = frontmatter(page.read_text())
            if previous.get("type") != "source":
                raise ValueError("existing page must have type: source")
            if previous.get("source_id") and previous["source_id"] != sid:
                raise ValueError("existing page belongs to another source")
            fields = {**previous, **fields, "created": previous.get("created", today)}
            if not fields["tags"]:
                fields["tags"] = previous.get("tags", [])
            if not author and not upstream.get("author") and not upstream.get("creator"):
                fields["author"] = previous.get("author", "Unknown")
            if old:
                if not published_date and not upstream.get("published_at") and not upstream.get("published"):
                    fields["published_date"] = previous.get("published_date")
                    fields["date"] = previous.get("date", "unknown")
                if coverage is None and not upstream.get("coverage") and kind != "video-report":
                    fields["coverage"] = previous.get("coverage", "unknown")
                if confidence is None and not upstream.get("confidence"):
                    fields["confidence"] = previous.get("confidence", "low")
                if not evidence_level and not upstream.get("evidence_level"):
                    fields["evidence_level"] = previous.get("evidence_level", fields["evidence_level"])
            fields["processing_status"] = "blocked" if extracted["status"] == "blocked" else "needs-review"
        else:
            if page.exists():
                raise ValueError("refusing to overwrite an unregistered source page")
            body = source_stub(title, extracted)
        # Fail before recording a new revision if extraction did not preserve pages.
        if len(extracted.get("pages", [])) != extracted.get("page_count"):
            raise ValueError("extractor returned incomplete page accounting")
        snapshot(inside(root, snap), payload)
        # Extraction is reproducible local material; do not change a stored result.
        snapshot(inside(root, derived), extraction_bytes)
        atomic_write(page, document(fields, body).encode())
        version = {"sha256": checksum, "source_path": snap, "extraction_path": derived, "extraction_sha256": digest(extraction_bytes), "imported_at": today, "upstream_path": str(path), "processing_status": fields["processing_status"], "extraction_status": extracted["status"], "warnings": extracted.get("warnings", []), "method": extracted["method"]}
        entry = {"source_id": sid, "source_type": kind, "source_url": url, "title": title, "source_page": page_rel, "source_path": snap, "current_sha256": checksum, "processing_status": fields["processing_status"], "coverage": fields["coverage"], "confidence": fields["confidence"], "versions": [*(old or {}).get("versions", []), version]}
        if video_id:
            entry["video_id"] = video_id
        data["sources"][sid] = entry
        save_registry(root, data)
        refresh_index(root)
        log(root, "ingest", title, page_rel, f"Imported {kind}; status={fields['processing_status']}; SHA-256={checksum}.")
        return {"changed": True, **entry}


def review_source(root: Path, sid: str, status: str, note: str, acknowledge_warnings=False) -> dict:
    if status not in STATUSES or not note.strip():
        raise ValueError("review requires a valid status and a non-empty evidence/review note")
    with locked(root):
        data = registry(root)
        entry = data["sources"][sid]
        page = inside(root, entry["source_page"])
        text = page.read_text()
        fields, body = frontmatter(text)
        version = entry["versions"][-1]
        if digest(inside(root, version["source_path"]).read_bytes()) != version["sha256"]:
            raise ValueError("source snapshot integrity check failed")
        if digest(inside(root, version["extraction_path"]).read_bytes()) != version["extraction_sha256"]:
            raise ValueError("extraction integrity check failed")
        if status == "ready":
            if version.get("extraction_status") == "blocked":
                raise ValueError("blocked extraction must be reimported with usable evidence before ready")
            if PLACEHOLDER in body:
                raise ValueError("replace the source-card review placeholder before marking ready")
            if version["warnings"] and not acknowledge_warnings:
                raise ValueError("explicitly acknowledge recorded extraction warnings after review")
        fields["processing_status"] = entry["processing_status"] = version["processing_status"] = status
        fields["updated"] = dt.date.today().isoformat()
        version.setdefault("reviews", []).append({"date": fields["updated"], "status": status, "note": note, "warnings_acknowledged": bool(acknowledge_warnings)})
        atomic_write(page, document(fields, body).encode())
        save_registry(root, data)
        refresh_index(root)
        log(root, "review", entry["title"], entry["source_page"], f"Status={status}; {note}")
        return entry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add")
    add.add_argument("path", type=Path)
    add.add_argument("--kind", choices=("auto", "pdf", "article", "video-report"), default="auto")
    for option in ("url", "title", "author", "published-date", "source-id", "existing-page"):
        add.add_argument("--" + option, default="")
    add.add_argument("--coverage", choices=COVERAGES)
    add.add_argument("--confidence", choices=("low", "medium", "high"))
    add.add_argument("--evidence-level", choices=("original-document", "secondary-summary", "source-notes"), default="")
    add.add_argument("--reextract", action="store_true", help="Record a fresh extraction revision of the same immutable source")
    review = sub.add_parser("review")
    review.add_argument("source_id")
    review.add_argument("--status", required=True, choices=STATUSES)
    review.add_argument("--note", required=True)
    review.add_argument("--acknowledge-warnings", action="store_true")
    sub.add_parser("list")
    args = vars(parser.parse_args())
    root, command = args.pop("root").resolve(), args.pop("command")
    try:
        result = add_source(root, **args) if command == "add" else review_source(root, args.pop("source_id"), **args) if command == "review" else registry(root)
    except (ValueError, OSError, KeyError, ImportError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
