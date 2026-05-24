---
type: concept
aliases: ["full table scans", "table scan", "sequential scan"]
tags: [system-design, databases, query-optimization]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Full Table Scan

## Definition

A full table scan is a query execution pattern where the database reads many or all rows in a table to find matching records because no useful index or access path narrows the search. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers the failure mode where high-QPS lookup paths become expensive as table size grows, such as a QR redirect query scanning `qr_codes` rows to find one token. [[2026-05-15--database-indexing|Database Indexing]] It does not mean every scan is always wrong; the issue is a frequent or latency-sensitive access path doing unbounded work. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **B-Tree Index**: A B-tree index can locate candidate rows for equality, range, sort, or unique lookups, while a full table scan checks the table broadly. [[2026-05-15--database-indexing|Database Indexing]]
- **Query Shape Optimization**: Query shape optimization may reduce selected data or avoid deep offsets, while indexing prevents the lookup from scanning irrelevant rows. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source uses QR redirect by token as the example of an unindexed query becoming an expensive full table scan at high QPS.

## Related

- [[database-indexing|Database Indexing]]
- [[b-tree-index|B-Tree Index]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[read-scaling|Read Scaling]]

## Open Questions

- Which future source should define `EXPLAIN` plan terms such as sequential scan, index scan, and bitmap scan?
