---
type: concept
aliases: ["selectivity", "column selectivity", "index cardinality"]
tags: [system-design, databases, indexing, query-optimization]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Index Selectivity

## Definition

Index selectivity is how well an indexed field narrows a query's result set, usually based on how many distinct values the field has and how evenly values are distributed. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers why high-cardinality fields such as token, email, booking ID, or user ID often make useful lookup indexes, while low-cardinality fields such as status may be weak as standalone indexes. [[2026-05-15--database-indexing|Database Indexing]] It also covers pairing low-selectivity fields with other columns in composite indexes when that matches the query shape. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **Shard Key Cardinality**: Index selectivity helps a database narrow a query inside an index, while shard-key cardinality helps distribute records across shards. [[2026-05-15--database-indexing|Database Indexing]] [[2026-05-15--sharding|Sharding]]
- **Composite Index**: Selectivity is a property of fields and predicates, while a composite index is a concrete access path that can combine multiple fields. [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source contrasts high-selectivity fields such as token and email with low-selectivity status fields, then recommends composite indexes for common multi-field queries.

## Related

- [[database-indexing|Database Indexing]]
- [[composite-index|Composite Index]]
- [[shard-key|Shard Key]]
- [[query-shape-optimization|Query Shape Optimization]]

## Open Questions

- Which future source should cover statistics, histograms, and query planner estimates?
