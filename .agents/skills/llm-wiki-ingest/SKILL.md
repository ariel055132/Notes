---
name: llm-wiki-ingest
description: Parse, summarize and import local PDFs, saved articles or video reports into Notes from a file path, retaining evidence and linking related knowledge.
---

# Notes document analysis and import

A file path is enough to invoke this workflow. Read the repository's [AGENTS.md](../../../AGENTS.md) and [README.md](../../../README.md); run its tools from the Notes root containing this skill.

## Input and defaults

In the Codex conversation, the operator can enter:

```text
$llm-wiki-ingest "/Users/adrianli/Downloads/document.pdf"
```

An optional focus can follow the path, such as `重點：如何用在工作上的知識管理`. Accept absolute paths or paths relative to the user's working directory. Files may stay in Downloads or another readable location; no staging folder or move is required. Process only the selected file(s), not their whole folder.

Supported inputs are PDF, Markdown, UTF-8 text, saved HTML and completed video analysis reports. For another format, explain the needed conversion rather than feeding binary content to the text importer. A URL alone is not a local file input; the importer does not fetch websites or media.

Default to Traditional Chinese analysis and local Notes ingestion: explain the central question, key claims and supporting evidence, useful applications, limitations and relevant existing notes. Respect another language or focus supplied by the operator. Do not require a topic questionnaire when a path is the only input; ask only for a missing/unreadable/ambiguous path or information that materially blocks the requested work. Do not invent the operator's personal reflection or commitment.

## Complete the import

1. **Identify the source and interpreter.** Check `inbox/sources.json` and existing source cards. Reuse the known `source_id` and canonical URL for the same work; a matching snapshot hash or recorded upstream path can identify a moved local file. Do not merge unrelated works merely because titles match. Use `--existing-page` for an already curated, unregistered source. For PDFs, check that the selected Python can import `pdfplumber` and use that interpreter for the importer. Prefer an existing project/runtime environment; if needed, create a project `.venv` and install `requirements-pdf.txt` under the current execution permissions.
2. **Snapshot and extract.** Run `scripts/import_source.py add INPUT` with available source metadata. Preserve originals. The tool creates immutable `raw/imports/` snapshots, full `derived/` evidence and registry state. These evidence files are local and gitignored. Unknown author/date/URL remain unknown; do not substitute capture date for publication. If `changed:false`, inspect the existing card: unfinished cards still need analysis; a complete reviewed card can be reused and supplemented for the user's focus. Use `--reextract` only when the extraction needs refreshing, including after fixing a blocked extractor.
3. **Read and verify.** Read the full extraction, not just the opening preview, and its warnings. For PDFs, render and inspect relevant original pages, tables and figures with available PDF tools; text-layer success does not prove complete evidence. Record page/section locators and gaps. Retain `needs-review` or `blocked` for unresolved extraction problems; do not infer missing visual content.
4. **Write the source summary.** Complete the source card using AGENTS.md's required headings. Include a concise overview, key claims with evidence, applicable situations and limitations; preserve existing useful content and operator-authored views. Remove `REVIEW_REQUIRED` only after reading and curating the card. Direct quotes must match the source; mark translations. Preserve upstream video coverage and `secondary-summary`; short web reading notes remain `source-notes`, not an original article. Keep source claims and assistant inference distinct.
5. **Connect and record review.** Find related notes with `scripts/wiki_qa_bot.py` and the index, then read matches before linking or updating useful concepts. Create/update a synthesis only when it adds a meaningful comparison; incidental nouns need no new pages. Use `scripts/import_source.py review SOURCE_ID --status ... --note ...` to record the actual reviewed scope. Acknowledge warnings only after examining the affected evidence. `ready` means the recorded scope was reviewed, not that all author claims are true; blocked extraction requires usable evidence before promotion.
6. **Maintain and verify.** Rebuild the index after manual Wiki edits, append a log entry for manual syntheses, and run index `--check`, strict schema validation and log validation as documented in README.md. The importer logs import/review operations. Do not silently overwrite operator edits or publish/schedule anything as part of ingestion.

## Delivery

Return a short Traditional Chinese summary of what the document contributes, links to the source card and any synthesis changed, the processing status, and material uncertainties with affected pages/sections. If the file was already fully processed, link its existing result and explain any additions. Finish the local workflow rather than handing the operator Python commands to run themselves.
