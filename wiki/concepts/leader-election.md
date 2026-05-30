---
type: concept
aliases: ["leader election", "controller election", "leader candidate", "active leader election"]
tags: [system-design, distributed-systems, coordination, reliability]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Leader Election

## Definition

Leader election is the process of choosing exactly one active owner or controller among candidates so one node coordinates a task, region, partition, controller role, or scheduler responsibility. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers ZooKeeper-style leader election with sequential ephemeral znodes, where the smallest sequence number is leader and other candidates watch their predecessor. [[2026-05-15--zookeeper|Zookeeper]] It also covers the system-design need behind the mechanism: avoiding two active leaders for the same region, bucket, market, partition, controller, or sequencer. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Failover**: Leader election chooses a new owner or leader, while failover includes detection, promotion, rerouting, and making old owners harmless. [[2026-05-02--replication|Replication]] [[2026-05-15--zookeeper|Zookeeper]]
- **Single-Writer Pattern**: Leader election chooses who the single writer is, while single-writer pattern is the architectural decision that writes for a resource should be serialized through one owner. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]]
- **Distributed Lock**: Leader election usually chooses an owner for a continuing role, while a distributed lock often protects one shorter critical section. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source describes creating sequential ephemeral candidate nodes, selecting the smallest sequence as leader, and watching the immediate predecessor to avoid herd effects.

## Related

- [[zookeeper|ZooKeeper]]
- [[sequential-znode|Sequential ZNode]]
- [[ephemeral-znode|Ephemeral ZNode]]
- [[zookeeper-watch|ZooKeeper Watch]]
- [[failover|Failover]]
- [[split-brain|Split Brain]]
- [[single-writer-pattern|Single-Writer Pattern]]

## Open Questions

- Which future source should compare leader election through ZooKeeper, etcd leases, Kubernetes Lease, database advisory locks, and queue partitions?
