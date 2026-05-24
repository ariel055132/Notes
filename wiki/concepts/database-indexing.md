---
type: concept
aliases: ["index", "database index", "secondary index"]
tags: [system-design, databases, query-optimization]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Database Indexing

## Definition

Database indexing is the use of auxiliary data structures that let a database locate rows for common query patterns without scanning an entire table. [[2026-05-14--scaling-reads|Scaling Reads]] It trades extra storage, write overhead, and maintenance complexity for faster reads on specific access patterns. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers indexes for frequent WHERE predicates, join keys, sort and pagination columns, high-selectivity lookup fields such as QR tokens or order IDs, composite indexes for multi-field query shapes, and specialized indexes for full-text, vector, geospatial, and append-heavy access patterns. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--database-indexing|Database Indexing]] It also includes tradeoffs: indexes add write cost and storage cost because inserts, updates, and deletes must maintain the index, and too many indexes can make maintenance and planner choices heavier. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **Query Shape Optimization**: Indexing makes the database find data efficiently, while query shape optimization reduces unnecessary fields, joins, deep offsets, and repeated queries. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Caching**: Indexing improves database execution, while caching avoids repeated database execution for reusable answers. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Database Sharding**: Indexing improves access paths inside a database or shard, while sharding distributes data ownership across database machines or clusters. [[2026-05-15--database-indexing|Database Indexing]] [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source presents indexing as the first database-layer fix before adding new infrastructure such as replicas or caches.
- [[2026-05-15--database-indexing|Database Indexing]] — The source maps query shapes to index types and emphasizes selectivity, composite indexes, and write-cost tolerance.

## Related

- [[read-scaling|Read Scaling]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[full-table-scan|Full Table Scan]]
- [[b-tree-index|B-Tree Index]]
- [[hash-index|Hash Index]]
- [[lsm-tree|LSM Tree]]
- [[geospatial-index|Geospatial Index]]
- [[inverted-index|Inverted Index]]
- [[vector-index|Vector Index]]
- [[composite-index|Composite Index]]
- [[index-selectivity|Index Selectivity]]
- [[read-replica|Read Replica]]
- [[database-sharding|Database Sharding]]

## Open Questions

- Which future source should add query planner and `EXPLAIN` examples for these index patterns?
