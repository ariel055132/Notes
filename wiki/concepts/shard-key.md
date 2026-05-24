---
type: concept
aliases: ["shard keys", "partition key", "routing key"]
tags: [system-design, databases, sharding]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Shard Key

## Definition

A shard key is the value used by the application, router, or database to decide which shard owns a record or request. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers choosing keys with high cardinality, relatively even distribution, and alignment with common access patterns and consistency boundaries. [[2026-05-15--sharding|Sharding]] It also covers the fact that different bounded contexts in the same system may need different shard keys, such as metadata by QR token, scan events by QR code plus time bucket, booking inventory by home ID, and portfolio read models by user ID. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Replication Placement**: A shard key decides which partition of the dataset owns data, while replication placement decides where copies of the same data live. [[2026-05-15--sharding|Sharding]] [[2026-05-02--replication|Replication]]
- **Cache Key**: A cache key identifies a cached answer, while a shard key defines database ownership and routing. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source frames shard-key choice around access patterns, transaction boundaries, hot keys, and resharding cost rather than around even distribution alone.

## Related

- [[database-sharding|Database Sharding]]
- [[single-shard-transaction|Single-Shard Transaction]]
- [[hot-key|Hot Key]]
- [[scatter-gather-query|Scatter-Gather Query]]
- [[resharding|Resharding]]

## Open Questions

- Which future examples should compare user ID, tenant ID, entity ID, region, and time as shard keys under real workloads?
