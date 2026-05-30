---
type: concept
aliases: ["document database", "JSON document store", "document-oriented database"]
tags: [system-design, databases, nosql, documents]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Document Store

## Definition

A document store is a database model that stores records as JSON-like documents, allowing nested structure and flexible fields across records in a collection. [[2026-04-15--database|Database]]

## Scope

This concept covers data that changes shape over time or benefits from storing a whole nested object together, such as user profiles, content management records, and product catalogs. [[2026-04-15--database|Database]] The source uses MongoDB as the main document-store example and notes that DynamoDB can also be considered key-value plus document-style in managed high-scale OLTP contexts. [[2026-04-15--database|Database]]

## Contrasts

- **Relational Database**: Document stores favor flexible nested records, while relational databases favor normalized tables, shared schema, foreign keys, and joins. [[2026-04-15--database|Database]]
- **Key-Value Store**: A document store can retrieve by key, but the document model also treats the nested record as the primary unit of structure. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source describes document stores as JSON-like storage for flexible, fast-changing data structures.

## Related

- [[nosql-database|NoSQL Database]]
- [[data-model|Data Model]]
- [[database-selection|Database Selection]]
- [[oltp|OLTP]]
- [[key-value-store|Key-Value Store]]

## Open Questions

- Which future source should cover document modeling tradeoffs such as embedding versus referencing and secondary-index limits?
