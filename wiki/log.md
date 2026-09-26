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

## [2026-05-26] ingest | CDN (Content Delivery Network)

- **Action**: Ingested `raw/sources/CDN (Content Delivery Network).pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--cdn-content-delivery-network.md`, `wiki/concepts/cdn-cache-key-design.md`, `wiki/concepts/signed-cdn-access.md`, `wiki/concepts/object-storage.md`, `wiki/concepts/cdn-and-edge-caching.md`, `wiki/concepts/cache-invalidation.md`, `wiki/concepts/freshness-budget.md`, `wiki/concepts/stale-while-revalidate.md`, `wiki/concepts/read-through-cache.md`, `wiki/concepts/cache-stampede.md`, `wiki/concepts/cache-warming.md`, `wiki/concepts/cache-fallback-limit.md`, `wiki/concepts/hot-key.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing CDN as a system-design read-path and edge-cache layer. The ingest focuses on what belongs at the edge, CDN cache-key design, versioned URLs versus purge, signed URL and signed cookie access for private downloads, object storage as durable origin, cache-miss storm protection, origin shielding, request coalescing, warmup, and CDN observability.
- **Open questions**: Create a synthesis comparing CDN, distributed cache, object storage, application cache, and read replicas as read-path layers with different ownership, freshness, privacy, and failure boundaries.

## [2026-05-26] ingest | Distributed Lock

- **Action**: Ingested `raw/sources/Distributed Lock.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--distributed-lock.md`, `wiki/concepts/distributed-lock.md`, `wiki/concepts/lease-based-locking.md`, `wiki/concepts/fencing-token.md`, `wiki/concepts/owner-token.md`, `wiki/concepts/conditional-update.md`, `wiki/concepts/unique-constraint.md`, `wiki/concepts/single-writer-pattern.md`, `wiki/concepts/idempotency-key.md`, `wiki/concepts/optimistic-locking.md`, `wiki/concepts/pessimistic-locking.md`, `wiki/concepts/deadlock.md`, `wiki/concepts/request-coalescing.md`, `wiki/concepts/failover.md`, `wiki/concepts/split-brain.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing distributed lock as a system-design correctness boundary. The ingest prioritizes deciding when not to use a lock, preferring database transactions, unique constraints, conditional updates, queues, or single writers when they fit, and using distributed locks only as short leases with owner tokens, fencing tokens or version checks, idempotency, small critical sections, and lock observability.
- **Open questions**: Create a synthesis comparing database transactions, row locks, conditional updates, unique constraints, distributed locks, fencing tokens, queues, and single writers as competing concurrency-control tools.

## [2026-05-26] ingest | Zookeeper

