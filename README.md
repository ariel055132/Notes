# Notes：可追溯的學習知識庫

Notes 整理文章、PDF、影片分析報告和既有筆記。原始資料保持不變；AI 整理概念與跨來源分析；個人判斷只記錄使用者實際提供的內容。

## 從這裡開始

- [AI 輔助學習與知識管理試作](wiki/syntheses/2026-09-24--ai-learning-knowledge-management.md)：六份文件的比較、適用範圍與來源關係。
- [知識索引](wiki/index.md)：自動生成，不手動維護。
- [來源與處理狀態](inbox/sources.json)：身分、版本、覆蓋與核對紀錄。
- [PDF 品質與舊擷取程式評估](verification/pdf-quality-2026-09-24.md)：18 份 PDF 的全量指標與代表頁視覺抽查。
- [操作規範](AGENTS.md)。既有 AWS、Stock、Container、SystemDesign 筆記及 Obsidian 圖均保留。

## 用 Codex 解析新文件

先在 Notes 根目錄啟動 Codex CLI：

```sh
cd /Users/adrianli/Documents/GitHub/Notes
codex
```

然後在 **Codex 對話輸入框**輸入（不是 Terminal 的 shell 指令）：

```text
$llm-wiki-ingest "/Users/adrianli/Downloads/文件名稱.pdf"
```

文件可以留在原位。只提供路徑時，skill 預設完成繁體中文解析與摘要、來源保存、相關筆記連結、核讀狀態和索引更新。想指定用途，可在路徑後補上 `重點：如何用於工作上的知識管理`。支援 PDF、Markdown、UTF-8 文字、儲存的 HTML 與影片分析報告；格式不支援或資料不足時會說明缺少什麼。

這是 Notes 專案的 skill；在 Notes 中用 `/skills` 或輸入 `$` 選取 `llm-wiki-ingest`。若更新沒有出現，重新啟動 Codex。完整流程見 [skill](.agents/skills/llm-wiki-ingest/SKILL.md)；[官方 skill 使用說明](https://learn.chatgpt.com/docs/build-skills)。

## 中文查詢

在 Notes 根目錄執行：

```sh
python3 scripts/wiki_qa_bot.py --question '快取失效怎麼處理？'
python3 scripts/wiki_qa_bot.py --question 'AI 輔助學習與知識管理' --json
python3 scripts/wiki_qa_bot.py --question '最小權限' --no-legacy
```

輸出是有檔名、段落、行號與狀態的**證據摘錄**，不是模型生成的答案。AI 助理可讀取摘錄及原頁後再整理回答。預設搜尋 Wiki 和四個既有筆記資料夾；`--no-legacy` 僅搜尋 Wiki。草稿、受阻頁、未整理模板及待研究問題不當作答案。

目前使用離線詞彙搜尋與 [雙語詞彙表](config/search-aliases.json)。已支援繁／簡中文與常用英文概念，並非任意語意翻譯；陌生同義詞可以補入詞彙表。找到片段不代表它已證實，請閱讀列出的處理狀態與來源限制。

## 共用匯入

接收本機 Markdown、UTF-8 文字、儲存的 HTML、PDF 與影片分析報告；網址用來記錄出處及去重，CLI 不自動抓網站或媒體。

```sh
python3 scripts/import_source.py add /absolute/path/article.md --url https://example.com/article --author '作者'
python3 scripts/import_source.py add /absolute/path/video-report.md
python3 scripts/import_source.py add /absolute/path/document.pdf --kind pdf
python3 scripts/import_source.py list
```

只有 PDF 擷取需要 `pdfplumber`：使用具備此套件的 Python，或在自己的虛擬環境安裝 `requirements-pdf.txt`。本次驗證使用 Codex bundled Python。所有原始檔均保留；快照放在 `raw/imports/<source-id>/`，完整擷取結果放在 `derived/<source-id>/`。這兩者不進 Git，須自行納入本機備份。HTML 的圖像和複雜表格、PDF 的圖解／表格／浮水印都可能需要人工或視覺核讀。

匯入會建立**待整理來源卡**，不從標題自動編造摘要。閱讀擷取與原頁、填寫來源卡並移除 `REVIEW_REQUIRED` 標記後，記錄核對結果：

```sh
python3 scripts/import_source.py review SOURCE_ID --status ready --note '已核對原文第 2–4 節；保留尚未驗證的限制。'
```

若有機器偵測的警示，核讀後另加 `--acknowledge-warnings`；未核讀就保留 `needs-review`。`ready` 只表示核對了記錄範圍，不表示原作者所有主張都是真的。狀態為 `draft`、`needs-review`、`ready`、`blocked`，與 `coverage`、`confidence` 分別記錄。

同一來源以網址或穩定影片 ID 去重，以 SHA-256 區分版本。已有來源頁用 `--existing-page wiki/sources/文件.md` 登記，避免重複建頁。來源更新會保留舊快照與既有人工正文，標為待重新核對；換擷取方法時用 `--reextract` 記錄新的擷取版本。沒有網址的檔案可指定 `--source-id`，使日後搬檔仍沿用相同身分。

自己寫的網站閱讀筆記應加 `--evidence-level source-notes --coverage partial`；影片報告會標為 `secondary-summary`，並保留上游 `analysis_level`、`transcript_coverage`、信心與評分。不能把二手摘要標成原文。

## 與影片篩選專案的分工

`video-content-filter-assistant` 維護正式影片報告；Notes 接收選定報告的快照並整理跨來源知識。正式報告仍在原專案，Notes 不回寫上游。這輪已實際匯入兩份報告，未建立背景監控、排程或 GitHub 自動發布。

## 維護與驗證

```sh
python3 scripts/rebuild_index.py
python3 scripts/rebuild_index.py --check
python3 scripts/lint_schema.py --strict
python3 scripts/validate_log.py
python3 -B -m unittest discover -s tests -v
```

PDF 測試需要另外具備 `reportlab`、`pypdf`、Pillow（Codex bundled runtime 已備）。測試不呼叫模型或網路。圖的節點大小表示筆記連結，索引的來源數表示直接引用的不同文件；兩者均不等於獨立研究證據數或學習成效。
