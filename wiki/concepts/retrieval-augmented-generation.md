---
type: concept
aliases: ["RAG", "retrieval augmented generation", "grounded generation"]
tags: [prompt-engineering, retrieval, grounding]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Retrieval-Augmented Generation

## Definition

Retrieval-augmented generation is a prompting and system pattern where relevant source material is supplied to the model and the model is instructed to answer from that material. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers grounded answers using notes, documents, search results, database records, or other supplied context. It does not mean the model should rely on its memory when source-grounded evidence is required. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Long Context Prompting**: Retrieval-augmented generation selects and supplies relevant material, while long context prompting focuses on arranging large supplied inputs so the model can use them. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Ungrounded generation**: Ungrounded generation depends mainly on model memory, while retrieval-augmented generation constrains the answer to provided sources. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source describes RAG as supplying the material the model should use and telling it how to answer from that material.

## Related

- [[Prompt Engineering]]
- [[Long Context Prompting]]
- [[Tool Use]]
- [[Prompt Testing and Versioning]]

## Open Questions

- Which wiki queries should require retrieval-grounded citations before an answer is filed as synthesis?