- **Action**: Ingested `raw/sources/Zookeeper.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--zookeeper.md`, `wiki/concepts/zookeeper.md`, `wiki/concepts/coordination-metadata.md`, `wiki/concepts/znode.md`, `wiki/concepts/ephemeral-znode.md`, `wiki/concepts/sequential-znode.md`, `wiki/concepts/zookeeper-watch.md`, `wiki/concepts/zookeeper-session.md`, `wiki/concepts/zookeeper-ensemble.md`, `wiki/concepts/zookeeper-atomic-broadcast.md`, `wiki/concepts/leader-election.md`, `wiki/concepts/service-discovery.md`, `wiki/concepts/dynamic-configuration.md`, `wiki/concepts/distributed-lock.md`, `wiki/concepts/lease-based-locking.md`, `wiki/concepts/failover.md`, `wiki/concepts/split-brain.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing ZooKeeper as a system-design control-plane and coordination-metadata topic. The ingest distinguishes coordination metadata from business and data-plane state, connects ZooKeeper primitives to distributed locks, leader election, service discovery, failover, split-brain prevention, watches, sessions, ephemeral and sequential znodes, quorum ensembles, ZAB, modern alternatives, and operational metrics.
- **Open questions**: Create a synthesis comparing ZooKeeper, etcd, Consul, Kubernetes Lease, Redis leases, database leases, and queue single-writer ownership as coordination choices.

## [2026-05-26] ingest | Database

- **Action**: Ingested `raw/sources/Database.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-04-15--database.md`, `wiki/concepts/database.md`, `wiki/concepts/database-selection.md`, `wiki/concepts/data-model.md`, `wiki/concepts/database-workload.md`, `wiki/concepts/relational-database.md`, `wiki/concepts/nosql-database.md`, `wiki/concepts/key-value-store.md`, `wiki/concepts/document-store.md`, `wiki/concepts/wide-column-store.md`, `wiki/concepts/graph-database.md`, `wiki/concepts/oltp.md`, `wiki/concepts/olap.md`, `wiki/concepts/vector-database.md`, `wiki/concepts/base-consistency-model.md`, `wiki/concepts/database-indexing.md`, `wiki/concepts/database-sharding.md`, `wiki/concepts/read-scaling.md`, `wiki/concepts/vector-index.md`, `wiki/concepts/database-transactions.md`, `wiki/concepts/acid-transactions.md`, `wiki/concepts/application-level-caching.md`, `wiki/concepts/object-storage.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator approved emphasizing Database as a system-design database-selection framework and requested links to existing database-related concepts plus a brief introduction of database products. The ingest creates a Database hub and concept taxonomy around data model, workload, relational databases, NoSQL families, key-value stores, document stores, wide-column stores, graph databases, OLTP, OLAP, vector databases, and BASE tradeoffs. Product names are introduced as examples inside concept/source pages rather than standalone entity pages.
- **Open questions**: Create a system-design map synthesis that divides the Obsidian graph into sections such as storage model, workload, consistency, scaling, caching, messaging, coordination, CDN, analytics, and search.

## [2026-05-30] query | Concepts of Caching

- **Action**: Filed the operator-requested caching explanation as a reusable synthesis page.
- **Pages touched**: `wiki/syntheses/2026-05-30--concepts-of-caching.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: The synthesis answers "Please explain the concepts of caching" using the existing caching source and concept cluster, including application-level caching, cache-aside, read-through, write-through, write-behind, freshness budgets, invalidation, stampede protection, and CDN/edge caching.
- **Open questions**: Consider filing a separate comparison synthesis for application cache, CDN, read replicas, materialized views, and database indexing as read-scaling tools.

## [2026-06-13] ingest | API Gateway

- **Action**: Ingested `raw/sources/API Gateway.pdf` into the wiki layer.
- **Pages touched**: `wiki/sources/2026-05-15--api-gateway.md`, `wiki/concepts/api-gateway.md`, `wiki/concepts/public-api-contract.md`, `wiki/concepts/api-routing.md`, `wiki/concepts/api-versioning.md`, `wiki/concepts/gateway-authentication.md`, `wiki/concepts/gateway-authorization.md`, `wiki/concepts/rate-limiting.md`, `wiki/concepts/tls-termination.md`, `wiki/concepts/cross-origin-resource-sharing.md`, `wiki/concepts/request-size-limit.md`, `wiki/concepts/api-timeout.md`, `wiki/concepts/request-id.md`, `wiki/concepts/request-response-transformation.md`, `wiki/concepts/request-aggregation.md`, `wiki/concepts/backend-for-frontend.md`, `wiki/concepts/load-balancer.md`, `wiki/concepts/api-gateway-observability.md`, `wiki/concepts/api-gateway-boundary.md`, `wiki/concepts/edge-gateway.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: Operator requested spelling out BFF as `Backend For Frontend`. The ingest emphasizes API Gateway as the external API contract and policy layer for routing, authentication, coarse authorization, rate limiting, TLS, CORS, request ID propagation, versioning, light transformation, observability, and load-balancer contrast. It also preserves the source's boundary warning: the gateway should not absorb core domain decisions, data-level authorization, transaction outcomes, idempotency decisions, or long-running work that belongs in backend services, queues, workers, object storage, and data stores. Product names are treated as examples rather than dedicated entity pages.
- **Open questions**: Create a synthesis comparing API Gateway, load balancer, reverse proxy, service mesh ingress, CDN edge worker, and Backend For Frontend as adjacent traffic-entry patterns.

## [2026-06-13] lint | Wiki health check

