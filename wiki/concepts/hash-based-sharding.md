---
type: concept
aliases: ["hash sharding", "hashed sharding"]
tags: [system-design, databases, sharding]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Hash-Based Sharding

## Definition

Hash-based sharding hashes a shard key and maps the hash result to a shard or owner, usually to spread records more evenly across shards or serving nodes. [[2026-05-15--sharding|Sharding]] [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Scope

This concept covers formulas such as `hash(user_id) % shard_count`, the benefit of relatively even distribution, and the costs of making range queries harder and moving many keys when the shard count changes. [[2026-05-15--sharding|Sharding]] The consistent-hashing source gives the routing-layer version of the same issue: direct modulo works only while node count is stable, and changing `N` can cause broad cache misses, data movement, or connection redistribution. [[2026-05-15--consistent-hashing|Consistent Hashing]] Production systems often combine hash-based routing with virtual buckets, fixed hash slots, or consistent hashing to make later resharding less disruptive. [[2026-05-15--sharding|Sharding]] [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Contrasts

- **Range-Based Sharding**: Hash-based sharding spreads keys and reduces range hot spots, while range-based sharding keeps adjacent keys together and supports range scans. [[2026-05-15--sharding|Sharding]]
- **Consistent Hashing**: Naive hash-based sharding can remap many keys when `N` changes, while consistent hashing limits remapping to affected ring ranges. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Directory-Based Sharding**: Hash-based sharding derives the shard from a function, while directory-based sharding looks up a key-to-shard mapping. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source presents hash sharding as a common default but warns that modulo-based routing makes shard-count changes expensive.
- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source shows why `hash(key) % N` can remap most keys after node-count changes and motivates consistent hashing or fixed slots.

## Related

- [[database-sharding|Database Sharding]]
- [[shard-key|Shard Key]]
- [[virtual-buckets|Virtual Buckets]]
- [[consistent-hashing|Consistent Hashing]]
- [[fixed-hash-slots|Fixed Hash Slots]]
- [[range-based-sharding|Range-Based Sharding]]

## Open Questions

- Which future source should quantify remapping costs for modulo hashing versus consistent hashing?
