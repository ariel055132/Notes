---
type: concept
aliases: ["cross-shard transactions", "distributed transaction", "distributed transactions", "2PC"]
tags: [system-design, databases, sharding, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Cross-Shard Transaction

## Definition

A cross-shard transaction is a transaction whose required reads or writes span more than one shard, service, or database, making it harder to rely on a single database's local atomic commit. [[2026-05-15--sharding|Sharding]] [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers the main consistency cost introduced by sharding and service decomposition: operations that were once local to one database can require coordination across independent database machines or service-owned databases. [[2026-05-15--sharding|Sharding]] [[2026-03-31--database-transactions|Database Transactions]] The sharding source recommends avoiding cross-shard transactions by choosing shard boundaries around invariants, and the transactions source explains the tradeoff between two-phase commit and Saga when the boundary cannot stay local. [[2026-05-15--sharding|Sharding]] [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Single-Shard Transaction**: A single-shard transaction keeps the invariant on one shard, while a cross-shard transaction needs distributed coordination or a compensating workflow. [[2026-05-15--sharding|Sharding]] [[2026-03-31--database-transactions|Database Transactions]]
- **Replication Lag**: Cross-shard transactions are a coordination problem caused by partitioned ownership, while replication lag is a staleness problem caused by copying writes to replicas after the fact. [[2026-05-15--sharding|Sharding]] [[2026-05-02--replication|Replication]]
- **Two-Phase Commit**: Two-phase commit is one way to coordinate a cross-boundary commit, but it can reduce availability when participants or coordinators fail. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source emphasizes that cross-shard transactions are expensive and should usually be avoided by placing strong consistency operations inside one shard.
- [[2026-03-31--database-transactions|Database Transactions]] — The source explains why cross-service transaction boundaries make one local `BEGIN`/`COMMIT` insufficient and compares 2PC with Saga.

## Related

- [[database-sharding|Database Sharding]]
- [[single-shard-transaction|Single-Shard Transaction]]
- [[shard-key|Shard Key]]
- [[replication|Replication]]
- [[consistent-prefix-reads|Consistent Prefix Reads]]
- [[two-phase-commit|Two-Phase Commit]]
- [[saga-pattern|Saga Pattern]]

## Open Questions

- Which future source should add dedicated pages for outbox, idempotency, and compensation patterns?
