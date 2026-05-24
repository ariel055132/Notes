---
type: concept
aliases: ["back pressure", "queue backpressure", "producer throttling", "load shedding"]
tags: [system-design, message-queue, reliability, operations]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Backpressure

## Definition

Backpressure is the system behavior of signaling or applying pressure upstream when downstream processing capacity cannot keep up with incoming work. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers queue backlog growth, producer throttling, worker scaling, degradation of noncritical work, and splitting heavy work into smaller stages. [[2026-05-15--message-queue|Message Queue]] The source warns that a queue is not a garbage can: if backlog continues to grow, the underlying consumer or downstream system lacks enough capacity. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Traffic Smoothing**: Traffic smoothing absorbs temporary spikes, while backpressure responds when processing capacity is persistently insufficient. [[2026-05-15--message-queue|Message Queue]]
- **Queue Depth**: Queue depth is one metric that can reveal pressure, while backpressure is the broader control response. [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source says growing backlog means the system should add workers, slow producers, degrade noncore work, or split heavy work into stages.

## Related

- [[message-queue|Message Queue]]
- [[queue-health-metrics|Queue Health Metrics]]
- [[retry-policy|Retry Policy]]
- [[dead-letter-queue|Dead Letter Queue]]
- [[read-scaling|Read Scaling]]

## Open Questions

- Which future source should connect queue backpressure to rate limiting, circuit breakers, and autoscaling?
