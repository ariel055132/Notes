---
type: concept
aliases: ["sharding", "database shards", "horizontal partitioning"]
tags: [system-design, databases, partitioning]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Database Sharding

## Definition

Database sharding is the practice of splitting one logical dataset across multiple database machines or clusters so each shard owns a subset of the data and handles a portion of the read or write load. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers when to introduce sharding, how to choose shard keys such as user ID, content ID, market ID, home ID, region, or business function, and how to keep common queries and strong-consistency operations on one shard where possible. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--sharding|Sharding]] It also includes operational tradeoffs such as hot keys, scatter-gather queries, cross-shard transactions, resharding, routing directories, virtual buckets, and shard-level observability. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Replication**: Sharding partitions a logical dataset so different shards own different records, while replication copies the same records to multiple machines for latency, availability, or read throughput. [[2026-05-15--sharding|Sharding]] [[2026-05-02--replication|Replication]]
- **Read Replica**: A read replica duplicates the dataset or a shard's dataset, while sharding partitions the dataset. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--sharding|Sharding]]
- **Database Partitioning**: Partitioning splits data inside one database instance, while sharding splits data across database machines or clusters. [[2026-05-15--sharding|Sharding]]
- **Application-Level Caching**: Sharding reduces database working-set and load per shard, while caching avoids database access for repeated reads. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source presents sharding as useful when data size or working set exceeds what a single database can handle, but not usually as the first read-scaling move.
- [[2026-05-15--sharding|Sharding]] — The source frames sharding as a later-stage scaling move for capacity, throughput, and operations, with shard-key choice driven by access patterns and invariants rather than even distribution alone.

## Related

- [[read-scaling|Read Scaling]]
- [[replication|Replication]]
- [[read-replica|Read Replica]]
- [[database-partitioning|Database Partitioning]]
- [[shard-key|Shard Key]]
- [[single-shard-transaction|Single-Shard Transaction]]
- [[cross-shard-transaction|Cross-Shard Transaction]]
- [[scatter-gather-query|Scatter-Gather Query]]
- [[resharding|Resharding]]
- [[hot-key|Hot Key]]
- [[database-indexing|Database Indexing]]

## Open Questions

- Which future examples should be filed for user feeds, order history, market data, and geospatial dispatch?
