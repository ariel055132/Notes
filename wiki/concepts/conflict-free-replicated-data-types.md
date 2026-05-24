---
type: concept
aliases: ["CRDT", "CRDTs", "conflict-free replicated datatype"]
tags: [system-design, replication, distributed-systems]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Conflict-Free Replicated Data Types

## Definition

Conflict-free replicated data types are data structures designed so concurrent updates on replicas can be merged automatically into a consistent result. [[2026-05-02--replication|Replication]]

## Scope

This concept covers mergeable structures such as counters, sets, and ordered lists when those structures can encode concurrent changes in a way that preserves intended updates. [[2026-05-02--replication|Replication]] It is relevant to multi-leader and leaderless systems where conflict resolution must happen without forcing all writes through one leader. [[2026-05-02--replication|Replication]]

## Contrasts

- **Last Write Wins**: CRDTs aim to preserve concurrent updates for supported data structures, while last-write-wins discards all but one version. [[2026-05-02--replication|Replication]]
- **Operational Transformation**: CRDTs use mergeable replicated data structures, while operational transformation transforms concurrent operations, especially in collaborative text editing. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source presents CRDTs as an automatic conflict-resolution research direction for replicated counters, sets, ordered lists, and similar structures.

## Related

- [[write-conflict-resolution|Write Conflict Resolution]]
- [[multi-leader-replication|Multi-Leader Replication]]
- [[leaderless-replication|Leaderless Replication]]
- [[operational-transformation|Operational Transformation]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should explain CRDT families and their merge laws in detail?
