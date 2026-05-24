---
type: concept
aliases: ["write-behind caching", "write back cache", "write-back cache"]
tags: [system-design, caching, write-scaling]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Write-Behind Cache

## Definition

Write-behind cache is a caching pattern where writes are accepted into a cache or buffer first and later flushed to the database asynchronously by a background process. [[2026-05-24--caching|Caching]]

## Scope

This concept covers high-throughput write buffering for data such as metrics, analytics, counters, and other values where delayed persistence or reconstruction may be acceptable. [[2026-05-24--caching|Caching]] It requires retry, durable queues, or explicit acceptance of data-loss risk because cache failure before flush can lose writes. [[2026-05-24--caching|Caching]]

## Contrasts

- **Write-Through Cache**: Write-behind improves write latency and batching by delaying database writes, while write-through waits for database success before acknowledging the client. [[2026-05-24--caching|Caching]]
- **Durable Log**: Write-behind cache may lose data unless backed by durability, while a durable log is designed to preserve events before asynchronous processing. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source says write-behind can fit QR scan count aggregation but not booking, payment, or trade correctness paths.

## Related

- [[application-level-caching|Application-Level Caching]]
- [[write-through-cache|Write-Through Cache]]
- [[cache-invalidation|Cache Invalidation]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should define durable queues, outbox, and write aggregation as safer alternatives?
