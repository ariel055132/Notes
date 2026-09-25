import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_qa_bot import UNKNOWN_ANSWER, WikiQABot

ROOT = Path(__file__).resolve().parents[1]


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="notes-search-test-"))
        self.wiki = self.root / "wiki"
        self.wiki.mkdir()
        self.write("wiki/concepts/caching.md", '# Caching\n\n## Definition\n\nCaching retains frequently accessed data to reduce database load. Cache invalidation removes stale entries. (p. 4) [[source-a]]\n\n## Open Questions\n\nCould phoenix crystal protocol solve this?\n', 'aliases: ["快取"]\ntags: [performance]\n')
        self.write("wiki/syntheses/learning.md", '# Learning Workflow\n\n## Answer / Analysis\n\nAI assists learning by connecting source evidence in a knowledge management workflow.\n', 'aliases: ["AI 輔助學習與知識管理"]\ntags: [knowledge-management]\n')
        self.write("wiki/sources/questions.md", '# Unresolved\n\n## Follow-ups\n\nBuild a phoenix crystal protocol summary next.\n')
        self.write("AWS/Notes/permissions.md", '# 權限設計\n\n服務角色採用最小權限原則，以降低非必要的資料存取。\n', frontmatter=False)
        self.write("private/secret.md", '# Secret\n\nVelvet banana spaceship.\n', frontmatter=False)

    def write(self, rel, body, metadata="", frontmatter=True):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        prefix = f"---\ntype: concept\ncreated: 2026-09-24\n{metadata}---\n" if frontmatter else ""
        path.write_text(prefix + body, encoding="utf-8")
        return path

    def test_english_traditional_simplified_and_mixed_queries_find_english_evidence(self):
        bot = WikiQABot(self.wiki)
        for query in ("cache invalidation", "快取失效", "缓存失效", "快取 invalidation"):
            with self.subTest(query=query):
                results = bot.search(query)["results"]
                self.assertTrue(results)
                self.assertEqual(results[0]["file"], "wiki/concepts/caching.md")
                self.assertIn("Cache invalidation", results[0]["excerpt"])

    def test_aliases_tags_and_chinese_text_are_searchable(self):
        bot = WikiQABot(self.wiki)
        self.assertEqual(bot.search("AI 輔助學習與知識管理")["results"][0]["file"], "wiki/syntheses/learning.md")
        self.assertEqual(bot.search("最小權限")["results"][0]["collection"], "legacy")
        self.assertTrue(bot.search("performance")["matched"])

    def test_no_evidence_and_open_questions_do_not_become_answers(self):
        bot = WikiQABot(self.wiki)
        for query in ("phoenix crystal protocol", "velvet banana spaceship", "量子海豚", "", "the and what"):
            with self.subTest(query=query):
                self.assertFalse(bot.search(query)["matched"])
                self.assertEqual(bot.answer(query), UNKNOWN_ANSWER)

    def test_draft_blocked_placeholder_and_code_are_not_evidence(self):
        self.write("wiki/sources/draft.md", "# Draft\n\nA dragonfruit protocol exists.\n", "processing_status: draft\n")
        self.write("wiki/sources/blocked.md", "# Blocked\n\nA dragonfruit protocol exists.\n", "processing_status: blocked\n")
        self.write("wiki/sources/todo.md", "# Intake\n\nTODO: dragonfruit protocol summary\n\n```\ndragonfruit protocol\n```\n")
        self.write("wiki/sources/review.md", "# Dragonfruit Protocol\n\n<!-- REVIEW_REQUIRED -->\n\n## Summary\n\n尚待閱讀來源並撰寫摘要。\n", "processing_status: needs-review\n")
        self.assertFalse(WikiQABot(self.wiki).search("dragonfruit protocol")["matched"])

    def test_evidence_locations_citations_and_legacy_opt_out(self):
        bot = WikiQABot(self.wiki)
        result = bot.search("快取失效")["results"][0]
        self.assertEqual(result["citations"], ["source-a"])
        self.assertEqual(result["page_refs"], ["p. 4"])
        original_line = (self.root / result["file"]).read_text().splitlines()[result["line"] - 1]
        self.assertIn("Caching retains", original_line)
        self.assertEqual(result["status"], "needs-review")
        self.assertFalse(WikiQABot(self.wiki, include_legacy=False).search("最小權限")["matched"])

    def test_navigation_and_link_only_fragments_are_not_evidence(self):
        self.write("wiki/sources/navigation.md", "# Navigation\n\n相關主題：AI 輔助學習與知識管理。\n\n[[learning|AI 輔助學習與知識管理]]\n")
        results = WikiQABot(self.wiki).search("AI 輔助學習與知識管理")["results"]
        self.assertTrue(results)
        self.assertFalse(any(item["file"].endswith("navigation.md") for item in results))

    def test_specific_compound_concept_beats_generic_database_and_metadata_match(self):
        self.write("wiki/concepts/vector.md", "# Vector Database\n\n## Definition\n\nA vector database stores embeddings for semantic similarity search and retrieval across text, images, and documents.\n")
        self.write("wiki/sources/generic.md", "# Knowledge Base\n\n## Summary\n\nDatabase encryption protects all stored data and limits unauthorized access.\n", 'aliases: ["知識庫", "database"]\n')
        result = WikiQABot(self.wiki).search("知識庫一定要向量資料庫嗎")["results"]
        self.assertEqual(result[0]["file"], "wiki/concepts/vector.md")
        self.assertFalse(any(item["file"].endswith("generic.md") for item in result))

    def test_specific_principle_beats_permission_context_and_tiny_fragment(self):
        self.write("AWS/least-privilege.md", "# IAM\n\n## Best practices\n\nApply least-privilege permissions: grant users only the access they need for their assigned tasks.\n", frontmatter=False)
        self.write("AWS/fragment.md", "# Process\n\nHarder to apply least privilege.\n", frontmatter=False)
        self.write("AWS/attacks.md", "# Permission Boundaries\n\nHorizontal attacks can expand the permissions assigned to a user group.\n", frontmatter=False)
        results = WikiQABot(self.wiki).search("最小權限")["results"]
        self.assertEqual(results[0]["file"], "AWS/least-privilege.md")
        self.assertFalse(any(item["file"].endswith("attacks.md") for item in results))

    def test_cli_json_returns_evidence_contract_and_no_hit(self):
        completed = subprocess.run([sys.executable, str(ROOT / "scripts/wiki_qa_bot.py"), "--wiki-dir", str(self.wiki), "--question", "量子海豚", "--json"], check=True, capture_output=True, text=True)
        data = json.loads(completed.stdout)
        self.assertEqual(data["mode"], "evidence-search")
        self.assertFalse(data["matched"])
        self.assertEqual(data["results"], [])


if __name__ == "__main__":
    unittest.main()
