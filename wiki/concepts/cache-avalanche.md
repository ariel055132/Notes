---
type: concept
aliases: ["cache avalanche", "mass cache expiration", "bulk cache expiry"]
tags: [system-design, caching, reliability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Cache Avalanche

## Definition

Cache avalanche is a failure mode where many cache keys expire or become unavailable at roughly the same time, causing a large backend traffic spike. [[2026-05-24--caching|Caching]]

## Scope

This concept covers broad synchronized expiration across many keys, which differs from a single hot-key stampede. [[2026-05-24--caching|Caching]] Mitigations include TTL jitter, staggered warming, stale fallback, and degradation protection. [[2026-05-24--caching|Caching]]

## Contrasts

- **Cache Stampede**: A cache stampede usually centers on one hot key expiring, while cache avalanche involves many keys expiring together. [[2026-05-24--caching|Caching]]
- **TTL Jitter**: Cache avalanche is the failure mode, while TTL jitter is a mitigation that spreads expirations over time. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source distinguishes avalanche from hot-key stampede and recommends TTL jitter, batch warming, stale fallback, and degradation.

## Related

- [[cache-stampede|Cache Stampede]]
- [[ttl-jitter|TTL Jitter]]
- [[cache-warming|Cache Warming]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[application-level-caching|Application-Level Caching]]

## Open Questions

- Which future source should define degraded serving policies when cache or origin is under avalanche pressure?
