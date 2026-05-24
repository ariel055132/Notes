---
type: concept
aliases: ["leader-follower replication", "primary-replica replication", "master-slave replication"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Single-Leader Replication

## Definition

Single-leader replication is a replication architecture where one replica is designated as the leader or primary, all writes go through that leader, and followers apply the leader's changes from a replication log. [[2026-05-02--replication|Replication]]

## Scope

This concept covers primary/follower roles, write routing, read replicas, synchronous and asynchronous follower updates, follower catch-up, leader failover, and replication lag. [[2026-05-02--replication|Replication]] It is strongest when a system needs a simple write path with no multi-leader write conflicts and can tolerate a single primary as the write coordination point. [[2026-05-02--replication|Replication]]

## Contrasts

- **Multi-Leader Replication**: Single-leader replication avoids write conflicts by routing all writes to one leader, while multi-leader replication allows writes at multiple leaders and must resolve conflicts. [[2026-05-02--replication|Replication]]
- **Leaderless Replication**: Single-leader replication centralizes writes through one node, while leaderless replication lets clients write to multiple replicas directly. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes single-leader replication as the most common and intuitive architecture, with writes handled by the leader and reads optionally served by leader or followers.

## Related

- [[replication|Replication]]
- [[read-replica|Read Replica]]
- [[synchronous-replication|Synchronous Replication]]
- [[asynchronous-replication|Asynchronous Replication]]
- [[replication-log|Replication Log]]
- [[failover|Failover]]
- [[replication-lag|Replication Lag]]

## Open Questions

- Which operational patterns should be added for fencing, controller election, and client rerouting during failover?
