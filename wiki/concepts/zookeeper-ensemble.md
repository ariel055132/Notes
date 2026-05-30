---
type: concept
aliases: ["ZooKeeper ensemble", "ensemble", "ZooKeeper quorum", "ZooKeeper cluster"]
tags: [system-design, distributed-systems, coordination, zookeeper, quorum]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# ZooKeeper Ensemble

## Definition

A ZooKeeper ensemble is a group of ZooKeeper servers, usually an odd number such as 3, 5, or 7, that uses a leader, followers, and quorum to replicate and commit coordination metadata. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers ensemble sizing, leader and follower roles, quorum commit, failure tolerance, and the operational cost of stronger coordination. [[2026-05-15--zookeeper|Zookeeper]] A 3-node ensemble can tolerate 1 failed server, a 5-node ensemble can tolerate 2, and larger ensembles increase write coordination cost. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Leaderless Replication**: Leaderless replication lets clients contact replicas directly, while ZooKeeper ensembles route writes through a leader and commit through quorum. [[2026-05-02--replication|Replication]] [[2026-05-15--zookeeper|Zookeeper]]
- **Distributed Cache Cluster**: A cache cluster optimizes read throughput and capacity, while a ZooKeeper ensemble optimizes correctness of coordination metadata. [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--zookeeper|Zookeeper]]
- **Single ZooKeeper Server**: A single server has no quorum fault tolerance, while an ensemble survives some server failures. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source describes leader, followers, quorum, and common 3/5/7-node ensemble sizing.

## Related

- [[zookeeper|ZooKeeper]]
- [[zookeeper-atomic-broadcast|ZooKeeper Atomic Broadcast]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[failover|Failover]]
- [[split-brain|Split Brain]]

## Open Questions

- Which future source should cover ZooKeeper observer nodes, snapshotting, log disks, and ensemble reconfiguration?
