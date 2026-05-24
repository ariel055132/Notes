---
type: concept
aliases: ["hash indexes", "hashed index"]
tags: [system-design, databases, indexing]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Hash Index

## Definition

A hash index is an index structure optimized for exact equality lookups by hashing the indexed key. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers fast lookup by identifiers such as market ID, session ID, or cache key. [[2026-05-15--database-indexing|Database Indexing]] It does not support range queries or sorting well because hashing destroys key order. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **B-Tree Index**: Hash indexes are strong for exact equality lookup, while B-tree indexes also support range scans and sorting. [[2026-05-15--database-indexing|Database Indexing]]
- **Hash-Based Sharding**: A hash index accelerates lookup inside a database, while hash-based sharding maps data ownership across shards. [[2026-05-15--database-indexing|Database Indexing]] [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source describes hash indexes as suitable for exact equality lookup and unsuitable for range queries or sorting.

## Related

- [[database-indexing|Database Indexing]]
- [[b-tree-index|B-Tree Index]]
- [[hash-based-sharding|Hash-Based Sharding]]
- [[query-shape-optimization|Query Shape Optimization]]

## Open Questions

- Which future source should compare practical hash-index support across common databases?
