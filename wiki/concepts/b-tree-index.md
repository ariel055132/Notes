---
type: concept
aliases: ["B-tree", "B+tree", "B-tree indexes", "B+tree index"]
tags: [system-design, databases, indexing]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# B-Tree Index

## Definition

A B-tree index is a general-purpose database index structure suited to equality lookups, range queries, sorting, and uniqueness constraints. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers common relational-database indexes on fields such as token, creation time, tenant ID plus creation time, or other columns used in WHERE, ORDER BY, or uniqueness checks. [[2026-05-15--database-indexing|Database Indexing]] It is often the default index family in relational databases, but it should still be chosen from the query shape and write-cost tradeoff. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **Hash Index**: B-tree indexes support range and sort access patterns, while hash indexes are mainly for exact equality lookup. [[2026-05-15--database-indexing|Database Indexing]]
- **Inverted Index**: B-tree indexes do not solve full-text term-to-document search well, while inverted indexes are designed for that query shape. [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source names B-tree or B+tree as the usual relational database default for equality, range, sort, and unique constraints.

## Related

- [[database-indexing|Database Indexing]]
- [[composite-index|Composite Index]]
- [[index-selectivity|Index Selectivity]]
- [[full-table-scan|Full Table Scan]]
- [[hash-index|Hash Index]]

## Open Questions

- Which future source should explain B-tree left-prefix behavior and covering indexes?