- **Action**: Ran a full wiki health check covering schema, log contract, index freshness, wikilink resolution, source-path resolution, orphan pages, source-count consistency, missing pages, stale claims, contradictions, and data gaps.
- **Pages touched**: `verification/lint-schema-report.json`, `wiki/log.md`
- **Notes**: Schema checker reported 0 issues across 209 scanned files; strict wikilink and source-path checks found 0 broken links and 0 missing source paths. Findings requiring operator approval before fixes: `wiki/index.md` is out of date, `wiki/syntheses/2026-05-30--concepts-of-caching.md` has no inbound wiki links, 59 entity/concept pages have frontmatter `source_count` lower than their cited source-page count, and several recurring terms lack dedicated pages.
- **Open questions**: Approve whether to rebuild `wiki/index.md`, link the caching synthesis from related caching pages, normalize `source_count` fields, and create missing concept pages for topics such as Bloom Filter, Circuit Breaker, Service Mesh, mTLS, Reverse Proxy, GraphQL, Redis, and Memcached.

## [2026-09-24] ingest | EP286 | 讓 AI 成為第二大腦

- **Action**: Imported video-report; status=draft; SHA-256=efb6cb0dd29883d39013193ba8dd79573f38b80189949b3210bea12a3578c77e.
- **Pages touched**: `wiki/sources/2026-09-24--techporn-ep286.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] ingest | EP292 | AI 能自己寫一整晚，工程師還剩什麼？Fabal 5、GPT 5.6 實測與下一代開發！

- **Action**: Imported video-report; status=draft; SHA-256=2ff6fe7b05268c8f1a0a381ef7d4627d3fb23e2c6a67050182a151e7ca89c7a9.
- **Pages touched**: `wiki/sources/2026-09-24--techporn-ep292.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] ingest | Prompt Engineering in 2025: Complete Guide for ChatGPT, Claude, and Gemini

- **Action**: Imported article; status=needs-review; SHA-256=64c289db7934357690429d1d462fe8f52b169b99c4ffc0ab75030630542e4f5b.
- **Pages touched**: `wiki/sources/2025-06-13--prompt-engineering-in-2025-complete-guide.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] ingest | Prompting best practices

- **Action**: Imported article; status=needs-review; SHA-256=ff14a34585f6ac5eff1fd20fd41bdc7798b30b0f4cb76869170d51648b357f3a.
- **Pages touched**: `wiki/sources/2026-05-24--prompting-best-practices.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] ingest | LLM Wiki — 原文閱讀筆記

- **Action**: Imported article; status=draft; SHA-256=151bafc20e884ba51881a028dda32c8cce20863637eaee91747119c1cb5429ea.
- **Pages touched**: `wiki/sources/2026-09-24--karpathy-llm-wiki.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] ingest | Effective context engineering for AI agents — 閱讀筆記

- **Action**: Imported article; status=draft; SHA-256=d20a7f5570e54883aa86fabd1ecff57d028b94b10c38c77d067ab3d21f0b395a.
- **Pages touched**: `wiki/sources/2026-09-24--anthropic-context-engineering.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] ingest | Caching

- **Action**: Imported pdf; status=needs-review; SHA-256=1327a78d257db55e4ec37f89fe729e02988be48b7fe983624958edfe0cbf302a.
- **Pages touched**: `wiki/sources/2026-05-24--caching.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] review | EP286 | 讓 AI 成為第二大腦

- **Action**: Status=ready; 已核讀完整上游報告；採核心重點、批判分析與使用者既有心得，保留轉錄和時間碼限制。未重新驗證原音。
- **Pages touched**: `wiki/sources/2026-09-24--techporn-ep286.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] review | EP292 | AI 能自己寫一整晚，工程師還剩什麼？Fabal 5、GPT 5.6 實測與下一代開發！

- **Action**: Status=ready; 已核讀完整上游報告；採需求、驗收和理解關卡，跨到知識管理的應用標為助理推論。
- **Pages touched**: `wiki/sources/2026-09-24--techporn-ep292.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] review | Prompt Engineering in 2025: Complete Guide for ChatGPT, Claude, and Gemini

- **Action**: Status=ready; 已核讀本機歷史剪藏文字；只採提示與測試流程，圖像和當前版本未驗證，coverage保留partial。
- **Pages touched**: `wiki/sources/2025-06-13--prompt-engineering-in-2025-complete-guide.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] review | Prompting best practices

