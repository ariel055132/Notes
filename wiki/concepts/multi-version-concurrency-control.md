---
type: concept
aliases: ["MVCC", "multi-version concurrency control", "snapshot reads"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Multi-Version Concurrency Control

## Definition

Multi-version concurrency control is a database concurrency technique that keeps multiple versions of rows so reads can use an appropriate snapshot while writes proceed concurrently. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers how modern databases such as PostgreSQL and MySQL InnoDB can provide useful isolation without forcing every read to wait for every write. [[2026-03-31--database-transactions|Database Transactions]] The source presents MVCC as storing older committed versions and letting a transaction read the version visible at its start or read view, with old versions cleaned up after no active transaction needs them. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Pessimistic Locking**: MVCC allows many reads and writes to proceed without blocking each other, while pessimistic locking deliberately blocks conflicting operations by taking locks. [[2026-03-31--database-transactions|Database Transactions]]
- **Replication Version Vector**: MVCC versions support local transaction visibility, while version vectors track causal relationships among writes across replicas. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source explains that a transaction started before another transaction commits continues to see the older row version.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[repeatable-read|Repeatable Read]]
- [[read-committed|Read Committed]]
- [[pessimistic-locking|Pessimistic Locking]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should distinguish MVCC snapshots from lock-based serializability?
