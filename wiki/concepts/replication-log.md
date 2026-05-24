---
type: concept
aliases: ["replication logs", "write-ahead log shipping", "logical replication log", "binlog"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Replication Log

## Definition

A replication log is an ordered record of data changes that replicas consume so they can apply the same writes and converge toward the leader's state. [[2026-05-02--replication|Replication]]

## Scope

This concept covers statement-based replication, write-ahead log shipping, logical row-based replication, trigger-based replication, follower catch-up positions, and log coordinates such as log sequence numbers or binlog positions. [[2026-05-02--replication|Replication]] It also supports lag-aware reads because clients or routers can compare a user's last write position to a replica's applied log position. [[2026-05-02--replication|Replication]]

## Contrasts

- **Statement-Based Replication**: Replicates SQL statements but can diverge when statements use nondeterministic functions or side effects. [[2026-05-02--replication|Replication]]
- **Write-Ahead Log Shipping**: Replicates low-level storage-engine log bytes, which can couple replication tightly to storage format and version. [[2026-05-02--replication|Replication]]
- **Logical Log Replication**: Replicates row-level changes in a storage-engine-independent format and can serve as a basis for change data capture. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source compares several replication-log implementations and connects log positions to follower creation and read-after-write routing.

## Related

- [[replication|Replication]]
- [[single-leader-replication|Single-Leader Replication]]
- [[read-after-write-consistency|Read-After-Write Consistency]]
- [[replication-lag|Replication Lag]]

## Open Questions

- Should change data capture become a dedicated page after ingesting a source focused on event streams or data pipelines?