- **Action**: Status=ready; 已核讀本機歷史剪藏；只採上下文與狀態管理。發布日未知，剪藏日不作發布日；保留partial。
- **Pages touched**: `wiki/sources/2026-05-24--prompting-best-practices.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] review | LLM Wiki — 原文閱讀筆記

- **Action**: Status=ready; 已核讀原作者正文的架構、操作和索引部分；本機只保存短閱讀筆記，evidence_level=source-notes且partial。
- **Pages touched**: `wiki/sources/2026-09-24--karpathy-llm-wiki.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] review | Effective context engineering for AI agents — 閱讀筆記

- **Action**: Status=ready; 已核讀相關原文小節；本機只保存短閱讀筆記，未使用圖片細節，保留source-notes及partial。
- **Pages touched**: `wiki/sources/2026-09-24--anthropic-context-engineering.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] query | AI 輔助學習與知識管理試作

- **Action**: 整合六份文件（四個新來源頁、兩個既有來源頁），區分作者主張、助理推論、使用者已提供觀點與來源相依性；未量測學習成效。
- **Pages touched**: `wiki/syntheses/2026-09-24--ai-learning-knowledge-management.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] ingest | Caching

- **Action**: Imported pdf; status=needs-review; SHA-256=1327a78d257db55e4ec37f89fe729e02988be48b7fe983624958edfe0cbf302a.
- **Pages touched**: `wiki/sources/2026-05-24--caching.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-24] lint | 第一輪索引、中文查詢與匯入驗收

- **Action**: 完成 39 項測試、索引／schema／log 驗證、七題實際查詢與來源快照完整性核對；PDF 原始檔保持不變。
- **Pages touched**: `verification/first-round-validation.md`, `verification/first-round-validation.json`
- **Notes**: 六份主題來源已核讀；PDF 圖表與浮水印限制保留 needs-review。
- **Open questions**: 詞彙搜尋尚非任意語意查詢；圖表正確性仍須逐頁核讀。

## [2026-09-24] maintenance | 單一路徑的文件解析 skill 入口

- **Action**: 更新 llm-wiki-ingest，支援只提供檔案路徑即完成繁中解析、摘要、關聯與入庫；明確處理既有來源、PDF 依賴及未完成的來源卡。
- **Pages touched**: `.agents/skills/llm-wiki-ingest/SKILL.md`, `.agents/skills/llm-wiki-ingest/agents/openai.yaml`, `README.md`
- **Notes**: 此次只更新 skill 與使用說明，沒有匯入新文件或改寫來源摘要。
- **Open questions**: 遇到不支援格式或無法辨識的圖表，仍需說明限制並保留待核讀狀態。

## [2026-09-25] ingest | 建立自己的資訊流：FreshRSS × NetNewsWire 架構筆記

- **Action**: Imported article; status=draft; SHA-256=8d79521ab8361fe47cb12158059d3ede27ed5b6de356e6498b5103d06dc7c15a.
- **Pages touched**: `wiki/sources/2026-09-25--personal-information-feed-architecture.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-25] review | 建立自己的資訊流：FreshRSS × NetNewsWire 架構筆記

