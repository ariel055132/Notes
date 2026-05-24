---
type: concept
aliases: ["Dynamo-style replication", "leaderless database replication"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Leaderless Replication

## Definition

Leaderless replication is a replication architecture where clients can send reads and writes directly to multiple replicas instead of routing writes through a designated leader. [[2026-05-02--replication|Replication]]

## Scope

This concept covers high write availability, writing to multiple replicas, reading from multiple replicas, stale replica detection, read repair, anti-entropy, quorum reads and writes, sloppy quorum, hinted handoff, last-write-wins, and version vectors. [[2026-05-02--replication|Replication]] It is suited to workloads that can tolerate eventual consistency or application-level merge logic in exchange for remaining writable through node failures. [[2026-05-02--replication|Replication]]

## Contrasts

- **Single-Leader Replication**: Leaderless replication lets replicas accept writes directly, while single-leader replication centralizes writes through one primary. [[2026-05-02--replication|Replication]]
- **Multi-Leader Replication**: Leaderless replication has no special leader role, while multi-leader replication has multiple write leaders that replicate with each other. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes leaderless replication as the Dynamo-style architecture behind systems such as Cassandra-like designs, emphasizing quorum behavior and weak consistency tradeoffs.

## Related

- [[replication|Replication]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[read-repair|Read Repair]]
- [[anti-entropy-process|Anti-Entropy Process]]
- [[sloppy-quorum|Sloppy Quorum]]
- [[hinted-handoff|Hinted Handoff]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future sources should compare leaderless replication with consensus-backed replicated logs?
