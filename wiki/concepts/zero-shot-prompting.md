---
type: concept
aliases: ["zero-shot prompts"]
tags: [prompt-engineering]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Zero-Shot Prompting

## Definition

Zero-shot prompting is asking a model to perform a task using only instructions, context, constraints, and output requirements, without providing examples of the desired answer pattern. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers simple, well-defined tasks where the desired format is standard or obvious. It does not cover tasks where tone, schema, edge-case handling, or stylistic imitation require examples. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Few-Shot Prompting**: Zero-shot prompting relies on written instructions alone, while few-shot prompting adds examples that demonstrate the desired pattern. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Prompt Chaining**: Zero-shot prompting can be a single request, while prompt chaining splits a larger workflow into multiple dependent prompts. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source recommends starting with zero-shot prompting for simple tasks and adding examples when the desired pattern needs more control.

## Related

- [[Prompt Engineering]]
- [[Few-Shot Prompting]]
- [[POWER Prompt Framework]]

## Open Questions

- Which wiki operations are simple enough for zero-shot prompts without examples?
