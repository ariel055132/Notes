---
type: concept
aliases: ["cache invalidation", "active invalidation", "versioned cache key", "tagged invalidation"]
tags: [system-design, caching, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Cache Invalidation

## Definition

Cache invalidation is the set of strategies used to stop stale cached data from being served beyond the system's acceptable freshness or correctness limits. [[2026-05-14--scaling-reads|Scaling Reads]] It includes write-time deletion or update, event-driven purge, versioned keys, and short TTLs chosen from the read path's freshness budget. [[2026-05-24--caching|Caching]]

## Scope

This concept covers TTL, write-through updates, write-around/cache-aside, active deletion, event-driven invalidation, versioned keys, tagged invalidation, browser cache, CDN invalidation, and mixed strategies that treat critical and noncritical data differently. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]]

## Contrasts

- **Freshness Budget**: Freshness budget defines tolerated staleness, while cache invalidation implements the mechanisms that keep cached data within that budget. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Stale-While-Revalidate**: Stale-while-revalidate intentionally serves bounded stale data while cache invalidation decides when cached data should be replaced or abandoned. [[2026-05-14--scaling-reads|Scaling Reads]]
- **TTL Jitter**: Cache invalidation defines when data should stop being used, while TTL jitter spreads expirations to reduce simultaneous backend load. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source explains that cached data may exist in application cache, CDN, browser cache, and service-local cache, making invalidation a distributed concern.
- [[2026-05-24--caching|Caching]] — The source lists write invalidate, write update, short TTL, event-driven invalidation, and versioned keys as consistency strategies.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[application-level-caching|Application-Level Caching]]
- [[cache-aside|Cache-Aside]]
- [[write-through-cache|Write-Through Cache]]
- [[ttl-jitter|TTL Jitter]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]

## Open Questions

- Which future sources should cover event-driven invalidation and cache dependency graphs?
