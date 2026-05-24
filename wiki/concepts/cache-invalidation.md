---
type: concept
aliases: ["cache invalidation", "active invalidation", "versioned cache key", "tagged invalidation"]
tags: [system-design, caching, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Cache Invalidation

## Definition

Cache invalidation is the set of strategies used to stop stale cached data from being served beyond the system's acceptable freshness or correctness limits. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers TTL, write-through updates, write-around/cache-aside, active deletion, versioned keys, tagged invalidation, browser cache, CDN invalidation, and mixed strategies that treat critical and noncritical data differently. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Freshness Budget**: Freshness budget defines tolerated staleness, while cache invalidation implements the mechanisms that keep cached data within that budget. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Stale-While-Revalidate**: Stale-while-revalidate intentionally serves bounded stale data while cache invalidation decides when cached data should be replaced or abandoned. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source explains that cached data may exist in application cache, CDN, browser cache, and service-local cache, making invalidation a distributed concern.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[application-level-caching|Application-Level Caching]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]

## Open Questions

- Which future sources should cover event-driven invalidation and cache dependency graphs?
