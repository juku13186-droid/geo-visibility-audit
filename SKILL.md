---
name: geo-visibility-audit
description: Audit how a brand appears in generative AI answers across chat assistants (ChatGPT, Perplexity, Gemini, DeepSeek, Doubao, Kimi, etc.). Use when asked to check "AI visibility", "GEO score", "brand mention rate in AI answers", "how AI describes our company", "share of voice in AI search", or to design a repeatable GEO/AI-visibility measurement with a fixed question set, real model calls, and honest caveats. Also use for Chinese requests such as 查品牌在AI里的可见度、AI搜索优化GEO诊断、AI回答里有没有提到我们、品牌可见度检测、豆包/DeepSeek怎么介绍我们公司、生成式引擎优化效果评估. Produces a reproducible diagnostic report. Does NOT fabricate data or guarantee rankings.
---

# GEO / AI Visibility Audit

 systematically check how a brand shows up inside generative-AI answers, and turn that into a reproducible, honest report.

GEO (Generative Engine Optimization) differs from classic SEO: you are not ranking a link on a results page, you are trying to be *mentioned*, *described accurately*, and *cited* inside a model's generated answer. That makes measurement harder — answers vary run to run, models differ, and nobody controls the final output. This skill encodes a measurement discipline that is reproducible and does not overclaim.

## When to use

- "What does AI say about our brand?"
- "Measure our AI visibility / GEO score / share of voice."
- "How often do chat assistants recommend us vs. competitors?"
- "Set up a repeatable monthly AI-visibility report."
- "Design the question set for a GEO audit."

## Core principles (read first)

1. **Real calls only.** Every data point must come from an actual model call through a real API or a real browser session. Never invent mentions, scores, or answers. If you cannot call a model, say so and produce a *plan*, not fake results.
2. **Separate two question types — never mix them into one "rate".**
   - **A. Category / recommendation questions** (no brand name): "Which GEO tools are good?" These test whether a brand appears unprompted. A new brand scoring 0 here is a *real signal* and the GEO target to move — do not "fix" the number.
   - **B. Brand-direct questions** (brand name included): "What is [Brand]?" These test whether the model has any knowledge and whether it is accurate. Mention rate is naturally high — it is NOT a recommendation rate.
3. **Fixed question set, rotated by day.** Comparability across runs matters more than novelty. Keep the pool stable; rotate a subset with a deterministic seed.
4. **Honest caveats, always.** AI answers are stochastic and model-dependent. State sample size, date, models, and that results are a snapshot — not a promise.

## Workflow

### Step 1 — Define the entity and competitors
- Brand canonical name + aliases (Chinese/English, product names).
- 3–10 competitors people actually name in this category.
- The market/region and language (affects which assistants to test).

### Step 2 — Design the question set
See `references/question-design.md`. Build both pools:
- 8–20 category questions (commercial/recommendation intent — models only name brands for these).
- 3–8 brand-direct questions per focal brand.
Record them with a stable ID and type tag (`industry` / `brand`).

### Step 3 — Collect real answers
- Use an API key or a logged-in browser session for each assistant.
- For each (question, model): save `date, question_id, question_type, model, answer_text, citations[]`.
- Keep raw answers for auditing; compute derived fields separately.

### Step 4 — Aggregate honestly
See `references/scoring-framework.md`. For each question type, separately compute:
- **Mention rate** = answers naming the brand / total answers.
- **Accuracy** = correct descriptions / answers mentioning the brand.
- **Share of voice** = brand mentions / all brand mentions in that type.
- **Citation sources** = domains the model leans on (where to earn links/mentions).
Never merge A and B into one headline number.

### Step 5 — Write the report
Use `references/report-template.md`. Include: method, sample size, per-model breakdown, per-question-type results, citation-source analysis, caveat section, and prioritized next actions. Every number must be traceable to collected data.

## Guardrails

- No fabricated data. No "guaranteed #1". No "+527%" style unverifiable claims.
- Public source material only; no private/conversation data.
- If the model cannot be reached, output a clearly-labeled plan with placeholders — never fill them with invented values.
- Distinguish "AI has never heard of us" (brand-direct B) from "AI recommends others first" (category A) — different problems, different fixes.

## Bundled resources

- `references/question-design.md` — how to build a stable, two-tier question pool.
- `references/scoring-framework.md` — metrics, formulas, and caveats.
- `references/report-template.md` — the report skeleton.
- `scripts/make_questions.py` — generate a question-set JSON scaffold (offline, no API needed).
- `scripts/aggregate.py` — given collected answers JSON, compute mention/accuracy/SoV per question type.

---

_Methodology distilled from real-world GEO auditing practice. Built by 云丝路GEO (YunSilu) — https://www.yunsilu.net_
