---
type: concept
aliases: ["lazy loading cache", "lazy cache", "cache aside"]
tags: [system-design, caching, read-scaling]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Cache-Aside

## Definition

Cache-aside is an application-managed caching pattern where the application checks cache first, queries the source of truth on miss, writes the result back to cache, and returns the result. [[2026-05-24--caching|Caching]]

## Scope

This concept covers the default Redis/Memcached application-cache pattern for read-heavy data such as QR redirects, listing details, market metadata, video metadata, and other data that can tolerate a freshness policy. [[2026-05-24--caching|Caching]] It is simple and controllable, but the first miss is slower and hot-key misses can cause stampedes without coalescing, locks, stale fallback, or warming. [[2026-05-24--caching|Caching]]

## Contrasts

- **Read-Through Cache**: Cache-aside makes application code fetch from the database on miss, while read-through cache makes the cache layer fetch from origin. [[2026-05-24--caching|Caching]]
- **Write-Through Cache**: Cache-aside is primarily a read pattern with refill on miss, while write-through updates cache and database synchronously on writes. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source calls cache-aside the common default and gives QR redirect, Airbnb listing detail, and Polymarket metadata as good fits.

## Related

- [[application-level-caching|Application-Level Caching]]
- [[cache-stampede|Cache Stampede]]
- [[request-coalescing|Request Coalescing]]
- [[cache-invalidation|Cache Invalidation]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should compare cache-aside with write-around and refresh-ahead variants?
