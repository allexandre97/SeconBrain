#!/usr/bin/env python3
"""Search wiki Markdown files with compact text snippets."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
SNIPPET_CHARS = 160
MAX_SNIPPETS_PER_FILE = 3


def wiki_files() -> list[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(WIKI_DIR).parts)
    )


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def snippet(text: str, start: int, end: int) -> str:
    midpoint = (start + end) // 2
    left = max(0, midpoint - SNIPPET_CHARS // 2)
    right = min(len(text), left + SNIPPET_CHARS)
    left = max(0, right - SNIPPET_CHARS)
    prefix = "..." if left > 0 else ""
    suffix = "..." if right < len(text) else ""
    return prefix + compact(text[left:right]) + suffix


def find_matches(path: Path, terms: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lower_text = text.lower()
    snippets: list[str] = []
    seen: set[str] = set()

    for term in terms:
        lower_term = term.lower()
        start = 0
        while len(snippets) < MAX_SNIPPETS_PER_FILE:
            index = lower_text.find(lower_term, start)
            if index == -1:
                break
            item = snippet(text, index, index + len(term))
            if item not in seen:
                snippets.append(item)
                seen.add(item)
            start = index + max(1, len(term))

    return snippets


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search Markdown files under wiki/ and print compact snippets."
    )
    parser.add_argument("terms", nargs="+", help="One or more case-insensitive search terms")
    args = parser.parse_args()

    if not WIKI_DIR.is_dir():
        print("ERROR: wiki/ directory not found", file=sys.stderr)
        return 1

    terms = [term for term in args.terms if term.strip()]
    if not terms:
        print("ERROR: provide at least one non-empty query term", file=sys.stderr)
        return 2

    found = 0
    for path in wiki_files():
        snippets = find_matches(path, terms)
        if not snippets:
            continue

        found += 1
        print(path.relative_to(ROOT).as_posix())
        for item in snippets:
            print(f"  - {item}")

    if found == 0:
        print("No matches found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
