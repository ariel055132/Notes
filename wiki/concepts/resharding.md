---
type: concept
aliases: ["re-sharding", "shard rebalancing", "shard migration"]
tags: [system-design, databases, sharding, operations]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Resharding

## Definition

Resharding is the process of changing shard layout by moving data, buckets, or ownership mappings when capacity, traffic, or placement requirements change. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers adding shards, moving virtual buckets, updating routing maps, dual writing or using change data capture during migration, validating with shadow reads or checksums, and preserving rollback paths. [[2026-05-15--sharding|Sharding]] It is often the hardest part of sharding because the initial split is less important than the system's ability to change the split later. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Initial Sharding**: Initial sharding picks a layout, while resharding changes a live layout without losing data or breaking routing. [[2026-05-15--sharding|Sharding]]
- **Replica Catch-Up**: Resharding changes data ownership across shards, while replica catch-up copies missed changes to an existing replica of the same dataset. [[2026-05-15--sharding|Sharding]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source recommends virtual buckets, routing-layer mappings, partial bucket movement, dual write or CDC, shadow reads, checksums, and rollback planning for resharding.

## Related

- [[database-sharding|Database Sharding]]
- [[virtual-buckets|Virtual Buckets]]
- [[consistent-hashing|Consistent Hashing]]
- [[directory-based-sharding|Directory-Based Sharding]]
- [[replication-log|Replication Log]]

## Open Questions

- Which future source should explain live migration runbooks for resharding production databases?
