---
type: concept
aliases: ["virtual shards", "logical buckets", "virtual partitions"]
tags: [system-design, databases, sharding]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Virtual Buckets

## Definition

Virtual buckets are logical partitions that sit between shard keys and physical shards, letting the system map many stable buckets onto fewer physical database shards. [[2026-05-15--sharding|Sharding]] They are related to fixed hash slots, where keys hash into a stable slot space before slot ownership is assigned to physical nodes. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Scope

This concept covers routing a key to a large number of virtual buckets, then assigning those buckets to physical shards through a mapping layer. [[2026-05-15--sharding|Sharding]] When adding shards, the system can move only some buckets instead of recalculating and moving most keys. [[2026-05-15--sharding|Sharding]] The consistent-hashing source describes the same broad ownership-stability goal in fixed-slot systems such as Redis Cluster: the key-to-slot mapping remains stable while slot ownership changes. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Contrasts

- **Modulo Hashing**: Direct `hash(key) % shard_count` can remap many keys when the shard count changes, while virtual buckets keep key-to-bucket mapping stable and move bucket ownership instead. [[2026-05-15--sharding|Sharding]]
- **Fixed Hash Slots**: Fixed hash slots are a concrete slot-based ownership model; virtual buckets are the broader database-sharding pattern of mapping stable logical partitions onto physical shards. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--sharding|Sharding]]
- **Virtual Nodes**: Virtual nodes put multiple positions for one physical node on a consistent-hash ring, while virtual buckets use stable bucket identifiers and an ownership map. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Directory-Based Sharding**: Virtual buckets map bucket IDs to shards, while directory-based sharding may map individual tenants, keys, or special hot objects to shards. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source recommends virtual buckets as a production pattern to reduce data movement when adding shards.
- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source contrasts hash-ring placement with fixed hash slots, where the key space is cut into stable buckets and slot ranges move between nodes.

## Related

- [[database-sharding|Database Sharding]]
- [[hash-based-sharding|Hash-Based Sharding]]
- [[consistent-hashing|Consistent Hashing]]
- [[fixed-hash-slots|Fixed Hash Slots]]
- [[virtual-nodes|Virtual Nodes]]
- [[directory-based-sharding|Directory-Based Sharding]]
- [[resharding|Resharding]]

## Open Questions

- Which future source should describe bucket movement workflows with dual writes, change data capture, and checksums?
