---
type: concept
aliases: ["database choice", "choosing a database", "database selection framework"]
tags: [system-design, databases, architecture]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Database Selection

## Definition

Database selection is the system-design process of choosing a storage technology by deriving requirements from data shape, query pattern, workload type, consistency needs, scale, and operational constraints. [[2026-04-15--database|Database]]

## Scope

This concept covers the interview and architecture workflow for choosing among relational databases, NoSQL families, OLTP stores, OLAP warehouses, vector databases, caches, and object storage. [[2026-04-15--database|Database]] It starts with questions such as whether the data is tabular, document-shaped, key-addressed, highly connected, or embedding-based; whether the workload is transactional or analytical; and whether strong consistency, flexible schema, managed scale, write throughput, or semantic search is the dominant need. [[2026-04-15--database|Database]]

## Contrasts

- **SQL vs NoSQL Comparison**: SQL versus NoSQL is a late comparison; the source recommends first deriving the choice from data shape, query pattern, workload, consistency, and scale. [[2026-04-15--database|Database]]
- **Product Memorization**: Product names are examples after the design reasoning, not the starting point for the answer. [[2026-04-15--database|Database]]
- **Read Scaling**: Read scaling optimizes how reads are served, while database selection chooses the primary storage model and workload fit before later scaling layers are added. [[2026-04-15--database|Database]] [[read-scaling|Read Scaling]]

## Evidence

- [[2026-04-15--database|Database]] — The source gives an interview decision path: identify data shape and query pattern, classify OLTP versus OLAP, then explain the scale and consistency tradeoff behind the chosen product.

## Related

- [[database|Database]]
- [[data-model|Data Model]]
- [[database-workload|Database Workload]]
- [[relational-database|Relational Database]]
- [[nosql-database|NoSQL Database]]
- [[oltp|OLTP]]
- [[olap|OLAP]]
- [[vector-database|Vector Database]]
- [[database-indexing|Database Indexing]]
- [[database-sharding|Database Sharding]]
- [[application-level-caching|Application-Level Caching]]
- [[object-storage|Object Storage]]

## Open Questions

- Which future synthesis should compare concrete choices for user profiles, timelines, payments, analytics dashboards, semantic search, and media storage?
