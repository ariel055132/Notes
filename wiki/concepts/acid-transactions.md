---
type: concept
aliases: ["ACID", "ACID guarantees", "transaction guarantees"]
tags: [system-design, databases, transactions, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# ACID Transactions

## Definition

ACID transactions are database transactions that provide atomicity, consistency, isolation, and durability so multi-step writes can be reasoned about as reliable units. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

Atomicity means all writes in the transaction succeed or roll back together, consistency means declared database and business invariants hold before and after the transaction, isolation controls how concurrent transactions observe each other, and durability means committed data survives failure. [[2026-03-31--database-transactions|Database Transactions]] This source emphasizes ACID as a system-design correctness vocabulary for operations involving balances, inventory, orders, and other state where partial writes are unacceptable. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **CAP Consistency**: ACID consistency is about preserving valid database states and constraints, while CAP consistency is about distributed replicas seeing the same data at the same time. [[2026-03-31--database-transactions|Database Transactions]]
- **Saga Pattern**: ACID describes one transaction boundary, while Saga decomposes a distributed workflow into local commits plus compensation. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source defines each ACID property and warns that ACID consistency is different from CAP consistency.

## Related

- [[database-transactions|Database Transactions]]
- [[write-ahead-log|Write-Ahead Log]]
- [[transaction-isolation|Transaction Isolation]]
- [[saga-pattern|Saga Pattern]]
- [[replication|Replication]]

## Open Questions

- Which future source should connect ACID consistency to explicit constraint design, ledger invariants, and schema-level enforcement?
