---
type: concept
aliases: ["write-through caching", "write through cache"]
tags: [system-design, caching, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Write-Through Cache

## Definition

Write-through cache is a caching pattern where the write path updates cache and database synchronously before acknowledging the client. [[2026-05-24--caching|Caching]]

## Scope

This concept covers cases where read freshness is important enough to make writes pay extra latency and complexity. [[2026-05-24--caching|Caching]] In practical Redis-style systems this is often implemented in application logic rather than by Redis directly writing the database. [[2026-05-24--caching|Caching]]

## Contrasts

- **Cache-Aside**: Cache-aside fills cache on read misses, while write-through updates cache as part of the write path. [[2026-05-24--caching|Caching]]
- **Write-Behind Cache**: Write-through waits for the database write before success, while write-behind acknowledges before asynchronous database flush. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source says write-through can make reads fresher but slows writes and requires infrastructure or application logic to keep cache and database synchronized.

## Related

- [[cache-invalidation|Cache Invalidation]]
- [[application-level-caching|Application-Level Caching]]
- [[cache-aside|Cache-Aside]]
- [[write-behind-cache|Write-Behind Cache]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should cover write-through failure handling when cache and database updates partially fail?
