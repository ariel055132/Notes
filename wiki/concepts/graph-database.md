---
type: concept
aliases: ["graph DB", "graph database model", "property graph database"]
tags: [system-design, databases, graph]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Graph Database

## Definition

A graph database represents data as nodes and edges so relationships are first-class data and multi-hop relationship queries can be expressed directly. [[2026-04-15--database|Database]]

## Scope

This concept covers highly connected data such as social networks, recommendation graphs, and knowledge graphs where the relationship structure is central to the query. [[2026-04-15--database|Database]] The source uses Neo4j and Cypher as the main product and query-language examples, and contrasts graph traversal with deeply nested joins over highly connected relational data. [[2026-04-15--database|Database]]

## Contrasts

- **Relational Database**: Relational databases can model relationships through foreign keys and joins, while graph databases make nodes, edges, and traversal the primary abstraction. [[2026-04-15--database|Database]]
- **Document Store**: Document stores center on nested documents, while graph databases center on relationships across entities. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source positions graph databases for multi-hop relationship queries in highly connected data.

## Related

- [[nosql-database|NoSQL Database]]
- [[data-model|Data Model]]
- [[database-selection|Database Selection]]
- [[relational-database|Relational Database]]

## Open Questions

- Which future source should compare graph database traversal with relational recursive queries and search indexes?
