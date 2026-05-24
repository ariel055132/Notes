---
type: concept
aliases: ["LSM tree", "log-structured merge tree", "LSM-based store"]
tags: [system-design, databases, indexing, storage]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# LSM Tree

## Definition

An LSM tree is a write-optimized storage/indexing structure suited to append-heavy workloads by buffering and merging writes over time. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers event logs, time-series data, delivery attempts, and other append-heavy workloads where write throughput matters and reads must be designed around compaction and storage layout. [[2026-05-15--database-indexing|Database Indexing]] The source treats LSM-tree access patterns as a different fit than simply adding B-tree indexes to high-write relational tables. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **B-Tree Index**: B-tree indexes are common general-purpose relational indexes, while LSM trees are more explicitly optimized for high write throughput and later compaction. [[2026-05-15--database-indexing|Database Indexing]]
- **Write-Behind Cache**: Write-behind cache buffers writes outside the database and flushes asynchronously, while LSM-tree systems are durable storage/index structures designed around write-heavy persistence. [[2026-05-24--caching|Caching]] [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source names event logs, time-series data, and delivery attempts as append-heavy workloads where LSM-style access patterns fit.

## Related

- [[database-indexing|Database Indexing]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[write-behind-cache|Write-Behind Cache]]
- [[database-sharding|Database Sharding]]

## Open Questions

- Which future source should explain compaction, read amplification, and write amplification in LSM systems?
