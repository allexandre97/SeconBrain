#!/usr/bin/env python3
"""Suggest missing wiki categories from registry match terms."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
REGISTRY = ROOT / "schema" / "category_registry.md"
PAGE_TYPES = {"source", "concept", "answer", "question", "overview"}
CATEGORY_RE = re.compile(r"^- `([^`]+)`")
TERMS_RE = re.compile(r"^\s+- Match terms:\s*(.+)$")
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")


@dataclass(frozen=True)
class CategoryRule:
    category: str
    terms: tuple[str, ...]


@dataclass(frozen=True)
class Suggestion:
    page: Path
    label: str
    category: str
    matched_terms: tuple[str, ...]


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def split_frontmatter(text: str) -> tuple[dict[str, object], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return {}, lines

    data: dict[str, object] = {}
    key: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "[]":
                data[key] = []
            elif value:
                data[key] = unquote(value)
            else:
                data[key] = []
        elif key and line.strip().startswith("- "):
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(unquote(line.strip()[2:].strip()))
    return data, lines[end + 1 :]


def as_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def h1(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def summary_section(lines: list[str]) -> str:
    capture = False
    selected: list[str] = []
    for line in lines:
        if line.startswith("## "):
            capture = line.strip().casefold() == "## summary"
            continue
        if capture and line.startswith("## "):
            break
        if capture:
            selected.append(line)
    return "\n".join(selected)


def concept_links(lines: list[str]) -> str:
    links: list[str] = []
    for match in WIKILINK_RE.finditer("\n".join(lines)):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0]
        if "/concepts/" in target or target.startswith("wiki/concepts/"):
            links.append(target.rsplit("/", 1)[-1].replace("-", " "))
    return " ".join(links)


def headings(lines: list[str]) -> str:
    return "\n".join(line.lstrip("#").strip() for line in lines if line.startswith("#"))


def page_label(path: Path, frontmatter: dict[str, object], body: list[str]) -> str:
    for key in ("short_title", "display_title"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return h1(body) or path.stem.replace("-", " ").title()


def evidence_text(frontmatter: dict[str, object], body: list[str]) -> str:
    parts: list[str] = []
    for key in ("display_title", "short_title", "summary"):
        value = frontmatter.get(key)
        if isinstance(value, str):
            parts.append(value)
    for key in ("aliases", "tags"):
        parts.extend(as_list(frontmatter.get(key, [])))
    parts.append(summary_section(body))
    parts.append(headings(body))
    parts.append(concept_links(body))
    return "\n".join(parts)


def registry_rules() -> list[CategoryRule]:
    rules: list[CategoryRule] = []
    current: str | None = None
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        category_match = CATEGORY_RE.match(line)
        if category_match:
            current = category_match.group(1)
            continue
        terms_match = TERMS_RE.match(line)
        if current and terms_match:
            terms = tuple(term.strip() for term in terms_match.group(1).split(",") if term.strip())
            rules.append(CategoryRule(current, terms))
            current = None
    return rules


def term_pattern(term: str) -> re.Pattern[str]:
    escaped = re.escape(term)
    if term[0].isalnum() and term[-1].isalnum():
        return re.compile(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])", re.IGNORECASE)
    return re.compile(escaped, re.IGNORECASE)


def matched_terms(text: str, terms: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(term for term in terms if term_pattern(term).search(text))


def wiki_pages() -> list[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if ".obsidian" not in path.parts
        and "categories" not in path.relative_to(WIKI_DIR).parts
        and "dashboards" not in path.relative_to(WIKI_DIR).parts
    )


def suggestions() -> list[Suggestion]:
    rules = registry_rules()
    results: list[Suggestion] = []
    for path in wiki_pages():
        frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
        page_type = str(frontmatter.get("type", "")).strip()
        if page_type not in PAGE_TYPES:
            continue
        if str(frontmatter.get("graph_exclude", "")).strip().casefold() == "true":
            continue
        categories = set(as_list(frontmatter.get("categories", [])))
        text = evidence_text(frontmatter, body)
        for rule in rules:
            if rule.category in categories:
                continue
            matches = matched_terms(text, rule.terms)
            if matches:
                results.append(Suggestion(path, page_label(path, frontmatter, body), rule.category, matches))
    return results


def main() -> int:
    results = suggestions()
    if not results:
        print("No missing category suggestions.")
        return 0

    print("Missing category suggestions:")
    current_page: Path | None = None
    for item in sorted(results, key=lambda s: (s.page.as_posix(), s.category)):
        if item.page != current_page:
            current_page = item.page
            print(f"\n{item.page.relative_to(ROOT).as_posix()} - {item.label}")
        terms = ", ".join(item.matched_terms)
        print(f"- {item.category} (matched: {terms})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
