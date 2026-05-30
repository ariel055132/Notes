---
type: concept
aliases: ["lock owner token", "owner id", "lock value", "compare-and-delete lock"]
tags: [system-design, distributed-systems, locking, reliability]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Owner Token

## Definition

An owner token is a unique owner value stored with a distributed lock so a client can verify it still owns the lock before releasing it. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers safe release for short leases such as Redis `SET lock_key owner_id NX PX ttl`, where release must check that the stored value still equals the releasing owner before deleting the lock key. [[2026-05-15--distributed-lock|Distributed Lock]] Without an owner token, a paused worker can resume after its lease expires and accidentally delete a lock that a new owner acquired. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Fencing Token**: Owner tokens protect lock release, while fencing tokens protect writes to the downstream resource. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Lease TTL**: TTL limits how long a lock can be held, while owner tokens make release conditional on current ownership. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Idempotency Key**: Owner tokens identify lock ownership, while idempotency keys identify an operation so retries do not repeat side effects. [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source warns not to directly delete a Redis lock key; release should first confirm the value is still the releasing owner ID.

## Related

- [[distributed-lock|Distributed Lock]]
- [[lease-based-locking|Lease-Based Locking]]
- [[fencing-token|Fencing Token]]
- [[idempotency-key|Idempotency Key]]

## Open Questions

- Which future source should document safe compare-and-delete scripts for Redis lock release?
