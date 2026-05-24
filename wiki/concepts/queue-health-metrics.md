---
type: concept
aliases: ["queue metrics", "queue depth", "oldest message age", "DLQ count", "retry rate"]
tags: [system-design, message-queue, observability, operations]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Queue Health Metrics

## Definition

Queue health metrics are the operational measurements used to understand queue backlog, user-visible delay, worker performance, retry behavior, and failed work. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers queue depth, oldest message age, processing latency, retry rate, and dead letter queue count. [[2026-05-15--message-queue|Message Queue]] The source notes that oldest message age is often closer to user experience than raw queue depth because it tells how long the oldest unit of work has waited. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Queue Depth**: Queue depth counts waiting work, while oldest message age captures delay and SLO risk. [[2026-05-15--message-queue|Message Queue]]
- **DLQ Count**: Retry rate can indicate instability or bugs, while DLQ count indicates work that exceeded automatic recovery and needs investigation or compensation. [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source lists queue depth, oldest message age, processing latency, retry rate, and DLQ count as the core health metrics for queue systems.

## Related

- [[message-queue|Message Queue]]
- [[backpressure|Backpressure]]
- [[retry-policy|Retry Policy]]
- [[dead-letter-queue|Dead Letter Queue]]
- [[visibility-timeout|Visibility Timeout]]

## Open Questions

- Which future source should define alert thresholds and autoscaling signals for queue workers?
