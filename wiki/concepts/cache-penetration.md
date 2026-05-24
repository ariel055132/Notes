---
type: concept
aliases: ["cache penetration attack", "nonexistent key cache miss"]
tags: [system-design, caching, reliability, security]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Cache Penetration

## Definition

Cache penetration is a failure mode where many requests ask for nonexistent keys, miss cache every time, and repeatedly hit the backend source. [[2026-05-24--caching|Caching]]

## Scope

This concept covers attack or accidental traffic such as repeated requests for nonexistent QR tokens. [[2026-05-24--caching|Caching]] Defenses include negative caching, Bloom filters, rate limiting, and rejecting invalid token formats before cache or database lookup. [[2026-05-24--caching|Caching]]

## Contrasts

- **Cache Stampede**: Cache penetration is repeated miss traffic for nonexistent keys, while a cache stampede is simultaneous miss traffic for an existing hot key whose cache entry expires. [[2026-05-24--caching|Caching]]
- **Negative Caching**: Cache penetration is the problem, while negative caching is one mitigation that stores short-lived "not found" results. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source uses nonexistent QR token lookups as an example and recommends negative caching, Bloom filters, rate limiting, and token-format validation.

## Related

- [[negative-caching|Negative Caching]]
- [[cache-stampede|Cache Stampede]]
- [[application-level-caching|Application-Level Caching]]
- [[hot-key|Hot Key]]

## Open Questions

- Which future source should define Bloom filters and false-positive tradeoffs for penetration defense?
