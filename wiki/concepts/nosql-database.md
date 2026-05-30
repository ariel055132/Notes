---
type: concept
aliases: ["NoSQL", "Not Only SQL", "non-relational database"]
tags: [system-design, databases, nosql]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# NoSQL Database

## Definition

NoSQL database is an umbrella category for non-relational or less-relational database designs that trade parts of the relational model, SQL interface, or strong consistency for flexible data structures, horizontal scale, or specialized access patterns. [[2026-04-15--database|Database]]

## Scope

This concept covers key-value stores, document stores, wide-column stores, and graph databases as separate families rather than one interchangeable technology. [[2026-04-15--database|Database]] The source describes DynamoDB as a managed key-value and document-style option for high-concurrency low-latency OLTP, Redis as a low-latency key-value store with rich structures, Cassandra as a high-write-throughput wide-column OLTP system, MongoDB as a document-store example, and Neo4j as a graph-database example. [[2026-04-15--database|Database]]

## Contrasts

- **Relational Database**: Relational databases emphasize schema, SQL, constraints, and ACID, while NoSQL systems often optimize for horizontal scaling, flexible shape, or access-pattern-specific performance. [[2026-04-15--database|Database]]
- **BASE Consistency Model**: BASE is a common consistency framing for NoSQL systems, while NoSQL is the broader database-family category. [[2026-04-15--database|Database]]
- **OLAP**: NoSQL systems such as Cassandra can serve OLTP access patterns and are not automatically analytical systems. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source explicitly says NoSQL is not one thing but a set of database designs with different data models and tradeoffs.

## Related

- [[key-value-store|Key-Value Store]]
- [[document-store|Document Store]]
- [[wide-column-store|Wide-Column Store]]
- [[graph-database|Graph Database]]
- [[base-consistency-model|BASE Consistency Model]]
- [[database-selection|Database Selection]]
- [[database-sharding|Database Sharding]]
- [[replication|Replication]]
- [[oltp|OLTP]]

## Open Questions

- Which future source should compare DynamoDB, Cassandra, MongoDB, and Redis in depth by consistency, partitioning, indexing, pricing, and operation model?
