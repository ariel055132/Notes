---
type: concept
aliases: ["cache prewarming", "cache pre-warming", "warm cache", "cache warmup"]
tags: [system-design, caching, reliability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Cache Warming

## Definition

Cache warming is proactively loading or refreshing cache entries before user traffic needs them. [[2026-05-24--caching|Caching]]

## Scope

This concept covers refreshing known-hot data ahead of expiration, preloading cache after deploys or purges, and reducing cold-start or stampede risk for popular pages, market snapshots, QR codes, or media metadata. [[2026-05-24--caching|Caching]] It requires knowing or predicting which keys matter and does not replace invalidation or source-of-truth checks for correctness-critical data. [[2026-05-24--caching|Caching]]

## Contrasts

- **Cache-Aside**: Cache-aside fills cache reactively on misses, while cache warming fills cache proactively before misses occur. [[2026-05-24--caching|Caching]]
- **Stale-While-Revalidate**: Cache warming refreshes before demand, while stale-while-revalidate can refresh after serving stale data. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source lists cache warming as a defense against stampedes and avalanche-like traffic spikes.

## Related

- [[cache-stampede|Cache Stampede]]
- [[cache-avalanche|Cache Avalanche]]
- [[ttl-jitter|TTL Jitter]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[hot-key|Hot Key]]

## Open Questions

- Which future source should cover workload prediction and warmup ordering for large caches?