- **Action**: Status=ready; 已核讀完整架構筆記第 1–6 節、兩段 Mermaid 圖與表格；核對匿名化及完整檔案保存，保留 source-notes、medium confidence，不聲稱重新驗證實際部署。另在 TLS Termination 概念頁加入來源關聯。
- **Pages touched**: `wiki/sources/2026-09-25--personal-information-feed-architecture.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-25] lint | FreshRSS × NetNewsWire 架構筆記匯入檢查

- **Action**: 已通過索引一致性、嚴格 schema 與 log contract 檢查，並核對原筆記逐位元相同、兩段 Mermaid 原始碼完整及網域匿名化。
- **Pages touched**: `SystemDesign/personal-information-feed-architecture.md`, `wiki/sources/2026-09-25--personal-information-feed-architecture.md`, `wiki/concepts/tls-termination.md`, `inbox/sources.json`, `wiki/index.md`, `wiki/log.md`
- **Notes**: 新來源卡標為 ready；此狀態僅指完整核讀筆記。使用者明確要求 Git 提交與推送，既有 Obsidian 工作區修改保留。
- **Open questions**: 實際服務部署與備份還原未於本次匯入重新測試；內容處理另行整理。

## [2026-09-25] query | 影片分析與 Notes 的 CLI 整合流程提案

- **Action**: 核對兩個專案的現行規範、報告格式、Notes 匯入程式、既有來源卡與官方 CLI 文件；整理操作入口與流程交接建議，保存為 draft synthesis。
- **Pages touched**: `wiki/syntheses/2026-09-25--video-notes-cli-workflow.md`, `wiki/syntheses/2026-09-24--ai-learning-knowledge-management.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: 明確區分現況、使用者方向與助理提案；未變更流程規範、匯入原始資料、建立 skill、執行影片分析或 GitHub 發布。保留既有 Obsidian 工作區變更。
- **Open questions**: 實作時確定預設入庫條件、Notes 發布範圍，以及首個決策驗收問題。

## [2026-09-25] lint | CLI 流程提案的文件一致性檢查

- **Action**: 執行索引一致性、strict schema、log contract 與 diff 空白檢查，全部通過；schema 掃描 216 份文件，沒有問題。
- **Pages touched**: `wiki/syntheses/2026-09-25--video-notes-cli-workflow.md`, `wiki/syntheses/2026-09-24--ai-learning-knowledge-management.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: 此為文件結構與紀錄驗證，未進行全庫語意矛盾審查，也不表示提案流程已實作或通過端到端測試。
- **Open questions**: 後續實作仍須驗收去重、版本更新、略過／未看先保留與發布失敗接續。

## [2026-09-25] maintenance | 啟用 Notes 專案的 video-analyze skill

- **Action**: 依使用者明確指示，將已確認的 skill 初稿、影片報告範本及顯示資訊加入 `.agents/skills/video-analyze/`，並補上 README 使用入口與提案進度。
- **Pages touched**: `.agents/skills/video-analyze/SKILL.md`, `.agents/skills/video-analyze/assets/video-summary.md`, `.agents/skills/video-analyze/agents/openai.yaml`, `README.md`, `wiki/syntheses/2026-09-25--video-notes-cli-workflow.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: 保留完整分析／初篩、雙評分、個人回饋後預設入庫及四組獨立狀態；沿用 llm-wiki-ingest 維護來源快照與 Wiki。未搬移既有報告，未執行影片分析、提醒或 GitHub 發布；媒體流程實測依使用者安排由另一對話進行。
- **Open questions**: 完整素材取得與轉錄的驗證結果、共用發布流程仍待後續整合。

## [2026-09-25] lint | video-analyze 啟用與文件驗證

- **Action**: 通過 skill-creator quick_validate、資源路徑與 ingest 依賴檢查、Wiki 索引一致性、strict schema、log contract 與 diff 空白檢查。Codex CLI 的 skills/list 實際回報 video-analyze 為 repo scope、enabled=true，無同名重複項。
- **Pages touched**: `.agents/skills/video-analyze/SKILL.md`, `.agents/skills/video-analyze/assets/video-summary.md`, `.agents/skills/video-analyze/agents/openai.yaml`, `README.md`, `wiki/syntheses/2026-09-25--video-notes-cli-workflow.md`, `wiki/index.md`, `wiki/log.md`
- **Notes**: 僅驗證技能載入與文件結構，未呼叫模型、建立新對話或執行素材取得／轉錄。驗證器依賴僅安裝於暫存目錄，沒有變更系統或專案 Python 依賴。
- **Open questions**: 完整影片流程實測與共用發布流程仍由後續工作處理。

## [2026-09-25] query | Edwin H. iPhone 評測完整字幕分析

