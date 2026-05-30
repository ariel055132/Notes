---
type: concept
aliases: ["vector indexes", "embedding index", "semantic search index", "ANN index"]
tags: [system-design, databases, indexing, search, ai]
created: 2026-05-24
updated: 2026-05-26
source_count: 2
---

# Vector Index

## Definition

A vector index is an index family used to search embeddings or high-dimensional vectors for semantic or similarity-based retrieval. [[2026-05-15--database-indexing|Database Indexing]] In vector-database workloads, approximate-nearest-neighbor search uses these vector representations to retrieve semantically similar text, images, audio, products, or documents. [[2026-04-15--database|Database]]

## Scope

This concept covers semantic search use cases such as support article retrieval, QA support, and retrieval-augmented systems where lexical term matching is not enough. [[2026-05-15--database-indexing|Database Indexing]] The indexing source mentions vector indexes as a possible search index family alongside inverted indexes, while the database overview connects embeddings, vector distance, and ANN search to vector databases such as Pinecone, Weaviate, Milvus, pgvector, Redis VSS, and Elasticsearch. [[2026-05-15--database-indexing|Database Indexing]] [[2026-04-15--database|Database]]

## Contrasts

- **Inverted Index**: Inverted indexes map terms to documents for lexical search, while vector indexes search embedding similarity. [[2026-05-15--database-indexing|Database Indexing]]
- **B-Tree Index**: B-tree indexes organize scalar keys, while vector indexes organize high-dimensional similarity spaces. [[2026-05-15--database-indexing|Database Indexing]]
- **Vector Database**: Vector index is the retrieval structure or capability, while vector database is the broader storage and serving system for embedding similarity workloads. [[2026-04-15--database|Database]]

## Evidence

- [[2026-05-15--database-indexing|Database Indexing]] — The source lists vector index as a possible fit for support article search alongside inverted index.
- [[2026-04-15--database|Database]] — The source describes vector databases as systems for embedding-based similarity search and gives semantic search, RAG, image search, and recommendations as examples.

## Related

- [[vector-database|Vector Database]]
- [[inverted-index|Inverted Index]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[database-indexing|Database Indexing]]
- [[query-shape-optimization|Query Shape Optimization]]

## Open Questions

- Which future source should define ANN structures such as HNSW, IVF, and product quantization?
