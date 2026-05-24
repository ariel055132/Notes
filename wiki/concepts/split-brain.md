---
type: concept
aliases: ["split-brain failure", "dual primary", "dual leader"]
tags: [system-design, reliability, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Split Brain

## Definition

Split brain is a failure mode where two or more nodes believe they are the leader and accept writes independently, risking divergent or corrupted data. [[2026-05-02--replication|Replication]]

## Scope

This concept covers leader-election ambiguity, network partitions, stale leaders returning after failover, and mechanisms that prevent old leaders from accepting writes after a new leader is chosen. [[2026-05-02--replication|Replication]] It is especially important in single-leader failover because the architecture's no-conflict property depends on there being exactly one active writer. [[2026-05-02--replication|Replication]]

## Contrasts

- **Write Conflict Resolution**: Split brain is an unintended leadership failure in a system meant to have one writer, while write conflict resolution is an expected requirement in systems that intentionally allow multiple writers. [[2026-05-02--replication|Replication]]
- **Replication Lag**: Replication lag is a delay in applying writes, while split brain is a control-plane failure about who may accept writes. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source lists split brain as a key failover hazard and notes that poorly designed shutdown or fencing mechanisms can make failure worse.

## Related

- [[failover|Failover]]
- [[single-leader-replication|Single-Leader Replication]]
- [[multi-leader-replication|Multi-Leader Replication]]
- [[write-conflict-resolution|Write Conflict Resolution]]

## Open Questions

- Which future source should define fencing tokens and STONITH-style mechanisms more rigorously?
