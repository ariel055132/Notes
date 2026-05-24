---
type: concept
aliases: ["TTL jitter", "expiration jitter", "randomized TTL"]
tags: [system-design, caching, distributed-cache, reliability]
created: 2026-05-24
updated: 2026-05-25
source_count: 2
---

# TTL Jitter

## Definition

TTL jitter is the practice of adding random variation to cache expiration times so many keys do not expire at exactly the same moment. [[2026-05-24--caching|Caching]] In distributed cache systems, it helps prevent synchronized misses from turning into database fallback spikes. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers avoiding synchronized expiration that can cause cache stampedes or avalanches across distributed cache nodes. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] It is usually combined with TTL, stale fallback, cache warming, request coalescing, or background refresh rather than used as the only cache-protection mechanism. [[2026-05-24--caching|Caching]]

## Contrasts

- **Cache Stampede**: TTL jitter reduces synchronized hot-key expiration risk, while request coalescing limits rebuild fanout after a miss occurs. [[2026-05-24--caching|Caching]]
- **Cache Avalanche**: TTL jitter spreads many key expirations over time, while avalanche describes many keys expiring together and spiking backend load. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source lists TTL jitter as a defense against both hot-key stampedes and broad cache avalanches.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source lists TTL jitter as a protection against distributed-cache stampede and database fallback overload.

## Related

- [[cache-stampede|Cache Stampede]]
- [[cache-avalanche|Cache Avalanche]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[cache-warming|Cache Warming]]
- [[request-coalescing|Request Coalescing]]
- [[distributed-cache|Distributed Cache]]

## Open Questions

- Which future source should quantify jitter windows for different TTL and traffic profiles?
