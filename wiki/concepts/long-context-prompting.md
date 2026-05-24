---
type: concept
aliases: ["long context prompting", "large-document prompting"]
tags: [prompt-engineering, long-context]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Long Context Prompting

## Definition

Long context prompting is the practice of arranging large documents or data-rich inputs so the model can retrieve, ground, and reason over them effectively. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers placing long source material before the task request, structuring documents with metadata and content tags, and asking for relevant quotes before analysis when grounding matters. It does not replace indexing, retrieval systems, or source verification for very large corpora. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Retrieval-augmented generation**: Long context prompting places material directly in context, while retrieval systems select and inject relevant material from an external store.
- **Short prompt writing**: Short prompts can rely on concise instructions, while long-context prompts need stronger document boundaries and ordering.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source recommends putting longform data near the top, placing the query later, and using document tags with metadata.

## Related

- [[Prompt Engineering]]
- [[XML Prompt Structure]]
- [[Agentic Systems]]

## Open Questions

- Which wiki query workflows should quote relevant source passages before synthesis?
