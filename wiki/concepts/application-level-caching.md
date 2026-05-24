---
type: concept
aliases: ["application cache", "cache-aside", "Redis cache", "Memcached cache"]
tags: [system-design, caching, distributed-cache, databases]
created: 2026-05-24
updated: 2026-05-25
source_count: 4
---

# Application-Level Caching

## Definition

Application-level caching is the use of a cache such as Redis or Memcached between the application and database so repeated reads can be served without rerunning the database query. [[2026-05-14--scaling-reads|Scaling Reads]] It should target a specific read path whose data is frequently read, expensive to read, or latency-sensitive, rather than being a generic "add Redis" step. [[2026-05-24--caching|Caching]] In a multi-node cache cluster, the cache layer also needs key routing, failover behavior, warmup, and fallback protection so node changes or failures do not remap most keys or overload the database. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers cache-aside reads, cache hit/miss behavior, TTL selection, jitter, negative caching, in-process cache, cache warming, read-through/write-through/write-behind variants, and choosing cacheable data such as public profiles, popular listing details, QR token mappings, video metadata, market snapshots, or short-lived recommendation snapshots. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]] It also covers distributed-cache concerns: cache-node ownership stability, hot keys, replica lag, invalidation events, cold cache, partial slow nodes, and bounded database fallback. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **Database Indexing**: Indexing makes database reads cheaper, while application-level caching can avoid repeated database reads. [[2026-05-14--scaling-reads|Scaling Reads]]
- **CDN and Edge Caching**: Application cache usually sits near backend services, while CDN/edge cache serves public cacheable content near users. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Source of Truth**: Application cache accelerates reads but should not replace the source of truth for correctness-critical decisions such as booking inventory, payment state, ledgers, or matching engines. [[2026-05-24--caching|Caching]]
- **Consistent Hashing**: Application-level caching is the cache layer being routed to, while consistent hashing is one routing strategy for assigning cache keys to cache nodes. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Distributed Cache**: Distributed cache is the multi-node operational form of application-level caching, adding routing, replication, failover, and failure-containment concerns. [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source describes cache-aside flow: check cache, return on hit, query database on miss, then write the result back to cache.
- [[2026-05-24--caching|Caching]] — The source frames external cache as one cache location among several and emphasizes miss handling, failure behavior, freshness, hot keys, penetration, and observability.
- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source uses Redis cache sharding as a primary example where consistent hashing reduces cache churn during node expansion.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source expands external cache into a clustered design problem around routing, hot keys, replication, invalidation, fallback limits, and regional cache.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[cache-aside|Cache-Aside]]
- [[write-through-cache|Write-Through Cache]]
- [[write-behind-cache|Write-Behind Cache]]
- [[read-through-cache|Read-Through Cache]]
- [[in-process-cache|In-Process Cache]]
- [[cache-invalidation|Cache Invalidation]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[request-coalescing|Request Coalescing]]
- [[negative-caching|Negative Caching]]
- [[hot-key|Hot Key]]
- [[cache-stampede|Cache Stampede]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[consistent-hashing|Consistent Hashing]]
- [[fixed-hash-slots|Fixed Hash Slots]]
- [[distributed-cache|Distributed Cache]]
- [[cache-routing|Cache Routing]]
- [[cache-fallback-limit|Cache Fallback Limit]]

## Open Questions

- Should Redis and Memcached become separate entity pages after more sources compare their operational tradeoffs?
