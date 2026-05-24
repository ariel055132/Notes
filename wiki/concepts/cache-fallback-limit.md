---
type: concept
aliases: ["bounded DB fallback", "database fallback limit", "cache fallback budget", "origin fallback limit"]
tags: [system-design, distributed-cache, distributed-queue, caching, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Cache Fallback Limit

## Definition

A cache fallback limit is a control that bounds how much traffic may fall through from cache to the database or origin during cache misses, slowness, warmup, or outage. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers protecting the database when distributed cache is cold, partially slow, stampeding, or unavailable. [[2026-05-15--distributed-cache|Distributed Cache]] The source recommends limiting database fallback, serving stale data where acceptable, returning degraded responses, using short timeouts and retry budgets, and preventing cache failure from becoming a database outage. [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **Cache Stampede**: Cache stampede is the synchronized miss pattern; cache fallback limits constrain the downstream damage when misses occur. [[2026-05-15--distributed-cache|Distributed Cache]]
- **Request Coalescing**: Request coalescing reduces duplicate rebuilds for one key, while cache fallback limits bound total origin or database load. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-15--distributed-cache|Distributed Cache]] — The source says many incidents happen because all services fall back to the database at once after cache failure.

## Related

- [[distributed-cache|Distributed Cache]]
- [[cache-stampede|Cache Stampede]]
- [[request-coalescing|Request Coalescing]]
- [[ttl-jitter|TTL Jitter]]
- [[cache-warming|Cache Warming]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should cover circuit breakers, stale-if-error, and fallback admission control?
