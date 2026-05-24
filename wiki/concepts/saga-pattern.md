---
type: concept
aliases: ["Saga", "sagas", "distributed saga", "compensating transaction"]
tags: [system-design, databases, transactions, distributed-systems]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Saga Pattern

## Definition

The Saga pattern breaks a distributed transaction into a sequence of local transactions with compensating actions for failure cases. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers microservice workflows where one global ACID transaction is impractical because order, inventory, payment, or other steps live in separate services and databases. [[2026-03-31--database-transactions|Database Transactions]] The source frames Saga as giving up strong global consistency in exchange for better availability and fault tolerance, using compensation such as restoring inventory and canceling an order if a later payment step fails. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Two-Phase Commit**: Saga uses local commits and compensation, while 2PC coordinates participants before one distributed commit decision. [[2026-03-31--database-transactions|Database Transactions]]
- **ACID Transactions**: A local ACID transaction gives all-or-nothing behavior inside one database boundary, while Saga composes multiple local transactions and accepts temporary inconsistency. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source uses order creation, inventory deduction, and payment as a Saga example with compensation after payment failure.

## Related

- [[two-phase-commit|Two-Phase Commit]]
- [[cross-shard-transaction|Cross-Shard Transaction]]
- [[database-transactions|Database Transactions]]
- [[acid-transactions|ACID Transactions]]
- [[failover|Failover]]

## Open Questions

- Which future source should cover choreography versus orchestration, outbox messaging, and idempotent compensation?
