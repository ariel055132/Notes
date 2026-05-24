---
type: concept
aliases: ["async processing", "background processing", "background job", "background jobs", "deferred work"]
tags: [system-design, message-queue, async-processing, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Asynchronous Processing

## Definition

Asynchronous processing moves work out of the user-facing request path so the foreground flow can acknowledge receipt or return a processing state while background workers complete slower work later. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers operations whose final completion is not required before responding to the user, such as analytics aggregation after QR redirects, webhook delivery retries, scheduled task execution, and video post-processing stages. [[2026-05-15--message-queue|Message Queue]] It is useful when the deferred work is slow, unstable, retryable, or independently scalable. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Synchronous Processing**: Synchronous processing is required when the user must know the final result immediately, while asynchronous processing fits accepted or processing states. [[2026-05-15--message-queue|Message Queue]]
- **Write-Behind Cache**: Write-behind cache is one specific asynchronous write-buffering pattern; asynchronous processing is the broader workflow pattern. [[2026-05-24--caching|Caching]] [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source uses QR scan analytics, webhook delivery, scheduled tasks, and video processing as examples of work moved behind a queue.

## Related

- [[message-queue|Message Queue]]
- [[producer-consumer-pattern|Producer-Consumer Pattern]]
- [[write-behind-cache|Write-Behind Cache]]
- [[materialized-view|Materialized View]]
- [[queue-health-metrics|Queue Health Metrics]]

## Open Questions

- Which future source should define user-facing accepted, pending, and processing states for async workflows?
