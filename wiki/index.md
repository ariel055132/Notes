# Wiki Index

> Content catalog. Updated after every ingest, query, or lint operation.

## Entities

| Page | Summary | Sources | Status | Updated |
|------|---------|---------|--------|---------|
| [[anthropic]] | Anthropic is the AI company that publishes the prompting guide and develops the Claude model family. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[chatgpt]] | ChatGPT is one of the target model products for the practical prompt-engineering guide, which frames its recommendations as reusable across ChatGPT, Claude, and Gemini. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[claude]] | Claude is Anthropic's model family addressed by the Anthropic prompting guide and one of the target model products in Prompt Builder's practical prompt-engineering guide. [[2026-05-24--prompting-best-practices\|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 2 | active | 2026-05-24 |
| [[claude-haiku-4-5]] | Claude Haiku 4.5 is named in the source as part of the covered Claude model set and context-awareness discussion. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[claude-opus-4-6]] | Claude Opus 4.6 appears in the source mainly as a comparison and migration baseline for Claude Opus 4.7 behavior. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[claude-opus-4-7]] | Claude Opus 4.7 is presented as Anthropic's most capable generally available Claude model in the source, with guidance around effort, verbosity, tool use, subagents, writing style, and agentic work. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[claude-sonnet-4-6]] | Claude Sonnet 4.6 is discussed in the source as a Claude model with effort-level migration considerations and support for adaptive thinking workflows. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[gemini]] | Gemini is one of the target model products for the practical prompt-engineering guide, which presents its core prompt structure and testing workflow as applicable across Gemini, ChatGPT, and Claude. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[prompt-builder]] | Prompt Builder is the publisher of the practical prompt-engineering guide and related prompt-generator resources for ChatGPT, Claude, Gemini, Grok, prompt libraries, and model comparison. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |

## Concepts

| Page | Summary | Sources | Status | Updated |
|------|---------|---------|--------|---------|
| [[adaptive-thinking]] | Adaptive thinking is a Claude reasoning mode where the model dynamically decides whether and how much to reason based on task complexity and configured effort. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[agentic-systems]] | Agentic systems are workflows where a model pursues a task across multiple steps using tools, state tracking, verification, progress updates, and autonomy. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[chain-of-thought-prompting]] | Chain-of-thought prompting is asking a model to work through assumptions, intermediate reasoning, or calculations before producing an answer, especially for tasks where skipped steps can change the result. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[code-review-harnesses]] | Code review harnesses are prompt and evaluation setups that direct a model to inspect code, surface defects, and optionally separate finding coverage from later confidence or severity filtering. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[effort-parameter]] | The effort parameter is a Claude runtime setting used to trade off intelligence, latency, token spend, and reasoning depth for a task. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[few-shot-prompting]] | Few-shot prompting is the use of representative examples in a prompt to steer a model's output format, tone, structure, and edge-case behavior. [[2026-05-24--prompting-best-practices\|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 2 | active | 2026-05-24 |
| [[frontend-design-defaults]] | Frontend design defaults are recurring visual styles a model may produce without specific aesthetic direction, plus the prompt techniques used to steer toward a more fitting design. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[iterative-refinement]] | Iterative refinement is a prompt workflow where an output is drafted, evaluated against stated criteria, and then revised based on the review. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[long-context-prompting]] | Long context prompting is the practice of arranging large documents or data-rich inputs so the model can retrieve, ground, and reason over them effectively. [[2026-05-24--prompting-best-practices\|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 2 | active | 2026-05-24 |
| [[metacognitive-prompting]] | Metacognitive prompting asks a model to consider its assumptions, missing information, limitations, or uncertainty before giving a recommendation or answer. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[parallel-tool-calling]] | Parallel tool calling is the practice of running independent tool calls concurrently when their inputs and outputs do not depend on one another. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[power-prompt-framework]] | The POWER Prompt Framework is a practical prompt structure that combines Purpose, Output Format, Working Context, Examples, and Refinement Instructions to make model requests clearer and easier to evaluate. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[prompt-chaining]] | Prompt chaining is a workflow pattern where a sequence of prompts decomposes a larger task and each step uses the previous output as input for the next step. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[prompt-engineering]] | Prompt engineering is the practice of designing instructions, context, examples, constraints, roles, and output expectations so a model can produce reliable, useful, and repeatable responses. [[2026-05-24--prompting-best-practices\|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 2 | active | 2026-05-24 |
| [[prompt-testing-and-versioning]] | Prompt testing and versioning is the practice of storing reusable prompts, reviewing prompt changes, and evaluating prompt behavior against representative inputs and quality criteria over time. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[retrieval-augmented-generation]] | Retrieval-augmented generation is a prompting and system pattern where relevant source material is supplied to the model and the model is instructed to answer from that material. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |
| [[subagent-orchestration]] | Subagent orchestration is the practice of delegating independent workstreams to separate agent contexts when parallelism, isolation, or specialized focus is useful. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[tool-use]] | Tool use is the model behavior of invoking external capabilities to inspect state, search, read files, retrieve context, modify artifacts, run commands, or otherwise act beyond text generation. [[2026-05-24--prompting-best-practices\|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 2 | active | 2026-05-24 |
| [[xml-prompt-structure]] | XML prompt structure is the use of descriptive XML-style tags to separate instructions, context, examples, inputs, documents, metadata, and expected outputs inside a prompt. [[2026-05-24--prompting-best-practices\|Prompting best practices]] | 1 | active | 2026-05-24 |
| [[zero-shot-prompting]] | Zero-shot prompting is asking a model to perform a task using only instructions, context, constraints, and output requirements, without providing examples of the desired answer pattern. [[2025-06-13--prompt-engineering-in-2025-complete-guide\|Prompt Engineering in 2025]] | 1 | active | 2026-05-24 |

## Sources

| Page | Summary | Sources | Status | Updated |
|------|---------|---------|--------|---------|
| [[2025-06-13--prompt-engineering-in-2025-complete-guide]] | This source presents prompt engineering as a practical discipline for getting consistent, reusable outputs from models such as ChatGPT, Claude, and Gemini. It prioritizes a simple prompt structure: state the goal, provide working context, define constraints, and specify the output format. It explains core techniques such as zero-shot prompting, few-shot prompting, chain-of-thought prompting, retrieval-augmented generation, prompt chaining, and iterative refinement. It also treats prompts as assets that should be tested, versioned, reused, and evaluated for accuracy, format adherence, cost, and latency. | 0 | active | 2026-05-24 |
| [[2026-05-24--prompting-best-practices]] | Anthropic's guide presents prompt engineering as the practice of making instructions explicit, structured, contextual, and verifiable. Its most reusable guidance is to specify the desired output, provide motivation and context, use representative examples, separate prompt components with XML-style tags, and match the prompt's formatting to the desired answer style. The source also gives extensive operational guidance for tool-using and agentic systems: be explicit about when the model should act, use parallel tools when work is independent, calibrate thinking and effort to task complexity, maintain state across long workflows, and verify outputs before completion. Model-specific Claude guidance appears throughout, but this ingest emphasizes the general practices and the agentic/tool-use workflow patterns. | 0 | active | 2026-05-24 |

## Syntheses

| Page | Summary | Sources | Status | Updated |
|------|---------|---------|--------|---------|

## Statistics

- **Total pages**: 31
- **Total sources**: 2
- **Last updated**: 2026-05-24
