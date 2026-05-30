---
type: concept
aliases: ["database transaction", "transaction", "transactions", "ACID transaction"]
tags: [system-design, databases, transactions, consistency]
created: 2026-05-24
updated: 2026-05-26
source_count: 2
---

# Database Transactions

## Definition

A database transaction is a logical unit that groups related database operations so they are executed as one correctness boundary rather than as independent partial steps. [[2026-03-31--database-transactions|Database Transactions]] Relational databases use ACID transactions as a core reason they fit money, inventory, order, payment, and state-transition workflows. [[2026-04-15--database|Database]]

## Scope

This concept covers local database work such as account transfers, order creation, inventory deduction, and payment request creation where partial success would leave invalid state. [[2026-03-31--database-transactions|Database Transactions]] In system design, the important question is not just whether a transaction exists, but which records and invariants are inside the transaction boundary, which isolation level is required, and what happens when the workflow crosses service, database, or shard boundaries. [[2026-03-31--database-transactions|Database Transactions]] The database overview connects this to selection: choose a relational system when ACID, constraints, and complex SQL are central requirements. [[2026-04-15--database|Database]]

## Contrasts

- **Single-Shard Transaction**: A database transaction may be local to one database or shard; a single-shard transaction is the distributed-data design pattern that deliberately keeps the invariant local. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--sharding|Sharding]]
- **Cross-Shard Transaction**: A local database transaction uses one database's atomic commit, while a cross-shard transaction requires distributed coordination or a weaker consistency workflow. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--sharding|Sharding]]
- **BASE Consistency Model**: Database transactions emphasize ACID correctness inside a transaction boundary, while BASE relaxes immediate consistency for availability and scale. [[2026-04-15--database|Database]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source uses transfers and order workflows to explain why a set of related database steps should commit or roll back together.
- [[2026-04-15--database|Database]] — The source explains ACID as the central relational-database guarantee for business transactions.

## Related

- [[database|Database]]
- [[relational-database|Relational Database]]
- [[acid-transactions|ACID Transactions]]
- [[base-consistency-model|BASE Consistency Model]]
- [[transaction-isolation|Transaction Isolation]]
- [[single-shard-transaction|Single-Shard Transaction]]
- [[cross-shard-transaction|Cross-Shard Transaction]]
- [[saga-pattern|Saga Pattern]]

## Open Questions

- Which future source should add transaction examples for reservations, ledger design, and idempotent payment workflows?
