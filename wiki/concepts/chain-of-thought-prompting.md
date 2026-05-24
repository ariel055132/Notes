---
type: concept
aliases: ["CoT prompting", "step-by-step prompting", "reasoning prompts"]
tags: [prompt-engineering, reasoning]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Chain-of-Thought Prompting

## Definition

Chain-of-thought prompting is asking a model to work through assumptions, intermediate reasoning, or calculations before producing an answer, especially for tasks where skipped steps can change the result. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers math, planning, trade-off analysis, ROI estimates, and decisions that benefit from visible assumptions. It does not require exposing every private reasoning detail when the useful deliverable is a concise final answer with assumptions and checks. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Zero-Shot Prompting**: Zero-shot prompts may ask directly for an answer, while chain-of-thought prompts ask the model to structure the path to that answer. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Metacognitive Prompting**: Chain-of-thought prompting emphasizes solving steps, while metacognitive prompting emphasizes assumptions, missing information, and limits before answering. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source recommends chain-of-thought prompting for math, planning, trade-off analysis, and decisions that need explicit assumptions.

## Related

- [[prompt-engineering|Prompt Engineering]]
- [[metacognitive-prompting|Metacognitive Prompting]]
- [[iterative-refinement|Iterative Refinement]]

## Open Questions

- Which wiki syntheses should include explicit assumptions before conclusions?
