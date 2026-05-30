---
type: concept
aliases: ["RDBMS", "relational database management system", "SQL database"]
tags: [system-design, databases, relational, sql]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Relational Database

## Definition

A relational database stores data in tables with rows, columns, relationships, constraints, and SQL queries, making it a strong fit for structured data with transaction and query-expression requirements. [[2026-04-15--database|Database]]

## Scope

This concept covers fixed-schema business data, SQL joins, aggregation, subqueries, window functions, foreign keys, uniqueness constraints, and ACID transaction boundaries for money, inventory, orders, and state transitions. [[2026-04-15--database|Database]] PostgreSQL is the source's main example of a relational choice when ACID guarantees, complex joins, and a mature ecosystem matter. [[2026-04-15--database|Database]]

## Contrasts

- **NoSQL Database**: Relational databases prioritize structured schema, SQL expressiveness, constraints, and ACID, while NoSQL families often trade some of those properties for scale, flexibility, or specialized access patterns. [[2026-04-15--database|Database]]
- **Database Sharding**: Relational databases can scale vertically well, but horizontal scaling introduces sharding, cross-node transaction, and cross-node join complexity. [[2026-04-15--database|Database]] [[database-sharding|Database Sharding]]
- **Document Store**: Relational databases model shared structure across tables, while document stores keep nested records with more flexible per-document fields. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source presents relational databases as mature and widely used, with ACID and SQL as central strengths and schema changes or horizontal scaling as common costs.

## Related

- [[database|Database]]
- [[database-selection|Database Selection]]
- [[data-model|Data Model]]
- [[database-transactions|Database Transactions]]
- [[acid-transactions|ACID Transactions]]
- [[database-indexing|Database Indexing]]
- [[database-sharding|Database Sharding]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[oltp|OLTP]]

## Open Questions

- Which future source should cover PostgreSQL-specific architecture, indexing, replication, and high availability?
