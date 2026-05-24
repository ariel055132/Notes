---
type: concept
aliases: ["hot keys", "hot cache key", "hot shard", "access skew"]
tags: [system-design, caching, distributed-cache, load-distribution]
created: 2026-05-24
updated: 2026-05-25
source_count: 5
---

# Hot Key

## Definition

A hot key is a cache key, database row, shard partition, or content object that receives disproportionately high request volume and can overload a single serving path. [[2026-05-14--scaling-reads|Scaling Reads]] In sharded systems, a hot key can create a hot shard even when data volume is evenly distributed. [[2026-05-15--sharding|Sharding]] In cache systems, a hot key can overload one Redis node, one cache shard, or one backend rebuild path despite a high overall cache hit rate. [[2026-05-24--caching|Caching]] Consistent hashing and distributed cache routing can distribute key ownership, but they cannot make one extremely popular key stop being concentrated on its owner. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers access skew, single-key overload, cache-shard pressure, hot shards, local cache, request coalescing, key fanout, dedicated replicas or cache pools, CDN edge cache, compound event keys, queue or single-writer serialization, rate limiting, and graceful degradation of nonessential fields. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-15--sharding|Sharding]] [[2026-05-24--caching|Caching]] The consistent-hashing and distributed-cache sources add the operational warning that key-count balance is not traffic balance, so systems should monitor per-key QPS, per-shard latency, top miss keys, and database fallback rate instead of only per-node key counts. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **Cache hit rate**: A high cache hit rate can still fail if most hits target one overloaded key or shard. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache Stampede**: A hot key is sustained concentration on one key, while a cache stampede is a synchronized miss or expiration event that floods the backend. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Even sharding**: Even data distribution does not guarantee even traffic distribution when one key or object receives disproportionate demand. [[2026-05-15--sharding|Sharding]]
- **Consistent Hashing**: Consistent hashing reduces broad key remapping when nodes change, but a single hot key can still overload its assigned owner. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Distributed Cache**: Distributed cache spreads many keys across nodes, but hot keys need explicit mitigation such as local cache, key replication, key splitting, or CDN. [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source uses QR codes and market snapshots to show how one popular key can overload Redis or backend infrastructure even when data is cached.
- [[2026-05-15--sharding|Sharding]] — The source uses popular videos, markets, QR codes, and events to show that one shard can receive most traffic because it owns a hot key.
- [[2026-05-24--caching|Caching]] — The source identifies large-event QR tokens, hot markets, viral video metadata, and city-center availability snapshots as cache hot-key examples.
- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source explicitly warns that consistent hashing can balance key counts without balancing traffic, and recommends replicas, key splitting, local cache, CDN, and per-key QPS monitoring.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source uses QR redirect tokens and cache shards to show that a hot key can overload one distributed-cache owner despite healthy cluster-wide capacity.

## Related

- [[read-scaling|Read Scaling]]
- [[application-level-caching|Application-Level Caching]]
- [[in-process-cache|In-Process Cache]]
- [[request-coalescing|Request Coalescing]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[database-sharding|Database Sharding]]
- [[shard-key|Shard Key]]
- [[directory-based-sharding|Directory-Based Sharding]]
- [[cache-stampede|Cache Stampede]]
- [[consistent-hashing|Consistent Hashing]]
- [[virtual-nodes|Virtual Nodes]]
- [[distributed-cache|Distributed Cache]]
- [[cache-replication|Cache Replication]]

## Open Questions

- Which future notes should compare key fanout, local cache, and request coalescing under real production constraints?
