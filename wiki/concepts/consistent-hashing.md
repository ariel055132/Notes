---
type: concept
aliases: ["consistent hash", "consistent hash ring"]
tags: [system-design, databases, sharding, load-distribution]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Consistent Hashing

## Definition

Consistent hashing is a key-to-node mapping strategy designed to limit how many keys move when shards or nodes are added or removed. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers using hashing to distribute ownership while reducing remapping compared with direct modulo by shard count. [[2026-05-15--sharding|Sharding]] In the source, it appears as one of the ways to reduce future resharding cost alongside virtual buckets and directory mapping. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Virtual Buckets**: Both reduce movement during resharding; virtual buckets emphasize a logical bucket mapping, while consistent hashing emphasizes a hash-space mapping that changes minimally as nodes change. [[2026-05-15--sharding|Sharding]]
- **Directory-Based Sharding**: Consistent hashing derives placement algorithmically, while directory-based sharding stores explicit placement metadata. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source lists consistent hashing as a design option when future resharding cost makes direct modulo hashing risky.

## Related

- [[hash-based-sharding|Hash-Based Sharding]]
- [[virtual-buckets|Virtual Buckets]]
- [[resharding|Resharding]]
- [[database-sharding|Database Sharding]]

## Open Questions

- Which future source should detail consistent-hash rings, virtual nodes, and load balancing under uneven traffic?
