---
type: concept
aliases: ["ZooKeeper watch", "watch", "watch notification", "predecessor watch"]
tags: [system-design, distributed-systems, coordination, zookeeper, notifications]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# ZooKeeper Watch

## Definition

A ZooKeeper watch is a notification mechanism where a client asks to be notified when a znode value or child list changes. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers watches for dynamic config changes, worker membership changes, room ownership changes, leader candidate predecessor disappearance, and lock handoff. [[2026-05-15--zookeeper|Zookeeper]] It is for coordination metadata changes, not a high-throughput message bus for chat messages, market trades, QR scans, or events. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Message Queue**: A message queue transports high-volume work or events, while ZooKeeper watches notify clients about coordination metadata changes. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--zookeeper|Zookeeper]]
- **Polling**: Polling repeatedly asks for state, while a watch lets clients maintain a local cache and update it after notifications. [[2026-05-15--zookeeper|Zookeeper]]
- **Herd Effect**: Watching a single leader node can wake many candidates at once, while watching each predecessor limits notification fanout. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source says watches are powerful but should not be treated as a high-throughput message bus.

## Related

- [[zookeeper|ZooKeeper]]
- [[znode|ZNode]]
- [[leader-election|Leader Election]]
- [[service-discovery|Service Discovery]]
- [[dynamic-configuration|Dynamic Configuration]]

## Open Questions

- Which future source should cover one-shot watch semantics, watch re-registration, and missed update handling?
