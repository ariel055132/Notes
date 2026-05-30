---
type: concept
aliases: ["pessimistic concurrency control", "row lock", "SELECT FOR UPDATE"]
tags: [system-design, databases, transactions, concurrency, locking]
created: 2026-05-24
updated: 2026-05-26
source_count: 2
---

# Pessimistic Locking

## Definition

Pessimistic locking is a concurrency-control technique that locks data before making changes so other transactions must wait instead of concurrently modifying the same record. [[2026-03-31--database-transactions|Database Transactions]] It is often a simpler alternative to distributed lock when the contested resource and state both live inside one database transaction boundary. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers row-level locking strategies such as `SELECT ... FOR UPDATE` for cases where conflicting updates are likely or correctness is more important than maximum concurrency. [[2026-03-31--database-transactions|Database Transactions]] It also covers the system-design choice to prefer database row locks over distributed locks when the invariant is local to one database. [[2026-05-15--distributed-lock|Distributed Lock]] The transaction source warns that pessimistic locking can reduce concurrency and create deadlocks when transactions acquire locks in inconsistent orders. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Optimistic Locking**: Pessimistic locking prevents concurrent conflicting updates by waiting, while optimistic locking lets work proceed and rejects stale writes later. [[2026-03-31--database-transactions|Database Transactions]]
- **MVCC**: MVCC improves read/write concurrency through versions, while pessimistic locking intentionally serializes conflicting write paths. [[2026-03-31--database-transactions|Database Transactions]]
- **Distributed Lock**: Pessimistic locking uses the database's local lock manager, while distributed lock uses an external coordination service for ownership outside one database boundary. [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source uses `SELECT balance FROM accounts WHERE id = 1 FOR UPDATE` as the pessimistic locking example.
- [[2026-05-15--distributed-lock|Distributed Lock]] — The source says database transaction or row lock is usually preferred when the resource and state are protected by one database.

## Related

- [[lost-update|Lost Update]]
- [[optimistic-locking|Optimistic Locking]]
- [[deadlock|Deadlock]]
- [[multi-version-concurrency-control|Multi-Version Concurrency Control]]
- [[serializable-isolation|Serializable Isolation]]
- [[distributed-lock|Distributed Lock]]
- [[conditional-update|Conditional Update]]

## Open Questions

- Which future source should add lock granularity, lock escalation, and timeout strategy?
