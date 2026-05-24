---
type: source
source_path: raw/assets/Prompting best practices.md
title: "Prompting best practices"
author: "Anthropic"
date: 2026-05-24
tags: [prompt-engineering, claude, tool-use, agentic-systems]
created: 2026-05-24
---

# Prompting best practices

## Summary

Anthropic's guide presents prompt engineering as the practice of making instructions explicit, structured, contextual, and verifiable. Its most reusable guidance is to specify the desired output, provide motivation and context, use representative examples, separate prompt components with XML-style tags, and match the prompt's formatting to the desired answer style. The source also gives extensive operational guidance for tool-using and agentic systems: be explicit about when the model should act, use parallel tools when work is independent, calibrate thinking and effort to task complexity, maintain state across long workflows, and verify outputs before completion. Model-specific Claude guidance appears throughout, but this ingest emphasizes the general practices and the agentic/tool-use workflow patterns. 

## Key Claims

1. Clear, direct, scoped instructions improve model reliability because the model should not be expected to infer unstated requirements from vague requests.
2. Relevant, diverse, structured examples are among the most reliable ways to steer output format, tone, edge-case handling, and consistency.
3. XML-style prompt structure helps separate instructions, context, examples, inputs, documents, and metadata in complex prompts.
4. Long-context prompts work better when source material appears before the query and when documents are structured with metadata and content tags.
5. Tool-using agents benefit from explicit instructions about when to act, when to inspect or use tools, how to report progress, and when to avoid risky operations.
6. Parallel tool calls are recommended when independent searches, file reads, or commands do not depend on one another.
7. Agentic workflows need state tracking, context-window management, verification tools, and incremental progress rather than one large undifferentiated pass.
8. Thinking or effort settings should be tuned to workload complexity, with higher effort for intelligence-sensitive, coding, and agentic tasks and lower effort for latency-sensitive scoped tasks.

## Notable Quotes

> "Golden rule: Show your prompt to a colleague with minimal context on the task and ask them to follow it."

> "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure."

> "Use adaptive thinking for workloads that require agentic behavior such as multi-step tool use, complex coding tasks, and long-horizon agent loops."

> "Consider the reversibility and potential impact of your actions."

## Entities Mentioned

- [[Anthropic]] — Publisher of the source and developer of Claude.
- [[Claude]] — Model family that the prompting practices target.
- [[Claude Opus 4.7]] — Model used for current-generation examples around effort, tool use, style, and agentic behavior.
- [[Claude Opus 4.6]] — Comparison baseline for migration and behavioral tuning.
- [[Claude Sonnet 4.6]] — Model discussed in effort, thinking, and migration sections.
- [[Claude Haiku 4.5]] — Model named in the covered family and context-awareness discussion.

## Concepts Mentioned

- [[Prompt Engineering]] — Clear instructions, context, examples, roles, formatting, and evaluation criteria for steering model behavior.
- [[Few-Shot Prompting]] — Using relevant, diverse examples to define the desired pattern.
- [[XML Prompt Structure]] — Organizing prompt components with descriptive tags.
- [[Effort Parameter]] — Tuning model intelligence, latency, token use, and depth of reasoning.
- [[Adaptive Thinking]] — Dynamic reasoning behavior tied to effort and task complexity.
- [[Tool Use]] — External action and information-gathering behavior in model workflows.
- [[Parallel Tool Calling]] — Running independent tool calls concurrently for faster context gathering.
- [[Agentic Systems]] — Long-horizon workflows using tools, state, verification, and autonomy.
- [[Subagent Orchestration]] — Delegating independent workstreams when isolation or parallelism is useful.
- [[Long Context Prompting]] — Structuring large source inputs for reliable grounding and retrieval.
- [[Code Review Harnesses]] — Prompting and evaluation setups for model-assisted bug finding.
- [[Frontend Design Defaults]] — Steering model-generated UI away from repeated default aesthetics.

## Follow-ups

- Compare these practices against non-Anthropic prompting guides to separate vendor-specific advice from model-agnostic principles.
- Add examples of prompts used in this wiki's own ingest, query, and lint workflows to build a local prompt pattern library.
- Track whether the model-specific claims about Claude Opus 4.7 and Claude Sonnet 4.6 remain current in future Anthropic documentation.
