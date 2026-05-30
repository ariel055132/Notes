---
type: concept
aliases: ["ephemeral znode", "ephemeral node", "ephemeral ZooKeeper node"]
tags: [system-design, distributed-systems, coordination, zookeeper, reliability]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Ephemeral ZNode

## Definition

An ephemeral znode is a ZooKeeper node that is automatically deleted when the client session that created it expires. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers service membership, worker liveness, lock ownership, broker membership, dispatcher membership, and other coordination metadata that should disappear when the owner is no longer considered alive. [[2026-05-15--zookeeper|Zookeeper]] It depends on ZooKeeper session timeout, so choosing the timeout trades false failure detection against slow failover. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Persistent ZNode**: Persistent znodes remain until explicitly deleted, while ephemeral znodes are tied to a session's liveness. [[2026-05-15--zookeeper|Zookeeper]]
- **Lease-Based Locking**: Ephemeral znodes provide session-backed lease-like cleanup, while a generic lease may be implemented through TTL or heartbeat in another system. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]]
- **Health Check Registry**: A health-check registry may poll services, while ephemeral znodes remove membership automatically when the session expires. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source says ephemeral nodes are critical because worker, dispatcher, or broker nodes disappear automatically after session timeout.

## Related

- [[znode|ZNode]]
- [[zookeeper-session|ZooKeeper Session]]
- [[service-discovery|Service Discovery]]
- [[leader-election|Leader Election]]
- [[distributed-lock|Distributed Lock]]

## Open Questions

- Which future source should compare ephemeral-node failure detection with Kubernetes readiness/liveness probes and leases?
