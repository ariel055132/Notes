---
type: "source"
source_id: "personal-information-feed-architecture"
source_type: "article"
source_path: "raw/imports/personal-information-feed-architecture/8d79521ab8361fe47cb12158059d3ede27ed5b6de356e6498b5103d06dc7c15a.md"
source_url: ""
title: "建立自己的資訊流：FreshRSS × NetNewsWire 架構筆記"
author: "使用者與 Codex 對話整理"
date: "2026-09-25"
published_date: "2026-09-25"
tags: ["rss", "self-hosting", "system-design", "networking", "knowledge-management"]
created: "2026-09-25"
updated: "2026-09-25"
processing_status: "ready"
coverage: "full"
confidence: "medium"
evidence_level: "source-notes"
extraction_path: "derived/personal-information-feed-architecture/8d79521ab8361fe47cb12158059d3ede27ed5b6de356e6498b5103d06dc7c15a-6d45143d630168ef.json"
upstream_sha256: "8d79521ab8361fe47cb12158059d3ede27ed5b6de356e6498b5103d06dc7c15a"
captured_at: "2026-09-25"
source_count: 1
---

# 建立自己的資訊流：FreshRSS × NetNewsWire 架構筆記

## Summary

這份對話整理筆記描述以 FreshRSS 集中收集內容、NetNewsWire 負責閱讀的自架資訊流。DigitalOcean 提供持續運作的主機，Docker Compose 管理服務，Cloudflare DNS 與 Caddy 分別負責網域解析及 HTTPS 入口。原筆記保留兩張 Mermaid 架構圖，區分收集與閱讀同步，並說明持久化、備份及維護責任。這是使用者與助理整理的架構紀錄，已隱藏實際網域；不作為目前服務部署或備份已驗證完成的證明。

完整筆記：[[personal-information-feed-architecture|FreshRSS × NetNewsWire 架構筆記（含 Mermaid 圖）]]，存放於 `SystemDesign/personal-information-feed-architecture.md`。

## Key Claims

1. FreshRSS 負責定期收集、保存文章與閱讀狀態；NetNewsWire 透過 API 同步。因此收集工作不必依賴個人裝置保持開機，但雲端主機及排程必須正常運作。（原筆記第 1、2、4 節）
2. DNS only 模式下，Cloudflare 負責網域解析，客戶端 HTTPS 流量直接到 Caddy；Caddy 再透過 Docker 內部網路將請求轉交 FreshRSS。（第 2、3 節）
3. FreshRSS 主動抓取外部訂閱，與 Caddy 接收外部使用者請求，是不同方向的流程。（第 2 節）
4. 容器重建所需的持久化與故障復原所需的備份有不同用途；資料庫、使用者設定、Compose、擴充套件及 Caddy 資料需要納入保存規劃。（第 5、6 節）

## Notable Quotes

> 「FreshRSS 負責收集與保存。」（原筆記第 1 節，逐字引文）

> 「容器可以重新建立，但重要資料必須保存在容器之外。」（第 5 節，逐字引文）

## Entities Mentioned

FreshRSS、NetNewsWire、DigitalOcean、Docker Compose、Caddy、Cloudflare。這些產品在本來源中作為架構元件，暫不建立個別 entity 頁。

## Concepts Mentioned

- [[tls-termination|TLS Termination]]：Caddy 集中處理外部 HTTPS 與憑證；此關聯是助理依第 2、3 節與既有概念頁建立的映射。
- [[personal-information-feed-architecture|完整架構筆記]]：收集端與閱讀端分工、DNS only、容器持久化及備份。

## Follow-ups

- 全文核讀範圍為這份架構筆記第 1–6 節，包含兩段 Mermaid 原始碼及表格；沒有擷取警示。`coverage: full` 指完整保存筆記，不表示已重新測試所有服務。
- 訂閱來源、全文擷取、圖片顯示與篩選刻意不納入本次範圍。
- 待後續安排備份及還原驗證；本來源未提供已完成驗證的證據。
- 匯入日期與筆記整理日期為 2026-09-25；沒有對外出版網址。原始快照與擷取證據依 Repo 規則留在本機，Git 另保存可閱讀的完整 Markdown。
