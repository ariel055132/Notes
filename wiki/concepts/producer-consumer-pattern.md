---
type: concept
aliases: ["producer consumer", "producer/consumer", "consumer worker", "consumer workers", "worker pool"]
tags: [system-design, message-queue, async-processing]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Producer-Consumer Pattern

## Definition

The producer-consumer pattern separates the component that describes and enqueues work from the workers that execute the work. [[2026-05-15--message-queue|Message Queue]]

## Scope

In the queue model from the source, the producer is responsible for describing the work, the queue is responsible for temporary storage and dispatch, and consumer workers execute the work and report success or failure. [[2026-05-15--message-queue|Message Queue]] This separation lets worker pools scale independently, isolates slow downstream dependencies from request latency, and creates a visible backlog when processing capacity falls behind. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Synchronous Call Chain**: A synchronous chain directly calls downstream services during the request, while producer-consumer design inserts a queue boundary. [[2026-05-15--message-queue|Message Queue]]
- **Publish-Subscribe Event Fanout**: A task queue usually sends each task to one consumer, while events may be consumed by multiple subscribers. [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source presents the simplified model `producer -> queue -> consumer workers -> database / object storage / external API`.

## Related

- [[message-queue|Message Queue]]
- [[message-payload|Message Payload]]
- [[visibility-timeout|Visibility Timeout]]
- [[backpressure|Backpressure]]
- [[queue-health-metrics|Queue Health Metrics]]

## Open Questions

- Which future source should compare consumer group semantics across queues and streams?
