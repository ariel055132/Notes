---
type: concept
aliases: ["idempotency keys", "idempotent request key", "deduplication key", "stable operation id"]
tags: [system-design, reliability, concurrency, idempotency]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Idempotency Key

## Definition

An idempotency key is a stable identifier for an operation or external side effect that lets a system recognize retries and avoid applying the same effect multiple times. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers retries around external APIs, payment flows, task execution, and compensating workflows where a distributed lock cannot make the external side effect rollback-safe. [[2026-05-15--distributed-lock|Distributed Lock]] It complements leases and locks because a worker can crash, retry, or lose ownership after partially performing work. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Distributed Lock**: A distributed lock reduces simultaneous execution, while an idempotency key makes repeated execution safe when retries still happen. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Owner Token**: Owner tokens identify who owns a lock, while idempotency keys identify the operation being attempted. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Idempotent Consumer**: Idempotent consumer is the queue-processing behavior; idempotency key is one mechanism used to recognize repeated work. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source warns not to use lock as a substitute for idempotency because retries can still create side effects.

## Related

- [[distributed-lock|Distributed Lock]]
- [[owner-token|Owner Token]]
- [[idempotent-consumer|Idempotent Consumer]]
- [[unique-constraint|Unique Constraint]]
- [[saga-pattern|Saga Pattern]]

## Open Questions

- Which future source should compare idempotency-key storage, deduplication windows, and external payment-provider idempotency semantics?
