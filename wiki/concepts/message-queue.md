---
type: concept
aliases: ["message queues", "queue", "job queue", "work queue", "brokered queue"]
tags: [system-design, message-queue, async-processing, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Message Queue

## Definition

A message queue is a buffering and delivery mechanism that lets producers hand off work to consumer workers so non-immediate or retryable work can be processed outside the synchronous request path. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers traffic smoothing, asynchronous background jobs, retryable delivery, queue-backed pipelines, and deferred work such as email, external API calls, analytics updates, webhook delivery, scheduled task execution, and media post-processing. [[2026-05-15--message-queue|Message Queue]] The source emphasizes that a queue should be introduced after clarifying whether the message is a task or an event, how much delay is acceptable, whether ordering matters, and how failure is handled. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Synchronous Request Path**: A queue lets the foreground request return after accepting work, while synchronous processing makes the user wait for the full operation. [[2026-05-15--message-queue|Message Queue]]
- **Event Log**: A typical task queue is for work execution, while an event log is better when full event history and replay are required. [[2026-05-15--message-queue|Message Queue]]
- **Database Transaction**: A queue should not replace a database transaction when work must succeed or fail atomically with the request. [[2026-05-15--message-queue|Message Queue]] [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source frames queues as separating "must finish now" from "can finish later" and highlights smoothing, async processing, and retry.

## Related

- [[asynchronous-processing|Asynchronous Processing]]
- [[producer-consumer-pattern|Producer-Consumer Pattern]]
- [[visibility-timeout|Visibility Timeout]]
- [[retry-policy|Retry Policy]]
- [[dead-letter-queue|Dead Letter Queue]]
- [[backpressure|Backpressure]]
- [[outbox-pattern|Outbox Pattern]]

## Open Questions

- Which future source should compare queue ordering guarantees across managed queues, broker queues, and log-based streams?
