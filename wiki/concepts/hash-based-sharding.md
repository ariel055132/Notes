---
type: concept
aliases: ["hash sharding", "hashed sharding"]
tags: [system-design, databases, sharding]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Hash-Based Sharding

## Definition

Hash-based sharding hashes a shard key and maps the hash result to a shard, usually to spread records more evenly across shards. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers formulas such as `hash(user_id) % shard_count`, the benefit of relatively even distribution, and the costs of making range queries harder and moving many keys when the shard count changes. [[2026-05-15--sharding|Sharding]] Production systems often combine hash-based routing with virtual buckets or consistent hashing to make later resharding less disruptive. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Range-Based Sharding**: Hash-based sharding spreads keys and reduces range hot spots, while range-based sharding keeps adjacent keys together and supports range scans. [[2026-05-15--sharding|Sharding]]
- **Directory-Based Sharding**: Hash-based sharding derives the shard from a function, while directory-based sharding looks up a key-to-shard mapping. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source presents hash sharding as a common default but warns that modulo-based routing makes shard-count changes expensive.

## Related

- [[database-sharding|Database Sharding]]
- [[shard-key|Shard Key]]
- [[virtual-buckets|Virtual Buckets]]
- [[consistent-hashing|Consistent Hashing]]
- [[range-based-sharding|Range-Based Sharding]]

## Open Questions

- Which future source should quantify remapping costs for modulo hashing versus consistent hashing?
