---
type: concept
aliases: ["cache prewarming", "cache pre-warming", "warm cache", "cache warmup"]
tags: [system-design, caching, distributed-cache, cdn, reliability]
created: 2026-05-24
updated: 2026-05-26
source_count: 3
---

# Cache Warming

## Definition

Cache warming is proactively loading or refreshing cache entries before user traffic needs them. [[2026-05-24--caching|Caching]] In distributed cache, it is especially important after new nodes, restarts, slot migration, or region failover create cold ownership ranges. [[2026-05-15--distributed-cache|Distributed Cache]] In CDN design, warming likely-hot assets before a launch or after a purge can reduce origin miss storms. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Scope

This concept covers refreshing known-hot data ahead of expiration, preloading cache after deploys or purges, gradual traffic shifting to new cache nodes, CDN prewarming for popular assets, and reducing cold-start or stampede risk for popular pages, market snapshots, QR codes, images, video segments, or media metadata. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] It requires knowing or predicting which keys matter and does not replace invalidation or source-of-truth checks for correctness-critical data. [[2026-05-24--caching|Caching]]

## Contrasts

- **Cache-Aside**: Cache-aside fills cache reactively on misses, while cache warming fills cache proactively before misses occur. [[2026-05-24--caching|Caching]]
- **Stale-While-Revalidate**: Cache warming refreshes before demand, while stale-while-revalidate can refresh after serving stale data. [[2026-05-24--caching|Caching]]
- **Cache Routing**: Cache routing changes can create cold ranges, while cache warming makes those ranges safer before full traffic arrives. [[2026-05-15--distributed-cache|Distributed Cache]]
- **CDN Cache-Key Design**: CDN cache-key design determines what should be warmed, while cache warming loads those keys before traffic depends on them. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source lists cache warming as a defense against stampedes and avalanche-like traffic spikes.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source recommends warmup and gradual traffic shifting after cache node changes to avoid database fallback spikes.
- [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] — The source recommends warming popular CDN content and using origin shielding or request coalescing so edge misses do not overwhelm origin.

## Related

- [[cache-stampede|Cache Stampede]]
- [[cache-avalanche|Cache Avalanche]]
- [[ttl-jitter|TTL Jitter]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[hot-key|Hot Key]]
- [[distributed-cache|Distributed Cache]]
- [[cache-routing|Cache Routing]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[cdn-cache-key-design|CDN Cache-Key Design]]

## Open Questions

- Which future source should cover workload prediction and warmup ordering for large caches?
