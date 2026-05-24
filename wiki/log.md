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
