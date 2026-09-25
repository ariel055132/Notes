# LLM Wiki Schema

> This is the authoritative schema document. The LLM must follow these conventions when maintaining the wiki. Treat this as the system prompt for wiki operations.

## Mission

Build and maintain a persistent, compounding knowledge base. The wiki is not a dump of raw text—it is a structured, interlinked artifact that grows richer with every source. Cross-references are pre-built. Contradictions are flagged. Synthesis reflects everything read so far.

## Non-negotiables

1. **Raw source contents are immutable.** Never edit raw contents. New imports create content-addressed snapshots in `raw/imports/`; originals stay where the user kept them. Existing archives remain valid.
2. **The LLM maintains the wiki layer.** Preserve operator-authored judgments and distinguish source claims, assistant inference and confirmed personal views. Never invent a personal reflection.
3. **Every action is logged.** Every ingest, query result filed, and lint pass appends an entry to `wiki/log.md`.
4. **The index is always current.** `wiki/index.md` must reflect the state of the wiki after every operation that touches pages.
5. **Cross-references are first-class.** Every page must link to related pages. Orphan pages are bugs.

## Directory Layout

```
LLM-wiki/
├── AGENTS.md          # This file. Authoritative schema.
├── README.md          # Human quickstart.
├── inbox/sources.json  # Source identity, revisions and processing state.
├── derived/           # Local ignored full extraction evidence, never treated as a summary.
├── raw/               # Immutable source documents; local backup required separately from Git.
│   ├── imports/       # Content-addressed snapshots from the common importer.
│   ├── sources/       # Text sources (articles, papers, transcripts).
│   ├── assets/        # Downloaded images, data files.
│   └── archive/       # Post-ingest archived original source files.
├── wiki/              # LLM-generated markdown. LLM owns this tree.
│   ├── index.md       # Generated catalog; do not edit by hand.
│   ├── log.md         # Append-only timeline.
│   ├── entities/      # Concrete things (people, places, organizations, products).
│   ├── concepts/      # Abstract ideas (theories, frameworks, methodologies).
│   ├── sources/       # One summary page per ingested source.
│   ├── syntheses/     # Cross-source analysis, comparisons, answers.
│   └── templates/     # Reusable page templates.
├── .agents/            # Project-level skill definitions (OpenCode autodiscovery).
│   └── skills/
│       ├── llm-wiki-ingest/   # Ingest workflow skill.
│       ├── llm-wiki-query/    # Query workflow skill.
│       └── llm-wiki-lint/     # Lint workflow skill.
└── verification/      # TDD fixtures and acceptance cases.
```

## Page Types & Conventions

### Entity Pages (`wiki/entities/`)

- Filename: `kebab-case.md`
- Purpose: A concrete thing that appears across multiple sources.
- Frontmatter:
  ```yaml
  ---
  type: entity
  aliases: ["Alternative Name", "Abbreviation"]
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  source_count: 0
  ---
  ```
- Sections:
  - `# Entity Name` — H1 title, exact canonical name.
  - `## Identity` — What it is, one concise paragraph.
  - `## Aliases` — List of known aliases.
  - `## Key Attributes` — Structured facts (table or bullet list).
  - `## Evidence` — Links to source summaries that mention this entity, with brief quote or context per link.
  - `## Related` — Links to related entity and concept pages.
  - `## Open Questions` — Uncertainties or gaps about this entity.

### Concept Pages (`wiki/concepts/`)

- Filename: `kebab-case.md`
- Purpose: An abstract idea, theory, or methodology.
- Frontmatter:
  ```yaml
  ---
  type: concept
  aliases: ["Synonym", "Related Term"]
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  source_count: 0
  ---
  ```
- Sections:
  - `# Concept Name`
  - `## Definition` — Precise definition in one paragraph.
  - `## Scope` — What this concept covers and what it does not.
  - `## Contrasts` — Differences from related concepts.
  - `## Evidence` — Source links with context.
  - `## Related` — Cross-links.
  - `## Open Questions`

### Source Pages (`wiki/sources/`)

- Filename: `YYYY-MM-DD--source-title-slug.md`
- Purpose: Summary and extraction from a single raw source.
- Frontmatter:
  ```yaml
  ---
  type: source
  source_path: raw/imports/source-id/sha256.pdf
  title: "Exact Title of Source"
  author: "Author Name"
  date: YYYY-MM-DD # or "unknown"; never substitute capture date for publication
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  source_id: stable-id
  source_type: pdf # article | video-report
  source_url: "https://example.com/original"
  processing_status: needs-review # draft | ready | blocked
  coverage: partial # unknown | none | full
  confidence: low # medium | high
  evidence_level: original-document # secondary-summary | source-notes
  ---
  ```
- Sections:
  - `# Source Title`
  - `## Summary` — 3-5 sentence overview.
  - `## Key Claims` — Numbered list of main assertions.
  - `## Notable Quotes` — Direct quotes with page/section references if available.
  - `## Entities Mentioned` — Links to entity pages created or updated.
  - `## Concepts Mentioned` — Links to concept pages.
  - `## Follow-ups` — Questions or leads from this source.

### Synthesis Pages (`wiki/syntheses/`)

- Filename: `YYYY-MM-DD--question-slug.md` or `YYYY-MM-DD--topic-slug.md`
- Purpose: Cross-source analysis, answers to questions, comparisons.
- Frontmatter:
  ```yaml
  ---
  type: synthesis
  question: "The exact question this page answers"
  tags: [tag-one, tag-two]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  ---
  ```
- Sections:
  - `# Synthesis Title`
  - `## Question / Purpose`
  - `## Answer / Analysis`
  - `## Comparison Table` (if applicable)
  - `## Citations` — Links to source pages with brief evidence snippets.
  - `## Implications` — Why this matters.
  - `## Follow-up Questions`

