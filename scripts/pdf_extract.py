#!/usr/bin/env python3
"""Conservative, page-addressable PDF evidence extraction (no file writes).

Requires pdfplumber. `ready` means that this text-layer pass found no review
triggers, not that the document's meaning or visual completeness was verified.
Images are not OCR'd; table candidates are not verified; rotated text is retained.
The caller must keep full extraction JSON in an ignored derived directory.
"""
from __future__ import annotations

import math
import logging
import re
import threading
import unicodedata
from contextlib import contextmanager
from pathlib import Path
from typing import Any


class _FontBBoxWarningCounter(logging.Filter):
    """Capture one noisy parser warning for this extraction thread only."""

    def __init__(self):
        super().__init__()
        self.thread_id = threading.get_ident()
        self.count = 0

    def filter(self, record: logging.LogRecord) -> bool:
        if (
            record.thread == self.thread_id
            and record.levelno == logging.WARNING
            and record.getMessage().startswith("Could not get FontBBox from font descriptor because ")
        ):
            self.count += 1
            return False
        return True


@contextmanager
def _capture_font_bbox_warnings(result: dict[str, Any]):
    # Do not disable logging or change logger levels/handlers/propagation. The
    # filter affects only this known warning in the calling thread, and is
    # removed even when opening or parsing the PDF raises an exception.
    logger = logging.getLogger("pdfminer.pdffont")
    counter = _FontBBoxWarningCounter()
    logger.addFilter(counter)
    try:
        yield
    finally:
        logger.removeFilter(counter)
        if counter.count:
            result.setdefault("diagnostics", {})["font_bbox_warning_count"] = counter.count
            result["warnings"].append(
                f"font-bbox-warning: {counter.count} repeated parser warnings captured; "
                "font geometry requires review"
            )


def _text_warnings(text: str) -> list[str]:
    warnings = []
    if not text.strip():
        warnings.append("no-text-extracted: inspect page; OCR may be required")
    if re.search(r"\(cid:\d+\)|\ufffd|\x00", text):
        warnings.append("encoding-anomaly: unresolved/replacement characters")
    private = sum(unicodedata.category(c) == "Co" for c in text)
    if private:
        warnings.append("encoding-anomaly: private-use characters need verification")
    if len(re.findall(r"(?:\b[A-Za-z]\b\s+){8,}", text)) >= 2:
        warnings.append("possible-font-map-or-spaced-letter-layout: inspect original")
    # PDF fonts sometimes map common Chinese characters to visually identical
    # radicals. Preserve exact extracted text; search may separately normalize.
    if any("\u2e80" <= c <= "\u2fdf" for c in text):
        warnings.append("cjk-radical-codepoints: normalize only in search, retain evidence")
    return warnings


def _rotated_char(char: dict[str, Any]) -> bool:
    matrix = char.get("matrix")
    if matrix and len(matrix) >= 4:
        # pdfminer upright=True also covers diagonal glyphs; do not rely on it.
        angle = math.degrees(math.atan2(float(matrix[1]), float(matrix[0])))
        return abs(angle) > 0.5
    return not char.get("upright", True)


def extract_pdf(path: Path) -> dict[str, Any]:
    """Return all page text, table candidates, diagnostics and an ingestion gate.

    Status is blocked for an unreadable file, no extractable text anywhere, or
    encoding anomalies on every nonempty page; needs-review for any page warning.
    Neither page count nor character count is a measure of semantic accuracy.
    No source is edited, no text is truncated, and no network/API is used.
    """
    result: dict[str, Any] = {
        "status": "blocked", "pages": [], "warnings": [], "page_count": 0,
        "method": "pdfplumber-text-layer-and-line-table-candidates-v1",
        "coverage": "text-layer-only; visual relationships and OCR not verified",
        "ocr_performed": False,
    }
    try:
        import pdfplumber
    except ImportError:
        result["warnings"] = ["dependency-missing: install pdfplumber to extract PDFs"]
        return result
    result["extractor_version"] = pdfplumber.__version__
    if not Path(path).is_file():
        result["warnings"] = ["source-missing-or-not-a-file"]
        return result
    try:
        with _capture_font_bbox_warnings(result), pdfplumber.open(path) as document:
            result["page_count"] = len(document.pages)
            for number, page in enumerate(document.pages, 1):
                entry: dict[str, Any] = {
                    "page": number, "text": "", "warnings": [], "tables": [],
                }
                # Keep page failures isolated so later evidence isn't discarded.
                try:
                    entry["text"] = page.extract_text(x_tolerance=2, y_tolerance=3) or ""
                    entry["warnings"].extend(_text_warnings(entry["text"]))
                    chars = page.chars
                    rotated = sum(_rotated_char(char) for char in chars)
                    images = len(page.images)
                    vectors = len(page.lines) + len(page.curves)
                    rects = len(page.rects)
                    entry["metrics"] = {
                        "extracted_characters": len(entry["text"]),
                        "glyph_count": len(chars), "rotated_glyphs": rotated,
                        "image_count": images, "line_curve_count": vectors,
                        "rectangle_count": rects,
                        "width": float(page.width), "height": float(page.height),
                    }
                    if rotated:
                        entry["warnings"].append(
                            "rotated-text-retained: possible watermark/diagram labels; reading order unverified"
                        )
                    if images:
                        entry["warnings"].append(
                            "images-not-interpreted: text inside images and relationships require page review"
                        )
                    if vectors or rects:
                        entry["warnings"].append(
                            "vector-layout-unverified: rules/shapes may be tables or diagrams"
                        )
                    try:
                        for table in page.find_tables():
                            entry["tables"].append({
                                "bbox": [float(v) for v in table.bbox],
                                "rows": table.extract(),
                                "method": "pdfplumber-default-line-strategy",
                                "verified": False,
                            })
                    except Exception as exc:
                        entry["warnings"].append(f"table-extraction-failed: {type(exc).__name__}")
                    if entry["tables"]:
                        entry["warnings"].append(
                            "table-candidates-unverified: merged cells, column order and meaning require review"
                        )
                except Exception as exc:
                    entry["warnings"].append(f"page-extraction-failed: {type(exc).__name__}")
                result["pages"].append(entry)
    except Exception as exc:
        result["warnings"].append(f"pdf-open-or-read-failed: {type(exc).__name__}")
        return result
    nonempty = [p for p in result["pages"] if p["text"].strip()]
    if not nonempty:
        result["warnings"].append("no-extractable-document-text: OCR or alternate source required")
    elif all(any(w.startswith("encoding-anomaly") for w in p["warnings"]) for p in nonempty):
        result["warnings"].append("document-encoding-unreliable: alternate extraction required")
    elif result["warnings"] or any(p["warnings"] for p in result["pages"]):
        result["status"] = "needs-review"
        result["warnings"].append("page-review-required: see document and per-page warnings before synthesis")
    else:
        result["status"] = "ready"
    return result
