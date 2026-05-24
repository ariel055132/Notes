---
type: concept
aliases: ["OT", "operation transformation", "collaborative editing transformation"]
tags: [system-design, collaboration, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Operational Transformation

## Definition

Operational transformation is an algorithm family for collaborative editing that transforms concurrent operations so users can edit shared ordered content while replicas converge. [[2026-05-02--replication|Replication]]

## Scope

This concept covers collaborative document editing where each participant applies local edits immediately and replicas exchange operations asynchronously. [[2026-05-02--replication|Replication]] It is presented as a specialized conflict-resolution approach for ordered character lists and similar collaborative editing structures. [[2026-05-02--replication|Replication]]

## Contrasts

- **CRDTs**: Operational transformation transforms operations against one another, while CRDTs use data structures whose concurrent updates can merge by construction. [[2026-05-02--replication|Replication]]
- **Last Write Wins**: Operational transformation aims to preserve concurrent edits, while last-write-wins discards all but one concurrent value. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source names operational transformation as the approach used by Etherpad and Google Docs-style collaborative editing systems.

## Related

- [[write-conflict-resolution|Write Conflict Resolution]]
- [[multi-leader-replication|Multi-Leader Replication]]
- [[conflict-free-replicated-data-types|Conflict-Free Replicated Data Types]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should compare operational transformation and CRDTs for modern collaborative editors?
