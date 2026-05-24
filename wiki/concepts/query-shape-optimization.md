---
type: concept
aliases: ["query shape", "database query optimization", "read query optimization"]
tags: [system-design, databases, query-optimization]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Query Shape Optimization

## Definition

Query shape optimization is the practice of designing database reads so they retrieve only the necessary data and avoid execution patterns that grow poorly under high read volume. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers reducing selected columns, separating list and detail APIs, replacing deep offset pagination with cursor-based pagination, avoiding N+1 queries, reducing repeated joins, and ensuring sort columns are indexed. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Database Indexing**: Indexing improves access paths for a query, while query shape optimization changes the query's requested work. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Denormalization**: Query shape optimization may still use normalized tables, while denormalization changes the stored data model to reduce read-time joins. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source lists common query-shape problems such as selecting too many fields, deep offsets, N+1 queries, unindexed sorts, and repeated joins.

## Related

- [[read-scaling|Read Scaling]]
- [[database-indexing|Database Indexing]]
- [[denormalization|Denormalization]]
- [[materialized-view|Materialized View]]

## Open Questions

- Which query-shape examples should be added for search, feeds, and recommendation endpoints?
