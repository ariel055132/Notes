---
type: concept
aliases: ["prompt refinement", "draft-review-rewrite"]
tags: [prompt-engineering, workflow]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Iterative Refinement

## Definition

Iterative refinement is a prompt workflow where an output is drafted, evaluated against stated criteria, and then revised based on the review. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers feedback loops for writing, analysis, prompt improvement, and output quality checks. It does not assume the model's self-review is sufficient for production use without external evals or human review when the stakes are high. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Single-shot prompting**: Single-shot prompting expects one pass to be enough, while iterative refinement builds evaluation and revision into the workflow. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Prompt Testing and Versioning**: Iterative refinement improves a particular output or prompt, while prompt testing and versioning preserve and evaluate prompt behavior across repeated inputs. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source recommends workflows that draft, self-review against criteria, rewrite, evaluate, and refine.

## Related

- [[Prompt Engineering]]
- [[POWER Prompt Framework]]
- [[Prompt Testing and Versioning]]
- [[Chain-of-Thought Prompting]]

## Open Questions

- Which wiki page updates should include a draft-review-rewrite cycle before filing?
