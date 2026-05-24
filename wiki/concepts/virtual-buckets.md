---
type: concept
aliases: ["virtual shards", "logical buckets", "virtual partitions"]
tags: [system-design, databases, sharding]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Virtual Buckets

## Definition

Virtual buckets are logical partitions that sit between shard keys and physical shards, letting the system map many stable buckets onto fewer physical database shards. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers routing a key to a large number of virtual buckets, then assigning those buckets to physical shards through a mapping layer. [[2026-05-15--sharding|Sharding]] When adding shards, the system can move only some buckets instead of recalculating and moving most keys. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Modulo Hashing**: Direct `hash(key) % shard_count` can remap many keys when the shard count changes, while virtual buckets keep key-to-bucket mapping stable and move bucket ownership instead. [[2026-05-15--sharding|Sharding]]
- **Directory-Based Sharding**: Virtual buckets map bucket IDs to shards, while directory-based sharding may map individual tenants, keys, or special hot objects to shards. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source recommends virtual buckets as a production pattern to reduce data movement when adding shards.

## Related

- [[database-sharding|Database Sharding]]
- [[hash-based-sharding|Hash-Based Sharding]]
- [[consistent-hashing|Consistent Hashing]]
- [[directory-based-sharding|Directory-Based Sharding]]
- [[resharding|Resharding]]

## Open Questions

- Which future source should describe bucket movement workflows with dual writes, change data capture, and checksums?
