---
type: concept
aliases: ["idempotent consumers", "idempotent worker", "idempotent message handler", "duplicate-safe consumer"]
tags: [system-design, message-queue, reliability, consistency]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Idempotent Consumer

## Definition

An idempotent consumer is a queue worker or message handler designed so processing the same message more than once does not produce incorrect duplicate effects. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers the consumer-side design required by at-least-once queue delivery. [[2026-05-15--message-queue|Message Queue]] Because a worker can fail after partially completing work or before acknowledging the message, database writes, external API calls, state transitions, and webhook deliveries should use stable IDs, deduplication, conditional updates, or safe state machines where possible. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **At-Least-Once Delivery**: At-least-once delivery may execute a message more than once; idempotent consumers make that delivery model safe. [[2026-05-15--message-queue|Message Queue]]
- **Optimistic Locking**: Optimistic locking detects stale concurrent writes, while idempotent consumers prevent duplicate message handling from creating duplicate effects. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source explicitly states that consumers must assume the same message may be processed more than once.

## Related

- [[message-queue|Message Queue]]
- [[visibility-timeout|Visibility Timeout]]
- [[retry-policy|Retry Policy]]
- [[dead-letter-queue|Dead Letter Queue]]
- [[optimistic-locking|Optimistic Locking]]

## Open Questions

- Which future source should cover idempotency keys, deduplication tables, and exactly-once claims?
