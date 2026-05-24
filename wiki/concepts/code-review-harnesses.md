---
type: concept
aliases: ["code review prompts", "bug-finding harnesses"]
tags: [code-review, prompt-engineering, evaluation]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Code Review Harnesses

## Definition

Code review harnesses are prompt and evaluation setups that direct a model to inspect code, surface defects, and optionally separate finding coverage from later confidence or severity filtering. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers bug-finding prompts, severity thresholds, confidence reporting, deduplication, ranking, and evaluation against test cases. It does not cover manual human review practices except where prompts model them. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **General code assistance**: General code assistance may answer or implement, while review harnesses optimize for finding and reporting issues.
- **Self-filtered review**: A self-filtered review reports only above a stated bar, while a coverage-first harness reports uncertain or low-severity findings for downstream filtering.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The guide recommends explicitly telling the model whether the review stage should maximize coverage or apply a concrete reporting bar.

## Related

- [[prompt-engineering|Prompt Engineering]]
- [[few-shot-prompting|Few-Shot Prompting]]
- [[tool-use|Tool Use]]
- [[agentic-systems|Agentic Systems]]

## Open Questions

- Should wiki linting adopt a coverage-first reporting phase before prioritizing fixes?
