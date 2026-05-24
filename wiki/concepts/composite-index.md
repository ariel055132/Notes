---
type: concept
aliases: ["composite indexes", "compound index", "multi-column index", "compound indexes"]
tags: [system-design, databases, indexing, query-optimization]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Composite Index

## Definition

A composite index is an index over multiple columns designed for queries that commonly filter, sort, or page using those columns together. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers indexes such as `(user_id, status, next_run_at)` for due tasks or `(tenant_id, created_at)` for tenant event history. [[2026-05-15--database-indexing|Database Indexing]] It is different from adding independent single-column indexes because the query shape often needs the combined access path. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **Single-Column Index**: A composite index captures a multi-field access pattern, while separate single-column indexes may not support the same filtering and ordering efficiently. [[2026-05-15--database-indexing|Database Indexing]]
- **Index Selectivity**: Composite indexes can pair a low-selectivity field such as status with more selective fields such as tenant ID and timestamp. [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source recommends considering composite indexes when queries commonly use fields together, such as tenant ID and creation time.

## Related

- [[database-indexing|Database Indexing]]
- [[b-tree-index|B-Tree Index]]
- [[index-selectivity|Index Selectivity]]
- [[query-shape-optimization|Query Shape Optimization]]

## Open Questions

- Which future source should explain column order and left-prefix matching in composite indexes?
