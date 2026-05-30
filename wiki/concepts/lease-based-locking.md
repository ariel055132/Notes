---
type: concept
aliases: ["lease", "lease lock", "lock lease", "TTL lock", "lease timeout"]
tags: [system-design, distributed-systems, locking, reliability, coordination]
created: 2026-05-26
updated: 2026-05-26
source_count: 2
---

# Lease-Based Locking

## Definition

Lease-based locking treats lock ownership as a time-limited lease that expires after a TTL unless renewed, preventing a crashed or unreachable owner from holding a resource forever. [[2026-05-15--distributed-lock|Distributed Lock]] ZooKeeper implements a related session-based model where ephemeral znodes disappear after client session timeout. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers TTL-based distributed locks, heartbeat or renewal behavior, lock-acquisition timeout, short critical sections, session-backed ephemeral ownership, and the failure case where a lease expires while the old owner is paused and later resumes. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--zookeeper|Zookeeper]] A lease alone does not protect downstream state from stale writes; important writes still need fencing tokens, owner tokens, or version checks. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Permanent Lock**: A permanent lock can block recovery after owner failure, while a lease expires so another owner can eventually proceed. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Fencing Token**: A lease limits how long ownership is valid in the lock service, while a fencing token lets the protected resource reject stale owners after lease expiry. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Visibility Timeout**: Visibility timeout is a message-processing lease for queue delivery, while lease-based locking is a general coordination lease for shared-resource ownership. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--distributed-lock|Distributed Lock]]
- **ZooKeeper Session**: A ZooKeeper session is not just a local TTL; it is the coordination relationship that controls ephemeral-node lifetime and watch notifications. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source recommends thinking of distributed lock as a lease with TTL rather than a lock held forever.
- [[2026-05-15--zookeeper|Zookeeper]] — The source describes sessions, heartbeats, session timeout, and ephemeral-node cleanup as the core liveness mechanism.

## Related

- [[distributed-lock|Distributed Lock]]
- [[fencing-token|Fencing Token]]
- [[owner-token|Owner Token]]
- [[failover|Failover]]
- [[visibility-timeout|Visibility Timeout]]
- [[zookeeper-session|ZooKeeper Session]]
- [[ephemeral-znode|Ephemeral ZNode]]

## Open Questions

- Which future source should cover lease renewal, clock drift, and session semantics in ZooKeeper or etcd?
