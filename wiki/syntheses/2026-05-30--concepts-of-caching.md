---
type: synthesis
question: "Please explain the concepts of caching"
tags: [system-design, caching, read-scaling, reliability]
created: 2026-05-30
updated: 2026-05-30
---

# Concepts of Caching

## Question / Purpose

Explain the core concepts of caching in system design, with emphasis on cache placement, read/write patterns, freshness, invalidation, and failure modes.

## Answer / Analysis

Caching stores frequently read, expensive-to-compute, or latency-sensitive data in a faster or closer layer than the source of truth. It is an acceleration layer, not the authoritative record, so cache design should start from a specific read path and bottleneck rather than from a generic decision to add Redis or another cache. [[2026-05-24--caching|Caching]] [[application-level-caching|Application-Level Caching]]

A cache hit returns data directly from cache; a cache miss falls back to the database, origin, or another source of truth and often repopulates the cache. In cache-aside, the application owns this miss flow: check cache, read the source on miss, write the result into cache, and return it. [[cache-aside|Cache-Aside]] Read-through caching moves miss-fetch behavior into the cache layer itself; CDN edge caching is a common read-through-like example because edge misses fetch from origin and later edge hits avoid origin. [[read-through-cache|Read-Through Cache]] [[cdn-and-edge-caching|CDN and Edge Caching]]

Cache placement determines latency, sharing, invalidation difficulty, and failure behavior. Client-side caches reduce repeated client fetches; in-process caches are very fast but local to one application instance; external application caches such as Redis or Memcached can be shared by backend services; CDN and edge caches serve public cacheable content close to users; database buffer caches optimize storage-engine reads but do not replace application-level cache design. [[2026-05-24--caching|Caching]] [[application-level-caching|Application-Level Caching]] [[cdn-and-edge-caching|CDN and Edge Caching]]

Write behavior changes the consistency and latency tradeoff. Write-through caching updates cache and database synchronously before acknowledging success, improving read freshness while making writes slower and more complex. [[write-through-cache|Write-Through Cache]] Write-behind caching accepts writes into a cache or buffer first and flushes to the database later, which can improve throughput for metrics, counters, or analytics-like data but requires durable buffering or explicit acceptance of data-loss risk. [[write-behind-cache|Write-Behind Cache]]

Freshness is the central correctness question. A TTL is only a technical expiration setting; the more important design input is the freshness budget, meaning how stale a read path may be before product behavior becomes wrong or unacceptable. Static assets and public listing surfaces may tolerate longer stale windows, while payments, ledgers, matching, and inventory usually require source-of-truth checks. [[freshness-budget|Freshness Budget]]

Cache invalidation is the mechanism for keeping cached data within that freshness budget. Common strategies include short TTLs, write-time delete or update, event-driven invalidation, distributed invalidation events, versioned keys, CDN purge, and versioned URLs. [[cache-invalidation|Cache Invalidation]]

Caching also adds failure modes. A cache stampede happens when many requests miss or expire for a hot key at the same time and overwhelm the backend or origin rebuilding the result. Defenses include request coalescing, single-flight rebuilds, TTL jitter, stale-while-revalidate, cache warming, and fallback limits. [[cache-stampede|Cache Stampede]]

Good caching design should therefore answer six questions: which read path is being accelerated, what data is cacheable, where the cache should live, how stale the data may be, who rebuilds on a miss, and what happens when the cache is slow, cold, stale, or unavailable. [[2026-05-24--caching|Caching]]

## Comparison Table

| Concept | What It Optimizes | Main Tradeoff |
|---|---|---|
| Application-level cache | Repeated backend reads and database load | Staleness, invalidation, miss handling, and cache outage behavior. [[application-level-caching|Application-Level Caching]] |
| Cache-aside | Simple application-controlled read caching | First miss is slower; hot misses can stampede without protection. [[cache-aside|Cache-Aside]] |
| Read-through cache | Encapsulated miss fetching in the cache layer | Cache layer needs origin-fetch behavior and origin protection. [[read-through-cache|Read-Through Cache]] |
| Write-through cache | Fresher cached reads after writes | Higher write latency and synchronization complexity. [[write-through-cache|Write-Through Cache]] |
| Write-behind cache | Faster writes and batching | Possible data loss or delayed persistence unless durability is added. [[write-behind-cache|Write-Behind Cache]] |
| CDN / edge cache | Global latency reduction and origin offload | Works best for public, shareable content with careful cache keys and freshness rules. [[cdn-and-edge-caching|CDN and Edge Caching]] |

## Citations

- [[2026-05-24--caching|Caching]] — Defines caching as a targeted read-path acceleration layer and outlines cache locations, patterns, freshness, invalidation, and failure modes.
- [[application-level-caching|Application-Level Caching]] — Explains Redis/Memcached-style backend caching between application and database.
- [[cache-aside|Cache-Aside]] — Defines application-managed read miss and refill behavior.
- [[read-through-cache|Read-Through Cache]] — Defines cache-layer-managed origin fetch on miss.
- [[write-through-cache|Write-Through Cache]] — Defines synchronous cache and database update on writes.
- [[write-behind-cache|Write-Behind Cache]] — Defines asynchronous persistence after accepting writes into cache or buffer.
- [[freshness-budget|Freshness Budget]] — Explains staleness tolerance as the driver of TTL, invalidation, and source-of-truth decisions.
- [[cache-invalidation|Cache Invalidation]] — Lists strategies for preventing stale cache from outliving correctness limits.
- [[cache-stampede|Cache Stampede]] — Explains synchronized miss failure modes and common defenses.
- [[cdn-and-edge-caching|CDN and Edge Caching]] — Explains edge cache placement for public, shareable repeated content.

## Implications

Caching is strongest when repeated reads are common, source reads are expensive, and the product can tolerate a clear freshness policy. It is risky when stale data would violate correctness, when miss traffic is unbounded, or when cache failures simply shift overload to the database or origin. [[2026-05-24--caching|Caching]] [[freshness-budget|Freshness Budget]] [[cache-stampede|Cache Stampede]]

## Follow-up Questions

- When should a system choose application cache, CDN, read replicas, materialized views, or indexing for read scaling?
- What observability dashboard best detects cache stampedes, stale responses, hot keys, and failed invalidations?
- Which Redis and Memcached operational tradeoffs deserve dedicated wiki pages?
