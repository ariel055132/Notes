---
type: concept
aliases: ["negative cache", "not-found caching", "404 caching"]
tags: [system-design, caching, reliability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Negative Caching

## Definition

Negative caching stores short-lived negative results, such as "not found," so repeated requests for nonexistent keys do not repeatedly hit the backend. [[2026-05-24--caching|Caching]]

## Scope

This concept covers protecting databases from repeated misses, especially in cache-penetration scenarios. [[2026-05-24--caching|Caching]] Negative results usually need short TTLs because a key that does not exist now may be created later. [[2026-05-24--caching|Caching]]

## Contrasts

- **Positive Caching**: Positive caching stores existing data, while negative caching stores absence or rejection results. [[2026-05-24--caching|Caching]]
- **Bloom Filter**: Negative caching learns from actual misses, while a Bloom filter can reject keys before lookup if they are definitely not present or probably absent depending on design. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source lists negative caching as a direct defense against cache penetration from nonexistent keys.

## Related

- [[cache-penetration|Cache Penetration]]
- [[application-level-caching|Application-Level Caching]]
- [[freshness-budget|Freshness Budget]]
- [[cache-invalidation|Cache Invalidation]]

## Open Questions

- Which future source should define safe TTLs and invalidation behavior for negative cache entries?
