---
type: concept
aliases: ["Vector DB", "embedding database", "vector store"]
tags: [system-design, databases, search, ai, vectors]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Vector Database

## Definition

A vector database stores or indexes embeddings so systems can retrieve items by semantic or similarity distance rather than exact key, term, or relational predicates. [[2026-04-15--database|Database]]

## Scope

This concept covers semantic search, retrieval-augmented generation, image search, recommendation, and other similarity-search workloads over text, image, audio, or product embeddings. [[2026-04-15--database|Database]] The source names Pinecone, Weaviate, and Milvus as dedicated vector database examples, and pgvector, Redis VSS, and Elasticsearch as examples of adding vector search to existing database or search systems. [[2026-04-15--database|Database]]

## Contrasts

- **Relational Database**: Relational databases answer structured predicates and joins, while vector databases answer nearest-neighbor similarity queries over embeddings. [[2026-04-15--database|Database]]
- **Vector Index**: Vector database is the storage and serving system category, while vector index is the indexing structure or capability that makes vector similarity search practical. [[2026-04-15--database|Database]] [[vector-index|Vector Index]]
- **Inverted Index**: Inverted indexes support lexical term search, while vector databases retrieve by embedding distance. [[2026-04-15--database|Database]] [[inverted-index|Inverted Index]]

## Evidence

- [[2026-04-15--database|Database]] — The source contrasts exact database lookup with semantic similarity search and describes embeddings plus approximate nearest-neighbor search as the core vector database pattern.

## Related

- [[database-selection|Database Selection]]
- [[vector-index|Vector Index]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[inverted-index|Inverted Index]]
- [[database-indexing|Database Indexing]]
- [[query-shape-optimization|Query Shape Optimization]]

## Open Questions

- Which future source should cover ANN algorithms such as HNSW, IVF, and product quantization?
