---
type: concept
aliases: ["split-brain failure", "dual primary", "dual leader"]
tags: [system-design, reliability, replication, locking]
created: 2026-05-24
updated: 2026-05-26
source_count: 3
---

# Split Brain

## Definition

Split brain is a failure mode where two or more nodes believe they are the leader and accept writes independently, risking divergent or corrupted data. [[2026-05-02--replication|Replication]] Distributed-lock stale-owner failures are a smaller version of the same control problem: an expired owner can still act unless downstream writes are fenced. [[2026-05-15--distributed-lock|Distributed Lock]] ZooKeeper-style coordination reduces split-brain risk by making leadership and ownership explicit coordination metadata. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers leader-election ambiguity, network partitions, stale leaders returning after failover, and mechanisms that prevent old leaders from accepting writes after a new leader is chosen. [[2026-05-02--replication|Replication]] It also covers stale lease owners that resume after lock expiry and attempt to write with obsolete authority. [[2026-05-15--distributed-lock|Distributed Lock]] ZooKeeper connects this to session timeout and ephemeral-node cleanup: until a session expires, the system may still treat an owner as alive, so timeout tuning matters. [[2026-05-15--zookeeper|Zookeeper]] It is especially important in single-leader failover because the architecture's no-conflict property depends on there being exactly one active writer. [[2026-05-02--replication|Replication]]

## Contrasts

- **Write Conflict Resolution**: Split brain is an unintended leadership failure in a system meant to have one writer, while write conflict resolution is an expected requirement in systems that intentionally allow multiple writers. [[2026-05-02--replication|Replication]]
- **Replication Lag**: Replication lag is a delay in applying writes, while split brain is a control-plane failure about who may accept writes. [[2026-05-02--replication|Replication]]
- **Fencing Token**: Fencing tokens do not prevent every split-brain condition, but they can make stale leaders or expired lock owners unable to overwrite newer state. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Service Discovery**: Service discovery tracks live instances; split-brain prevention also requires agreeing on which instance may act as leader or owner. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source lists split brain as a key failover hazard and notes that poorly designed shutdown or fencing mechanisms can make failure worse.
- [[2026-05-15--distributed-lock|Distributed Lock]] — The source explains why TTL alone is insufficient when an old owner wakes up and tries to write after another owner has acquired a newer token.
- [[2026-05-15--zookeeper|Zookeeper]] — The source uses dispatcher leadership and partition ownership to show why strong coordination is needed when two active leaders would be dangerous.

## Related

- [[failover|Failover]]
- [[single-leader-replication|Single-Leader Replication]]
- [[multi-leader-replication|Multi-Leader Replication]]
- [[write-conflict-resolution|Write Conflict Resolution]]
- [[fencing-token|Fencing Token]]
- [[lease-based-locking|Lease-Based Locking]]
- [[leader-election|Leader Election]]
- [[zookeeper-session|ZooKeeper Session]]

## Open Questions

- Which future source should define fencing tokens and STONITH-style mechanisms more rigorously?
