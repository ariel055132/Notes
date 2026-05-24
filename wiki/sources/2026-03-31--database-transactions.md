---
type: source
source_path: raw/archive/Database Transactions.pdf
title: "Database Transactions"
author: "BuildMoat"
date: 2026-03-31
tags: [system-design, databases, transactions, consistency]
created: 2026-05-24
---

# Database Transactions

## Summary

This source explains database transactions as the mechanism for grouping related database operations into one logical unit so system-design workflows such as transfers, order creation, inventory deduction, and payment initiation do not leave partial state behind. [[2026-03-31--database-transactions|Database Transactions]] It frames ACID as the core correctness contract: atomicity rolls back partial work, consistency preserves constraints, isolation controls concurrent behavior, and durability keeps committed data after failure. [[2026-03-31--database-transactions|Database Transactions]] The source emphasizes isolation as the main design tradeoff, comparing common isolation levels, read anomalies, MVCC, lost updates, optimistic locking, pessimistic locking, and deadlock handling. [[2026-03-31--database-transactions|Database Transactions]] It also extends the transaction discussion into distributed systems by contrasting two-phase commit with Saga, positioning Saga as the more common microservice approach when availability and fault tolerance matter more than a single global ACID commit. [[2026-03-31--database-transactions|Database Transactions]]

## Key Claims

1. A transaction should wrap multi-step database work that must succeed or fail as one unit, especially where money movement, inventory, reservations, or other invariants would be corrupted by partial completion. [[2026-03-31--database-transactions|Database Transactions]]
2. ACID captures the core guarantees expected from reliable transactions: all-or-nothing execution, preservation of valid database states, isolation from concurrent transactions, and persistence after commit. [[2026-03-31--database-transactions|Database Transactions]]
3. The consistency in ACID means application and database invariants remain valid before and after a transaction; it is not the same concept as consistency in CAP, which concerns replica agreement. [[2026-03-31--database-transactions|Database Transactions]]
4. Isolation levels trade correctness protection for concurrency: Read Uncommitted allows dirty reads, Read Committed prevents dirty reads, Repeatable Read prevents non-repeatable reads, and Serializable prevents dirty, non-repeatable, and phantom reads. [[2026-03-31--database-transactions|Database Transactions]]
5. MVCC improves concurrency by letting reads use a snapshot or older committed version instead of forcing every reader and writer to block one another. [[2026-03-31--database-transactions|Database Transactions]]
6. Lost update is a common system-design bug where concurrent transactions overwrite each other's computed writes; atomic conditional updates, optimistic locking, or pessimistic row locks are typical fixes. [[2026-03-31--database-transactions|Database Transactions]]
7. Cross-service transactions are fundamentally harder than local database transactions: 2PC provides stronger coordination but weaker availability, while Saga uses local transactions and compensation to reach eventual consistency. [[2026-03-31--database-transactions|Database Transactions]]
8. Strong system-design answers should state the transaction boundary, isolation level, concurrency-control mechanism, deadlock/retry strategy, and distributed consistency tradeoff instead of merely saying "use a transaction." [[2026-03-31--database-transactions|Database Transactions]]

## Notable Quotes

- "Transaction is the core function of database systems." [[2026-03-31--database-transactions|Database Transactions]]
- "Isolation is the most flexible part of ACID." [[2026-03-31--database-transactions|Database Transactions]]
- "Do not only say 'I use transaction'." [[2026-03-31--database-transactions|Database Transactions]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter rather than as a dedicated entity page. [[2026-03-31--database-transactions|Database Transactions]]

## Concepts Mentioned

- [[database-transactions|Database Transactions]] — Grouping related database operations into one logical unit. [[2026-03-31--database-transactions|Database Transactions]]
- [[acid-transactions|ACID Transactions]] — The core transaction guarantees of atomicity, consistency, isolation, and durability. [[2026-03-31--database-transactions|Database Transactions]]
- [[write-ahead-log|Write-Ahead Log]] — Logging intended changes before data pages are considered durable, supporting recovery and rollback. [[2026-03-31--database-transactions|Database Transactions]]
- [[transaction-isolation|Transaction Isolation]] — The part of ACID that controls how concurrent transactions observe and interfere with one another. [[2026-03-31--database-transactions|Database Transactions]]
- [[read-uncommitted|Read Uncommitted]] — The lowest isolation level, allowing reads of uncommitted writes. [[2026-03-31--database-transactions|Database Transactions]]
- [[read-committed|Read Committed]] — An isolation level that prevents dirty reads by exposing only committed data. [[2026-03-31--database-transactions|Database Transactions]]
- [[repeatable-read|Repeatable Read]] — An isolation level where repeated reads of the same row inside one transaction stay stable. [[2026-03-31--database-transactions|Database Transactions]]
- [[serializable-isolation|Serializable Isolation]] — The strongest common isolation model, equivalent to transactions running in some serial order. [[2026-03-31--database-transactions|Database Transactions]]
- [[dirty-read|Dirty Read]] — Reading another transaction's uncommitted data. [[2026-03-31--database-transactions|Database Transactions]]
- [[non-repeatable-read|Non-Repeatable Read]] — Reading the same row twice in one transaction and seeing different committed values. [[2026-03-31--database-transactions|Database Transactions]]
- [[phantom-read|Phantom Read]] — Repeating a range query and seeing rows appear or disappear because another transaction committed inserts or deletes. [[2026-03-31--database-transactions|Database Transactions]]
- [[multi-version-concurrency-control|Multi-Version Concurrency Control]] — Keeping multiple committed versions so readers can use a snapshot while writers proceed. [[2026-03-31--database-transactions|Database Transactions]]
- [[lost-update|Lost Update]] — Concurrent read-modify-write operations overwriting one another. [[2026-03-31--database-transactions|Database Transactions]]
- [[optimistic-locking|Optimistic Locking]] — Detecting write conflicts at commit or update time, often with a version column. [[2026-03-31--database-transactions|Database Transactions]]
- [[pessimistic-locking|Pessimistic Locking]] — Locking rows before update to prevent concurrent conflicting writes. [[2026-03-31--database-transactions|Database Transactions]]
- [[deadlock|Deadlock]] — Transactions wait on each other's locks so one must be rolled back or retried. [[2026-03-31--database-transactions|Database Transactions]]
- [[two-phase-commit|Two-Phase Commit]] — A distributed commit protocol with prepare and commit/abort phases. [[2026-03-31--database-transactions|Database Transactions]]
- [[saga-pattern|Saga Pattern]] — A distributed workflow of local transactions plus compensation. [[2026-03-31--database-transactions|Database Transactions]]
- [[single-shard-transaction|Single-Shard Transaction]] — The local transaction case that preserves invariants inside one shard. [[2026-03-31--database-transactions|Database Transactions]]
- [[cross-shard-transaction|Cross-Shard Transaction]] — The distributed coordination case that motivates 2PC, Saga, or redesigning boundaries. [[2026-03-31--database-transactions|Database Transactions]]

## Follow-ups

- File a synthesis comparing local ACID transactions, single-shard transactions, cross-shard transactions, 2PC, Saga, and replication consistency as a system-design consistency decision tree.
