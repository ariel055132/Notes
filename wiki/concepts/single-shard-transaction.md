---
type: concept
aliases: ["single shard transaction", "single-shard invariant", "local transaction"]
tags: [system-design, databases, sharding, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Single-Shard Transaction

## Definition

A single-shard transaction is a transaction whose required records and invariants are kept on one shard so a normal database transaction can enforce correctness locally. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers designing shard keys and data boundaries so strong-consistency operations do not cross shard boundaries. [[2026-05-15--sharding|Sharding]] Examples include keeping a home's date inventory together for booking correctness, keeping a market's order book on one matching boundary, or checking an autonomous vehicle's active assignment through a shard-local conditional update or unique constraint. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Cross-Shard Transaction**: Single-shard transactions keep coordination local, while cross-shard transactions require distributed coordination. [[2026-05-15--sharding|Sharding]]
- **Read Model**: A single-shard transaction protects write-side correctness, while read models can be built separately to serve query paths that would otherwise cross shards. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source uses Airbnb inventory and Polymarket matching as examples where correctness depends on choosing shard boundaries that keep the core invariant local.

## Related

- [[database-sharding|Database Sharding]]
- [[cross-shard-transaction|Cross-Shard Transaction]]
- [[shard-key|Shard Key]]
- [[denormalization|Denormalization]]
- [[materialized-view|Materialized View]]

## Open Questions

- Which future source should formalize invariant-driven partitioning as a design method?
