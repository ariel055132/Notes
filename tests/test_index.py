import tempfile
import unittest
from pathlib import Path

from scripts.rebuild_index import load_pages, parse_frontmatter_text, render


def make_page(root, relative, kind, body, metadata=""):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\ntype: {kind}\ntags: []\ncreated: 2026-09-24\n{metadata}---\n# {path.stem}\n\n{body}\n", encoding="utf-8")
    return path


class IndexTests(unittest.TestCase):
    def setUp(self):
        # Intentionally retained: project policy prohibits recursive fixture cleanup.
        self.root = Path(tempfile.mkdtemp(prefix="notes-index-test-")) / "wiki"
        self.root.mkdir()

    def test_all_pages_including_nested_and_duplicate_stems_are_catalogued_once(self):
        make_page(self.root, "concepts/topic.md", "concept", "First definition.")
        make_page(self.root, "concepts/nested/topic.md", "concept", "Second definition.")
        make_page(self.root, "syntheses/new.md", "synthesis", "Analysis.")
        pages = load_pages(wiki_root=self.root)
        self.assertEqual(len(pages), 3)
        self.assertEqual({p.link_target for p in pages}, {"concepts/topic", "concepts/nested/topic", "new"})
        rendered = render(pages)
        for p in pages:
            self.assertEqual(rendered.count(f"[[{p.link_target}]]"), 1)

    def test_distinct_source_references_ignore_manual_counts_and_deduplicate_versions(self):
        make_page(self.root, "sources/a.md", "source", "Source", 'source_id: stable-a\naliases: ["Source A"]\n')
        make_page(self.root, "sources/a-v2.md", "source", "New source snapshot", "source_id: stable-a\n")
        make_page(self.root, "sources/b.md", "source", "Another source")
        make_page(self.root, "concepts/topic.md", "concept", "[[a]] [[a|again]] [[Source A]] [[a-v2]] [b](../sources/b.md#page-1) [[missing]]", "source_count: 99\n")
        pages = {p.link_target: p for p in load_pages(wiki_root=self.root)}
        self.assertEqual(pages["topic"].source_count, 2)
        self.assertEqual(pages["a"].source_count, 1)
        self.assertIn("source_count: 99", (self.root / "concepts/topic.md").read_text())

    def test_status_is_not_assumed_ready_and_processing_status_wins(self):
        make_page(self.root, "sources/a.md", "source", "Source")
        make_page(self.root, "sources/b.md", "source", "Source", "status: ready\nprocessing_status: blocked\n")
        pages = {p.link_target: p for p in load_pages(wiki_root=self.root)}
        self.assertEqual(pages["a"].status, "needs-review")
        self.assertEqual(pages["b"].status, "blocked")

    def test_yaml_quotes_block_lists_and_calendar_validation(self):
        metadata, body = parse_frontmatter_text('---\ntitle: "A, B: \\"title\\""\naliases:\n  - 中文\n  - "two words"\n---\n# Title\n'.replace('\\\\"', '\\"'))
        self.assertEqual(metadata["aliases"], ["中文", "two words"])
        self.assertIn("# Title", body)
        make_page(self.root, "sources/a.md", "source", "Source", "updated: 2026-02-30\n")
        with self.assertRaisesRegex(ValueError, "calendar"):
            load_pages(wiki_root=self.root)


if __name__ == "__main__":
    unittest.main()
