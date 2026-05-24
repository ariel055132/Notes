---
type: concept
aliases: ["long context prompting", "large-document prompting"]
tags: [prompt-engineering, long-context]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Long Context Prompting

## Definition

Long context prompting is the practice of arranging large documents or data-rich inputs so the model can retrieve, ground, and reason over them effectively. [[2026-05-24--prompting-best-practices|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers placing long source material before the task request, structuring documents with metadata and content tags, prioritizing the most relevant information, and breaking extremely long contexts into focused sequential prompts. It does not replace indexing, retrieval systems, or source verification for very large corpora. [[2026-05-24--prompting-best-practices|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Retrieval-Augmented Generation**: Long context prompting arranges large supplied inputs, while retrieval-augmented generation selects and injects relevant material from an external store or source set. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Short prompt writing**: Short prompts can rely on concise instructions, while long-context prompts need stronger document boundaries and ordering. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source recommends putting longform data near the top, placing the query later, and using document tags with metadata.
- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source recommends prioritizing relevant information at the beginning and end, using structured formatting, and splitting very long contexts into sequential prompts.

## Related

- [[Prompt Engineering]]
- [[Retrieval-Augmented Generation]]
- [[Prompt Chaining]]
- [[XML Prompt Structure]]
- [[Agentic Systems]]

## Open Questions

- Which wiki query workflows should quote relevant source passages before synthesis?
