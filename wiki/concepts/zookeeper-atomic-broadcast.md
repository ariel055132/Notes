---
type: concept
aliases: ["ZAB", "ZooKeeper Atomic Broadcast", "atomic broadcast"]
tags: [system-design, distributed-systems, coordination, zookeeper, consensus]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# ZooKeeper Atomic Broadcast

## Definition

ZooKeeper Atomic Broadcast, or ZAB, is the protocol family ZooKeeper uses to order writes through a leader, replicate proposals to followers, and commit updates after quorum accepts them. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers the high-level consistency path for ZooKeeper writes: a request reaches the ZooKeeper leader, the leader orders the change, followers receive the proposal, quorum acceptance commits the update, and watches notify interested clients. [[2026-05-15--zookeeper|Zookeeper]] It is related to consensus systems such as Raft or Paxos, but the source only requires the interview-level understanding that ZooKeeper's consistency comes from ordered quorum replication rather than one machine's memory. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Raft / Paxos**: ZAB is ZooKeeper's atomic-broadcast protocol family, while Raft and Paxos are other consensus protocol families with similar goals around ordered replicated state. [[2026-05-15--zookeeper|Zookeeper]]
- **Asynchronous Replication**: Asynchronous replication may acknowledge before followers apply writes, while ZooKeeper writes commit only after quorum accepts the update. [[2026-05-02--replication|Replication]] [[2026-05-15--zookeeper|Zookeeper]]
- **Quorum Reads and Writes**: Quorum reads/writes describe client-level thresholds in replicated stores, while ZAB describes ZooKeeper's ordered write broadcast. [[2026-05-02--replication|Replication]] [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source explains ZAB as leader-ordered write broadcast where quorum commit makes metadata changes effective.

## Related

- [[zookeeper|ZooKeeper]]
- [[zookeeper-ensemble|ZooKeeper Ensemble]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[synchronous-replication|Synchronous Replication]]
- [[failover|Failover]]

## Open Questions

- Which future source should add a dedicated consensus page comparing ZAB, Raft, Paxos, Zab epochs, and log terms?
