---
type: concept
aliases: ["quorum reads", "quorum writes", "quorum replication", "quorum consistency"]
tags: [system-design, databases, replication, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Quorum Reads and Writes

## Definition

Quorum reads and writes are leaderless-replication operations where a write must be acknowledged by `w` replicas, a read queries `r` replicas, and the system chooses values so that `w + r > n` for `n` total replicas. [[2026-05-02--replication|Replication]]

## Scope

This concept covers overlap between read and write replica sets, common configurations such as `n = 3, w = 2, r = 2`, and tradeoffs between read latency, write latency, and fault tolerance. [[2026-05-02--replication|Replication]] It also covers limitations: sloppy quorum, concurrent writes, concurrent read/write races, and failure/recovery sequences can still allow stale reads or lost conflict information. [[2026-05-02--replication|Replication]]

## Contrasts

- **Synchronous Replication**: Quorum reads and writes rely on threshold overlap across replicas, while synchronous replication often describes a leader waiting for follower acknowledgement before committing. [[2026-05-02--replication|Replication]]
- **Sloppy Quorum**: Strict quorum uses the intended replica set, while sloppy quorum can accept writes on reachable non-home nodes and weakens the overlap guarantee. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source explains `w + r > n` as the condition that makes read and write sets overlap, then lists cases where quorum still does not provide stronger session or causal guarantees.

## Related

- [[leaderless-replication|Leaderless Replication]]
- [[sloppy-quorum|Sloppy Quorum]]
- [[hinted-handoff|Hinted Handoff]]
- [[read-repair|Read Repair]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should formalize quorum guarantees under partitions, clocks, and concurrent writes?
