---
type: concept
aliases: ["cross-shard transactions", "distributed transaction", "distributed transactions", "2PC"]
tags: [system-design, databases, sharding, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Cross-Shard Transaction

## Definition

A cross-shard transaction is a transaction whose required reads or writes span more than one shard, making it harder to rely on a single database's local atomic commit. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers the main consistency cost introduced by sharding: operations that were once local to one database can require coordination across independent database machines. [[2026-05-15--sharding|Sharding]] The source recommends avoiding cross-shard transactions by choosing shard boundaries around invariants, and using sagas, outbox patterns, idempotency, compensation, or two-phase commit only when necessary. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Single-Shard Transaction**: A single-shard transaction keeps the invariant on one shard, while a cross-shard transaction needs distributed coordination. [[2026-05-15--sharding|Sharding]]
- **Replication Lag**: Cross-shard transactions are a coordination problem caused by partitioned ownership, while replication lag is a staleness problem caused by copying writes to replicas after the fact. [[2026-05-15--sharding|Sharding]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source emphasizes that cross-shard transactions are expensive and should usually be avoided by placing strong consistency operations inside one shard.

## Related

- [[database-sharding|Database Sharding]]
- [[single-shard-transaction|Single-Shard Transaction]]
- [[shard-key|Shard Key]]
- [[replication|Replication]]
- [[consistent-prefix-reads|Consistent Prefix Reads]]

## Open Questions

- Which future source should add dedicated pages for sagas, outbox, idempotency, compensation, and two-phase commit?
