---
type: concept
aliases: ["metacognitive prompts", "assumption-checking prompts"]
tags: [prompt-engineering, reasoning]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Metacognitive Prompting

## Definition

Metacognitive prompting asks a model to consider its assumptions, missing information, limitations, or uncertainty before giving a recommendation or answer. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers prompts that improve judgment by surfacing constraints, unknowns, and caveats before analysis. It does not make a model's recommendation reliable without domain evidence, expert review, or task-specific validation. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Chain-of-Thought Prompting**: Chain-of-thought prompting focuses on stepwise solution work, while metacognitive prompting focuses on the quality and limits of the model's frame before answering. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Multiple Viewpoints**: Metacognitive prompting asks for self-checks, while multiple-viewpoint prompting asks the model to analyze a problem from distinct stakeholder perspectives. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source recommends asking what assumptions are being made, what information is missing, and what limits affect the analysis.

## Related

- [[Prompt Engineering]]
- [[Chain-of-Thought Prompting]]
- [[Iterative Refinement]]

## Open Questions

- Which high-stakes wiki answers should begin with an explicit assumptions and limitations check?
