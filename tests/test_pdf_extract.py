"""Gate regressions: actual generated PDFs plus controlled extraction failures."""
from __future__ import annotations

import importlib.util
import logging
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

try:
    import pdfplumber
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    from PIL import Image
    PDF_DEPS = True
except ImportError:
    PDF_DEPS = False

spec = importlib.util.spec_from_file_location("pdf_extract", Path(__file__).parents[1] / "scripts/pdf_extract.py")
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


@unittest.skipUnless(PDF_DEPS, "PDF tests require pdfplumber, reportlab and Pillow")
class PdfExtractTests(unittest.TestCase):
    def setUp(self):
        self.directory = Path(tempfile.mkdtemp(prefix="notes-pdf-test-"))
        self.files = []

    # Fixtures intentionally remain in this named OS temporary directory.
    # Repository policy prohibits bulk/recursive cleanup; no rmtree is used.

    def pdf(self, name="source.pdf"):
        path = self.directory / name
        self.files.append(path)
        return path, canvas.Canvas(str(path))

    def test_all_pages_and_late_content_retained_source_immutable(self):
        path, output = self.pdf()
        for page in range(3):
            for row in range(36):
                output.drawString(30, 800 - row * 18, f"Page {page + 1} line {row + 1}: full evidence remains available")
            output.showPage()
        output.save()
        original = path.read_bytes()
        result = adapter.extract_pdf(path)
        self.assertEqual(result["status"], "ready")
        self.assertEqual(result["page_count"], 3)
        self.assertEqual([p["page"] for p in result["pages"]], [1, 2, 3])
        self.assertIn("line 36", result["pages"][2]["text"])
        self.assertGreater(len(result["pages"][2]["text"]), 1500)
        self.assertEqual(path.read_bytes(), original)

    def test_diagonal_label_retained_and_flagged_even_if_upright(self):
        path, output = self.pdf()
        output.drawString(30, 700, "Main evidence")
        output.saveState()
        output.translate(150, 350)
        output.rotate(45)
        output.drawString(0, 0, "LEGITIMATE DIAGRAM LABEL")
        output.restoreState()
        output.save()
        result = adapter.extract_pdf(path)
        self.assertEqual(result["status"], "needs-review")
        self.assertGreater(result["pages"][0]["metrics"]["rotated_glyphs"], 0)
        self.assertTrue(any(w.startswith("rotated-text-retained") for w in result["pages"][0]["warnings"]))
        self.assertGreater(result["pages"][0]["metrics"]["glyph_count"], len("Main evidence"))

    def test_image_only_page_blocked_and_mixed_document_review(self):
        for mixed in (False, True):
            path, output = self.pdf(f"image-{mixed}.pdf")
            output.drawImage(ImageReader(Image.new("RGB", (30, 30), "red")), 50, 50, 100, 100)
            if mixed:
                output.showPage()
                output.drawString(20, 700, "Second page has text")
            output.save()
            result = adapter.extract_pdf(path)
            self.assertEqual(result["status"], "needs-review" if mixed else "blocked")
            self.assertFalse(result["ocr_performed"])
            self.assertIn("images-not-interpreted", " ".join(result["pages"][0]["warnings"]))

    def test_table_cells_preserved_as_unverified_candidates(self):
        path, output = self.pdf()
        for x in (20, 120, 220):
            output.line(x, 600, x, 680)
        for y in (600, 640, 680):
            output.line(20, y, 220, y)
        for x, y, text in ((25, 655, "Mode"), (125, 655, "Tradeoff"), (25, 615, "Async"), (125, 615, "Staleness")):
            output.drawString(x, y, text)
        output.save()
        result = adapter.extract_pdf(path)
        self.assertEqual(result["status"], "needs-review")
        table = result["pages"][0]["tables"][0]
        self.assertEqual(table["rows"], [["Mode", "Tradeoff"], ["Async", "Staleness"]])
        self.assertFalse(table["verified"])

    def test_page_failure_does_not_discard_later_pages(self):
        path, output = self.pdf()
        output.drawString(20, 700, "First page")
        output.showPage()
        output.drawString(20, 700, "Later evidence")
        output.save()
        original = pdfplumber.page.Page.extract_text
        def fail_first(page, *args, **kwargs):
            if page.page_number == 1:
                raise ValueError("fixture failure")
            return original(page, *args, **kwargs)
        with patch.object(pdfplumber.page.Page, "extract_text", fail_first):
            result = adapter.extract_pdf(path)
        self.assertEqual(result["status"], "needs-review")
        self.assertEqual(len(result["pages"]), 2)
        self.assertIn("Later evidence", result["pages"][1]["text"])

    def test_corrupt_missing_and_encrypted_files_blocked(self):
        from pypdf import PdfWriter
        path = self.directory / "bad.pdf"
        self.files.append(path)
        path.write_bytes(b"not a pdf")
        self.assertEqual(adapter.extract_pdf(path)["status"], "blocked")
        self.assertEqual(adapter.extract_pdf(self.directory / "missing.pdf")["status"], "blocked")
        locked = self.directory / "locked.pdf"
        self.files.append(locked)
        writer = PdfWriter()
        writer.add_blank_page(300, 300)
        writer.encrypt("not-known-to-adapter")
        writer.write(locked)
        self.assertEqual(adapter.extract_pdf(locked)["status"], "blocked")

    def test_bad_mapping_blocks_whole_document_and_cjk_is_not_discarded(self):
        path, output = self.pdf()
        output.drawString(20, 700, "Readable fixture")
        output.save()
        with patch.object(pdfplumber.page.Page, "extract_text", return_value="(cid:22) \ufffd"):
            self.assertEqual(adapter.extract_pdf(path)["status"], "blocked")
        with patch.object(pdfplumber.page.Page, "extract_text", return_value="中文知識庫和⼈⼯智慧"):
            result = adapter.extract_pdf(path)
        self.assertEqual(result["status"], "needs-review")
        self.assertEqual(result["pages"][0]["text"], "中文知識庫和⼈⼯智慧")

    def test_font_bbox_log_flood_is_counted_other_logs_and_threads_survive(self):
        path, output = self.pdf()
        output.drawString(20, 700, "Evidence remains")
        output.save()
        logger = logging.getLogger("pdfminer.pdffont")
        original_filters = tuple(logger.filters)
        original_extract = pdfplumber.page.Page.extract_text
        noisy = "Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats"
        def extract_with_warnings(page, *args, **kwargs):
            for _ in range(100):
                logger.warning(noisy)
            logger.warning("Unrelated parser warning must remain visible")
            other_thread = threading.Thread(target=lambda: logger.warning(noisy))
            other_thread.start()
            other_thread.join()
            return original_extract(page, *args, **kwargs)
        with self.assertLogs(logger, level="WARNING") as captured:
            with patch.object(pdfplumber.page.Page, "extract_text", extract_with_warnings):
                result = adapter.extract_pdf(path)
            # The same warning emitted after extraction is no longer filtered.
            logger.warning(noisy)
        self.assertEqual(len(captured.records), 3)
        self.assertEqual(result["diagnostics"]["font_bbox_warning_count"], 100)
        self.assertEqual(result["status"], "needs-review")
        self.assertIn("Evidence remains", result["pages"][0]["text"])
        self.assertEqual(tuple(logger.filters), original_filters)

    def test_real_open_error_is_not_hidden_by_font_bbox_capture(self):
        path, output = self.pdf()
        output.drawString(20, 700, "Source exists")
        output.save()
        logger = logging.getLogger("pdfminer.pdffont")
        original_filters = tuple(logger.filters)
        def failed_open(*args, **kwargs):
            logger.warning("Could not get FontBBox from font descriptor because None is invalid")
            logger.error("Actual parser failure")
            raise ValueError("unreadable object")
        with self.assertLogs(logger, level="WARNING") as captured:
            with patch.object(pdfplumber, "open", failed_open):
                result = adapter.extract_pdf(path)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["diagnostics"]["font_bbox_warning_count"], 1)
        self.assertEqual([r.getMessage() for r in captured.records], ["Actual parser failure"])
        self.assertIn("pdf-open-or-read-failed: ValueError", result["warnings"])
        self.assertEqual(tuple(logger.filters), original_filters)


if __name__ == "__main__":
    unittest.main()
