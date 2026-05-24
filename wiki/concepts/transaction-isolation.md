---
type: concept
aliases: ["isolation", "database isolation", "transaction isolation levels"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Transaction Isolation

## Definition

Transaction isolation is the ACID property that controls how concurrently running transactions can observe and affect one another. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers the design tradeoff between correctness and concurrency: fully serial execution is safest but limits throughput, so databases expose isolation levels that allow or prevent specific anomalies. [[2026-03-31--database-transactions|Database Transactions]] The source presents isolation as the most flexible ACID property and ties isolation choices to system-design scenarios such as user-profile reads, inventory deduction, and financial updates. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Atomicity**: Atomicity decides whether one transaction's writes commit or roll back together; isolation decides what concurrent transactions can see and interfere with while they run. [[2026-03-31--database-transactions|Database Transactions]]
- **MVCC**: Isolation is the guarantee being offered; MVCC is one implementation technique used to provide useful isolation without blocking all readers and writers. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source compares Read Uncommitted, Read Committed, Repeatable Read, and Serializable by which anomalies each level permits.

## Related

- [[read-uncommitted|Read Uncommitted]]
- [[read-committed|Read Committed]]
- [[repeatable-read|Repeatable Read]]
- [[serializable-isolation|Serializable Isolation]]
- [[multi-version-concurrency-control|Multi-Version Concurrency Control]]
- [[lost-update|Lost Update]]

## Open Questions

- Which future source should compare PostgreSQL and MySQL isolation semantics in more detail?
