---
type: concept
aliases: ["databases", "storage database", "database system"]
tags: [system-design, databases, storage]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Database

## Definition

A database is a system for storing and querying data, but in system design the useful question is which database model and workload fit the product's access patterns, consistency needs, scale, and operational constraints. [[2026-04-15--database|Database]]

## Scope

This concept is a hub for database choice in system design: data shape, query pattern, OLTP versus OLAP workload, transaction guarantees, scaling path, index needs, cache boundaries, and when not to put data in a database at all. [[2026-04-15--database|Database]] The source treats products such as PostgreSQL, DynamoDB, Redis, Cassandra, MongoDB, Neo4j, ClickHouse, BigQuery, Redshift, Pinecone, Weaviate, and Milvus as examples of design positions rather than as interchangeable database names. [[2026-04-15--database|Database]]

## Contrasts

- **Object Storage**: A database serves structured or queryable state, while object storage is usually a better fit for images, video, PDFs, and other large blobs. [[2026-04-15--database|Database]] [[object-storage|Object Storage]]
- **Application-Level Caching**: A database is normally the source of truth for application state, while cache is a read-path acceleration layer with freshness and invalidation tradeoffs. [[2026-04-15--database|Database]] [[application-level-caching|Application-Level Caching]]
- **Database Selection**: Database is the system category, while database selection is the decision framework for choosing among database families and products. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source frames databases as a map of data models and workloads, then advises choosing from requirements rather than starting with product comparisons.

## Related

- [[database-selection|Database Selection]]
- [[data-model|Data Model]]
- [[database-workload|Database Workload]]
- [[relational-database|Relational Database]]
- [[nosql-database|NoSQL Database]]
- [[oltp|OLTP]]
- [[olap|OLAP]]
- [[vector-database|Vector Database]]
- [[database-transactions|Database Transactions]]
- [[database-indexing|Database Indexing]]
- [[database-sharding|Database Sharding]]
- [[read-scaling|Read Scaling]]
- [[replication|Replication]]
- [[application-level-caching|Application-Level Caching]]
- [[object-storage|Object Storage]]

## Open Questions

- Should the wiki add a system-design map page that groups all database, cache, queue, CDN, coordination, and messaging concepts into sections for Obsidian navigation?
