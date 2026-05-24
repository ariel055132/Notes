---
type: concept
aliases: ["inverted indexes", "full-text index", "full text index", "search index"]
tags: [system-design, databases, indexing, search]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Inverted Index

## Definition

An inverted index is a search index that maps terms to the documents or records that contain those terms. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers full-text search for support articles, help centers, logs, market titles, and other text-heavy data. [[2026-05-15--database-indexing|Database Indexing]] It is appropriate when users search by terms rather than exact IDs or scalar ranges. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **B-Tree Index**: B-tree indexes suit exact, range, sort, and uniqueness patterns, while inverted indexes suit term-to-document lookup. [[2026-05-15--database-indexing|Database Indexing]]
- **Vector Index**: Inverted indexes support lexical search over terms, while vector indexes support embedding or semantic similarity search. [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source says full-text search should usually use an inverted index rather than a B-tree.

## Related

- [[database-indexing|Database Indexing]]
- [[vector-index|Vector Index]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]

## Open Questions

- Which future source should define tokenization, ranking, and hybrid search?
