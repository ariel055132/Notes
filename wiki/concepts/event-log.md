---
type: concept
aliases: ["event logs", "durable event log", "stream log", "replayable stream"]
tags: [system-design, message-queue, event-streaming, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Event Log

## Definition

An event log is an append-oriented, replayable history of events used when consumers need retention, replay, or multiple independent subscriber groups rather than one-time job execution. [[2026-05-15--message-queue|Message Queue]]

## Scope

This concept covers the source's distinction between simple job queues and stream or log systems used for high-throughput events, replay, or multiple consumer groups. [[2026-05-15--message-queue|Message Queue]] It is relevant when complete event history matters, when multiple teams or systems need to replay the same events, or when a queue should behave more like a durable stream. [[2026-05-15--message-queue|Message Queue]]

## Contrasts

- **Message Queue**: A message queue often represents work to execute once, while an event log preserves event history for replay and multiple consumers. [[2026-05-15--message-queue|Message Queue]]
- **Replication Log**: A replication log is a database change stream used to replicate state, while an event log is an application or platform stream used by consumers for processing and replay. [[2026-05-02--replication|Replication]] [[2026-05-15--message-queue|Message Queue]]

## Evidence

- [[2026-05-15--message-queue|Message Queue]] — The source says Kafka-like systems are more like logs or streams than simple job queues and are appropriate when replay or multiple consumer groups matter.

## Related

- [[message-queue|Message Queue]]
- [[producer-consumer-pattern|Producer-Consumer Pattern]]
- [[lsm-tree|LSM Tree]]
- [[replication-log|Replication Log]]
- [[materialized-view|Materialized View]]

## Open Questions

- Which future source should cover event sourcing and stream processing as separate concepts?
