"""Refresh public Scholar totals; leave the previous snapshot intact on failure."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

URL = "https://scholar.google.com/citations?user=eZVEUCIAAAAJ&hl=en"
OUTPUT = Path(__file__).resolve().parents[1] / "_data/scholar.json"


def parse_metrics(html):
    table = re.search(r'<table\b[^>]*id="gsc_rsb_st"[^>]*>.*?</table>', html, re.S)
    if not table:
        raise ValueError("Scholar statistics table missing; previous metrics preserved")
    metrics = {}
    for label, key in [("Citations", "citations"), ("h-index", "h_index")]:
        for row in re.findall(r'<tr\b[^>]*>.*?</tr>', table.group(), re.S):
            if f'>{label}</a>' in row:
                cells = re.findall(r'<td class="gsc_rsb_std">([\d,]+)</td>', row)
                if cells:
                    metrics[key] = int(cells[0].replace(",", ""))
    if set(metrics) != {"citations", "h_index"}:
        raise ValueError("Incomplete Scholar metrics; previous metrics preserved")
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", type=Path, help="Use an already downloaded profile")
    args = parser.parse_args()
    if args.html:
        html = args.html.read_bytes().decode("utf-8", errors="replace")
    else:
        with urlopen(Request(URL, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as response:
            html = response.read().decode("utf-8", errors="replace")
    data = parse_metrics(html)
    data.update(source_url=URL, updated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    OUTPUT.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data))
