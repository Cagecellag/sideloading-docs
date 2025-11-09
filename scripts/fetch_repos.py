#!/usr/bin/env python3
"""Fetch the remote IPA-Sources.md and write it to docs/side/repos.md.

Run this before `mkdocs build` so the docs/side/repos.md is present for the build.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

URL = (
    "https://gist.githubusercontent.com/ongkiii/b40620d8d4a98ab17642858dce4cb2ec/raw/"
    "04031ccf177079e8730cdf77664ec685886d915e/IPA-Sources.md"
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "side" / "repos.md"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    req = Request(URL, headers={"User-Agent": "fetch-repos-script"})
    try:
        with urlopen(req) as r:
            data = r.read()
    except HTTPError as e:
        print(f"HTTP error: {e.code} {e.reason}", file=sys.stderr)
        return 2
    except URLError as e:
        print(f"URL error: {e.reason}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 2

    OUT.write_bytes(data)
    print(f"Wrote {OUT}")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
