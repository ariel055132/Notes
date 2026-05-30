---
type: concept
aliases: ["ZooKeeper session", "session timeout", "client session"]
tags: [system-design, distributed-systems, coordination, zookeeper, reliability]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# ZooKeeper Session

## Definition

A ZooKeeper session is the heartbeat-backed client relationship that ZooKeeper uses to decide whether a client is alive and whether its ephemeral znodes should remain. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers client heartbeat, session timeout, ephemeral-node cleanup, membership removal, lock release by session expiry, and failover timing. [[2026-05-15--zookeeper|Zookeeper]] Short timeouts detect failures quickly but risk false failover during network jitter; long timeouts reduce false positives but delay recovery from real failure. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Lease-Based Locking**: ZooKeeper sessions provide session-backed liveness for ephemeral nodes, while generic lease-based locking may use TTL and explicit renewal. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]]
- **Application Heartbeat**: Application heartbeat can be ad hoc and inconsistent, while ZooKeeper session expiry is tied to coordination metadata cleanup. [[2026-05-15--zookeeper|Zookeeper]]
- **Visibility Timeout**: Visibility timeout leases message processing, while a ZooKeeper session controls client liveness and ephemeral coordination state. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source describes session heartbeat, session timeout, ephemeral-node deletion, and watch notification as the core failure-detection path.

## Related

- [[zookeeper|ZooKeeper]]
- [[ephemeral-znode|Ephemeral ZNode]]
- [[lease-based-locking|Lease-Based Locking]]
- [[failover|Failover]]
- [[split-brain|Split Brain]]

## Open Questions

- Which future source should compare session timeout tuning with failure detectors and phi-accrual heartbeat systems?
