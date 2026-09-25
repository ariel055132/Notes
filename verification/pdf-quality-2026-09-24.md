# Notes PDF 品質檢查與抽取程式審查

檢查日期：2026-09-24。原始資料位置：`/Users/adrianli/Documents/GitHub/Notes`。

**結論：目前 PDF 可以保留作為知識庫來源，但文字抽取結果不能直接視為完整、忠實的內容。** 本次完整跑過 18 份、202 頁的機器指標，另外檢視 9 份文件中的 12 張完整頁面圖片。抽查原頁清楚可讀；主要問題是浮水印混字、字碼差異、表格結構與圖解資訊。這些結果不代表已逐頁人工驗證全部 PDF，也不提供語意正確率。

## 範圍與方法

- 包含 `raw/archive/` 14 份、`raw/sources/` 3 份、`AWS/source/` 1 份 PDF。其他 repo 的 Tencent 財報只用來審查舊程式輸出，不計入 Notes 文件數。
- 使用 `pdfplumber 0.11.9` 逐頁抽取完整文字與表格候選、圖片數、旋轉字元及字碼警示；未執行 OCR。
- 以 Poppler `pdftoppm` 渲染代表頁（長邊 1800 px），逐張閱讀並對照文字和表格抽取。
- 18 份來源檔的 SHA-256 均與原 Notes 對應檔一致；原檔未修改。原始檔 hash、每頁 metrics 與抽查紀錄保存在 [JSON](pdf-quality-2026-09-24.json)。
- 追蹤中的審查文件不保存完整抽取文字或頁面圖片。原始抽取輸出由 importer 存至 Git 忽略的 `derived/`。

## 全量機器指標

| 指標 | 結果 | 解讀 |
| --- | ---: | --- |
| PDF / 頁數 | 18 / 202 | 全數完成逐頁 metrics |
| 抽取文字字元數 | 156,129 | 含空白與可能干擾字元，不是完整度 |
| 空文字頁 | 0 | 能抽文字不等於圖與表完整 |
| 圖片頁 / 嵌入圖片物件 | 58 / 128 | 含裝飾圖示；尚未 OCR 或解讀 |
| 表格候選頁 / 候選數 | 53 / 57 | 候選有誤判，不能當真實表格數 |
| 有旋轉字元的頁 | 165 | 17 份講義的每一頁；保守保留，不自動刪除 |
| CJK radical 字碼頁 | 164 | 視覺近似文字可能不同碼；搜尋可 NFKC 正規化 |
| cid / replacement / NUL 異常頁 | 0 | 僅此類指標未觸發，不排除其他錯字 |
| adapter 結果 | 18 needs-review | 可進檢查流程；不代表原 PDF 毀損 |

## 逐份盤點

| 文件 | 頁數 | 抽取字元 | 圖片頁 | 表格候選頁 | 狀態 |
| --- | ---: | ---: | ---: | ---: | --- |
| `AWS/source/AmazonS3Outpost.pdf` | 37 | 13,991 | 37 | 4 | needs-review |
| `raw/archive/API Gateway.pdf` | 12 | 9,353 | 1 | 2 | needs-review |
| `raw/archive/CDN (Content Delivery Network).pdf` | 5 | 3,606 | 0 | 5 | needs-review |
| `raw/archive/Caching.pdf` | 11 | 10,683 | 0 | 4 | needs-review |
| `raw/archive/Consistent Hashing.pdf` | 11 | 5,962 | 4 | 3 | needs-review |
| `raw/archive/Database Indexing.pdf` | 4 | 2,968 | 0 | 1 | needs-review |
| `raw/archive/Database Transactions.pdf` | 9 | 8,124 | 1 | 1 | needs-review |
| `raw/archive/Database.pdf` | 7 | 4,992 | 1 | 0 | needs-review |
| `raw/archive/Distributed Cache.pdf` | 8 | 7,146 | 0 | 7 | needs-review |
| `raw/archive/Distributed Lock.pdf` | 5 | 3,986 | 0 | 5 | needs-review |
| `raw/archive/Message Queue.pdf` | 4 | 3,380 | 0 | 3 | needs-review |
| `raw/archive/Replication.pdf` | 17 | 16,107 | 6 | 2 | needs-review |
| `raw/archive/Scaling Reads.pdf` | 16 | 14,015 | 4 | 0 | needs-review |
| `raw/archive/Sharding.pdf` | 11 | 11,538 | 0 | 5 | needs-review |
| `raw/archive/Zookeeper.pdf` | 13 | 12,721 | 0 | 6 | needs-review |
| `raw/sources/Blob Storage.pdf` | 11 | 9,720 | 1 | 1 | needs-review |
| `raw/sources/Container.pdf` | 10 | 8,584 | 1 | 2 | needs-review |
| `raw/sources/Serverless.pdf` | 11 | 9,253 | 2 | 2 | needs-review |

