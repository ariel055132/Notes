---
type: concept
aliases: ["application cache", "cache-aside", "Redis cache", "Memcached cache"]
tags: [system-design, caching, databases]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Application-Level Caching

## Definition

Application-level caching is the use of a cache such as Redis or Memcached between the application and database so repeated reads can be served without rerunning the database query. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers cache-aside reads, cache hit/miss behavior, TTL selection, jitter, negative caching, local cache, and choosing cacheable data such as public profiles, popular listing details, short URL mappings, video metadata, or short-lived recommendation snapshots. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Database Indexing**: Indexing makes database reads cheaper, while application-level caching can avoid repeated database reads. [[2026-05-14--scaling-reads|Scaling Reads]]
- **CDN and Edge Caching**: Application cache usually sits near backend services, while CDN/edge cache serves public cacheable content near users. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source describes cache-aside flow: check cache, return on hit, query database on miss, then write the result back to cache.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[cache-invalidation|Cache Invalidation]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[hot-key|Hot Key]]
- [[cache-stampede|Cache Stampede]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]

## Open Questions

- Should Redis and Memcached become separate entity pages after more sources compare their operational trade-offs?
