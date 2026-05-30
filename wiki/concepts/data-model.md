---
type: concept
aliases: ["database data model", "storage model", "data shape"]
tags: [system-design, databases, modeling]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Data Model

## Definition

A data model is the structural shape a database presents for stored information, such as tables, key-value pairs, JSON-like documents, column families, graph nodes and edges, or vectors. [[2026-04-15--database|Database]]

## Scope

This concept covers the first major axis of database selection: whether the data is fixed-schema relational data, simple key-addressed state, flexible nested documents, sparse wide rows, highly connected graph data, or unstructured content represented by embeddings. [[2026-04-15--database|Database]] The source treats data model as independent from workload, meaning a design still needs to ask whether the workload is transactional, analytical, or similarity-search oriented. [[2026-04-15--database|Database]]

## Contrasts

- **Database Workload**: Data model describes the data's shape, while workload describes the query and mutation pattern placed on that data. [[2026-04-15--database|Database]]
- **Schema**: Schema is the formal structure or constraints within some data models, while data model is the broader storage abstraction. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source names data model as one of the two most important independent dimensions for understanding database choices.

## Related

- [[database-selection|Database Selection]]
- [[relational-database|Relational Database]]
- [[key-value-store|Key-Value Store]]
- [[document-store|Document Store]]
- [[wide-column-store|Wide-Column Store]]
- [[graph-database|Graph Database]]
- [[vector-database|Vector Database]]
- [[database-workload|Database Workload]]

## Open Questions

- Which future source should cover schema design and logical data modeling in more depth?
