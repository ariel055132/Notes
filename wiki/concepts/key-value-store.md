---
type: concept
aliases: ["key-value database", "KV store", "key value store"]
tags: [system-design, databases, nosql, caching]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Key-Value Store

## Definition

A key-value store is a database model where each key maps directly to a value and the primary operations are get, set, and delete rather than relational querying. [[2026-04-15--database|Database]]

## Scope

This concept covers low-latency and high-throughput access patterns such as cache entries, sessions, counters, leaderboards, and simple object lookups. [[2026-04-15--database|Database]] The source uses Redis as a low-latency key-value example with richer structures such as lists, sets, sorted sets, and hashes, and DynamoDB as a managed key-value and document-style example for large-scale low-latency OLTP. [[2026-04-15--database|Database]]

## Contrasts

- **Relational Database**: Key-value stores optimize key-addressed access, while relational databases support joins, constraints, and expressive SQL across tables. [[2026-04-15--database|Database]]
- **Application-Level Caching**: A key-value store can be used as a cache technology, but the caching pattern still needs freshness, invalidation, and source-of-truth boundaries. [[2026-04-15--database|Database]] [[application-level-caching|Application-Level Caching]]
- **Document Store**: Key-value stores are centered on direct key lookup, while document stores expose a structured document as the stored unit and may support document-field queries. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source describes key-value stores as the simplest model and gives Redis and DynamoDB as examples for low-latency, high-throughput access.

## Related

- [[nosql-database|NoSQL Database]]
- [[application-level-caching|Application-Level Caching]]
- [[distributed-cache|Distributed Cache]]
- [[hot-key|Hot Key]]
- [[database-selection|Database Selection]]
- [[oltp|OLTP]]

## Open Questions

- Which future source should distinguish cache-oriented Redis usage from durable key-value database usage?
