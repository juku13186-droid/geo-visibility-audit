# Scoring Framework

Compute every metric **per question type**. Never roll Tier A and Tier B into one headline number.

## Inputs

Each collected answer is a record:
```json
{
  "date": "2026-11-24",
  "question_id": "A03",
  "question_type": "industry",     // or "brand"
  "model": "deepseek",
  "answer_text": "...",
  "mentions": ["BrandA", "BrandB"],   // brands actually named
  "accurate": true,                    // only meaningful for tier B focal brand
  "citations": ["example.com", "..."]  // domains cited/linked
}
```

## Metrics (per question type)

- **Mention rate** = count(answers where brand ∈ mentions) / count(answers). Report with the raw fraction, e.g. `3/38 (7.9%)`.
- **Accuracy rate** (tier B) = count(mentions where description correct) / count(answers mentioning brand). Requires human or rubric judgment — state the rubric.
- **Share of voice (SoV)** = brand mentions / total mentions of all tracked brands in that slice. Shows relative presence, not absolute quality.
- **Citation sources** = frequency of each cited domain. These are the domains that actually influence answers — the real GEO outreach targets.
- **Per-model breakdown** — always show models separately; assistants differ radically.

## Dimensions you can score (0–100), if the user wants a single score

Only compute these when data supports them; otherwise mark N/A. A composite score is optional and must show its inputs.

| Dimension | Meaning |
|---|---|
| Discoverability | Brand appears in category recommendations (Tier A mention rate) |
| Understanding | Tier B accuracy — described correctly |
| Mention rate | Headline presence in tracked answers |
| Recommendation rate | Positive/推荐 framing when named |
| Citation rate | Brand's own domains cited as sources |
| Authority | Quality/authority of citing domains |
| Share of voice | Relative share vs tracked competitors |
| Brand accuracy | Absence of wrong/hallucinated claims |

## Caveats — put these in every report

- AI answers are stochastic: same question, same model, different runs → different output. Rates are estimates over a sample.
- A snapshot, not a trend: need ≥2–3 runs over weeks before calling a movement a trend.
- Model coverage is partial: you test the assistants you can reach, not the whole market.
- 0 mentions in Tier A is a valid finding, not a measurement failure.
- No metric here is a guarantee of future AI behavior or ranking.
