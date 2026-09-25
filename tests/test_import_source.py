import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import import_source as ingest


class ImportTests(unittest.TestCase):
    def setUp(self):
        # Deliberately retain temporary fixtures: repository policy forbids
        # recursive / bulk deletion, including TemporaryDirectory cleanup.
        self.root = Path(tempfile.mkdtemp(prefix='notes-import-test-'))
        for directory in ('entities', 'concepts', 'sources', 'syntheses'):
            (self.root / 'wiki' / directory).mkdir(parents=True)
        self.article = self.root / 'article.md'
        self.article.write_text('# 學習筆記\n\n先定義問題，再核對來源。\n')

    def add(self, **kwargs):
        return ingest.add_source(self.root, self.article, url='https://example.com/learning', **kwargs)

    def curate(self, entry):
        path = self.root / entry['source_page']
        fields, _ = ingest.frontmatter(path.read_text())
        body = '# 學習筆記\n\n## Summary\n\n先定義問題，再核對來源。\n\n## Key Claims\n\n- 明確問題能設定核對範圍。\n\n## Notable Quotes\n\n無直接引文。\n\n## Entities Mentioned\n\n無。\n\n## Concepts Mentioned\n\n無新增概念頁。\n\n## Follow-ups\n\n驗證是否適用。\n'
        path.write_text(ingest.document(fields, body))

    def test_same_source_is_idempotent_and_keeps_original(self):
        original = self.article.read_bytes()
        first = self.add()
        log = (self.root / 'wiki/log.md').read_text()
        second = self.add()
        self.assertFalse(second['changed'])
        self.assertEqual(first['source_page'], second['source_page'])
        self.assertEqual(1, len(second['versions']))
        self.assertEqual(log, (self.root / 'wiki/log.md').read_text())
        self.assertEqual(original, self.article.read_bytes())
        self.assertEqual(original, (self.root / first['source_path']).read_bytes())

    def test_revision_preserves_curated_page_and_old_snapshot(self):
        first = self.add()
        self.curate(first)
        ingest.review_source(self.root, first['source_id'], 'ready', '核讀原文段落，保留適用範圍。')
        self.article.write_text('# 學習筆記\n\n更新後須檢查新例外。\n')
        second = self.add()
        self.assertEqual(first['source_page'], second['source_page'])
        self.assertEqual(2, len(second['versions']))
        self.assertEqual('needs-review', second['processing_status'])
        self.assertIn('先定義問題', (self.root / first['source_path']).read_text())
        self.assertIn('先定義問題', (self.root / second['source_page']).read_text())

    def test_placeholder_cannot_be_marked_ready(self):
        entry = self.add()
        with self.assertRaisesRegex(ValueError, 'placeholder'):
            ingest.review_source(self.root, entry['source_id'], 'ready', 'unchecked')

    def test_url_dedup_ignores_tracking(self):
        entry = self.add(source_id='learning')
        with self.assertRaisesRegex(ValueError, 'already registered'):
            ingest.add_source(self.root, self.article, url='https://example.com/learning?utm_source=mail#intro', source_id='duplicate')
        self.assertEqual(1, len(ingest.registry(self.root)['sources']))

    def test_blocks_source_id_and_page_traversal(self):
        with self.assertRaises(ValueError):
            self.add(source_id='../escape')
        with self.assertRaises(ValueError):
            self.add(existing_page='wiki/sources/../../../outside.md')

    def test_video_report_preserves_partial_evidence(self):
        self.article.write_text('---\ndocument_type: video-summary\ntitle: "Partial learning video"\nurl: "https://example.com/video"\nvideo_id: "xyz"\nanalysis_level: quick-screen\ntranscript_coverage: partial\nconfidence: low\nrecommendation_score: 4\nquality_score: 12\n---\n\nOnly description and incomplete captions.\n')
        entry = ingest.add_source(self.root, self.article)
        fields, _ = ingest.frontmatter((self.root / entry['source_page']).read_text())
        self.assertEqual('video-report', fields['source_type'])
        self.assertEqual('secondary-summary', fields['evidence_level'])
        self.assertEqual('partial', fields['coverage'])
        self.assertEqual('quick-screen', fields['analysis_level'])
        self.assertEqual('low', fields['confidence'])
        self.assertNotEqual('ready', fields['processing_status'])

    def test_html_uses_article_and_excludes_scripts(self):
        html = self.root / 'saved.html'
        html.write_text('<html><head><title>文章</title></head><body>Navigation<article><h1>學習</h1><p>核對來源</p><script>SECRET_JS</script></article></body></html>')
        entry = ingest.add_source(self.root, html, url='https://example.com/html')
        extracted = json.loads((self.root / entry['versions'][-1]['extraction_path']).read_text())
        self.assertIn('核對來源', extracted['pages'][0]['text'])
        self.assertNotIn('Navigation', extracted['pages'][0]['text'])
        self.assertNotIn('SECRET_JS', extracted['pages'][0]['text'])
        self.assertEqual('needs-review', entry['processing_status'])

    def test_blocked_extraction_cannot_be_laundered_through_draft(self):
        blocked = {'status':'blocked','method':'test','page_count':1,'pages':[{'page':1,'text':'','tables':[],'warnings':['no text']}],'warnings':['no text']}
        with patch.object(ingest, 'extract', return_value=blocked):
            entry = self.add()
        self.curate(entry)
        ingest.review_source(self.root, entry['source_id'], 'draft', 'OCR still needed')
        with self.assertRaisesRegex(ValueError, 'blocked extraction'):
            ingest.review_source(self.root, entry['source_id'], 'ready', 'unchecked', True)

    def test_snapshot_integrity_checked_on_review(self):
        entry = self.add()
        self.curate(entry)
        (self.root / entry['source_path']).write_text('corrupted fixture')
        with self.assertRaisesRegex(ValueError, 'integrity'):
            ingest.review_source(self.root, entry['source_id'], 'ready', 'review')

    def test_missing_extraction_is_not_success_and_reextract_recovers(self):
        entry = self.add()
        derived = self.root / entry['versions'][-1]['extraction_path']
        derived.rename(derived.with_suffix('.saved'))
        with self.assertRaisesRegex(ValueError, 'integrity/missing-file'):
            self.add()
        repaired = self.add(reextract=True)
        self.assertTrue((self.root / repaired['versions'][-1]['extraction_path']).is_file())

    def test_reextract_records_changed_extraction_without_replacing_raw(self):
        blocked = {'status':'blocked','method':'before','page_count':1,'pages':[{'page':1,'text':'','tables':[],'warnings':[]}],'warnings':['OCR needed']}
        with patch.object(ingest, 'extract', return_value=blocked):
            first = self.add()
        updated = self.add(reextract=True)
        self.assertEqual(first['current_sha256'], updated['current_sha256'])
        self.assertNotEqual(first['versions'][0]['extraction_path'], updated['versions'][-1]['extraction_path'])
        self.assertNotEqual('blocked', updated['processing_status'])

    def test_revision_does_not_erase_known_metadata(self):
        first = self.add(author='Author', published_date='2025-01-02', coverage='partial', confidence='medium')
        self.article.write_text('# Revised\n\nNew limitation.\n')
        updated = self.add()
        fm, _ = ingest.frontmatter((self.root / updated['source_page']).read_text())
        self.assertEqual('Author', fm['author'])
        self.assertEqual('2025-01-02', fm['published_date'])
        self.assertEqual('partial', fm['coverage'])
        self.assertEqual('medium', fm['confidence'])

    def test_article_notes_keep_evidence_level_and_multiline_author(self):
        self.article.write_text('---\nauthor:\n  - "A"\n  - "B"\nevidence_level: secondary-summary\ncoverage: partial\n---\n\nThese are reference notes, not the article.\n')
        entry = self.add()
        fm, _ = ingest.frontmatter((self.root / entry['source_page']).read_text())
        self.assertEqual(['A', 'B'], fm['author'])
        self.assertEqual('secondary-summary', fm['evidence_level'])
        self.assertEqual('partial', fm['coverage'])

    def test_same_video_id_different_url_uses_one_identity(self):
        self.article.write_text('---\ndocument_type: video-summary\nvideo_id: xyz\nurl: https://example.com/watch/xyz\n---\n\nVideo analysis.\n')
        first = ingest.add_source(self.root, self.article)
        self.article.write_text(self.article.read_text().replace('example.com/watch/xyz', 'example.com/embed/xyz'))
        second = ingest.add_source(self.root, self.article)
        self.assertEqual(first['source_id'], second['source_id'])
        self.assertEqual(1, len(ingest.registry(self.root)['sources']))


if __name__ == '__main__':
    unittest.main()
