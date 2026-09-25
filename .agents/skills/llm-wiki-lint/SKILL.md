---
name: llm-wiki-lint
description: Check Notes indexing, provenance, review status and semantic consistency; distinguish deterministic validation from factual review.
---

# Notes health check

Read `AGENTS.md`. Run the read-only checks first:

```sh
python3 scripts/rebuild_index.py --check
python3 scripts/lint_schema.py --strict
python3 scripts/validate_log.py
```

For the requested scope, inspect broken links, outdated claims, contradictions, source provenance, missing evidence, and useful navigation links. A passing schema check does not verify factual truth or diagram/table extraction. Source counts are generated from distinct directly referenced source identities, not from stale frontmatter hints.

Report concrete findings with file/section, severity and the evidence for the finding. Distinguish full scans from sampled semantic checks. Fix issues already covered by the operator's authorization; ask only for changes outside it. Do not create every missing noun as a page. Never resolve a contradiction by silently deleting the older claim or its source.

Preserve raw documents and user judgments. No bulk/recursive deletion. After actual changes rebuild/check the index, validate schema/log, run relevant tests, and append an operation entry. A read-only assessment needs no fabricated edit history or recurring automation.