- **Action**: 依 video-analyze 技能完成 YouTube lsUdyCJijS8 的 full-transcript 分析，完整核讀 1,214 段非自動粵語字幕，核對片長、段間缺口及自動字幕片尾，另查證 Apple／Samsung 官方產品文件。
- **Pages touched**: `reports/videos/2026-09-25-lsUdyCJijS8-iphone-18-pro-max-review.md`, `wiki/log.md`
- **Notes**: 建議 selected-sections，推薦 7/10、品質 18/25、confidence medium。報告保留標題差異、片尾無字幕時間、視覺與實測限制，修正 Fold8 立體聲說法並補充 AVS 快充條件。必備段落、評分、來源去重及狀態檢查通過，Wiki 索引已核對為最新，無新 Wiki 頁面需加入。暫存資料逐一依明確路徑刪除；沒有下載影音。個人回饋及入庫取捨仍 pending，觀看狀態 unknown；未執行入庫或 Git commit／push。
- **Open questions**: 使用者的一句話心得或保留取捨；相機原始畫面與測試條件尚未獨立驗證。

## [2026-09-25] ingest | 鏡頭原來可以... iPhone 18 Pro Max 終極評測 + iPhone Duo Q&A

- **Action**: Imported video-report; status=draft; SHA-256=4d783cd7e035eeff0273e1567d18838af07687ad3a6a553e54ab70a2f17f6b7c.
- **Pages touched**: `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-25] review | 鏡頭原來可以... iPhone 18 Pro Max 終極評測 + iPhone Duo Q&A

- **Action**: Status=ready; 完整核讀報告全部 16 個主要段落及 2026-09-25 使用者原話；快照與輸入逐位元相同、SHA-256 和完整擷取一致，無機器擷取警示。保留 full-transcript／full／medium／secondary-summary、片尾時間與視覺未核讀限制、官方查證與作者測試的區別；觀看方式 unknown，心得 provided，依預設流程 keep。未重新取得字幕或驗證產品測試。
- **Pages touched**: `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-25] ingest | iPhone 評測心得與新特性參考入庫

- **Action**: 原文保存使用者關於快速了解 iPhone 18 Pro／Pro Max 新特性的心得；依 video-analyze 具體回饋規則將 pending 改為 keep，交接 llm-wiki-ingest 完成報告快照、全文核讀與來源卡整理。
- **Pages touched**: `reports/videos/2026-09-25-lsUdyCJijS8-iphone-18-pro-max-review.md`, `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`, `wiki/log.md`
- **Notes**: 心得 provided、觀看方式 unknown；未推定購買、換機或完整觀看。來源為 secondary-summary，繼承 full-transcript／full／medium、7/10 與 18/25。已連結既有知識管理綜整作為整理方法脈絡，沒有新建零散產品頁；ready 僅表示保存報告的記錄範圍已核讀。上游報告僅補記入庫結果，不因此重複建立版本；未執行 Git commit／push。
- **Open questions**: 視覺證據、原始測試條件及產品未來安排仍受上游限制；目前未提出特定選購問題。

## [2026-09-25] lint | iPhone 影片回饋入庫驗證

- **Action**: 通過索引一致性、strict schema（217 頁零問題）、日誌契約、diff 空白檢查，以及 14 項共用匯入測試。
- **Pages touched**: `wiki/log.md`；已核對 `reports/videos/2026-09-25-lsUdyCJijS8-iphone-18-pro-max-review.md`, `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: 同一影片僅一個 source_id 與一份版本；不可變報告及擷取檔雜湊一致，原話與 provided／unknown／keep 狀態在上游、快照和來源卡一致。上游相對快照僅增加入庫結果紀錄；中文新特性查詢能找到 ready 來源卡。
- **Open questions**: 結構與檢索驗證不代表影片實測已獨立重現；原有限制繼續保留。

## [2026-09-26] ingest | 鏡頭原來可以... iPhone 18 Pro Max 終極評測 + iPhone Duo Q&A

- **Action**: Imported video-report; status=needs-review; SHA-256=6379409e7b8b0240a8e4a78211530041824af184e8b3034ed7965dac00c5439e.
- **Pages touched**: `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-26] review | 鏡頭原來可以... iPhone 18 Pro Max 終極評測 + iPhone Duo Q&A

