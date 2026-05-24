---
type: concept
aliases: ["frontend aesthetics defaults", "design default steering"]
tags: [frontend, prompt-engineering, design]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Frontend Design Defaults

## Definition

Frontend design defaults are recurring visual styles a model may produce without specific aesthetic direction, plus the prompt techniques used to steer toward a more fitting design. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers specifying concrete visual alternatives, asking for visual directions before implementation, avoiding generic patterns, and tailoring design to the product context. It does not define a universal design system. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Generic design prompts**: Generic prompts may trigger repeated default aesthetics, while concrete palettes, typography, layout, and interaction constraints steer more reliably.
- **Implementation details**: Design direction sets visual intent, while implementation still requires code, assets, and verification.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source describes repeated default aesthetics and recommends concrete alternative directions or asking the model to propose options before building.

## Related

- [[Prompt Engineering]]
- [[Claude Opus 4.7]]

## Open Questions

- Which frontend design defaults recur in this operator's own generated apps and should be explicitly avoided?
