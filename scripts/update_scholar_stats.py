#!/usr/bin/env python3
"""Fetch Google Scholar profile metrics and write them to a Jekyll data file."""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_USER_ID = "8-tCnnUAAAAJ"
DEFAULT_OUTPUT = Path("_data/scholar.json")


def fetch_profile(user_id: str) -> str:
    url = f"https://scholar.google.com/citations?user={user_id}&hl=en"
    user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0 Safari/537.36"
    )
    request = Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")
    except (HTTPError, URLError, TimeoutError):
        curl = subprocess.run(
            ["curl", "-L", "-s", "-A", user_agent, url],
            check=True,
            capture_output=True,
            text=True,
            timeout=45,
        )
        return curl.stdout


def parse_int(value: str) -> int:
    return int(re.sub(r"[^\d]", "", html.unescape(value)))


def parse_metrics(page: str) -> dict[str, object]:
    values = [parse_int(value) for value in re.findall(r'<td class="gsc_rsb_std">([^<]+)</td>', page)]
    name_match = re.search(r'<div id="gsc_prf_in">([^<]+)</div>', page)

    if len(values) >= 5:
        citations, h_index, i10_index = values[0], values[2], values[4]
    else:
        meta_match = re.search(r"Cited by\s*([\d,]+)", html.unescape(page))
        if not meta_match:
            raise ValueError("Could not find Google Scholar metrics in the fetched page.")
        citations = parse_int(meta_match.group(1))
        h_index = None
        i10_index = None

    return {
        "name": html.unescape(name_match.group(1)).strip() if name_match else "Mengqi Zhang",
        "citations": citations,
        "h_index": h_index,
        "i10_index": i10_index,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": f"https://scholar.google.com/citations?user={DEFAULT_USER_ID}&hl=en",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user-id", default=DEFAULT_USER_ID)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args()

    output = Path(args.output)
    try:
        page = fetch_profile(args.user_id)
        metrics = parse_metrics(page)
        metrics["source"] = f"https://scholar.google.com/citations?user={args.user_id}&hl=en"
    except (HTTPError, URLError, TimeoutError, subprocess.SubprocessError, ValueError) as exc:
        print(f"Warning: failed to update Scholar metrics: {exc}", file=sys.stderr)
        if output.exists():
            print(f"Keeping existing metrics in {output}.")
            return 0
        print(f"No existing metrics file found at {output}.", file=sys.stderr)
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
