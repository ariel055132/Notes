---
type: concept
aliases: ["consistent hash", "consistent hash ring"]
tags: [system-design, databases, sharding, load-distribution]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Consistent Hashing

## Definition

Consistent hashing is a key-to-owner mapping strategy designed to keep most keys on the same owner when shards, cache nodes, gateways, workers, or other serving nodes are added or removed. [[2026-05-15--sharding|Sharding]] [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Scope

This concept covers stable ownership for distributed caches, shard routing, rate limiter counters, WebSocket room owners, CDN or internal cache asset routing, and similar routing layers where the same key should usually go to the same owner. [[2026-05-15--consistent-hashing|Consistent Hashing]] Instead of routing with `hash(key) % number_of_nodes`, consistent hashing places keys and nodes in one hash space, often visualized as a ring, and assigns each key to the first node found clockwise from the key. [[2026-05-15--consistent-hashing|Consistent Hashing]] In the sharding source, it appears as one way to reduce future resharding cost alongside virtual buckets and directory mapping. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Virtual Buckets**: Both reduce movement during resharding; virtual buckets emphasize a logical bucket mapping, while consistent hashing emphasizes a hash-space mapping that changes minimally as nodes change. [[2026-05-15--sharding|Sharding]]
- **Virtual Nodes**: Consistent hashing is the ownership strategy; virtual nodes are a practical ring technique that gives each physical node multiple positions for better balance and finer movement. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Fixed Hash Slots**: Both avoid broad remapping on membership change; fixed hash slots use a stable slot layer, while consistent hashing uses ring positions and clockwise ownership. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Directory-Based Sharding**: Consistent hashing derives placement algorithmically, while directory-based sharding stores explicit placement metadata. [[2026-05-15--sharding|Sharding]]
- **Hot Key**: Consistent hashing can distribute key count, but it does not guarantee traffic is evenly distributed when one key is disproportionately popular. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source lists consistent hashing as a design option when future resharding cost makes direct modulo hashing risky.
- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source explains hash rings, virtual nodes, cache and ownership-routing use cases, fixed hash slots, and limits around hot keys, replication, failover, and consistency.

## Related

- [[hash-based-sharding|Hash-Based Sharding]]
- [[virtual-nodes|Virtual Nodes]]
- [[fixed-hash-slots|Fixed Hash Slots]]
- [[virtual-buckets|Virtual Buckets]]
- [[resharding|Resharding]]
- [[database-sharding|Database Sharding]]
- [[application-level-caching|Application-Level Caching]]
- [[hot-key|Hot Key]]

## Open Questions

- Which future source should detail membership protocols, health checks, and safe data movement for consistent-hash routing layers?
