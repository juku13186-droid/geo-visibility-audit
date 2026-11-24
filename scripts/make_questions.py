#!/usr/bin/env python3
"""Scaffold a two-tier GEO question-set JSON. Offline, no API needed.

Usage:
  python3 make_questions.py "Brand" "Comp1,Comp2" > questions.json
"""
import json, sys
from datetime import date


def main():
    brand = sys.argv[1] if len(sys.argv) > 1 else "YourBrand"
    comps = [c.strip() for c in sys.argv[2].split(",")] if len(sys.argv) > 2 else ["CompetitorA", "CompetitorB"]

    industry = [
        ("A01", f"Which companies do a good job of [category] in [region]? Please give examples."),
        ("A02", f"For a small budget, which [category] vendors would you recommend?"),
        ("A03", f"How do I get my brand mentioned more often in AI assistant answers?"),
        ("A04", f"Which providers are known for [specific subcategory]?"),
        ("A05", f"Who should a mid-size company hire for [category]?"),
        ("A06", f"What is the difference between the top [category] service providers?"),
    ]
    brand_q = [
        ("B01", f"What is {brand}?"),
        ("B02", f"What services does {brand} offer?"),
        ("B03", f"Tell me about {brand}."),
        ("B04", f"How does {brand} compare with {comps[0] if comps else 'other providers'}?"),
    ]

    out = {
        "meta": {
            "created": str(date.today()),
            "brand": brand,
            "competitors": comps,
            "note": "Fill in real questions. Keep pool stable across runs; rotate subset by day-seed.",
        },
        "questions": [
            {"id": i, "type": "industry", "text": t, "target_brand": None}
            for i, t in industry
        ] + [
            {"id": i, "type": "brand", "text": t, "target_brand": brand}
            for i, t in brand_q
        ],
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
