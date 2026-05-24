---
type: concept
aliases: ["POWER framework", "POWER prompting"]
tags: [prompt-engineering, framework]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# POWER Prompt Framework

## Definition

The POWER Prompt Framework is a practical prompt structure that combines Purpose, Output Format, Working Context, Examples, and Refinement Instructions to make model requests clearer and easier to evaluate. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers reusable prompt drafting for common work tasks where the user can state the goal, target format, background context, examples, and quality constraints. It does not replace domain review, source verification, or model-specific testing when a prompt is used in production. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Ad hoc prompting**: Ad hoc prompts may rely on implicit expectations, while POWER prompts make the objective, context, format, examples, and quality bar explicit. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Prompt Testing and Versioning**: POWER helps draft a prompt, while prompt testing and versioning check whether the drafted prompt continues to work over time. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source presents POWER as its central structure for effective prompts in 2025.

## Related

- [[prompt-engineering|Prompt Engineering]]
- [[few-shot-prompting|Few-Shot Prompting]]
- [[prompt-testing-and-versioning|Prompt Testing and Versioning]]
- [[iterative-refinement|Iterative Refinement]]

## Open Questions

- Which wiki workflows should standardize on POWER as the default prompt template?