## 代表頁視覺核對（12 頁，9 份文件）

| 文件／原 PDF 頁碼 | 觀察 |
| --- | --- |
| `raw/archive/Caching.pdf` p.4 | 原頁正文清楚；斜向 buildmoat.org 浮水印可辨。抽取會把浮水印字母交錯插入正文。 |
| `raw/archive/Caching.pdf` p.10 | 原頁 invalidation 清楚，抽取變成 invalidatuion；文字層存在不等於詞彙無誤。 |
| `raw/archive/Replication.pdf` p.5 | 時序圖清楚顯示 user/leader/follower 與箭頭；圖內 insert into comments、User 1234 不在抽取文字中。 |
| `raw/archive/Replication.pdf` p.16 | 原頁四欄、表頭加三種架構共四列；新 adapter 能取得 4x4 候選，但列欄意義仍須核對。 |
| `AWS/source/AmazonS3Outpost.pdf` p.6 | 五欄圖示加文字投影片清楚；偵測到的兩個 table candidates 其實來自圖形，不能當真實表格。 |
| `AWS/source/AmazonS3Outpost.pdf` p.22 | S3 Outposts 投影片文字可讀，含圖示與視覺強調；頁腳為 2020 年，內容不應當成當前規格。 |
| `raw/archive/Database Indexing.pdf` p.1 | 原頁三欄、六個案例加表頭的表格清楚；偵測器受 inline code 框影響給出 9x6 候選，不能直接採信。 |
| `raw/archive/CDN (Content Delivery Network).pdf` p.3 | 原頁同時有流程 code block 與三欄表格；純文字未保留 code fence，浮水印與表格需版面核對。 |
| `raw/archive/Consistent Hashing.pdf` p.4 | hash ring 圖的節點、箭頭與黃色區間清楚；圖的區間關係不能僅由正文完整重建。 |
| `raw/sources/Blob Storage.pdf` p.3 | 五欄儲存分層表格清楚；成本、延遲與 retrieval fee 必須保持橫向列對應，不能混成關鍵字。 |
| `raw/sources/Container.pdf` p.2 | 原頁有跨頁表格與 Dockerfile 片段；範例換行和指令需要保留，不能用每頁前14 blocks作原始依據。 |
| `raw/sources/Serverless.pdf` p.4 | 原頁的 image upload -> S3 -> Lambda -> thumbnail -> S3 流程圖清楚；箭頭和回折路徑需視覺解讀。 |

表格例子說明了為何不能只換一套 parser 就宣稱解決：Replication p.16 的 4×4 表格候選結構較吻合；Database Indexing p.1 卻把程式碼底色框當成額外格線，得出 9×6；AWS p.6 的圖示也被偵測成表格。因此所有表格候選都保存 `verified: false`。

## DocumentConverter 程式是否合理

閱讀範圍：[phase1_pdf_explore.py](/Users/adrianli/Documents/Codex/DocumentConverter/scripts/phase1_pdf_explore.py)、[rules/pdf.md](/Users/adrianli/Documents/Codex/DocumentConverter/rules/pdf.md)，以及既有 `runs/2026-06-02/` 的 index、candidate、review、failure。**沒有執行舊程式 main，也沒有修改 DocumentConverter。**

它作為第一階段探索工具合理：有原始來源、hash、頁碼和問題紀錄；既有 Tencent 財報範例也明確標示字型映射異常、需要 OCR。但不適合作為共用匯入流程的完整內容層。

