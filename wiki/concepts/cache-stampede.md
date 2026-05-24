---
type: concept
aliases: ["cache stampede", "thundering herd", "cache avalanche"]
tags: [system-design, caching, reliability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Cache Stampede

## Definition

A cache stampede is a failure mode where many requests miss or expire from cache at the same time and overwhelm the backend system that must rebuild the cached answer. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers synchronized TTL expiration, backend overload, TTL jitter, distributed locks, stale-while-revalidate, probabilistic early refresh, background refresh, and stale-data fallback. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Hot Key**: A hot key is a concentrated access pattern; a cache stampede is a synchronized miss pattern that can happen when cached hot data expires. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache Invalidation**: Cache invalidation handles freshness after writes, while cache stampede prevention handles backend protection during cache misses or expirations. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source describes popular results expiring at once, causing many requests to hit the database, search engine, or geospatial index together.

## Related

- [[read-scaling|Read Scaling]]
- [[application-level-caching|Application-Level Caching]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[hot-key|Hot Key]]
- [[cache-invalidation|Cache Invalidation]]

## Open Questions

- Which pattern should the wiki treat as the default cache-stampede defense for high-traffic public endpoints?
