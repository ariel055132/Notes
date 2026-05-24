---
type: concept
aliases: ["automatic failover", "leader failover", "primary failover"]
tags: [system-design, reliability, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Failover

## Definition

Failover is the process of recovering from leader failure by promoting another replica to leader, redirecting client writes, and reconfiguring the remaining replicas to follow the new leader. [[2026-05-02--replication|Replication]]

## Scope

This concept covers failure detection, leader election or controller-driven promotion, selecting the most up-to-date replica, client rerouting, demoting an old leader after it returns, and avoiding split brain. [[2026-05-02--replication|Replication]] It is central to high availability because a single-leader system cannot accept writes through a failed leader. [[2026-05-02--replication|Replication]]

## Contrasts

- **Follower Catch-Up**: Follower catch-up restores a failed follower by replaying missed changes, while failover changes which node accepts writes. [[2026-05-02--replication|Replication]]
- **Conflict Resolution**: Failover prevents or repairs leader loss in a single-leader system, while conflict resolution handles concurrent writes in multi-leader or leaderless systems. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes automatic failover as detecting leader failure, choosing a new leader, and reconfiguring clients and followers.

## Related

- [[single-leader-replication|Single-Leader Replication]]
- [[split-brain|Split Brain]]
- [[synchronous-replication|Synchronous Replication]]
- [[asynchronous-replication|Asynchronous Replication]]
- [[replication-lag|Replication Lag]]

## Open Questions

- Which future sources should cover fencing tokens, leases, and consensus-backed failover in production systems?
