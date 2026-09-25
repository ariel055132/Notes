import tempfile
import unittest
from pathlib import Path

from scripts.lint_schema import check_file, check_index, build_page_index_by_dir
from scripts.rebuild_index import load_pages, render


class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.wiki = Path(tempfile.mkdtemp(prefix="notes-schema-test-")) / "wiki"
        self.path = self.wiki / "sources/card.md"
        self.path.parent.mkdir(parents=True)
        self.metadata = '''type: source
source_path: raw/imports/stable-id/file.pdf
title: Card
author: unknown
date: unknown
tags: []
created: 2026-09-24
source_id: stable-id
source_type: pdf
source_url: https://example.com/paper
processing_status: needs-review
coverage: unknown
confidence: low
evidence_level: original-document
'''
        self.body = "# Card\n\n" + "\n\n".join("## " + name + "\n\nPending review." for name in ("Summary", "Key Claims", "Notable Quotes", "Entities Mentioned", "Concepts Mentioned", "Follow-ups"))
        self.write()

    def write(self):
        self.path.write_text("---\n" + self.metadata + "---\n" + self.body, encoding="utf-8")

    def test_new_import_metadata_accepts_unknown_coverage_and_raw_snapshot(self):
        self.assertEqual(check_file(self.path, self.wiki, {"card"}), [])

    def test_source_path_traversal_and_invalid_coverage_rejected(self):
        self.metadata = self.metadata.replace("raw/imports/stable-id/file.pdf", "raw/../secret.pdf").replace("coverage: unknown", "coverage: complete-probably")
        self.write()
        codes = {issue.code for issue in check_file(self.path, self.wiki, {"card"})}
        self.assertIn("invalid_source_path", codes)
        self.assertIn("invalid_source_metadata", codes)

    def test_index_checks_coverage_dedup_count_and_status(self):
        index = self.wiki / "index.md"
        output = render(load_pages(wiki_root=self.wiki))
        index.write_text(output, encoding="utf-8")
        by_dir = build_page_index_by_dir(self.wiki)
        self.assertEqual(check_index(index, self.wiki, by_dir), [])
        row = next(line for line in output.splitlines() if line.startswith("| [[card]]"))
        index.write_text(output.replace(row, ""), encoding="utf-8")
        self.assertIn("missing_index_page", {i.code for i in check_index(index, self.wiki, by_dir)})
        index.write_text(output.replace(row, row.replace("| 1 | needs-review |", "| 99 | ready |") + "\n" + row), encoding="utf-8")
        codes = {i.code for i in check_index(index, self.wiki, by_dir)}
        self.assertTrue({"incorrect_source_count", "incorrect_index_status", "duplicate_index_page"}.issubset(codes))


if __name__ == "__main__":
    unittest.main()
