---
type: concept
aliases: ["wide-column database", "column-family store", "column family store"]
tags: [system-design, databases, nosql, write-scaling]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Wide-Column Store

## Definition

A wide-column store organizes rows by column families, allowing rows to have different field sets while optimizing storage and access around known primary-key and column-family patterns. [[2026-04-15--database|Database]]

## Scope

This concept covers high-write-throughput OLTP workloads, time-series-like data, and large-scale systems with clear access patterns. [[2026-04-15--database|Database]] The source uses Cassandra as the example: it favors write-anywhere behavior, high write throughput, no single point of failure, and eventual consistency, but it is not a general analytical database for cross-row aggregation. [[2026-04-15--database|Database]]

## Contrasts

- **OLAP**: A wide-column OLTP store such as Cassandra is row/access-pattern oriented and not the same as a column-oriented analytical warehouse. [[2026-04-15--database|Database]]
- **Relational Database**: Wide-column stores can scale writes and tolerate flexible sparse rows, while relational databases provide stronger general-purpose SQL, joins, constraints, and ACID behavior. [[2026-04-15--database|Database]]
- **Database Sharding**: Wide-column systems often bake partitioned access into the model, while sharding is a broader distribution technique that can apply to many database designs. [[2026-04-15--database|Database]] [[database-sharding|Database Sharding]]

## Evidence

- [[2026-04-15--database|Database]] — The source describes wide-column stores by column families and positions Cassandra as high-write-throughput OLTP with clear access patterns, not OLAP.

## Related

- [[nosql-database|NoSQL Database]]
- [[oltp|OLTP]]
- [[base-consistency-model|BASE Consistency Model]]
- [[database-workload|Database Workload]]
- [[database-sharding|Database Sharding]]
- [[replication|Replication]]

## Open Questions

- Which future source should explain Cassandra partition-key design and query modeling?
