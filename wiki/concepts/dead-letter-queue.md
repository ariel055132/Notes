---
type: concept
aliases: ["DLQ", "dead letter queue", "dead-letter queue", "poison queue"]
tags: [system-design, message-queue, reliability, operations]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Dead Letter Queue

## Definition

A dead letter queue is a separate queue or holding area for messages that could not be processed successfully after the configured retry policy. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers failure surfacing and operational recovery for messages that repeatedly fail due to bad payloads, consumer bugs, permanently unavailable downstream systems, or external errors. [[2026-05-15--message-queue|Message Queue]] The source frames DLQ as the place where engineers or backend processes inspect, compensate, repair, or manually replay failed work. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Retry Policy**: Retry policy handles normal transient failures; DLQ handles messages that exceeded retry limits. [[2026-05-15--message-queue|Message Queue]]
- **Backpressure**: Backpressure indicates processing capacity is insufficient, while DLQ indicates specific messages failed processing enough times to require investigation. [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source says messages should move to a dead letter queue after maximum retry attempts so engineers or backend flows can inspect them.

## Related

- [[message-queue|Message Queue]]
- [[retry-policy|Retry Policy]]
- [[queue-health-metrics|Queue Health Metrics]]
- [[idempotent-consumer|Idempotent Consumer]]
- [[backpressure|Backpressure]]

## Open Questions

- Which future source should define DLQ replay safety checks and operator workflows?
