---
type: concept
aliases: ["retry policies", "exponential backoff", "bounded retry", "retry backoff"]
tags: [system-design, message-queue, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Retry Policy

## Definition

A retry policy defines when and how failed queue work is attempted again, including backoff, maximum attempts, and escalation to dead letter handling. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers retrying transient failures such as timeout, temporary downstream unavailability, or external API errors without requiring the user to resubmit the original request. [[2026-05-15--message-queue|Message Queue]] The source recommends exponential backoff and a maximum retry count, then moving messages to a dead letter queue when attempts are exhausted. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Unbounded Retry**: Unbounded retry can repeatedly overload an unhealthy downstream system, while a bounded retry policy limits attempts and exposes failures. [[2026-05-15--message-queue|Message Queue]]
- **Dead Letter Queue**: Retry policy decides how to retry; a dead letter queue stores messages that exceeded the retry policy. [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source says retry is not simply resending forever and recommends exponential backoff plus maximum retry attempts.

## Related

- [[message-queue|Message Queue]]
- [[dead-letter-queue|Dead Letter Queue]]
- [[visibility-timeout|Visibility Timeout]]
- [[backpressure|Backpressure]]
- [[queue-health-metrics|Queue Health Metrics]]

## Open Questions

- Which future source should describe retry jitter, poison-message detection, and retry storm prevention?
