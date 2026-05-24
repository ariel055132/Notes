---
type: concept
aliases: ["transactional outbox", "outbox", "outbox messaging"]
tags: [system-design, message-queue, transactions, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Outbox Pattern

## Definition

The outbox pattern stores a message or event record in the same database transaction as the business state change, then publishes it asynchronously to a queue or stream. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers the source's warning that some work must succeed or fail with a database transaction rather than being directly enqueued after the fact. [[2026-05-15--message-queue|Message Queue]] In those cases, the outbox pattern can preserve the local transaction boundary while still enabling later asynchronous delivery. [[2026-05-15--message-queue|Message Queue]] [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Direct Queue Publish**: Directly publishing after a database commit can lose the message if the process crashes between commit and publish; an outbox stores the publish intent inside the same transaction. [[2026-05-15--message-queue|Message Queue]]
- **Saga Pattern**: Outbox is a messaging reliability pattern, while Saga coordinates a multi-step distributed workflow using local transactions and compensation. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source says work that must succeed or fail with a transaction should stay in the same database transaction or use the outbox pattern.

## Related

- [[message-queue|Message Queue]]
- [[database-transactions|Database Transactions]]
- [[saga-pattern|Saga Pattern]]
- [[event-log|Event Log]]
- [[write-behind-cache|Write-Behind Cache]]

## Open Questions

- Which future source should explain polling outbox, CDC-based outbox, and exactly-once delivery claims?