## Citation Rules

1. Substantive source-based claims must cite supporting source pages and a page/section locator when available. A synthesis is a navigation aid, not independent evidence. Label assistant inference and personal views explicitly.
2. Use Obsidian wikilink syntax: `[[Page Name]]` or `[[Page Name|display text]]`.
3. Source cards record snapshot path, canonical URL, source ID, version hash, coverage and review state. Direct quotes reproduce source wording; mark translations and paraphrases. Preserve extraction warnings and inherited video report limits.
4. When updating a page based on a new source, append the new citation—do not remove old ones unless they are factually incorrect.

## Ingest Workflow

**Goal:** Integrate a new raw source into the wiki.

**Preconditions:**
- The operator has requested ingestion; a known topic/focus from the conversation is sufficient guidance.
- Input is a local saved article (Markdown/text/HTML), PDF or completed video analysis report. URLs are provenance; the CLI does not fetch websites or media.

**Steps:**
1. Use `scripts/import_source.py add` to snapshot, extract and register the source. Use `--existing-page` for an already curated source; do not create duplicate cards. Source ID identifies the work, SHA identifies a saved version.
2. Read the complete extraction and its warnings. Inspect relevant PDF images/tables against original pages; do not infer missing visual content. Keep uncertain evidence `needs-review` or `blocked`.
3. Curate the source card, replacing its `REVIEW_REQUIRED` placeholder only after reading the evidence. Preserve page/section references, limitations and the operator's supplied views. If intent is genuinely unclear, ask a focused question while continuing independent work.
4. Update only useful existing concepts or create topic syntheses. Do not create a page for every mentioned noun; recurring concepts or an actual query justify pages.
5. Use `scripts/import_source.py review` with a concrete review note. `ready` means the recorded scope was reviewed, not that all author claims are true. Never erase coverage or warnings to reach `ready`.
6. Rebuild/check the index, validate the log and schema, and run relevant tests. The importer logs its operations; append a separate entry for manually written syntheses.

**Done Criteria:**
- Source page exists and is complete.
- Relevant concepts and syntheses are linked; incidental entities need no dedicated page.
- `wiki/index.md` reflects all changes.
- `wiki/log.md` has a new entry.
- Original source is unchanged, snapshot hash matches, and local extraction/review state is recorded.

## Query Workflow

**Goal:** Answer a question using the wiki as the primary knowledge source.

**Steps:**
1. Use `scripts/wiki_qa_bot.py --question "..." --json` and the generated index to find evidence. Search includes the existing AWS, Stock, Container and SystemDesign folders.
2. Read the returned passages and their source cards; follow references to original pages for consequential details. Search returns lexical evidence excerpts, not a generated factual answer or arbitrary multilingual semantic search.
3. Synthesize an answer in the operator's language with per-claim citations. Preserve `needs-review`/partial/secondary-source limitations, conflicts and unknowns. Open questions are not established answers. If evidence is insufficient, say what is missing.
4. Present the answer to the operator.
5. If the answer is reusable or represents new synthesis, file it as a new synthesis page in `wiki/syntheses/` and update `wiki/index.md` and `wiki/log.md`.

**Done Criteria:**
- Answer is supported by cited wiki pages.
- If filed, synthesis page exists and is linked from index and log.

## Lint Workflow

**Goal:** Health-check the wiki for structural and logical issues.

**Checks:**
1. **Contradictions:** Claims on different pages that conflict.
2. **Stale Claims:** Assertions newer sources have superseded.
3. **Orphan Pages:** Pages with no inbound wikilinks.
4. **Missing Pages:** Important concepts mentioned but lacking dedicated pages.
5. **Broken Links:** Wikilinks pointing to non-existent pages.
6. **Data Gaps:** Areas where additional sources or web search could fill holes.

**Steps:**
1. Scan all pages for the above issues.
2. Produce a lint report (can be a temporary synthesis page or inline in chat).
3. Discuss fixes with the operator.
4. Apply agreed fixes.
5. Append an entry to `wiki/log.md`.

**Done Criteria:**
- Report lists all found issues with severity.
- Agreed fixes are applied.
- `wiki/log.md` updated.

## Update Rules for Special Files

### `wiki/index.md`

- Generate with `python3 scripts/rebuild_index.py`; verify with `--check`.
- Derive source counts from unique direct source-page references (deduplicate `source_id`); a source card itself counts as one. Existing frontmatter counters are legacy hints, not authoritative statistics or independent corroboration counts.
- Group by: Entities, Concepts, Sources, Syntheses.
- Each entry: `| [[Page Name]] | One-line summary | Source count | Status | Updated |`

### `wiki/log.md`

- Strictly append-only.
- Each entry starts with: `## [YYYY-MM-DD] action-type | Brief description`
- Include: action type (ingest/query/lint), pages touched, notes, open questions.

## Frontmatter Contract

Every wiki page must include YAML frontmatter with at minimum:
- `type`: entity | concept | source | synthesis
- `tags`: list of relevant tags
- `created`: ISO date

Optional but recommended:
- `updated`: ISO date
- `source_count`: integer
- `aliases`: list of alternative names

## Operator Communication Style

- When ingesting, summarize what was done and what pages were touched.
- When querying, cite sources and offer to file reusable answers.
- When linting, present findings with severity and suggested fixes.
- Always ask before making large structural changes.

## Schema Evolution

This document is co-evolved with the operator. If a workflow isn't working, propose a change here before changing behavior.

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting contradictions, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Private, actively curated, with the connections between documents as valuable as the documents themselves. The part Bush couldn't solve was who does the maintenance. The LLM handles that.
