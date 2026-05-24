# Wiki Log

> Append-only timeline of all operations. Each entry starts with `## [YYYY-MM-DD] action-type | description`.

---

## [2026-05-15] init | Project scaffold created

- **Action**: Initialized LLM Wiki project structure.
- **Pages touched**: `AGENTS.md`, `README.md`, `raw/README.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Set up directory structure, schema, and initial templates.
- **Open questions**: None.

## [2026-05-24] ingest | Prompting best practices

- **Action**: Ingested `raw/assets/Prompting best practices.md` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-24--prompting-best-practices.md`, `wiki/entities/anthropic.md`, `wiki/entities/claude.md`, `wiki/entities/claude-opus-4-7.md`, `wiki/entities/claude-opus-4-6.md`, `wiki/entities/claude-sonnet-4-6.md`, `wiki/entities/claude-haiku-4-5.md`, `wiki/concepts/prompt-engineering.md`, `wiki/concepts/effort-parameter.md`, `wiki/concepts/adaptive-thinking.md`, `wiki/concepts/tool-use.md`, `wiki/concepts/agentic-systems.md`, `wiki/concepts/subagent-orchestration.md`, `wiki/concepts/few-shot-prompting.md`, `wiki/concepts/xml-prompt-structure.md`, `wiki/concepts/code-review-harnesses.md`, `wiki/concepts/frontend-design-defaults.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Seeded the first wiki source and default entity/concept graph for Claude prompting, model tuning, tool use, thinking, and agentic workflows. The raw asset was intentionally left in place because project schema marks raw sources as immutable.
- **Open questions**: Future sources should verify whether model-specific claims about Claude Opus 4.7, Claude Sonnet 4.6, and effort levels remain current.

## [2026-05-24] ingest | Prompting best practices page materialization

- **Action**: Created the wiki pages referenced by the prior ingest entry and repaired the source index link.
- **Pages touched**: `wiki/sources/2026-05-24--prompting-best-practices.md`, `wiki/entities/anthropic.md`, `wiki/entities/claude.md`, `wiki/entities/claude-opus-4-7.md`, `wiki/entities/claude-opus-4-6.md`, `wiki/entities/claude-sonnet-4-6.md`, `wiki/entities/claude-haiku-4-5.md`, `wiki/concepts/prompt-engineering.md`, `wiki/concepts/effort-parameter.md`, `wiki/concepts/adaptive-thinking.md`, `wiki/concepts/tool-use.md`, `wiki/concepts/parallel-tool-calling.md`, `wiki/concepts/agentic-systems.md`, `wiki/concepts/subagent-orchestration.md`, `wiki/concepts/few-shot-prompting.md`, `wiki/concepts/xml-prompt-structure.md`, `wiki/concepts/long-context-prompting.md`, `wiki/concepts/code-review-harnesses.md`, `wiki/concepts/frontend-design-defaults.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator requested emphasis on general prompt-engineering practices and agentic/tool-use workflows. Model-specific Claude details were retained as supporting entities and configuration context, not the main analytical focus. The raw asset was left untouched under `raw/assets/` per the project immutability rule.
- **Open questions**: Build a local prompt pattern library from these practices, especially for wiki ingest/query/lint workflows.

## [2026-05-24] ingest | Prompt Engineering in 2025