- **Action**: Status=ready; 已核讀新版本完整報告及 2026-09-26 觀看確認原話「已觀看過了」，將 viewing_status 更新為 full。原有 2026-09-25 心得、provided／keep、雙評分與 full-transcript／full／medium／secondary-summary 均保留；確認日期不代替觀看日期。新舊快照與擷取雜湊完整，沒有新產品分析或實測。
- **Pages touched**: `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: Original files retained; local snapshot and provenance recorded.
- **Open questions**: Review extraction limitations and source claims before relying on them.

## [2026-09-26] ingest | 記錄 iPhone 評測已觀看確認

- **Action**: 保存使用者原話「已觀看過了」，將上游報告與來源卡的 viewing_status 由 unknown 更新為 full，沿用 youtube-lsudycjijs8 建立新版本並核讀為 ready。
- **Pages touched**: `reports/videos/2026-09-25-lsUdyCJijS8-iphone-18-pro-max-review.md`, `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`, `wiki/log.md`
- **Notes**: 保留 2026-09-25 原心得與 provided／keep、評分、覆蓋和信心。觀看確認日期為 2026-09-26，未推定實際觀看日期、購買決策或額外心得。舊版本與原始證據均未改動；只是同一來源的新版本，不新增獨立證據數。未執行 Git commit／push。
- **Open questions**: 原有視覺、原音與實測限制仍適用於助理分析。

## [2026-09-26] lint | 觀看狀態更新驗證

- **Action**: 通過索引一致性、strict schema（217 頁零問題）、日誌契約、diff 空白與觀看狀態一致性檢查。
- **Pages touched**: `wiki/log.md`；核對影片報告、`wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`
- **Notes**: 原心得與觀看確認在上游、最新快照及來源卡中一致，均為 provided／full／keep。兩份歷史快照及擷取雜湊完整，同一來源仍只計一次；上游相對快照僅補記完成結果。
- **Open questions**: 本次沒有新的內容分析或產品查證。

## [2026-09-26] lint | 影片分析與心得 GitHub 發布前檢查

- **Action**: 依使用者明確要求準備提交並推送影片分析相關更新；索引一致性、strict schema（217 頁零問題）、日誌契約、diff 空白檢查與 14 項共用匯入測試全部通過。
- **Pages touched**: `.agents/skills/video-analyze/`, `README.md`, `reports/videos/2026-09-25-lsUdyCJijS8-iphone-18-pro-max-review.md`, `wiki/sources/2026-09-25--youtube-lsudycjijs8.md`, `inbox/sources.json`, `wiki/index.md`, `wiki/log.md`, `wiki/syntheses/2026-09-24--ai-learning-knowledge-management.md`, `wiki/syntheses/2026-09-25--video-notes-cli-workflow.md`
- **Notes**: 發布目標為 origin/main（ariel055132/Notes）；本次包含先前已完成的影片技能與流程文件。Obsidian 視窗狀態保留在本機；原始快照與擷取證據沿用 Git 忽略設定。
- **Open questions**: 待 Git 提交與推送完成後補記實際結果；共用自動發布流程仍未建立。

## [2026-09-26] publish | 影片分析流程與 iPhone 報告已推送 GitHub

- **Action**: 完成提交 `4852cb81a34f0ffbe8ee6d86c9f0af714511ee61`（Add video analysis workflow and reviewed iPhone report），並成功推送至 `https://github.com/ariel055132/Notes.git` 的 `main`；遠端回覆 `379d398..4852cb8 main -> main`。
- **Pages touched**: 本次內容提交共 11 份檔案；發布結果補記於 `reports/videos/2026-09-25-lsUdyCJijS8-iphone-18-pro-max-review.md` 與 `wiki/log.md`。
- **Notes**: 推送涵蓋影片技能與範本、README、影片報告、個人心得及觀看確認、來源卡、登記檔、索引與相關流程綜整。保留 Obsidian 工作區修改於本機，原始快照與擷取結果沿用 Git 忽略設定。僅補記發布結果，未建立額外來源版本。
- **Open questions**: 共用自動發布流程尚未建立；本次 GitHub 發布由使用者明確指示完成。
