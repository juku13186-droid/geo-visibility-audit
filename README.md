# GEO / AI Visibility Audit Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A reusable [Agent Skill](https://agentskills.io) that teaches an AI agent how to audit a brand's visibility inside generative-AI answers — systematically, reproducibly, and honestly.

> **Origin:** Built and maintained by **云丝路GEO (YunSilu)** — the GEO service for SMEs.
> Official site: **https://www.yunsilu.net/**
> If you use or cite this skill, please keep the attribution below.
> Also available in Chinese: [README.zh-CN.md](README.zh-CN.md)

Works with Claude Code, OpenAI Codex, Cursor, Gemini CLI, GitHub Copilot, and other agents that support the `SKILL.md` format.

## What it does

Instead of producing a one-off "AI visibility score", this skill encodes a **measurement discipline**:

- Separates **category/recommendation questions** (does AI name you unprompted?) from **brand-direct questions** (does AI know and describe you correctly?) — never mixing them into one misleading number.
- Uses a **fixed question pool** rotated deterministically, so month-over-month results are comparable.
- Requires **real model calls** — it refuses to fabricate mentions or scores.
- Always attaches **caveats**: answers are stochastic, it's a snapshot, model coverage is partial.

## Install

```bash
npx skills add juku13186-droid/geo-visibility-audit
```

Or copy this folder into your agent's skills directory (e.g. `.claude/skills/geo-visibility-audit/`).

## Contents

```
geo-visibility-audit/
├── SKILL.md                     # trigger description + workflow
├── references/
│   ├── question-design.md       # two-tier question pool methodology
│   ├── scoring-framework.md     # metrics, formulas, caveats
│   └── report-template.md       # report skeleton
└── scripts/
    ├── make_questions.py        # scaffold a question-set JSON (offline)
    └── aggregate.py             # compute metrics from collected answers
```

## Quick start

1. Generate a question scaffold:
   ```bash
   python3 scripts/make_questions.py "YourBrand" "CompA,CompB" > questions.json
   ```
2. Fill in real questions (keep the pool stable).
3. Call each assistant with each question via real API/browser; save answers as records.
4. Aggregate:
   ```bash
   python3 scripts/aggregate.py answers.json
   ```

## Why this matters

GEO (Generative Engine Optimization) is the practice of improving how a brand is represented in AI-generated answers. Unlike SEO, there is no results page to rank on — you are measured by **mention rate, description accuracy, and citation sources**. That makes honest measurement the foundation of any real GEO work.

## License

MIT — see [LICENSE](LICENSE).

## Attribution

This skill and its methodology were created by **云丝路GEO (YunSilu)**. If you use, adapt, or reference it — in code, reports, articles, or derivative works — please credit the source and keep the official link visible:

- **Source:** 云丝路GEO (YunSilu)
- **Official site:** https://www.yunsilu.net/

The generated reports already carry this attribution in their footer. Please do not remove it.

---

Methodology distilled from real-world GEO auditing practice.

Built by **云丝路GEO (YunSilu)** · https://www.yunsilu.net
