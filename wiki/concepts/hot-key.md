---
type: concept
aliases: ["hot keys", "hot cache key", "hot shard", "access skew"]
tags: [system-design, caching, load-distribution]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Hot Key

## Definition

A hot key is a cache key, database row, shard partition, or content object that receives disproportionately high request volume and can overload a single serving path. [[2026-05-14--scaling-reads|Scaling Reads]] In sharded systems, a hot key can create a hot shard even when data volume is evenly distributed. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers access skew, single-key overload, cache-shard pressure, hot shards, local cache, request coalescing, key fanout, CDN edge cache, compound event keys, queue or single-writer serialization, and graceful degradation of nonessential fields. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Cache hit rate**: A high cache hit rate can still fail if most hits target one overloaded key or shard. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache Stampede**: A hot key is sustained concentration on one key, while a cache stampede is a synchronized miss or expiration event that floods the backend. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Even sharding**: Even data distribution does not guarantee even traffic distribution when one key or object receives disproportionate demand. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source uses QR codes and market snapshots to show how one popular key can overload Redis or backend infrastructure even when data is cached.
- [[2026-05-15--sharding|Sharding]] — The source uses popular videos, markets, QR codes, and events to show that one shard can receive most traffic because it owns a hot key.

## Related

- [[read-scaling|Read Scaling]]
- [[application-level-caching|Application-Level Caching]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[database-sharding|Database Sharding]]
- [[shard-key|Shard Key]]
- [[directory-based-sharding|Directory-Based Sharding]]
- [[cache-stampede|Cache Stampede]]

## Open Questions

- Which future notes should compare key fanout, local cache, and request coalescing under real production constraints?
