---
type: concept
aliases: ["sequential znode", "sequential node", "ZooKeeper sequential node"]
tags: [system-design, distributed-systems, coordination, zookeeper, ordering]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Sequential ZNode

## Definition

A sequential znode is a ZooKeeper node whose name receives a monotonically increasing sequence number, giving contenders an ordered position for leader election or fair locking. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers candidate ordering for leader election, fair distributed locks, predecessor watches, and queue-like coordination metadata. [[2026-05-15--zookeeper|Zookeeper]] It is often combined with ephemeral behavior so a candidate disappears automatically when its session expires. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Ephemeral ZNode**: Ephemeral znodes tie existence to session liveness, while sequential znodes add ordering; leader election often uses both. [[2026-05-15--zookeeper|Zookeeper]]
- **Fencing Token**: Sequential znode numbers order candidates inside ZooKeeper, while fencing tokens must be checked by downstream resources to reject stale writes. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]]
- **Single-Writer Pattern**: Sequential znodes help select a writer, while single-writer pattern is the architectural rule that all writes for a resource flow through one owner. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source uses sequential ephemeral nodes for leader election and fair locks, where the smallest sequence owns leadership or the lock.

## Related

- [[znode|ZNode]]
- [[ephemeral-znode|Ephemeral ZNode]]
- [[leader-election|Leader Election]]
- [[distributed-lock|Distributed Lock]]
- [[zookeeper-watch|ZooKeeper Watch]]

## Open Questions

- Which future source should compare ZooKeeper sequential znodes with Raft log indexes, epochs, and broker partition epochs?
