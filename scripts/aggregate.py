#!/usr/bin/env python3
"""Aggregate collected AI-answer records into per-question-type metrics.

Input JSON: {"records": [ {date, question_type, model, mentions:[...], accurate:bool, citations:[...]} ]}
Output: text report to stdout. No fabricated values — only counts what is present.

Usage:
  python3 aggregate.py answers.json
"""
import json, sys
from collections import Counter, defaultdict


def pct(n, d):
    return f"{n}/{d} ({100.0*n/d:.1f}%)" if d else "0/0 (n/a)"


def main():
    if len(sys.argv) < 2:
        print("Usage: aggregate.py answers.json", file=sys.stderr)
        sys.exit(1)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    recs = data.get("records", []) if isinstance(data, dict) else data
    if not recs:
        print("No records found.")
        return

    brands = sorted({b for r in recs for b in r.get("mentions", [])})
    types = sorted({r.get("question_type", "industry") for r in recs})

    print(f"Total answers: {len(recs)} | Brands seen: {brands}")
    for qtype in types:
        sub = [r for r in recs if r.get("question_type", "industry") == qtype]
        print("\n" + "=" * 56)
        print(f"[{qtype}] {len(sub)} answers")
        for b in brands:
            m = sum(1 for r in sub if b in r.get("mentions", []))
            print(f"  {b:20} mentioned {pct(m, len(sub))}")
        # share of voice
        total_mentions = sum(len(r.get("mentions", [])) for r in sub)
        if total_mentions:
            print("  Share of voice:")
            c = Counter(b for r in sub for b in r.get("mentions", []))
            for b, n in c.most_common():
                print(f"    {b:20} {100.0*n/total_mentions:.1f}%")
        # accuracy (tier B)
        if qtype == "brand":
            acc = sum(1 for r in sub if r.get("accurate") is True)
            judged = sum(1 for r in sub if r.get("accurate") is not None)
            print(f"  Accuracy (judged {judged}): {pct(acc, judged)}")
        # per model
        print("  Per model:")
        for model, n in Counter(r.get("model", "?") for r in sub).most_common():
            print(f"    {model:16} {n} answers")
        # citation sources
        cites = Counter(dom for r in sub for dom in r.get("citations", []))
        if cites:
            print("  Top citation sources:")
            for dom, n in cites.most_common(8):
                print(f"    {dom:32} {n}")

    print("\n" + "=" * 56)
    print("Caveats: stochastic answers; single snapshot; partial model coverage.")
    print("Tier A = unprompted presence (real GEO signal). Tier B = knowledge/accuracy, NOT recommendation rate.")


if __name__ == "__main__":
    main()
