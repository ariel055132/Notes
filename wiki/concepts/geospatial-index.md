---
type: concept
aliases: ["geo index", "spatial index", "geographic index", "geospatial indexes"]
tags: [system-design, databases, indexing, geospatial]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Geospatial Index

## Definition

A geospatial index is an index designed for spatial queries such as nearby search, map viewport lookup, or polygon intersection. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers location-oriented query paths such as Airbnb map search and Robotaxi pickup or availability search. [[2026-05-15--database-indexing|Database Indexing]] It is a specialized index family because ordinary equality or range indexes do not directly model spatial proximity and shape relationships. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **B-Tree Index**: B-tree indexes handle equality, range, and sort order on scalar values, while geospatial indexes handle spatial relationships. [[2026-05-15--database-indexing|Database Indexing]]
- **Directory-Based Sharding**: Geospatial indexes accelerate spatial queries, while region or geohash sharding assigns ownership or routing boundaries across databases. [[2026-05-15--database-indexing|Database Indexing]] [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source maps Airbnb search and Robotaxi pickup points to geospatial indexing.

## Related

- [[database-indexing|Database Indexing]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[database-sharding|Database Sharding]]
- [[shard-key|Shard Key]]

## Open Questions

- Which future source should compare geohash, R-tree, S2, H3, and database-native geospatial indexes?
