---
type: concept
aliases: ["Online Analytical Processing", "analytical workload", "analytics database", "data warehouse workload"]
tags: [system-design, databases, analytics, workload]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# OLAP

## Definition

OLAP, or Online Analytical Processing, is a database workload for analyzing historical data through large scans, aggregations, and reporting queries where seconds-to-minutes latency can be acceptable. [[2026-04-15--database|Database]]

## Scope

This concept covers analytical systems that are separated from product-facing OLTP paths so heavy analysis does not harm online business operations. [[2026-04-15--database|Database]] The source names ClickHouse, BigQuery, Redshift, and Snowflake as OLAP examples, and highlights column-oriented storage as useful when analytical queries read only a subset of columns across many rows. [[2026-04-15--database|Database]]

## Contrasts

- **OLTP**: OLAP scans and aggregates historical data, while OLTP serves live transaction paths with point reads and small writes. [[2026-04-15--database|Database]]
- **Wide-Column Store**: OLAP column-oriented storage for analytical scans is not the same as Cassandra-style wide-column OLTP storage. [[2026-04-15--database|Database]]
- **Read Scaling**: OLAP offloads analytical reads to a separate analytical system, while read scaling can also include indexes, replicas, caches, and CDN for product-facing reads. [[2026-04-15--database|Database]] [[read-scaling|Read Scaling]]

## Evidence

- [[2026-04-15--database|Database]] — The source explains that operational data commonly flows from OLTP into OLAP through ETL or CDC pipelines so analytical queries do not affect online performance.

## Related

- [[database-workload|Database Workload]]
- [[oltp|OLTP]]
- [[read-scaling|Read Scaling]]
- [[database-selection|Database Selection]]

## Open Questions

- Which future source should cover ETL, CDC, star schema, and HTAP in detail?
