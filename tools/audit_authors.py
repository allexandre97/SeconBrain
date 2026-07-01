#!/usr/bin/env python3
"""Audit structured author metadata on wiki source pages."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "[]":
        return []
    if value in {"true", "false"}:
        return value == "true"
    return unquote(value)


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
            data[key] = parse_scalar(value) if value else []
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


def h1(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def clean_wikilink(value: str) -> str:
    match = WIKILINK_RE.search(value)
    if match:
        return match.group(1).split("|", 1)[0].strip()
    return value.strip()


def normalize_name(value: str) -> str:
    value = clean_wikilink(value)
    value = re.sub(r"[^a-z0-9]+", " ", value.casefold())
    return " ".join(value.split())


def normalize_tag(value: str) -> str:
    value = value.casefold().replace("-", " ").replace("_", " ")
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


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
    source_missing_authors: list[str] = []
    sources_authors_no_year: list[str] = []
    source_author_tags: list[str] = []
    entity_mismatches: list[str] = []
    author_sources: dict[str, set[str]] = defaultdict(set)
    author_display: dict[str, str] = {}
    author_entity_links: dict[str, set[str]] = defaultdict(set)
    author_entity_pages: list[tuple[Path, dict[str, Any], list[str]]] = []

    for path in wiki_pages():
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        page_type = str(frontmatter.get("type", "")).strip()
        rel = page_id(path)

        if page_type == "source":
            source_id = str(frontmatter.get("source_id", "")).strip() or rel
            authors = as_list(frontmatter.get("authors", []))
            if not authors:
                source_missing_authors.append(rel)
            elif not str(frontmatter.get("year", "")).strip():
                sources_authors_no_year.append(rel)

            for author in authors:
                normalized = normalize_name(author)
                if normalized:
                    author_sources[normalized].add(source_id)
                    author_display.setdefault(normalized, author)

            author_name_set = {normalize_name(author) for author in authors}
            for tag in as_list(frontmatter.get("tags", [])):
                if normalize_tag(tag) in author_name_set:
                    source_author_tags.append(f"{rel}: tag `{tag}` matches an author name")

            for entity in as_list(frontmatter.get("author_entities", [])):
                entity_target = clean_wikilink(entity)
                if entity_target:
                    author_entity_links[entity_target].add(source_id)

        if page_type == "entity" and str(frontmatter.get("entity_type", "")).strip() == "author":
            author_entity_pages.append((path, frontmatter, body))

    multiple_authors = [
        f"{author_display[name]}: {', '.join(sorted(sources))}"
        for name, sources in sorted(author_sources.items(), key=lambda item: author_display[item[0]].casefold())
        if len(sources) > 1
    ]

    for path, frontmatter, body in author_entity_pages:
        rel = page_id(path)
        declared_sources = set(as_list(frontmatter.get("sources", [])))
        aliases = {normalize_name(alias) for alias in as_list(frontmatter.get("aliases", []))}
        aliases.add(normalize_name(h1(body) or path.stem.replace("-", " ")))
        expected_sources: set[str] = set()
        for alias in aliases:
            expected_sources.update(author_sources.get(alias, set()))
        expected_sources.update(author_entity_links.get(rel, set()))

        if declared_sources != expected_sources:
            entity_mismatches.append(
                f"{rel}: frontmatter sources {sorted(declared_sources)}; expected {sorted(expected_sources)}"
            )

    print("# Author Metadata Audit")
    print()
    report("Source Pages Missing Authors", source_missing_authors)
    report("Source Pages With Authors But No Year", sources_authors_no_year)
    report("Authors Appearing In Multiple Sources", multiple_authors)
    report("Author Entity Source Mismatches", entity_mismatches)
    report("Source Pages Using Author Names As Tags", source_author_tags)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
