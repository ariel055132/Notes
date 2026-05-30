---
type: concept
aliases: ["ZooKeeper", "Apache ZooKeeper", "Zookeeper"]
tags: [system-design, distributed-systems, coordination, control-plane]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# ZooKeeper

## Definition

ZooKeeper is a distributed coordination service for storing small, correctness-critical control-plane metadata such as leader ownership, service membership, runtime configuration, locks, and partition ownership. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers ZooKeeper as a coordination plane for infrastructure or platform systems where multiple machines need a consistent view of who is alive, who owns a resource, which version of config is active, or which node is leader. [[2026-05-15--zookeeper|Zookeeper]] It does not cover business data storage, high-QPS request storage, chat messages, trades, booking records, QR scans, task payloads, or large blobs, because those belong in databases, logs, queues, caches, or object storage. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Database**: A database stores durable business state and queryable records, while ZooKeeper stores small coordination metadata. [[2026-05-15--zookeeper|Zookeeper]]
- **Distributed Cache**: Distributed cache accelerates repeated reads, while ZooKeeper coordinates ownership, membership, and config. [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--zookeeper|Zookeeper]]
- **Event Log**: An event log carries high-volume ordered events, while ZooKeeper should not carry chat messages, trades, queue events, or task payloads. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source frames ZooKeeper as a strong coordination metadata service and warns not to put product data or hot-path events in it.

## Related

- [[coordination-metadata|Coordination Metadata]]
- [[znode|ZNode]]
- [[ephemeral-znode|Ephemeral ZNode]]
- [[sequential-znode|Sequential ZNode]]
- [[zookeeper-watch|ZooKeeper Watch]]
- [[zookeeper-session|ZooKeeper Session]]
- [[zookeeper-ensemble|ZooKeeper Ensemble]]
- [[leader-election|Leader Election]]
- [[distributed-lock|Distributed Lock]]

## Open Questions

- Which future source should compare ZooKeeper, etcd, Consul, Kubernetes Lease, and managed service-discovery systems in detail?