| 優先度 | 發現與程式位置 | 對規則／資料的影響 |
| --- | --- | --- |
| 高 | 每頁只輸出前 14 blocks；標題最多 160 字元、一般 block 最多 520（L164、247-253） | 原始證據遭截短。既有 Replication 遺漏 71 blocks／9 頁；Container 108／10；CDN 52／4。既有 candidate 有註明 omission，仍不能供完整分析使用 |
| 高 | 字碼檢查只看前 8 頁（L192）；空文字頁只是標 partial | 後半部異常可能漏檢；沒有真正 OCR fallback；不能因前面可讀就接受全部 |
| 高 | 同名 raw copy 存在就跳過複製，但 hash／extract 來自目前 Downloads（L95-109） | 新版本同名檔可能讓 source_path 指到舊內容；應依 hash 驗證或版本化 |
| 中 | 規則要求去浮水印、表格重建、code fence、圖片檢視；程式大多只有 heuristic 和警示 | 這些規則尚未由實作保證，不能當已完成的功能 |
| 中 | Compact Summary 取最早 12 個 regex 命中（L171-188） | 可能包含標題、殘句並偏重前幾頁；不是整份文件的重點摘要 |
| 中 | Source Map 固定宣稱 Summary 對應 1-8 頁（L263） | 與實際選取頁碼不一致；應由逐項來源計算 |
| 中 | 表格 heuristic 是寬鬆的英文單字／空白 pattern（L275） | 既有 table-like count 不代表正確解析的表格 |
| 中 | hard-coded Downloads 和日期；main 寫回 rules 與舊 run（L14-18、539-547） | 不利於重跑、共用和版本追溯；本次刻意沒有執行 |

## 第一輪採用的 PDF adapter

`scripts/pdf_extract.py` 提供 `extract_pdf(path: Path) -> dict`，不寫檔、不連網、不修改來源。

- 每一頁都有一基底頁碼、完整抽取文字、警示與表格候選；不做原程式的 blocks／字元截短。
- 保留所有旋轉字元，利用 matrix 偵測 45° 等斜向文字，避免只靠 `upright` 漏掉浮水印，也避免誤刪正常圖說。
- 圖片、向量／格線、旋轉文字、異常字碼、空文字頁及表格候選都會觸發 `needs-review`；完全沒有文字、無法開啟、整份有明顯字碼異常則 `blocked`。
- `ready` 僅代表這次文字層檢查未偵測到警示；不是內容真實性、語意準確度或圖解完整度的保證。
- 未執行 OCR、圖解轉述、自動修復字碼、跨頁表格拼接或浮水印刪除。這些是明示限制，不能把抽取 JSON 當成已覆核的來源卡。

## 驗證

使用 bundled Python 執行 `python3 -m unittest discover -s tests -p test_pdf_extract.py -v`：9 項通過。覆蓋多頁與頁尾內容不截短、原檔不變、45° 合法旋轉標籤保留、圖片頁分流、表格 cell 候選、單頁失敗保留後頁、損壞／不存在／密碼保護檔、異常字碼及中文保留。另驗證已知 FontBBox 重複警告局部彙整、其他執行緒與警告照常輸出，以及實際 parser exception 仍回傳 blocked。

整合補充：adapter 在單次抽取與當前執行緒內，僅捕獲 `pdfminer.pdffont` 的已知 FontBBox warning；以 `diagnostics.font_bbox_warning_count` 和一條文件級 warning 保存診斷，不全域關閉 logging，退出時移除 filter。原始 audit JSON 的 extractor hash 記錄盤點當時的版本；這次 logging 修正不改變上述文字／版面計數。

合成測試用 PDF 不代表真實文件準確率。測試使用 `pdfplumber`、`reportlab`、`Pillow`、`pypdf`；執行時只在獨立 OS 暫存目錄產生 fixture，沒有遞迴清理。抽查的 12 張渲染暫存圖逐一以明確路徑清除，沒有加入 Git。

## 適合下一步使用的界線

現有原 PDF 足以開始建立可回查頁碼的來源卡。整理正文時，可使用本次完整文字作搜尋候選；要採用表格數字、程式碼或圖解關係，就必須核對原頁。先處理實際主題要引用的頁面，無須因所有文件標 needs-review 就停止整個知識庫，也不應一次把整庫當作已驗證。
