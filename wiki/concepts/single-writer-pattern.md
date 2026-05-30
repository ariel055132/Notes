---
type: concept
aliases: ["single writer", "single-writer", "partition owner", "serialized owner"]
tags: [system-design, concurrency, queues, ordering]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Single-Writer Pattern

## Definition

The single-writer pattern routes all writes for a resource, partition, market, region, or key to one owner so operations are processed serially rather than by many concurrent contenders. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers order books, per-market matching, regional dispatchers, queue partitions, and similar designs where ordering and correctness are easier if all commands for one resource pass through one serialized processor. [[2026-05-15--distributed-lock|Distributed Lock]] It can be clearer than making every operation acquire a distributed lock, especially in high-concurrency workflows where ordering is part of the business logic. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Distributed Lock**: Distributed lock lets contenders race for temporary ownership, while single writer avoids repeated contention by assigning a durable processing owner. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Queue**: A queue can feed a single writer, while the single-writer pattern is the ownership rule that makes writes for one resource serial. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Shard Key**: A shard key partitions data storage, while a single-writer key partitions write execution and ordering. [[2026-05-15--sharding|Sharding]] [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source says order books are often better modeled as one single writer or partition owner per market or symbol than as many orders acquiring distributed locks.

## Related

- [[distributed-lock|Distributed Lock]]
- [[conditional-update|Conditional Update]]
- [[hot-key|Hot Key]]
- [[shard-key|Shard Key]]
- [[producer-consumer-pattern|Producer-Consumer Pattern]]

## Open Questions

- Which future source should compare single-writer throughput, partition rebalancing, failover, and exactly-once command processing?
