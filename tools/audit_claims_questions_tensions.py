#!/usr/bin/env python3
"""Audit first-class claim, question, and tension pages."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
CLAIM_STATUSES = {"supported", "contested", "limited", "needs-review"}
QUESTION_STATUSES = {"open", "partially-answered", "answered", "needs-review"}
TENSION_STATUSES = {"active", "resolved", "needs-review"}


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, Any], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return {}, lines

    data: dict[str, Any] = {}
    key: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            data[key] = [] if value == "[]" or not value else unquote(value)
        elif key and line.strip().startswith("- "):
            current = data.setdefault(key, [])
            if not isinstance(current, list):
                current = [current]
                data[key] = current
            current.append(unquote(line.strip()[2:].strip()))
    return data, lines[end + 1 :]


def as_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def wiki_pages() -> list[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if ".obsidian" not in path.parts and not path.name.startswith(".")
    )


def page_id(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


def section_links(body: list[str], heading: str) -> list[str]:
    links: list[str] = []
    in_section = False
    target_heading = f"## {heading}"
    for line in body:
        if line.startswith("## "):
            in_section = line.strip() == target_heading
            continue
        if not in_section:
            continue
        links.extend(match.group(1).split("|", 1)[0].strip() for match in WIKILINK_RE.finditer(line))
    return links


def report(title: str, items: list[str]) -> None:
    print(f"## {title}")
    print()
    if not items:
        print("- None")
    else:
        for item in items:
            print(f"- {item}")
    print()


def main() -> int:
    source_without_sections: list[str] = []
    single_source_claims: list[str] = []
    tensions_without_links: list[str] = []
    open_questions_without_links: list[str] = []
    invalid_statuses: list[str] = []

    for path in wiki_pages():
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        page_type = str(frontmatter.get("type", "")).strip()
        rel = page_id(path)

        if page_type == "source":
            linked = (
                section_links(body, "Claims")
                + section_links(body, "Questions")
                + section_links(body, "Tensions")
            )
            if not linked:
                source_without_sections.append(rel)

        if page_type == "claim":
            status = str(frontmatter.get("claim_status", "")).strip()
            if status and status not in CLAIM_STATUSES:
                invalid_statuses.append(f"{rel}: invalid claim_status `{status}`")
            sources = as_list(frontmatter.get("sources", []))
            if len(sources) == 1:
                single_source_claims.append(f"{rel}: {sources[0]}")

        if page_type == "question":
            status = str(frontmatter.get("question_status", "")).strip()
            if status and status not in QUESTION_STATUSES:
                invalid_statuses.append(f"{rel}: invalid question_status `{status}`")
            related = as_list(frontmatter.get("related", []))
            if status == "open" and not related:
                open_questions_without_links.append(rel)

        if page_type == "tension":
            status = str(frontmatter.get("tension_status", "")).strip()
            if status and status not in TENSION_STATUSES:
                invalid_statuses.append(f"{rel}: invalid tension_status `{status}`")
            related_claims = as_list(frontmatter.get("related_claims", []))
            related_questions = as_list(frontmatter.get("related_questions", []))
            if not related_claims and not related_questions:
                tensions_without_links.append(rel)

    print("# Claims, Questions, and Tensions Audit")
    print()
    report("Source Pages With No Linked Claim/Question/Tension Sections", source_without_sections)
    report("Claim Pages With Only One Source", single_source_claims)
    report("Tensions With No Linked Claims Or Questions", tensions_without_links)
    report("Open Questions With No Related Links", open_questions_without_links)
    report("Invalid Claim/Question/Tension Status Values", invalid_statuses)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
