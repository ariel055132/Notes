---
type: concept
aliases: ["automatic failover", "leader failover", "primary failover"]
tags: [system-design, reliability, replication, locking]
created: 2026-05-24
updated: 2026-05-26
source_count: 3
---

# Failover

## Definition

Failover is the process of recovering from leader failure by promoting another replica to leader, redirecting client writes, and reconfiguring the remaining replicas to follow the new leader. [[2026-05-02--replication|Replication]] Lease and fencing-token mechanisms are often needed around failover so an old leader that later resumes cannot continue writing stale state. [[2026-05-15--distributed-lock|Distributed Lock]] ZooKeeper supports failover through session expiry, ephemeral-node deletion, watches, and leader election. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers failure detection, leader election or controller-driven promotion, selecting the most up-to-date replica, client rerouting, demoting an old leader after it returns, and avoiding split brain. [[2026-05-02--replication|Replication]] It also covers the coordination problem of making old owners harmless through leases, fencing tokens, session expiry, or version checks. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]] It is central to high availability because a single-leader system cannot accept writes through a failed leader. [[2026-05-02--replication|Replication]]

## Contrasts

- **Follower Catch-Up**: Follower catch-up restores a failed follower by replaying missed changes, while failover changes which node accepts writes. [[2026-05-02--replication|Replication]]
- **Conflict Resolution**: Failover prevents or repairs leader loss in a single-leader system, while conflict resolution handles concurrent writes in multi-leader or leaderless systems. [[2026-05-02--replication|Replication]]
- **Distributed Lock**: Distributed lock or lease ownership can help elect a temporary owner, while failover must also ensure stale owners cannot write after promotion. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Leader Election**: Leader election chooses the new owner, while failover includes detection, promotion, routing changes, and old-owner handling. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes automatic failover as detecting leader failure, choosing a new leader, and reconfiguring clients and followers.
- [[2026-05-15--distributed-lock|Distributed Lock]] — The source explains that fencing tokens or version checks reject writes from expired owners that resume after a pause or network delay.
- [[2026-05-15--zookeeper|Zookeeper]] — The source uses Robotaxi dispatchers, schedulers, and broker controllers to show session-backed leader election and failover.

## Related

- [[single-leader-replication|Single-Leader Replication]]
- [[split-brain|Split Brain]]
- [[synchronous-replication|Synchronous Replication]]
- [[asynchronous-replication|Asynchronous Replication]]
- [[replication-lag|Replication Lag]]
- [[fencing-token|Fencing Token]]
- [[lease-based-locking|Lease-Based Locking]]
- [[leader-election|Leader Election]]
- [[zookeeper-session|ZooKeeper Session]]

## Open Questions

- Which future sources should cover fencing tokens, leases, and consensus-backed failover in production systems?
