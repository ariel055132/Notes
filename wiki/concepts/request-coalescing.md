---
type: concept
aliases: ["single flight", "singleflight", "request collapsing", "cache miss coalescing"]
tags: [system-design, caching, reliability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Request Coalescing

## Definition

Request coalescing is a cache-miss protection pattern where concurrent requests for the same missing key share one rebuild or origin fetch instead of all rebuilding independently. [[2026-05-24--caching|Caching]]

## Scope

This concept covers single-flight behavior, locks, one-worker rebuilds, and backend protection during hot-key expiration. [[2026-05-24--caching|Caching]] It is one of the strongest defenses against cache stampedes because it limits backend fanout when a hot key misses. [[2026-05-24--caching|Caching]]

## Contrasts

- **TTL Jitter**: TTL jitter reduces simultaneous expiration, while request coalescing controls what happens when simultaneous misses still occur. [[2026-05-24--caching|Caching]]
- **Stale-While-Revalidate**: Request coalescing makes one request do rebuild work, while stale-while-revalidate can let users receive stale data while refresh happens. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source calls request coalescing one of the most effective cache-stampede defenses because only one request rebuilds a key.

## Related

- [[cache-stampede|Cache Stampede]]
- [[cache-aside|Cache-Aside]]
- [[ttl-jitter|TTL Jitter]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[hot-key|Hot Key]]

## Open Questions

- Which future source should compare local singleflight, distributed locks, and lease-based refresh?
