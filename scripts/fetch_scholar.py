"""Fetches citation metrics from OpenAlex via ORCID and writes data/scholar.json."""

import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

ORCID = "0000-0002-8804-0722"
OPENALEX_URL = f"https://api.openalex.org/authors/https://orcid.org/{ORCID}"
OUT = Path(__file__).parent.parent / "data" / "scholar.json"


def fetch():
    req = urllib.request.Request(OPENALEX_URL, headers={"User-Agent": "lcossu.github.io/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        author = json.loads(resp.read())

    stats = author.get("summary_stats", {})
    return {
        "hindex":   stats.get("h_index"),
        "citedby":  author.get("cited_by_count"),
        "i10index": stats.get("i10_index"),
        "updated":  str(date.today()),
    }


if __name__ == "__main__":
    try:
        data = fetch()
        OUT.write_text(json.dumps(data, indent=2) + "\n")
        print(f"OK — h-index={data['hindex']}, citedby={data['citedby']}, updated={data['updated']}")
    except Exception as exc:
        print(f"WARNING: fetch failed ({exc}); keeping existing data.", file=sys.stderr)
        sys.exit(0)
