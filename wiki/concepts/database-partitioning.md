---
type: concept
aliases: ["partitioning", "table partitioning", "database partitions"]
tags: [system-design, databases, partitioning]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Database Partitioning

## Definition

Database partitioning splits a large table or dataset into partitions inside the same database instance so the database can manage scans, indexes, vacuuming, archiving, or maintenance more efficiently. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers intra-database table partitioning where the data remains on one database machine or instance. [[2026-05-15--sharding|Sharding]] It can reduce scan cost and improve large-table operations, but it does not break through the CPU, memory, disk, connection, or failure boundary of a single database machine. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Database Sharding**: Partitioning splits data inside one database instance, while sharding splits the logical dataset across multiple database machines or clusters. [[2026-05-15--sharding|Sharding]]
- **Replication**: Partitioning divides data into subsets, while replication keeps copies of the same data on multiple machines. [[2026-05-15--sharding|Sharding]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source explicitly separates partitioning from sharding and describes partitioning as useful for large-table management and range-oriented operations inside one database.

## Related

- [[database-sharding|Database Sharding]]
- [[replication|Replication]]
- [[range-based-sharding|Range-Based Sharding]]
- [[database-indexing|Database Indexing]]

## Open Questions

- Which future source should cover native partitioning features in PostgreSQL, MySQL, and managed databases?
