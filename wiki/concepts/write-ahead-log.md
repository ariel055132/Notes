---
type: concept
aliases: ["WAL", "write ahead log", "transaction log"]
tags: [system-design, databases, transactions, durability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Write-Ahead Log

## Definition

A write-ahead log is a durable log that records intended database changes before the database relies on those changes being applied to data pages, enabling recovery, rollback, and durability after crashes. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers the recovery mechanism behind transaction atomicity and durability: if a database crashes during a transaction, it can inspect the log to decide which work should be completed and which work should be rolled back. [[2026-03-31--database-transactions|Database Transactions]] It also relates to replication logs because some replicated systems ship write-ahead log data or logical log entries to followers. [[2026-05-02--replication|Replication]]

## Contrasts

- **Replication Log**: A write-ahead log primarily supports local transaction recovery and durability, while a replication log is consumed by replicas so they can apply the same changes. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-02--replication|Replication]]
- **Application Event Log**: A WAL is a database storage and recovery structure, while an application event log records domain events for workflows or downstream consumers. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source explains WAL as recording intended work before the real write so restart can complete or roll back interrupted transactions.

## Related

- [[acid-transactions|ACID Transactions]]
- [[database-transactions|Database Transactions]]
- [[replication-log|Replication Log]]

## Open Questions

- No dedicated durability page exists yet; decide whether durability should remain part of the ACID page or become its own concept after future storage-engine sources.
