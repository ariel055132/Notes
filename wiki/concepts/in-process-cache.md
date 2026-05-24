---
type: concept
aliases: ["local cache", "process-local cache", "in-memory application cache"]
tags: [system-design, caching, distributed-cache, latency]
created: 2026-05-24
updated: 2026-05-25
source_count: 2
---

# In-Process Cache

## Definition

In-process cache stores cached data inside an application process's memory, avoiding a network hop and making reads faster than an external cache. [[2026-05-24--caching|Caching]] In distributed-cache designs, a tiny in-process cache can also protect an extremely hot key from overloading one remote cache shard. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers feature flag snapshots, webhook endpoint configuration, hot market lists, extremely hot QR redirect tokens, and other small read-mostly data that can tolerate per-instance freshness differences. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] It is best treated as a local optimization in front of Redis, distributed cache, or a database, not as the sole source of truth, because each application instance has its own cache copy. [[2026-05-24--caching|Caching]]

## Contrasts

- **Application-Level Caching**: In-process cache is fastest but per-instance, while an external application cache such as Redis is shared across application servers. [[2026-05-24--caching|Caching]]
- **Hot Key Mitigation**: In-process cache can absorb repeated reads for a hot key locally, while request coalescing focuses on limiting rebuilds after misses. [[2026-05-24--caching|Caching]]
- **Distributed Cache**: In-process cache can sit in front of distributed cache to absorb ultra-hot read-mostly keys, but it makes invalidation and freshness harder. [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source presents in-process cache as faster than Redis but harder to invalidate consistently across application instances.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source recommends short-lived local cache for extremely hot QR redirect tokens that would otherwise overload one distributed-cache shard.

## Related

- [[application-level-caching|Application-Level Caching]]
- [[hot-key|Hot Key]]
- [[cache-invalidation|Cache Invalidation]]
- [[freshness-budget|Freshness Budget]]
- [[distributed-cache|Distributed Cache]]

## Open Questions

- Which future source should cover local-cache coherence and invalidation broadcasts?
