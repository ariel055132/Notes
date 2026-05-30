---
type: source
source_path: raw/archive/Zookeeper.pdf
title: "Zookeeper"
author: "BuildMoat"
date: 2026-05-15
tags: [system-design, distributed-systems, coordination, control-plane, reliability]
created: 2026-05-26
---

# Zookeeper

## Summary

This source frames ZooKeeper as a distributed coordination service for small, important control-plane metadata such as leader ownership, service membership, dynamic configuration, locks, and partition ownership. [[2026-05-15--zookeeper|Zookeeper]] It repeatedly separates coordination metadata from business data: booking state, payments, trades, messages, task payloads, and high-QPS events belong in databases, logs, queues, or caches, not ZooKeeper. [[2026-05-15--zookeeper|Zookeeper]] The source explains ZooKeeper primitives such as znodes, ephemeral znodes, sequential znodes, watches, sessions, ensembles, quorum writes, and ZAB-style atomic broadcast. [[2026-05-15--zookeeper|Zookeeper]] Its interview framing is to first identify a real coordination problem, then explain why the metadata is small, low-write-frequency, and correctness-critical enough to justify a coordination service instead of a simpler platform primitive. [[2026-05-15--zookeeper|Zookeeper]]

## Key Claims

1. ZooKeeper is a coordination service, not a business database, high-QPS cache, event log, or general data store. [[2026-05-15--zookeeper|Zookeeper]]
2. ZooKeeper fits small, important, low-write-frequency metadata such as leader ownership, membership, runtime config, partition ownership, and locks. [[2026-05-15--zookeeper|Zookeeper]]
3. Designers should distinguish data problems from coordination problems before choosing ZooKeeper; durable business state belongs in databases or logs. [[2026-05-15--zookeeper|Zookeeper]]
4. Ephemeral znodes tied to sessions are central for membership, liveness, and automatic cleanup after client failure. [[2026-05-15--zookeeper|Zookeeper]]
5. Sequential ephemeral znodes support leader election and fair locks; clients should watch their predecessor rather than all watching the leader to avoid herd effects. [[2026-05-15--zookeeper|Zookeeper]]
6. ZooKeeper ensembles use a leader, followers, and quorum; common ensemble sizes are 3, 5, and 7 nodes, with write cost rising as quorum coordination grows. [[2026-05-15--zookeeper|Zookeeper]]
7. ZooKeeper writes become consistent through ZAB-style atomic broadcast: the leader orders writes, followers replicate proposals, and quorum commit makes updates effective. [[2026-05-15--zookeeper|Zookeeper]]
8. Reads may be served by followers and can briefly be stale unless the client synchronizes before reading. [[2026-05-15--zookeeper|Zookeeper]]
9. ZooKeeper should stay off hot paths; high-frequency booking, QR scans, chat messages, trades, and request-level locks should use database constraints, Redis/database leases, queue serialization, or redesigned boundaries. [[2026-05-15--zookeeper|Zookeeper]]
10. Modern systems often use etcd, Consul, Kubernetes API or Lease, cloud service discovery, managed Kafka, or simpler database/Redis leases instead of operating ZooKeeper directly. [[2026-05-15--zookeeper|Zookeeper]]

## Notable Quotes

- "ZooKeeper 是分散式協調服務." [[2026-05-15--zookeeper|Zookeeper]]
- "ZooKeeper 通常不是一般產品系統的第一選擇." [[2026-05-15--zookeeper|Zookeeper]]
- "ZooKeeper 的核心價值是分散式協調." [[2026-05-15--zookeeper|Zookeeper]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter. ZooKeeper, etcd, Consul, Kafka, Kubernetes, HBase, Hadoop, SolrCloud, Pulsar, ClickHouse, and KRaft are treated as system examples rather than dedicated entity pages in this ingest. [[2026-05-15--zookeeper|Zookeeper]]

## Concepts Mentioned

- [[zookeeper|ZooKeeper]] — A distributed coordination service for small, correctness-critical metadata. [[2026-05-15--zookeeper|Zookeeper]]
- [[coordination-metadata|Coordination Metadata]] — Metadata describing ownership, liveness, config version, and membership rather than business records. [[2026-05-15--zookeeper|Zookeeper]]
- [[znode|ZNode]] — A path-addressed ZooKeeper node that stores small coordination data. [[2026-05-15--zookeeper|Zookeeper]]
- [[ephemeral-znode|Ephemeral ZNode]] — A znode that disappears when the owning client session expires. [[2026-05-15--zookeeper|Zookeeper]]
- [[sequential-znode|Sequential ZNode]] — A znode whose name receives a monotonic sequence number for ordering candidates. [[2026-05-15--zookeeper|Zookeeper]]
- [[zookeeper-watch|ZooKeeper Watch]] — A notification mechanism for changes to znode values or child lists. [[2026-05-15--zookeeper|Zookeeper]]
- [[zookeeper-session|ZooKeeper Session]] — The heartbeat-backed client session that drives ephemeral-node cleanup and failure detection. [[2026-05-15--zookeeper|Zookeeper]]
- [[zookeeper-ensemble|ZooKeeper Ensemble]] — A quorum-based set of ZooKeeper servers with one leader and followers. [[2026-05-15--zookeeper|Zookeeper]]
- [[zookeeper-atomic-broadcast|ZooKeeper Atomic Broadcast]] — The ordered broadcast protocol family that makes ZooKeeper writes quorum-committed. [[2026-05-15--zookeeper|Zookeeper]]
- [[leader-election|Leader Election]] — Choosing one active owner among candidates using sequential ephemeral nodes or platform primitives. [[2026-05-15--zookeeper|Zookeeper]]
- [[service-discovery|Service Discovery]] — Registering live service instances and removing them when sessions expire. [[2026-05-15--zookeeper|Zookeeper]]
- [[dynamic-configuration|Dynamic Configuration]] — Runtime configuration whose small, important changes need coordinated updates and notification. [[2026-05-15--zookeeper|Zookeeper]]
- [[distributed-lock|Distributed Lock]] — A low-frequency correctness-critical lock can be implemented with sequential ephemeral znodes. [[2026-05-15--zookeeper|Zookeeper]]
- [[failover|Failover]] — ZooKeeper-style sessions and leader election can coordinate who takes over after a controller or owner fails. [[2026-05-15--zookeeper|Zookeeper]]
- [[split-brain|Split Brain]] — ZooKeeper helps avoid dual active ownership by making leader ownership a coordinated metadata decision. [[2026-05-15--zookeeper|Zookeeper]]

## Follow-ups

- Create a synthesis comparing ZooKeeper, etcd, Consul, Kubernetes Lease, Redis leases, database leases, and queue single-writer ownership as coordination choices.
