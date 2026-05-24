---
type: concept
aliases: ["2PC", "two phase commit", "distributed commit"]
tags: [system-design, databases, transactions, distributed-systems]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Two-Phase Commit

## Definition

Two-phase commit is a distributed transaction protocol where a coordinator first asks participants to prepare, then instructs them to commit or abort based on the prepare responses. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers a strong-consistency approach to distributed commits across multiple databases or services. [[2026-03-31--database-transactions|Database Transactions]] In the source, 2PC has a prepare phase where each participant writes its work but does not commit, followed by a commit or abort phase; the key system-design problem is that coordinator failure can leave participants stuck in a prepared but unresolved state. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Saga Pattern**: 2PC tries to coordinate one distributed commit, while Saga accepts local commits plus compensation and eventual consistency. [[2026-03-31--database-transactions|Database Transactions]]
- **Single-Shard Transaction**: A single-shard transaction avoids distributed commit by keeping the invariant local to one shard. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source describes prepare and commit/abort phases and explains why 2PC is difficult in high-availability systems.

## Related

- [[cross-shard-transaction|Cross-Shard Transaction]]
- [[saga-pattern|Saga Pattern]]
- [[single-shard-transaction|Single-Shard Transaction]]
- [[database-transactions|Database Transactions]]
- [[failover|Failover]]

## Open Questions

- Which future source should compare 2PC with consensus-backed transaction coordinators?
