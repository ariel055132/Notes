---
type: concept
aliases: ["range sharding", "range partitioning across shards"]
tags: [system-design, databases, sharding]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Range-Based Sharding

## Definition

Range-based sharding assigns contiguous ranges of a shard key to different shards. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers shard layouts such as one shard owning IDs 0 through 9,999,999 and another owning the next range. [[2026-05-15--sharding|Sharding]] It is easy to understand and can support range scans, but it can create hot shards when the key grows with time and new writes all land in the newest range. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Hash-Based Sharding**: Range-based sharding preserves key locality and range scans, while hash-based sharding spreads keys more evenly but makes range queries harder. [[2026-05-15--sharding|Sharding]]
- **Database Partitioning**: Range-based sharding distributes ranges across machines, while range partitioning inside one database remains within one machine boundary. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source uses ID ranges as the basic sharding illustration and warns that time-correlated keys such as creation time can concentrate new writes on the latest shard.

## Related

- [[database-sharding|Database Sharding]]
- [[database-partitioning|Database Partitioning]]
- [[shard-key|Shard Key]]
- [[hot-key|Hot Key]]
- [[hash-based-sharding|Hash-Based Sharding]]

## Open Questions

- Which time-series workloads justify range sharding despite hot-range risk?
