"""Fetches h-index and citation count from Google Scholar and writes data/scholar.json."""

import json
import sys
from datetime import date
from pathlib import Path

SCHOLAR_ID = "QYEOj6wAAAAJ"
OUT = Path(__file__).parent.parent / "data" / "scholar.json"


def fetch():
    from scholarly import scholarly

    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics"])

    return {
        "hindex":   author.get("hindex"),
        "citedby":  author.get("citedby"),
        "i10index": author.get("i10index"),
        "updated":  str(date.today()),
    }


if __name__ == "__main__":
    try:
        data = fetch()
        OUT.write_text(json.dumps(data, indent=2) + "\n")
        print(f"OK — h-index={data['hindex']}, citedby={data['citedby']}, updated={data['updated']}")
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
