---
type: concept
aliases: ["serializable", "serializable isolation level", "serializability"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Serializable Isolation

## Definition

Serializable isolation is the strongest common isolation level, guaranteeing that the outcome of concurrent transactions is equivalent to some serial order. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers the safest but often most expensive isolation choice because it prevents dirty reads, non-repeatable reads, and phantom reads by constraining concurrency more aggressively. [[2026-03-31--database-transactions|Database Transactions]] The source recommends reserving Serializable for cases that genuinely cannot tolerate concurrency anomalies, such as some financial workflows, rather than using it as a default for every operation. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Repeatable Read**: Repeatable Read stabilizes repeated row reads, while Serializable protects the transaction result as if transactions ran one after another. [[2026-03-31--database-transactions|Database Transactions]]
- **Atomic Update**: Some inventory lost-update problems can be solved with a conditional atomic update or row lock without raising the entire workflow to Serializable. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source describes Serializable as the highest isolation level and warns about its performance cost.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[phantom-read|Phantom Read]]
- [[lost-update|Lost Update]]
- [[pessimistic-locking|Pessimistic Locking]]
- [[acid-transactions|ACID Transactions]]

## Open Questions

- Which future source should add examples of serializable transaction retries and serialization failures?
