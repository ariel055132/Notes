---
type: concept
aliases: ["coordination metadata", "control-plane metadata", "ownership metadata", "membership metadata"]
tags: [system-design, distributed-systems, coordination, control-plane]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Coordination Metadata

## Definition

Coordination metadata is small but correctness-critical metadata that lets distributed components agree on liveness, ownership, leadership, configuration version, or partition assignment. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers metadata such as which scheduler is leader, which broker owns a partition, which dispatcher is alive, which room owner handles connections, which config version is active, or which worker holds a low-frequency lock. [[2026-05-15--zookeeper|Zookeeper]] It excludes business records, payloads, high-frequency events, and arbitrary query data. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Business Data**: Business data records product facts such as bookings, payments, trades, and messages, while coordination metadata records who coordinates or owns operational work. [[2026-05-15--zookeeper|Zookeeper]]
- **Data Plane**: Data-plane state carries user-facing workload traffic, while coordination metadata belongs to a control plane that changes less often but must be correct. [[2026-05-15--zookeeper|Zookeeper]]
- **Cache Key**: A cache key identifies a cached response or object, while coordination metadata identifies operational ownership or membership. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source repeatedly says ZooKeeper should store small coordination metadata, not general product data.

## Related

- [[zookeeper|ZooKeeper]]
- [[leader-election|Leader Election]]
- [[service-discovery|Service Discovery]]
- [[dynamic-configuration|Dynamic Configuration]]
- [[znode|ZNode]]
- [[single-writer-pattern|Single-Writer Pattern]]

## Open Questions

- Which future source should define control plane versus data plane across queues, schedulers, gateways, and storage clusters?
