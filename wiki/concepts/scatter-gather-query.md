---
type: concept
aliases: ["scatter-gather", "cross-shard query", "fanout query"]
tags: [system-design, databases, sharding, query-patterns]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Scatter-Gather Query

## Definition

A scatter-gather query sends subqueries to multiple shards, gathers their partial results, and merges, sorts, or trims those results before returning the final answer. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers global or poorly aligned queries where the shard key does not point to one shard. [[2026-05-15--sharding|Sharding]] It is workable for rare administrative or analytic paths, but frequent scatter-gather queries increase fanout cost and make latency depend on the slowest participating shard. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Single-Shard Query**: A single-shard query routes directly to one shard through the shard key, while scatter-gather fans out to many shards and merges results. [[2026-05-15--sharding|Sharding]]
- **Read Model**: A read model or denormalized projection can precompute data for a query path, while scatter-gather computes across shards at request time. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source describes a router sending subqueries to shards, collecting local results, and aggregating them, while warning that frequent scatter-gather often signals a shard-key mismatch.

## Related

- [[database-sharding|Database Sharding]]
- [[shard-key|Shard Key]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[denormalization|Denormalization]]
- [[materialized-view|Materialized View]]

## Open Questions

- Which future source should compare scatter-gather with search indexes, analytics stores, and stream-built read models?
