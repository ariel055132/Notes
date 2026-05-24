---
type: concept
aliases: ["query shape", "database query optimization", "read query optimization"]
tags: [system-design, databases, query-optimization]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Query Shape Optimization

## Definition

Query shape optimization is the practice of designing database reads so they retrieve only the necessary data and avoid execution patterns that grow poorly under high read volume. [[2026-05-14--scaling-reads|Scaling Reads]] It includes matching the query shape to the right access path, such as B-tree, hash, LSM, geospatial, inverted, or vector indexes. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers reducing selected columns, separating list and detail APIs, replacing deep offset pagination with cursor-based pagination, avoiding N+1 queries, reducing repeated joins, ensuring sort columns are indexed, and choosing index families based on whether the query is equality, range, sort, append-heavy, geospatial, full-text, or vector search. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **Database Indexing**: Indexing improves access paths for a query, while query shape optimization changes the query's requested work. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Denormalization**: Query shape optimization may still use normalized tables, while denormalization changes the stored data model to reduce read-time joins. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Full-Text Search**: Query shape optimization should recognize when a B-tree is the wrong access path and a search index such as an inverted index is needed. [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source lists common query-shape problems such as selecting too many fields, deep offsets, N+1 queries, unindexed sorts, and repeated joins.
- [[2026-05-15--database-indexing|Database Indexing]] — The source presents an indexing decision framework based on query shape, selectivity, composite-index need, and write cost.

## Related

- [[read-scaling|Read Scaling]]
- [[database-indexing|Database Indexing]]
- [[composite-index|Composite Index]]
- [[index-selectivity|Index Selectivity]]
- [[inverted-index|Inverted Index]]
- [[geospatial-index|Geospatial Index]]
- [[denormalization|Denormalization]]
- [[materialized-view|Materialized View]]

## Open Questions

- Which query-shape examples should be added for search, feeds, and recommendation endpoints?
