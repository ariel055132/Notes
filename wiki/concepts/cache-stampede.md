---
type: concept
aliases: ["cache stampede", "thundering herd"]
tags: [system-design, caching, distributed-cache, cdn, reliability]
created: 2026-05-24
updated: 2026-05-26
source_count: 4
---

# Cache Stampede

## Definition

A cache stampede is a failure mode where many requests miss or expire from cache for a hot key at the same time and overwhelm the backend system that must rebuild the cached answer. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]] In distributed cache systems, stampedes can also happen during cold-cache warmup, node replacement, or broad routing churn. [[2026-05-15--distributed-cache|Distributed Cache]] In CDN systems, a popular launch or purge can create a cache-miss storm against origin. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Scope

This concept covers synchronized TTL expiration, backend overload, origin overload, request coalescing, origin shielding, locks or single-flight rebuilds, TTL jitter, stale-while-revalidate, probabilistic early refresh, background refresh, stale-data fallback, warmup, and database or origin fallback limits. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Contrasts

- **Hot Key**: A hot key is a concentrated access pattern; a cache stampede is a synchronized miss pattern that can happen when cached hot data expires. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache Invalidation**: Cache invalidation handles freshness after writes, while cache stampede prevention handles backend protection during cache misses or expirations. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache Avalanche**: A cache stampede usually centers on one hot key expiring, while cache avalanche is many keys expiring together. [[2026-05-24--caching|Caching]]
- **Cache Fallback Limit**: Stampede prevention reduces simultaneous misses, while fallback limits bound how much remaining miss traffic can reach the database. [[2026-05-15--distributed-cache|Distributed Cache]]
- **CDN Purge**: Purging CDN content solves freshness or removal needs, but broad purge can trigger miss storms unless origin protection is in place. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source describes popular results expiring at once, causing many requests to hit the database, search engine, or geospatial index together.
- [[2026-05-24--caching|Caching]] — The source gives hot market snapshots, large-event QR redirects, and hot video metadata as stampede examples and names request coalescing as a strong defense.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source names stampede as a distributed-cache failure mode and recommends TTL jitter, single-flight, request coalescing, warmup, and fallback limits.
- [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] — The source warns that popular content coming online or cache purge can send many edge misses to origin at once.

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
- [[distributed-cache|Distributed Cache]]
- [[cache-fallback-limit|Cache Fallback Limit]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]

## Open Questions

- When should the wiki recommend request coalescing versus stale-while-revalidate as the default defense?
