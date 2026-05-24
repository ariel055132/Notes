---
type: concept
aliases: ["cache stampede", "thundering herd"]
tags: [system-design, caching, reliability]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Cache Stampede

## Definition

A cache stampede is a failure mode where many requests miss or expire from cache for a hot key at the same time and overwhelm the backend system that must rebuild the cached answer. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]]

## Scope

This concept covers synchronized TTL expiration, backend overload, request coalescing, locks or single-flight rebuilds, TTL jitter, stale-while-revalidate, probabilistic early refresh, background refresh, and stale-data fallback. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]]

## Contrasts

- **Hot Key**: A hot key is a concentrated access pattern; a cache stampede is a synchronized miss pattern that can happen when cached hot data expires. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache Invalidation**: Cache invalidation handles freshness after writes, while cache stampede prevention handles backend protection during cache misses or expirations. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache Avalanche**: A cache stampede usually centers on one hot key expiring, while cache avalanche is many keys expiring together. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source describes popular results expiring at once, causing many requests to hit the database, search engine, or geospatial index together.
- [[2026-05-24--caching|Caching]] — The source gives hot market snapshots, large-event QR redirects, and hot video metadata as stampede examples and names request coalescing as a strong defense.

## Related

- [[read-scaling|Read Scaling]]
- [[application-level-caching|Application-Level Caching]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[request-coalescing|Request Coalescing]]
- [[ttl-jitter|TTL Jitter]]
- [[cache-warming|Cache Warming]]
- [[cache-avalanche|Cache Avalanche]]
- [[hot-key|Hot Key]]
- [[cache-invalidation|Cache Invalidation]]

## Open Questions

- When should the wiki recommend request coalescing versus stale-while-revalidate as the default defense?
