---
type: concept
aliases: ["conflict resolution", "replication conflict resolution", "write conflict handling"]
tags: [system-design, replication, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Write Conflict Resolution

## Definition

Write conflict resolution is the set of techniques used to handle concurrent writes that update the same data in multi-leader or leaderless replicated systems. [[2026-05-02--replication|Replication]]

## Scope

This concept covers conflict avoidance by routing a record to one leader, convergence rules such as last-write-wins or replica priority, preserving multiple versions for later application-level merge, custom conflict handlers, CRDTs, mergeable persistent data structures, and operational transformation. [[2026-05-02--replication|Replication]] It is required when a system allows more than one write authority to accept updates before those authorities have synchronized. [[2026-05-02--replication|Replication]]

## Contrasts

- **Split Brain**: Write conflict resolution is expected in designs that intentionally allow multiple write authorities, while split brain is an unintended leadership failure in a single-leader design. [[2026-05-02--replication|Replication]]
- **Conflict Avoidance**: Conflict avoidance prevents conflicts by routing all writes for a record to the same leader, while conflict resolution decides what to do after concurrent conflicting writes occur. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes conflict avoidance, convergence strategies, on-write and on-read custom conflict logic, CRDTs, three-way merge, and operational transformation.

## Related

- [[multi-leader-replication|Multi-Leader Replication]]
- [[leaderless-replication|Leaderless Replication]]
- [[last-write-wins|Last Write Wins]]
- [[conflict-free-replicated-data-types|Conflict-Free Replicated Data Types]]
- [[operational-transformation|Operational Transformation]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should add examples for shopping carts, calendars, document editing, and profile updates as separate conflict classes?
