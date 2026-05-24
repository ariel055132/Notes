---
type: source
source_path: raw/archive/Database Indexing.pdf
title: "Database Indexing"
author: "BuildMoat"
date: 2026-05-15
tags: [system-design, databases, indexing, query-optimization]
created: 2026-05-24
---

# Database Indexing

## Summary

This source explains database indexes as query access shortcuts that exchange extra storage, write overhead, and maintenance complexity for faster reads on specific access patterns. [[2026-05-15--database-indexing|Database Indexing]] It warns against treating indexes as a generic "make the database faster" switch; a good system-design answer starts from the high-frequency query shape, data size, selectivity, and write-cost tolerance. [[2026-05-15--database-indexing|Database Indexing]] The source maps different workloads to different index families: B-tree indexes for equality, range, sort, and uniqueness; hash indexes for exact lookup; LSM-tree access patterns for append-heavy workloads; geospatial indexes for nearby or map queries; and inverted or vector indexes for search. [[2026-05-15--database-indexing|Database Indexing]] Its practical framing connects indexing to read scaling: optimize the database access path before adding heavier infrastructure such as cache, replicas, or sharding. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--database-indexing|Database Indexing]]

## Key Claims

1. An index is a data-access shortcut for specific query patterns, not a magic database-wide optimization. [[2026-05-15--database-indexing|Database Indexing]]
2. Without an index on the lookup predicate, a high-QPS path such as QR redirect by token may degrade into an expensive full table scan. [[2026-05-15--database-indexing|Database Indexing]]
3. Every index has storage cost, write cost, maintenance cost, and planner complexity, so indexes should be chosen from the read/write ratio and access pattern. [[2026-05-15--database-indexing|Database Indexing]]
4. B-tree indexes fit equality lookups, range queries, sorting, and unique constraints in most relational databases. [[2026-05-15--database-indexing|Database Indexing]]
5. Hash indexes fit exact equality lookups but do not support range queries or sorting. [[2026-05-15--database-indexing|Database Indexing]]
6. Append-heavy workloads such as event logs, time-series data, and delivery attempts may fit LSM-tree-style access patterns better than simply adding many relational indexes. [[2026-05-15--database-indexing|Database Indexing]]
7. Geospatial, inverted, and vector indexes solve different query shapes that B-tree indexes do not handle well. [[2026-05-15--database-indexing|Database Indexing]]
8. Low-selectivity fields such as status are often weak standalone indexes and usually need to be paired with more selective fields in a composite index. [[2026-05-15--database-indexing|Database Indexing]]

## Notable Quotes

- "Do not just say 'add index'." [[2026-05-15--database-indexing|Database Indexing]]
- "The same word 'index' hides different data structures and tradeoffs." [[2026-05-15--database-indexing|Database Indexing]]
- "Indexing should be designed from the read path and write path ratio." [[2026-05-15--database-indexing|Database Indexing]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter rather than as a dedicated entity page. [[2026-05-15--database-indexing|Database Indexing]]

## Concepts Mentioned

- [[database-indexing|Database Indexing]] — Auxiliary access paths that let a database locate rows for common queries without scanning the whole table. [[2026-05-15--database-indexing|Database Indexing]]
- [[full-table-scan|Full Table Scan]] — Reading many or all rows when no useful access path narrows the query. [[2026-05-15--database-indexing|Database Indexing]]
- [[b-tree-index|B-Tree Index]] — General-purpose index for equality, range, sort, and unique constraints. [[2026-05-15--database-indexing|Database Indexing]]
- [[hash-index|Hash Index]] — Index for exact equality lookup without range or sort support. [[2026-05-15--database-indexing|Database Indexing]]
- [[lsm-tree|LSM Tree]] — Write-optimized structure or access pattern for append-heavy workloads. [[2026-05-15--database-indexing|Database Indexing]]
- [[geospatial-index|Geospatial Index]] — Index for nearby, viewport, or polygon spatial queries. [[2026-05-15--database-indexing|Database Indexing]]
- [[inverted-index|Inverted Index]] — Search index that maps terms to documents. [[2026-05-15--database-indexing|Database Indexing]]
- [[vector-index|Vector Index]] — Index family for embedding or semantic similarity search. [[2026-05-15--database-indexing|Database Indexing]]
- [[composite-index|Composite Index]] — Multi-column index designed for queries that filter or sort on multiple fields together. [[2026-05-15--database-indexing|Database Indexing]]
- [[index-selectivity|Index Selectivity]] — How well an indexed field narrows the result set. [[2026-05-15--database-indexing|Database Indexing]]
- [[query-shape-optimization|Query Shape Optimization]] — Matching query shape to the right access path and avoiding unnecessary work. [[2026-05-15--database-indexing|Database Indexing]]

## Follow-ups

- Add a future source on query planners and `EXPLAIN` plans to connect index choice to actual database execution.
- Add a future source on vector search, approximate nearest-neighbor indexes, and hybrid lexical/semantic retrieval.
