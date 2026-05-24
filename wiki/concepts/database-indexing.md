---
type: concept
aliases: ["index", "database index", "secondary index"]
tags: [system-design, databases, query-optimization]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Database Indexing

## Definition

Database indexing is the use of auxiliary data structures that let a database locate rows for common query patterns without scanning an entire table. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers indexes for frequent WHERE predicates, join keys, sort and pagination columns, and high-selectivity lookup fields such as QR tokens or order IDs. [[2026-05-14--scaling-reads|Scaling Reads]] It also includes trade-offs: indexes add write cost and storage cost because inserts, updates, and deletes must maintain the index. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Query Shape Optimization**: Indexing makes the database find data efficiently, while query shape optimization reduces unnecessary fields, joins, deep offsets, and repeated queries. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Caching**: Indexing improves database execution, while caching avoids repeated database execution for reusable answers. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source presents indexing as the first database-layer fix before adding new infrastructure such as replicas or caches.

## Related

- [[read-scaling|Read Scaling]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[read-replica|Read Replica]]
- [[database-sharding|Database Sharding]]

## Open Questions

- Which index patterns should be documented for common system-design examples such as feeds, search pages, and order histories?