- **Action**: Ingested `raw/assets/Prompt Engineering in 2025 Complete Guide for ChatGPT, Claude, and Gemini.md` into the wiki layer.
- **Pages touched**: `wiki/sources/2025-06-13--prompt-engineering-in-2025-complete-guide.md`, `wiki/entities/prompt-builder.md`, `wiki/entities/chatgpt.md`, `wiki/entities/gemini.md`, `wiki/entities/claude.md`, `wiki/concepts/prompt-engineering.md`, `wiki/concepts/power-prompt-framework.md`, `wiki/concepts/zero-shot-prompting.md`, `wiki/concepts/few-shot-prompting.md`, `wiki/concepts/chain-of-thought-prompting.md`, `wiki/concepts/retrieval-augmented-generation.md`, `wiki/concepts/metacognitive-prompting.md`, `wiki/concepts/iterative-refinement.md`, `wiki/concepts/prompt-chaining.md`, `wiki/concepts/prompt-testing-and-versioning.md`, `wiki/concepts/long-context-prompting.md`, `wiki/concepts/tool-use.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator requested emphasis on the source as a practical prompt-engineering guide, with prompt engineering prioritized. Promotional tool links were treated as context for the Prompt Builder entity rather than the main extract. The raw asset was left untouched under `raw/assets/` per the project immutability rule.
- **Open questions**: Build a reusable local prompt pattern library, especially POWER templates and eval cases for ingest, query, and lint workflows.

## [2026-05-24] ingest | Scaling Reads

- **Action**: Ingested `raw/sources/Scaling Reads.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-14--scaling-reads.md`, `wiki/entities/buildmoat.md`, `wiki/concepts/read-scaling.md`, `wiki/concepts/freshness-budget.md`, `wiki/concepts/database-indexing.md`, `wiki/concepts/query-shape-optimization.md`, `wiki/concepts/denormalization.md`, `wiki/concepts/materialized-view.md`, `wiki/concepts/read-replica.md`, `wiki/concepts/database-sharding.md`, `wiki/concepts/application-level-caching.md`, `wiki/concepts/cache-invalidation.md`, `wiki/concepts/stale-while-revalidate.md`, `wiki/concepts/cdn-and-edge-caching.md`, `wiki/concepts/hot-key.md`, `wiki/concepts/cache-stampede.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator requested a system-design framing. The ingest created the first system-design concept cluster around read-heavy architecture, database read-path optimization, read distribution, caching, CDN/edge caching, freshness, invalidation, hot keys, and cache stampedes.
- **Open questions**: Create a dedicated system-design synthesis or index section once more sources on write scaling, consistency, queues, search, storage, and observability are ingested.

## [2026-05-24] ingest | Scaling Reads entity cleanup

