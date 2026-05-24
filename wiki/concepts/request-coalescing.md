---
type: concept
aliases: ["single flight", "singleflight", "request collapsing", "cache miss coalescing"]
tags: [system-design, caching, distributed-cache, reliability]
created: 2026-05-24
updated: 2026-05-25
source_count: 2
---

# Request Coalescing

## Definition

Request coalescing is a cache-miss protection pattern where concurrent requests for the same missing key share one rebuild or origin fetch instead of all rebuilding independently. [[2026-05-24--caching|Caching]] In distributed cache systems, it is a core defense against many clients falling through to the database when a hot key misses or a cache shard is cold. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers single-flight behavior, locks, one-worker rebuilds, and backend protection during hot-key expiration, cold cache, or cache node replacement. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] It is one of the strongest defenses against cache stampedes because it limits backend fanout when a hot key misses. [[2026-05-24--caching|Caching]]

## Contrasts

- **TTL Jitter**: TTL jitter reduces simultaneous expiration, while request coalescing controls what happens when simultaneous misses still occur. [[2026-05-24--caching|Caching]]
- **Stale-While-Revalidate**: Request coalescing makes one request do rebuild work, while stale-while-revalidate can let users receive stale data while refresh happens. [[2026-05-24--caching|Caching]]
- **Cache Fallback Limit**: Request coalescing limits duplicate rebuilds for one key, while fallback limits bound total database traffic during broader cache failure. [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source calls request coalescing one of the most effective cache-stampede defenses because only one request rebuilds a key.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source names single-flight and request coalescing as protections for distributed-cache stampede and fallback failure modes.

## Related

- [[cache-stampede|Cache Stampede]]
- [[cache-aside|Cache-Aside]]
- [[ttl-jitter|TTL Jitter]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[hot-key|Hot Key]]
- [[distributed-cache|Distributed Cache]]
- [[cache-fallback-limit|Cache Fallback Limit]]

## Open Questions

- Which future source should compare local singleflight, distributed locks, and lease-based refresh?
