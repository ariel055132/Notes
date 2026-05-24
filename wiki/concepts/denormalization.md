---
type: concept
aliases: ["read denormalization", "read-optimized table", "prejoined read model"]
tags: [system-design, databases, data-modeling]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Denormalization

## Definition

Denormalization is a data-modeling trade-off where data is duplicated or prejoined into read-oriented structures to reduce expensive joins during frequent reads. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept applies when data is read often and changed relatively rarely, such as a booking summary that repeatedly needs guest, booking, and home fields together. [[2026-05-14--scaling-reads|Scaling Reads]] It requires write-side care because updates may need transactions, CDC, background repair, or multiple table updates to keep duplicated data consistent enough. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Normalization**: Normalization reduces duplicated storage and update errors, while denormalization reduces repeated read-time joins at the cost of more complex writes. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Materialized View**: Denormalization can be a manually maintained read table, while a materialized view is a precomputed database or summary object often used for aggregations. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source uses a booking summary example to show how a read-optimized table can avoid repeated joins for high-volume pages.

## Related

- [[read-scaling|Read Scaling]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[materialized-view|Materialized View]]
- [[cache-invalidation|Cache Invalidation]]

## Open Questions

- Which wiki examples should distinguish denormalized read models from event-sourced projections?
