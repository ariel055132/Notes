---
type: concept
aliases: ["cache key routing", "cache ownership", "cache shard routing", "cache shard map"]
tags: [system-design, distributed-cache, distributed-queue, caching, routing]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Cache Routing

## Definition

Cache routing is the process of mapping a cache key to the cache shard or node responsible for serving that key. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers ownership mechanisms such as shard maps, hash slots, and consistent hashing in distributed cache clusters. [[2026-05-15--distributed-cache|Distributed Cache]] The source emphasizes that naive `hash(cache_key) % shard_count` can cause broad cache misses when shard count changes, so production routing should limit remapping during expansion or shrinkage and protect the database during warmup. [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **Consistent Hashing**: Consistent hashing is one cache-routing strategy designed to limit key remapping when nodes change. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--distributed-cache|Distributed Cache]]
- **Fixed Hash Slots**: Fixed hash slots route keys through stable slots before assigning slot ownership to nodes, while cache routing is the broader ownership problem. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-15--distributed-cache|Distributed Cache]] — The source presents `cache key -> routing rule -> owner shard` as the new ownership layer introduced by distributed cache.

## Related

- [[distributed-cache|Distributed Cache]]
- [[consistent-hashing|Consistent Hashing]]
- [[fixed-hash-slots|Fixed Hash Slots]]
- [[hot-key|Hot Key]]
- [[cache-warming|Cache Warming]]

## Open Questions

- Which future source should document client-side cache sharding versus server-side cluster routing?
