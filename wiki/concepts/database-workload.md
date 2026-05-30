---
type: concept
aliases: ["workload", "database workload", "query workload", "access pattern"]
tags: [system-design, databases, workload]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Database Workload

## Definition

A database workload is the pattern of reads, writes, scans, joins, aggregations, latency needs, concurrency, and consistency requirements that a database must handle. [[2026-04-15--database|Database]]

## Scope

This concept covers the second major axis of database selection: whether the system primarily handles high-concurrency transactional point reads and small writes, historical analytical scans and aggregations, high-throughput writes with known access patterns, or similarity search over embeddings. [[2026-04-15--database|Database]] Workload should be evaluated together with the data model because the same product category can be a poor fit if the access pattern is wrong. [[2026-04-15--database|Database]]

## Contrasts

- **Data Model**: Data model asks what the data looks like, while workload asks how the system reads and writes it. [[2026-04-15--database|Database]]
- **Read Scaling**: Workload describes the demand pattern, while read scaling is one set of techniques for serving read-heavy workloads. [[2026-04-15--database|Database]] [[read-scaling|Read Scaling]]

## Evidence

- [[2026-04-15--database|Database]] — The source frames OLTP versus OLAP as a workload dimension independent from relational versus NoSQL data models.

## Related

- [[database-selection|Database Selection]]
- [[oltp|OLTP]]
- [[olap|OLAP]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[read-scaling|Read Scaling]]
- [[database-indexing|Database Indexing]]
- [[database-sharding|Database Sharding]]
- [[application-level-caching|Application-Level Caching]]

## Open Questions

- Which future source should define write-heavy workload patterns separately from read scaling?
