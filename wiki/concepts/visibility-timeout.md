---
type: concept
aliases: ["visibility timeout", "message visibility timeout", "ack timeout", "lease timeout"]
tags: [system-design, message-queue, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Visibility Timeout

## Definition

Visibility timeout is the interval during which a queue hides a message after a worker receives it, returning the message to the queue if the worker does not acknowledge success in time. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers acknowledgement-based delivery where a worker receives a message, the queue temporarily hides it, and the message is removed only after an acknowledgement. [[2026-05-15--message-queue|Message Queue]] If the worker crashes or exceeds the timeout before acknowledging, the message can be delivered again to another worker. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Acknowledgement**: Acknowledgement confirms successful processing and removes the message, while visibility timeout controls how long an unacknowledged message stays hidden. [[2026-05-15--message-queue|Message Queue]]
- **Idempotent Consumer**: Visibility timeout can cause duplicate processing, while idempotent consumers make duplicate delivery safe. [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source explains that messages reappear if the worker fails or times out without acknowledging them.

## Related

- [[message-queue|Message Queue]]
- [[idempotent-consumer|Idempotent Consumer]]
- [[retry-policy|Retry Policy]]
- [[dead-letter-queue|Dead Letter Queue]]
- [[queue-health-metrics|Queue Health Metrics]]

## Open Questions

- Which future source should cover choosing visibility timeout from processing-time distributions?
