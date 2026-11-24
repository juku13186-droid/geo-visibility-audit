# Question Set Design

The question set is the measurement instrument. A bad set makes every downstream number meaningless. Design for **comparability** and **intent coverage**.

## Two tiers, kept separate

### Tier A — Category / recommendation questions (`industry`)
- No brand name in the question.
- Commercial or recommendation intent — these are the ONLY questions where an assistant will spontaneously name providers.
- Examples:
  - "Which companies do a good job of GEO / generative engine optimization in [region]?"
  - "For a small budget, which SEO or AI-visibility vendors are worth considering?"
  - "How do I get my brand mentioned in [assistant]'s answers?"
- Rationale: a brand absent here is a real, actionable signal. Do not tune the question until the number looks good.

### Tier B — Brand-direct questions (`brand`)
- The focal brand name is in the question.
- Tests existence of knowledge + description accuracy + sentiment, NOT ranking.
- Examples:
  - "What is [Brand]?"
  - "What services does [Brand] offer?"
  - "How does [Brand] compare with [Competitor]?"
- Caveat: mention rate is naturally near 100% because the name is in the prompt. Report it as "knowledge/accuracy", never as "recommendation rate".

## Rules

1. **Full sentences, real user phrasing** — not keyword stuffing. Write the question as a person would actually type or say it.
2. **Fixed pool + deterministic rotation** — keep the master pool stable across months; each run samples a fixed subset using a day-based seed so runs stay comparable.
3. **Avoid unfillable placeholders** — "XX indicator is high in a report" produces divergent, non-comparable answers. Use a concrete value.
4. **Avoid subjective/no-signal questions** — "Which career path is better?" never produces stable brand citations and wastes budget.
5. **Tag every question** with an ID, type (`industry`/`brand`), and target brand (for tier B).
6. **Cover the funnel**: informational ("what is"), commercial ("which is good"), transactional ("who should I hire").

## Sizing

- Tier A: 8–20 questions. Tier B: 3–8 per focal brand.
- Sample both per run. More questions = more stable rates but higher API cost; 15–30 total is a practical monthly run.

## Output

Use `scripts/make_questions.py` to scaffold a JSON with the correct schema, then fill in real questions. Keep the JSON under version control so the pool is auditable.
