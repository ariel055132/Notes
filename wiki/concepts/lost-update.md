---
type: concept
aliases: ["lost updates", "update lost", "read-modify-write race"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Lost Update

## Definition

Lost update is a concurrency anomaly where two transactions read the same value, each computes a new value, and the later write overwrites the earlier update. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers a common system-design bug in inventory, balances, counters, reservations, and any read-modify-write workflow. [[2026-03-31--database-transactions|Database Transactions]] The source emphasizes that many oversell bugs are lost-update problems and can often be solved with an atomic conditional update, optimistic locking, or pessimistic row locking rather than automatically raising the whole workflow to Serializable. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Phantom Read**: Lost update is about overwriting concurrent writes, while phantom read is about a range-query result set changing. [[2026-03-31--database-transactions|Database Transactions]]
- **Write Conflict Resolution**: Lost update is a local transaction race; write conflict resolution often concerns concurrent writes accepted by separate leaders or replicas before synchronization. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source shows two transactions reading a balance of 1000 and writing 800 and 700, leaving 700 instead of the correct 500.

## Related

- [[optimistic-locking|Optimistic Locking]]
- [[pessimistic-locking|Pessimistic Locking]]
- [[transaction-isolation|Transaction Isolation]]
- [[serializable-isolation|Serializable Isolation]]
- [[write-conflict-resolution|Write Conflict Resolution]]

## Open Questions

- Which future source should add atomic SQL update patterns and compare them with explicit locks?
