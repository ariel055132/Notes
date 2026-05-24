---
type: concept
aliases: ["re-sharding", "shard rebalancing", "shard migration"]
tags: [system-design, databases, sharding, operations]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Resharding

## Definition

Resharding is the process of changing shard layout by moving data, buckets, ranges, or ownership mappings when capacity, traffic, membership, or placement requirements change. [[2026-05-15--sharding|Sharding]] [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Scope

This concept covers adding shards, moving virtual buckets, updating routing maps, dual writing or using change data capture during migration, validating with shadow reads or checksums, and preserving rollback paths. [[2026-05-15--sharding|Sharding]] It is often the hardest part of sharding because the initial split is less important than the system's ability to change the split later. [[2026-05-15--sharding|Sharding]] The consistent-hashing source adds the routing perspective: membership changes should affect only limited key ranges, but actual data copy, cache warmup, replication, and failure handling still require separate mechanisms. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Contrasts

- **Initial Sharding**: Initial sharding picks a layout, while resharding changes a live layout without losing data or breaking routing. [[2026-05-15--sharding|Sharding]]
- **Replica Catch-Up**: Resharding changes data ownership across shards, while replica catch-up copies missed changes to an existing replica of the same dataset. [[2026-05-15--sharding|Sharding]] [[2026-05-02--replication|Replication]]
- **Consistent Hashing**: Consistent hashing limits routing remaps during membership changes, while resharding includes the operational work of moving or rebuilding data behind the new routing decision. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source recommends virtual buckets, routing-layer mappings, partial bucket movement, dual write or CDC, shadow reads, checksums, and rollback planning for resharding.
- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source explains that adding or removing nodes changes only adjacent ownership ranges, but still needs rebalancing, warmup, replicas, or recomputation.

## Related

- [[database-sharding|Database Sharding]]
- [[virtual-buckets|Virtual Buckets]]
- [[consistent-hashing|Consistent Hashing]]
- [[fixed-hash-slots|Fixed Hash Slots]]
- [[virtual-nodes|Virtual Nodes]]
- [[directory-based-sharding|Directory-Based Sharding]]
- [[replication-log|Replication Log]]

## Open Questions

- Which future source should explain live migration runbooks for resharding production databases?
