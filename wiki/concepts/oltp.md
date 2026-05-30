---
type: concept
aliases: ["Online Transactional Processing", "transactional workload", "transaction processing"]
tags: [system-design, databases, workload, transactions]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# OLTP

## Definition

OLTP, or Online Transactional Processing, is a database workload for business transactions, high-concurrency point reads, and small writes with low-latency expectations. [[2026-04-15--database|Database]]

## Scope

This concept covers product-facing systems such as orders, payments, inventory, user profiles, sessions, counters, and operational records where requests are frequent and user-visible. [[2026-04-15--database|Database]] PostgreSQL, DynamoDB, and Cassandra are all presented as OLTP-capable examples with different consistency, data-model, and scaling tradeoffs. [[2026-04-15--database|Database]]

## Contrasts

- **OLAP**: OLTP handles live business transactions and point access, while OLAP handles historical analysis, scans, and aggregations over large datasets. [[2026-04-15--database|Database]]
- **Relational Database**: OLTP is a workload category, while relational database is a data model and database family; a relational database can serve OLTP, but so can some NoSQL systems. [[2026-04-15--database|Database]]
- **Database Transactions**: OLTP often needs transaction semantics, while database transactions are the specific correctness boundary inside a database operation. [[2026-04-15--database|Database]] [[database-transactions|Database Transactions]]

## Evidence

- [[2026-04-15--database|Database]] — The source defines OLTP as high-concurrency point queries and small writes with millisecond-level latency.

## Related

- [[database-workload|Database Workload]]
- [[olap|OLAP]]
- [[database-transactions|Database Transactions]]
- [[relational-database|Relational Database]]
- [[nosql-database|NoSQL Database]]
- [[key-value-store|Key-Value Store]]
- [[wide-column-store|Wide-Column Store]]
- [[read-scaling|Read Scaling]]

## Open Questions

- Which future source should define write-heavy OLTP scaling patterns?
