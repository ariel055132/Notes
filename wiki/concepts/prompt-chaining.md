---
type: concept
aliases: ["chained prompts", "sequential prompting"]
tags: [prompt-engineering, workflow]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Prompt Chaining

## Definition

Prompt chaining is a workflow pattern where a sequence of prompts decomposes a larger task and each step uses the previous output as input for the next step. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers multi-step workflows such as analyze, brainstorm, estimate, prioritize, and plan. It does not require full agent autonomy because the chain can be explicitly designed and reviewed step by step. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Agentic Systems**: Prompt chaining is a planned sequence of dependent prompts, while agentic systems may dynamically choose tools and intermediate steps. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] [[2026-05-24--prompting-best-practices|Prompting best practices]]
- **Single prompt workflows**: Single prompt workflows ask for all output at once, while prompt chaining separates analysis into stages. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source describes prompt chaining as a sequence where market analysis feeds feature ideas, estimation, prioritization, and roadmap creation.

## Related

- [[prompt-engineering|Prompt Engineering]]
- [[agentic-systems|Agentic Systems]]
- [[iterative-refinement|Iterative Refinement]]
- [[tool-use|Tool Use]]

## Open Questions

- Which wiki workflows should be represented as explicit prompt chains rather than one broad instruction?
