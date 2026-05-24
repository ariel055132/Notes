---
type: concept
aliases: ["vector indexes", "embedding index", "semantic search index", "ANN index"]
tags: [system-design, databases, indexing, search, ai]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Vector Index

## Definition

A vector index is an index family used to search embeddings or high-dimensional vectors for semantic or similarity-based retrieval. [[2026-05-15--database-indexing|Database Indexing]]

## Scope

This concept covers semantic search use cases such as support article retrieval, QA support, and retrieval-augmented systems where lexical term matching is not enough. [[2026-05-15--database-indexing|Database Indexing]] The source mentions vector indexes as a possible search index family alongside inverted indexes, but does not go into approximate-nearest-neighbor algorithms. [[2026-05-15--database-indexing|Database Indexing]]

## Contrasts

- **Inverted Index**: Inverted indexes map terms to documents for lexical search, while vector indexes search embedding similarity. [[2026-05-15--database-indexing|Database Indexing]]
- **B-Tree Index**: B-tree indexes organize scalar keys, while vector indexes organize high-dimensional similarity spaces. [[2026-05-15--database-indexing|Database Indexing]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source lists vector index as a possible fit for support article search alongside inverted index.

## Related

- [[inverted-index|Inverted Index]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[database-indexing|Database Indexing]]
- [[query-shape-optimization|Query Shape Optimization]]

## Open Questions

- Which future source should define ANN structures such as HNSW, IVF, and product quantization?
