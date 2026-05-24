---
type: concept
aliases: ["LWW", "timestamp conflict resolution", "last writer wins"]
tags: [system-design, replication, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Last Write Wins

## Definition

Last write wins is a conflict-resolution rule that assigns each write a timestamp or ordering value, keeps the write considered latest, and discards the other concurrent versions. [[2026-05-02--replication|Replication]]

## Scope

This concept covers simple convergence in multi-leader and leaderless systems, especially where losing some writes is acceptable, such as caches or rapidly replaced sensor readings. [[2026-05-02--replication|Replication]] It should be treated as a data-loss tradeoff because concurrent writes that lose the timestamp comparison are silently discarded. [[2026-05-02--replication|Replication]]

## Contrasts

- **Version Vector**: Last write wins collapses concurrent writes to one value, while version vectors help detect concurrency and preserve values that must be merged. [[2026-05-02--replication|Replication]]
- **CRDTs**: Last write wins may discard user intent, while CRDTs are designed so concurrent updates can merge without conflict for supported data types. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source warns that LWW is simple but can lose data and is appropriate only when that loss is acceptable.

## Related

- [[write-conflict-resolution|Write Conflict Resolution]]
- [[multi-leader-replication|Multi-Leader Replication]]
- [[leaderless-replication|Leaderless Replication]]
- [[version-vector|Version Vector]]
- [[conflict-free-replicated-data-types|Conflict-Free Replicated Data Types]]

## Open Questions

- Which future source should cover clock skew and hybrid logical clocks as ordering mechanisms?
