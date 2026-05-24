---
type: concept
aliases: ["cache prewarming", "cache pre-warming", "warm cache", "cache warmup"]
tags: [system-design, caching, distributed-cache, reliability]
created: 2026-05-24
updated: 2026-05-25
source_count: 2
---

# Cache Warming

## Definition

Cache warming is proactively loading or refreshing cache entries before user traffic needs them. [[2026-05-24--caching|Caching]] In distributed cache, it is especially important after new nodes, restarts, slot migration, or region failover create cold ownership ranges. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers refreshing known-hot data ahead of expiration, preloading cache after deploys or purges, gradual traffic shifting to new cache nodes, and reducing cold-start or stampede risk for popular pages, market snapshots, QR codes, or media metadata. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] It requires knowing or predicting which keys matter and does not replace invalidation or source-of-truth checks for correctness-critical data. [[2026-05-24--caching|Caching]]

## Contrasts

- **Cache-Aside**: Cache-aside fills cache reactively on misses, while cache warming fills cache proactively before misses occur. [[2026-05-24--caching|Caching]]
- **Stale-While-Revalidate**: Cache warming refreshes before demand, while stale-while-revalidate can refresh after serving stale data. [[2026-05-24--caching|Caching]]
- **Cache Routing**: Cache routing changes can create cold ranges, while cache warming makes those ranges safer before full traffic arrives. [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source lists cache warming as a defense against stampedes and avalanche-like traffic spikes.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source recommends warmup and gradual traffic shifting after cache node changes to avoid database fallback spikes.

## Related

- [[cache-stampede|Cache Stampede]]
- [[cache-avalanche|Cache Avalanche]]
- [[ttl-jitter|TTL Jitter]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[hot-key|Hot Key]]
- [[distributed-cache|Distributed Cache]]
- [[cache-routing|Cache Routing]]

## Open Questions

- Which future source should cover workload prediction and warmup ordering for large caches?
