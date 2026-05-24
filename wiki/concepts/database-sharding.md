---
type: concept
aliases: ["sharding", "database partitioning", "partition key"]
tags: [system-design, databases, partitioning]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Database Sharding

## Definition

Database sharding is the practice of splitting data across multiple databases so each shard handles a smaller dataset and a portion of the read load. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers choosing shard keys such as user ID, content ID, market ID, region, or business function, while avoiding read paths that must scatter-gather across many shards. [[2026-05-14--scaling-reads|Scaling Reads]] It also includes operational trade-offs such as data movement, cross-shard queries, transactions, rebalancing, and hot shard risk. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Read Replica**: A read replica duplicates the dataset, while sharding partitions the dataset. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Application-Level Caching**: Sharding reduces database working-set and load per shard, while caching avoids database access for repeated reads. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source presents sharding as useful when data size or working set exceeds what a single database can handle, but not usually as the first read-scaling move.

## Related

- [[read-scaling|Read Scaling]]
- [[read-replica|Read Replica]]
- [[hot-key|Hot Key]]
- [[database-indexing|Database Indexing]]

## Open Questions

- Which sharding examples should be filed for user feeds, order history, and market data?
