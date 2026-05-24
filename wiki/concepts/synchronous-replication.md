---
type: concept
aliases: ["sync replication", "semi-synchronous replication", "semi-sync replication"]
tags: [system-design, databases, replication, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Synchronous Replication

## Definition

Synchronous replication is a replication mode where the leader waits for at least one follower to receive and confirm a write before telling the client the write has completed. [[2026-05-02--replication|Replication]]

## Scope

This concept covers durability and freshness guarantees that come from waiting for follower acknowledgement, including semi-synchronous setups where one follower is synchronous and others are asynchronous. [[2026-05-02--replication|Replication]] It does not eliminate every distributed-system failure mode; it trades lower write availability and higher write latency for stronger protection against losing acknowledged writes. [[2026-05-02--replication|Replication]]

## Contrasts

- **Asynchronous Replication**: Synchronous replication improves durability and consistency but can block writes when the synchronous follower does not respond, while asynchronous replication keeps writes fast but may lose writes during leader failure. [[2026-05-02--replication|Replication]]
- **Consensus**: Synchronous follower acknowledgement can reduce failover data loss, while consensus algorithms are needed when the system requires majority agreement on committed writes. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source frames synchronous versus asynchronous replication as a central tradeoff: consistency and durability versus availability and write latency.

## Related

- [[replication|Replication]]
- [[single-leader-replication|Single-Leader Replication]]
- [[asynchronous-replication|Asynchronous Replication]]
- [[failover|Failover]]
- [[replication-lag|Replication Lag]]

## Open Questions

- Which future sources should distinguish synchronous replication from quorum-based consensus in more detail?
