---
type: concept
aliases: ["message body", "job payload", "queue payload", "event payload"]
tags: [system-design, message-queue, async-processing]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Message Payload

## Definition

A message payload is the data placed in a queue message so a consumer can reconstruct and execute the intended work. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers designing messages with identifiers, object-storage paths, target operation parameters, stable event IDs, and enough metadata to make the consumer independent of the original request context. [[2026-05-15--message-queue|Message Queue]] The source warns against putting large data bodies directly in the queue; for example, video processing messages should carry a video ID, object-storage path, and desired output resolutions rather than the video bytes. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Large File Transfer**: A queue message should reference a large file in object storage rather than embedding the file itself. [[2026-05-15--message-queue|Message Queue]]
- **Idempotency Key**: A payload carries the work description, while an idempotency key or stable event ID helps consumers deduplicate repeated deliveries. [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source says messages should contain enough information to rebuild the work but not large data bodies.

## Related

- [[message-queue|Message Queue]]
- [[producer-consumer-pattern|Producer-Consumer Pattern]]
- [[idempotent-consumer|Idempotent Consumer]]
- [[event-log|Event Log]]

## Open Questions

- Which future source should define message schema versioning and compatibility rules?
