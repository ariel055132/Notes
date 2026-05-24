---
type: concept
aliases: ["local cache", "process-local cache", "in-memory application cache"]
tags: [system-design, caching, latency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# In-Process Cache

## Definition

In-process cache stores cached data inside an application process's memory, avoiding a network hop and making reads faster than an external cache. [[2026-05-24--caching|Caching]]

## Scope

This concept covers feature flag snapshots, webhook endpoint configuration, hot market lists, extremely hot QR redirect tokens, and other small read-mostly data that can tolerate per-instance freshness differences. [[2026-05-24--caching|Caching]] It is best treated as a local optimization in front of Redis or a database, not as the sole source of truth, because each application instance has its own cache copy. [[2026-05-24--caching|Caching]]

## Contrasts

- **Application-Level Caching**: In-process cache is fastest but per-instance, while an external application cache such as Redis is shared across application servers. [[2026-05-24--caching|Caching]]
- **Hot Key Mitigation**: In-process cache can absorb repeated reads for a hot key locally, while request coalescing focuses on limiting rebuilds after misses. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source presents in-process cache as faster than Redis but harder to invalidate consistently across application instances.

## Related

- [[application-level-caching|Application-Level Caching]]
- [[hot-key|Hot Key]]
- [[cache-invalidation|Cache Invalidation]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should cover local-cache coherence and invalidation broadcasts?
