---
type: concept
aliases: ["multi-master replication", "active-active replication", "multi-primary replication"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Multi-Leader Replication

## Definition

Multi-leader replication is a replication architecture where multiple leaders can accept writes and replicate their changes to the other leaders and their followers. [[2026-05-02--replication|Replication]]

## Scope

This concept covers multi-datacenter deployments, offline operation, collaborative editing, leader-to-leader topologies, asynchronous cross-region replication, and write conflict handling. [[2026-05-02--replication|Replication]] It is usually not worth the complexity inside a single datacenter, but it can reduce user-visible write latency and improve datacenter-failure tolerance across geographic regions. [[2026-05-02--replication|Replication]]

## Contrasts

- **Single-Leader Replication**: Multi-leader replication reduces dependence on a single write leader, while single-leader replication avoids write conflicts by centralizing writes. [[2026-05-02--replication|Replication]]
- **Leaderless Replication**: Multi-leader systems still distinguish leader nodes that coordinate writes, while leaderless systems let clients write directly to replicas without a leader role. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source presents multi-leader replication as useful for multi-datacenter, offline, and collaborative-editing scenarios, with write conflict resolution as the main challenge.

## Related

- [[replication|Replication]]
- [[write-conflict-resolution|Write Conflict Resolution]]
- [[last-write-wins|Last Write Wins]]
- [[conflict-free-replicated-data-types|Conflict-Free Replicated Data Types]]
- [[operational-transformation|Operational Transformation]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should compare active-active databases, offline sync, and collaborative editing under one conflict-resolution framework?