- **Action**: Removed the dedicated `BuildMoat` entity page from the Scaling Reads ingest.
- **Pages touched**: `wiki/sources/2026-05-14--scaling-reads.md`, `wiki/entities/buildmoat.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator clarified that BuildMoat should be treated as the author/organization behind the PDF, not as a standalone entity in the wiki graph. The source keeps `author: "BuildMoat"` in frontmatter.
- **Open questions**: None.

## [2026-05-24] lint | Concept broken-link cleanup

- **Action**: Ran schema lint and a focused strict wikilink pass over `wiki/concepts/*.md`.
- **Pages touched**: All markdown files under `wiki/concepts/`, `verification/lint-schema-report.json`, `wiki/log.md`
- **Notes**: The schema checker reported 0 issues. A strict filename/path resolver found 159 concept-page wikilinks that targeted page titles instead of actual markdown filenames; these were rewritten as `[[slug|Title]]` links. A follow-up strict pass found 0 broken concept links.
- **Open questions**: Consider teaching `scripts/lint_schema.py` to validate all wikilinks with strict filename/path semantics, not just schema and `## Related` structure.

## [2026-05-24] ingest | Replication

- **Action**: Ingested `raw/sources/Replication.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-02--replication.md`, `wiki/concepts/replication.md`, `wiki/concepts/single-leader-replication.md`, `wiki/concepts/synchronous-replication.md`, `wiki/concepts/asynchronous-replication.md`, `wiki/concepts/replication-log.md`, `wiki/concepts/failover.md`, `wiki/concepts/split-brain.md`, `wiki/concepts/replication-lag.md`, `wiki/concepts/read-after-write-consistency.md`, `wiki/concepts/monotonic-reads.md`, `wiki/concepts/consistent-prefix-reads.md`, `wiki/concepts/multi-leader-replication.md`, `wiki/concepts/write-conflict-resolution.md`, `wiki/concepts/last-write-wins.md`, `wiki/concepts/conflict-free-replicated-data-types.md`, `wiki/concepts/operational-transformation.md`, `wiki/concepts/leaderless-replication.md`, `wiki/concepts/read-repair.md`, `wiki/concepts/anti-entropy-process.md`, `wiki/concepts/quorum-reads-and-writes.md`, `wiki/concepts/sloppy-quorum.md`, `wiki/concepts/hinted-handoff.md`, `wiki/concepts/version-vector.md`, `wiki/concepts/read-replica.md`, `wiki/concepts/read-scaling.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing system-design interview framing and connecting the source to the existing read-scaling/read-replica cluster. BuildMoat was kept as source author metadata rather than recreated as an entity page. The ingest created the replication concept cluster around architecture choice, lag, failover, session and causal consistency, multi-leader conflicts, and leaderless quorum behavior.
- **Open questions**: Add a future source on consensus, transactions, and strongly consistent replicated logs to contrast with the eventual-consistency patterns in this source.

## [2026-05-24] ingest | Sharding

- **Action**: Ingested `raw/sources/Sharding.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--sharding.md`, `wiki/concepts/database-sharding.md`, `wiki/concepts/database-partitioning.md`, `wiki/concepts/shard-key.md`, `wiki/concepts/range-based-sharding.md`, `wiki/concepts/hash-based-sharding.md`, `wiki/concepts/virtual-buckets.md`, `wiki/concepts/consistent-hashing.md`, `wiki/concepts/directory-based-sharding.md`, `wiki/concepts/scatter-gather-query.md`, `wiki/concepts/cross-shard-transaction.md`, `wiki/concepts/single-shard-transaction.md`, `wiki/concepts/resharding.md`, `wiki/concepts/replication.md`, `wiki/concepts/hot-key.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved the system-design sharding emphasis and specifically asked to prioritize the difference between sharding and replication. The ingest treats sharding as partitioning one logical dataset across machines and replication as copying the same data across machines, then connects that contrast to shard-key choice, transaction boundaries, hot keys, scatter-gather queries, and resharding.
- **Open questions**: Add a synthesis comparing sharding, replication, partitioning, caching, and read models as distinct but often combined data-distribution patterns.

## [2026-05-24] ingest | Caching

- **Action**: Ingested `raw/sources/Caching.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-24--caching.md`, `wiki/concepts/application-level-caching.md`, `wiki/concepts/cdn-and-edge-caching.md`, `wiki/concepts/client-side-cache.md`, `wiki/concepts/in-process-cache.md`, `wiki/concepts/cache-aside.md`, `wiki/concepts/write-through-cache.md`, `wiki/concepts/write-behind-cache.md`, `wiki/concepts/read-through-cache.md`, `wiki/concepts/freshness-budget.md`, `wiki/concepts/cache-invalidation.md`, `wiki/concepts/ttl-jitter.md`, `wiki/concepts/stale-while-revalidate.md`, `wiki/concepts/request-coalescing.md`, `wiki/concepts/cache-warming.md`, `wiki/concepts/cache-stampede.md`, `wiki/concepts/cache-penetration.md`, `wiki/concepts/negative-caching.md`, `wiki/concepts/cache-avalanche.md`, `wiki/concepts/hot-key.md`, `wiki/concepts/read-scaling.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing caching as a targeted system-design read-path optimization. The ingest expanded the existing caching/read-scaling cluster and added focused pages for cache locations, cache access/write patterns, freshness controls, and cache failure modes.
- **Open questions**: Add future pages for cache observability, circuit breakers, Bloom filters, Redis, and Memcached when dedicated sources cover them.

## [2026-05-24] ingest | Database Indexing

- **Action**: Ingested `raw/sources/Database Indexing.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--database-indexing.md`, `wiki/concepts/database-indexing.md`, `wiki/concepts/full-table-scan.md`, `wiki/concepts/b-tree-index.md`, `wiki/concepts/hash-index.md`, `wiki/concepts/lsm-tree.md`, `wiki/concepts/geospatial-index.md`, `wiki/concepts/inverted-index.md`, `wiki/concepts/vector-index.md`, `wiki/concepts/composite-index.md`, `wiki/concepts/index-selectivity.md`, `wiki/concepts/query-shape-optimization.md`, `wiki/concepts/read-scaling.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing database indexing as a system-design read-scaling and query-shape optimization cluster. The ingest updated the existing indexing hub and added focused pages for index families, full table scans, composite indexes, and selectivity.
- **Open questions**: Add a future source on query planners and `EXPLAIN` plans to connect index selection to actual execution behavior.

## [2026-05-24] ingest | Database Transactions

- **Action**: Ingested `raw/sources/Database Transactions.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-03-31--database-transactions.md`, `wiki/concepts/database-transactions.md`, `wiki/concepts/acid-transactions.md`, `wiki/concepts/write-ahead-log.md`, `wiki/concepts/transaction-isolation.md`, `wiki/concepts/read-uncommitted.md`, `wiki/concepts/read-committed.md`, `wiki/concepts/repeatable-read.md`, `wiki/concepts/serializable-isolation.md`, `wiki/concepts/dirty-read.md`, `wiki/concepts/non-repeatable-read.md`, `wiki/concepts/phantom-read.md`, `wiki/concepts/multi-version-concurrency-control.md`, `wiki/concepts/lost-update.md`, `wiki/concepts/optimistic-locking.md`, `wiki/concepts/pessimistic-locking.md`, `wiki/concepts/deadlock.md`, `wiki/concepts/two-phase-commit.md`, `wiki/concepts/saga-pattern.md`, `wiki/concepts/cross-shard-transaction.md`, `wiki/concepts/single-shard-transaction.md`, `wiki/concepts/replication-log.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator requested emphasis on database-design and system-design concepts. The ingest treats transactions as a correctness-boundary topic and connects local ACID behavior to isolation-level choices, concurrency anomalies, locking strategies, deadlock/retry handling, shard-local invariants, cross-boundary transactions, 2PC, and Saga.
- **Open questions**: Create a synthesis comparing local ACID transactions, single-shard transactions, cross-shard transactions, 2PC, Saga, replication consistency, and cache freshness as distinct consistency tools.

## [2026-05-24] ingest | Consistent Hashing

- **Action**: Ingested `raw/sources/Consistent Hashing.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--consistent-hashing.md`, `wiki/concepts/consistent-hashing.md`, `wiki/concepts/virtual-nodes.md`, `wiki/concepts/fixed-hash-slots.md`, `wiki/concepts/virtual-buckets.md`, `wiki/concepts/hash-based-sharding.md`, `wiki/concepts/resharding.md`, `wiki/concepts/hot-key.md`, `wiki/concepts/application-level-caching.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing consistent hashing as a system-design routing and ownership concept. The ingest connects hash rings, virtual nodes, fixed hash slots, cache-node routing, rate limiter ownership, WebSocket room ownership, asset cache routing, hot-key limits, and resharding or warmup concerns.
- **Open questions**: Create a synthesis comparing consistent hashing, virtual buckets, fixed hash slots, and directory-based sharding as ownership-mapping strategies.

## [2026-05-25] ingest | Distributed Cache

- **Action**: Ingested `raw/sources/Distributed Cache.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--distributed-cache.md`, `wiki/concepts/distributed-cache.md`, `wiki/concepts/cache-routing.md`, `wiki/concepts/cache-fallback-limit.md`, `wiki/concepts/cache-replication.md`, `wiki/concepts/regional-cache.md`, `wiki/concepts/application-level-caching.md`, `wiki/concepts/hot-key.md`, `wiki/concepts/cache-stampede.md`, `wiki/concepts/cache-invalidation.md`, `wiki/concepts/freshness-budget.md`, `wiki/concepts/in-process-cache.md`, `wiki/concepts/request-coalescing.md`, `wiki/concepts/ttl-jitter.md`, `wiki/concepts/cache-warming.md`, `wiki/concepts/replication-lag.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing distributed cache as a system-design read-path protection and failure-containment pattern, and requested a discoverable distributed-queue tag; new distributed-cache pages carry both `distributed-cache` and `distributed-queue` tags. The ingest connects cache routing, hash slots, consistent hashing, hot-key mitigation, replica lag, invalidation, freshness budgets, stampede protection, fallback limits, warmup, regional cache, and source-of-truth boundaries.
- **Open questions**: Create a synthesis comparing distributed cache, application-level cache, CDN/edge cache, local cache, and read replicas as read-path protection layers.
