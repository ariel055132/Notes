---
type: concept
aliases: ["ACID", "ACID guarantees", "transaction guarantees"]
tags: [system-design, databases, transactions, consistency]
created: 2026-05-24
updated: 2026-05-26
source_count: 2
---

# ACID Transactions

## Definition

ACID transactions are database transactions that provide atomicity, consistency, isolation, and durability so multi-step writes can be reasoned about as reliable units. [[2026-03-31--database-transactions|Database Transactions]] The database overview presents ACID as the core relational-database promise that makes RDBMS a natural fit for business transactions involving money, inventory, orders, payments, or state changes. [[2026-04-15--database|Database]]

## Scope

Atomicity means all writes in the transaction succeed or roll back together, consistency means declared database and business invariants hold before and after the transaction, isolation controls how concurrent transactions observe each other, and durability means committed data survives failure. [[2026-03-31--database-transactions|Database Transactions]] This source emphasizes ACID as a system-design correctness vocabulary for operations involving balances, inventory, orders, and other state where partial writes are unacceptable. [[2026-03-31--database-transactions|Database Transactions]] The database overview uses the same ACID framing to distinguish relational systems from NoSQL systems that may relax immediate consistency for horizontal scale. [[2026-04-15--database|Database]]

## Contrasts

- **CAP Consistency**: ACID consistency is about preserving valid database states and constraints, while CAP consistency is about distributed replicas seeing the same data at the same time. [[2026-03-31--database-transactions|Database Transactions]]
- **Saga Pattern**: ACID describes one transaction boundary, while Saga decomposes a distributed workflow into local commits plus compensation. [[2026-03-31--database-transactions|Database Transactions]]
- **BASE Consistency Model**: ACID prioritizes transaction correctness, while BASE relaxes immediate consistency to improve availability or horizontal scalability. [[2026-04-15--database|Database]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source defines each ACID property and warns that ACID consistency is different from CAP consistency.
- [[2026-04-15--database|Database]] — The source describes ACID as the key reason relational databases fit correctness-critical business transactions.

## Related

- [[database|Database]]
- [[relational-database|Relational Database]]
- [[database-transactions|Database Transactions]]
- [[base-consistency-model|BASE Consistency Model]]
- [[write-ahead-log|Write-Ahead Log]]
- [[transaction-isolation|Transaction Isolation]]
- [[saga-pattern|Saga Pattern]]
- [[replication|Replication]]

## Open Questions

- Which future source should connect ACID consistency to explicit constraint design, ledger invariants, and schema-level enforcement?
