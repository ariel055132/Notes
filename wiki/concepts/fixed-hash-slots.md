---
type: concept
aliases: ["fixed slots", "hash slots", "Redis Cluster slots", "slot-based sharding"]
tags: [system-design, load-distribution, sharding, caching]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Fixed Hash Slots

## Definition

Fixed hash slots are a key-ownership strategy where the hash space is divided into a fixed number of logical slots, and those slots are assigned to physical nodes. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Scope

This concept covers stable ownership through an intermediate slot layer, such as Redis Cluster's `CRC16(key) % 16384` slot calculation. [[2026-05-15--consistent-hashing|Consistent Hashing]] Like consistent hashing, fixed hash slots aim to avoid full key remapping when cluster membership changes; instead of changing the key-to-slot mapping, the system moves slot ownership among nodes. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Contrasts

- **Consistent Hashing**: Consistent hashing uses node positions on a ring to determine ranges, while fixed hash slots first divide the key space into stable buckets or slots and then assign slot ranges to nodes. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Modulo Hashing by Node Count**: Fixed hash slots keep the key-to-slot mapping stable, while `hash(key) % node_count` changes the mapping whenever the node count changes. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Evidence

- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source uses Redis Cluster's fixed slot design as an example of a production pattern that addresses the same stable key-ownership problem as consistent hashing.

## Related

- [[consistent-hashing|Consistent Hashing]]
- [[virtual-buckets|Virtual Buckets]]
- [[hash-based-sharding|Hash-Based Sharding]]
- [[resharding|Resharding]]
- [[application-level-caching|Application-Level Caching]]

## Open Questions

- Which future source should compare Redis Cluster hash slots with Cassandra-style token ranges?
