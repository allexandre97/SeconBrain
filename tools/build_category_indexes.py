#!/usr/bin/env python3
"""Build deterministic category and dashboard pages from wiki frontmatter."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
CATEGORY_DIR = WIKI_DIR / "categories"
DASHBOARD_DIR = WIKI_DIR / "dashboards"
GENERATED_DATE = "2026-06-30"
INDEXED_TYPES = ("source", "concept", "answer", "question", "tension", "claim", "entity")
TYPE_HEADINGS = {
    "source": "Sources",
    "concept": "Concepts",
    "answer": "Answers",
    "question": "Questions",
    "tension": "Tensions",
    "claim": "Claims",
    "entity": "Entities",
}


@dataclass(frozen=True)
class Page:
    path: Path
    page_type: str
    label: str
    categories: tuple[str, ...]
    coverage_profile: str = ""
    source_id: str = ""
    cites_sources: tuple[str, ...] = ()
    citation_match_status: str = ""


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


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def wiki_pages() -> list[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if ".obsidian" not in path.parts
        and path.name != "README.md"
        and "categories" not in path.relative_to(WIKI_DIR).parts
        and "dashboards" not in path.relative_to(WIKI_DIR).parts
    )


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


def page_label(path: Path, frontmatter: dict[str, object], body: list[str]) -> str:
    for key in ("short_title", "display_title"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    heading = h1(body)
    return heading or path.stem.replace("-", " ").title()


def category_ancestors(category: str) -> list[str]:
    parts = category.split("/")
    return ["/".join(parts[:i]) for i in range(1, len(parts) + 1)]


def category_path(category: str) -> Path:
    return CATEGORY_DIR / f"{category}.md"


def category_title(category: str) -> str:
    return category.split("/")[-1].replace("-", " ").title()


def wiki_link(path: Path, label: str) -> str:
    target = path.relative_to(ROOT).with_suffix("").as_posix()
    return f"[[{target}|{label}]]"


def category_link(category: str, label: str | None = None) -> str:
    return f"[[wiki/categories/{category}|{label or category}]]"


def load_pages() -> tuple[
    dict[str, dict[str, list[Page]]],
    set[str],
    list[Page],
]:
    members: dict[str, dict[str, list[Page]]] = defaultdict(lambda: defaultdict(list))
    all_categories: set[str] = set()
    pages: list[Page] = []

    for path in wiki_pages():
        frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
        page_type = str(frontmatter.get("type", "")).strip()
        if page_type not in INDEXED_TYPES:
            continue

        page = Page(
            path=path,
            page_type=page_type,
            label=page_label(path, frontmatter, body),
            categories=tuple(as_list(frontmatter.get("categories", []))),
            coverage_profile=str(frontmatter.get("coverage_profile", "")).strip(),
            source_id=str(frontmatter.get("source_id", "")).strip(),
            cites_sources=tuple(as_list(frontmatter.get("cites_sources", []))),
            citation_match_status=str(frontmatter.get("citation_match_status", "")).strip(),
        )
        pages.append(page)
        for category in page.categories:
            all_categories.update(category_ancestors(category))
            members[category][page_type].append(page)

    return members, all_categories, pages


def children_of(category: str, all_categories: set[str]) -> list[str]:
    prefix = f"{category}/"
    return sorted(
        candidate
        for candidate in all_categories
        if candidate.startswith(prefix) and "/" not in candidate[len(prefix) :]
    )


def direct_count(category: str, members: dict[str, dict[str, list[Page]]]) -> int:
    return sum(len(pages) for pages in members.get(category, {}).values())


def branch_pages(category: str, members: dict[str, dict[str, list[Page]]]) -> set[Path]:
    paths: set[Path] = set()
    for candidate, grouped_pages in members.items():
        if candidate == category or candidate.startswith(f"{category}/"):
            for pages in grouped_pages.values():
                paths.update(page.path for page in pages)
    return paths


def render_category(
    category: str,
    members: dict[str, dict[str, list[Page]]],
    all_categories: set[str],
) -> str:
    children = children_of(category, all_categories)
    lines = [
        "---",
        "type: category",
        "status: active",
        f"created: {GENERATED_DATE}",
        f"updated: {GENERATED_DATE}",
        "areas: []",
        "categories: []",
        "tags:",
        "  - generated",
        "  - navigation",
        "related:",
        '  - "[[wiki/categories/README]]"',
        "sources: []",
        "sensitivity: public",
        "encryption: none",
        "graph_exclude: false",
        "generated: true",
        f"category_path: {category}",
        "---",
        "",
        f"# {category_title(category)}",
        "",
        f"Category path: `{category}`",
        "",
        "This page is generated from wiki page frontmatter. Edit page categories at the source pages, then rerun `python3 tools/build_category_indexes.py`.",
        "",
    ]

    if "/" in category:
        parent = category.rsplit("/", 1)[0]
        lines.extend(["## Parent category", "", f"- {category_link(parent)}", ""])

    if children:
        lines.extend(["## Subcategories", ""])
        for child in children:
            direct = direct_count(child, members)
            branch = len(branch_pages(child, members))
            lines.append(f"- {category_link(child)} - {direct} direct, {branch} total pages in branch.")
        lines.append("")

    exact_members = members.get(category, {})
    if any(exact_members.values()):
        lines.extend(["## Direct members", ""])
    for page_type in INDEXED_TYPES:
        pages = sorted(
            exact_members.get(page_type, []),
            key=lambda page: (page.label.casefold(), page.path.as_posix()),
        )
        if not pages:
            continue
        lines.extend([f"### {TYPE_HEADINGS[page_type]}", ""])
        for page in pages:
            lines.append(f"- {wiki_link(page.path, page.label)}")
        lines.append("")

    if children and not any(exact_members.values()):
        lines.extend(["## Direct members", "", "- No pages are directly assigned to this category.", ""])
    if not children and not any(exact_members.values()):
        lines.extend(["## Pages", "", "- No pages are directly assigned to this category.", ""])

    return "\n".join(lines).rstrip() + "\n"


def dashboard_header(title: str) -> list[str]:
    slug = title.lower().replace(" ", "-")
    return [
        "---",
        "type: overview",
        "status: active",
        f"created: {GENERATED_DATE}",
        f"updated: {GENERATED_DATE}",
        "areas: []",
        "categories:",
        "  - admin/wiki-maintenance",
        "tags:",
        "  - dashboard",
        "  - generated",
        "related:",
        "  - \"[[wiki/index]]\"",
        "  - \"[[wiki/categories/README]]\"",
        "sources: []",
        "sensitivity: public",
        "encryption: none",
        "graph_exclude: true",
        "generated: true",
        f"dashboard: {slug}",
        "---",
        "",
        f"# {title}",
        "",
        "This dashboard is generated by `python3 tools/build_category_indexes.py`.",
        "",
    ]


def source_pages(pages: list[Page]) -> list[Page]:
    return sorted(
        [page for page in pages if page.page_type == "source"],
        key=lambda page: (page.label.casefold(), page.path.as_posix()),
    )


def render_sources_by_category(pages: list[Page]) -> str:
    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in source_pages(pages):
        for category in page.categories:
            grouped[category].append(page)

    lines = dashboard_header("Sources By Category")
    for category in sorted(grouped):
        lines.extend([f"## {category}", ""])
        for page in grouped[category]:
            lines.append(f"- {wiki_link(page.path, page.label)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_sources_by_branch(title: str, prefix: str, pages: list[Page]) -> str:
    lines = dashboard_header(title)
    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in source_pages(pages):
        for category in page.categories:
            if category.startswith(prefix):
                grouped[category].append(page)

    if not grouped:
        lines.extend(["- No source pages currently use this category branch.", ""])
    for category in sorted(grouped):
        lines.extend([f"## {category}", ""])
        for page in grouped[category]:
            lines.append(f"- {wiki_link(page.path, page.label)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_sources_by_method(pages: list[Page]) -> str:
    prefixes = (
        "research/adaptive-sampling",
        "research/bioimage-analysis",
        "research/computer-vision",
        "research/machine-learning",
        "research/molecular-simulation",
        "research/statistics",
        "research/high-performance-computing",
    )
    lines = dashboard_header("Sources By Method")
    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in source_pages(pages):
        for category in page.categories:
            if category.startswith(prefixes):
                grouped[category].append(page)

    for category in sorted(grouped):
        lines.extend([f"## {category}", ""])
        for page in grouped[category]:
            lines.append(f"- {wiki_link(page.path, page.label)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_math_heavy_sources(pages: list[Page]) -> str:
    lines = dashboard_header("Math Heavy Sources")
    math_sources = [
        page
        for page in source_pages(pages)
        if page.coverage_profile in {"math-standard", "math-deep"}
    ]
    if not math_sources:
        lines.extend(["- No math-heavy source pages are currently marked.", ""])
    for page in math_sources:
        lines.append(f"- {wiki_link(page.path, page.label)} - `{page.coverage_profile}`")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def source_by_id(pages: list[Page]) -> dict[str, Page]:
    return {
        page.source_id: page
        for page in source_pages(pages)
        if page.source_id
    }


def source_id_link(source_id: str, sources_by_id: dict[str, Page]) -> str:
    page = sources_by_id.get(source_id)
    if page:
        return wiki_link(page.path, source_id)
    return f"`{source_id}`"


def load_citation_candidates() -> list[dict[str, Any]]:
    path = ROOT / "wiki" / "graph" / "source_citation_candidates.json"
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict) and isinstance(data.get("matches"), list):
        return [item for item in data["matches"] if isinstance(item, dict)]
    return []


def render_source_citation_links(pages: list[Page]) -> str:
    sources = source_pages(pages)
    sources_by_id = source_by_id(pages)
    lines = dashboard_header("Source Citation Links")
    lines[lines.index("  - dashboard") + 1:lines.index("  - generated")] = ["  - citations"]
    lines.append("Confirmed links come from source-page `cites_sources` frontmatter. Candidate matches come from `wiki/graph/source_citation_candidates.json` when generated by `python3 tools/match_cited_sources.py`.")
    lines.append("")

    lines.extend(["## Confirmed Source Citation Links", ""])
    confirmed_count = 0
    for page in sources:
        for cited_source_id in sorted(page.cites_sources):
            confirmed_count += 1
            lines.append(
                f"- {wiki_link(page.path, page.label)} -> {source_id_link(cited_source_id, sources_by_id)}"
            )
    if confirmed_count == 0:
        lines.append("- No confirmed source citation links are recorded.")
    lines.append("")

    unchecked = [
        page
        for page in sources
        if not page.citation_match_status or page.citation_match_status == "unchecked"
    ]
    lines.extend(["## Sources With Citation Match Status: unchecked", ""])
    if not unchecked:
        lines.append("- No source pages are currently unchecked.")
    for page in unchecked:
        lines.append(f"- {wiki_link(page.path, page.label)}")
    lines.append("")

    partial = [page for page in sources if page.citation_match_status == "partial"]
    lines.extend(["## Sources With Citation Match Status: partial", ""])
    if not partial:
        lines.append("- No source pages are currently partial.")
    for page in partial:
        lines.append(f"- {wiki_link(page.path, page.label)}")
    lines.append("")

    confirmed_pairs = {
        (page.source_id, cited_source_id)
        for page in sources
        for cited_source_id in page.cites_sources
    }
    candidates = [
        item
        for item in load_citation_candidates()
        if (
            str(item.get("confidence", "")).strip() == "candidate"
            or (
                str(item.get("citing_source_id", "")).strip(),
                str(item.get("cited_source_id", "")).strip(),
            )
            not in confirmed_pairs
        )
    ]
    lines.extend(["## Candidate Matches From Tool Report", ""])
    if not candidates:
        lines.append("- No unaccepted candidate matches are currently reported.")
    for item in candidates:
        citing_id = str(item.get("citing_source_id", "")).strip()
        cited_id = str(item.get("cited_source_id", "")).strip()
        match_type = str(item.get("match_type", "")).strip()
        confidence = str(item.get("confidence", "")).strip()
        evidence = str(item.get("evidence", "")).strip()
        citing_page = sources_by_id.get(citing_id)
        citing = wiki_link(citing_page.path, citing_page.label) if citing_page else f"`{citing_id}`"
        lines.append(
            f"- {citing} -> {source_id_link(cited_id, sources_by_id)} - `{match_type}`, `{confidence}`: {evidence}"
        )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_open_questions(pages: list[Page]) -> str:
    lines = dashboard_header("Open Questions")
    questions = sorted(
        [page for page in pages if page.page_type == "question"],
        key=lambda page: (page.label.casefold(), page.path.as_posix()),
    )
    if not questions:
        lines.extend(["- No question pages currently exist.", ""])
    for page in questions:
        lines.append(f"- {wiki_link(page.path, page.label)}")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_pages_by_type(title: str, page_type: str, pages: list[Page]) -> str:
    lines = dashboard_header(title)
    selected = sorted(
        [page for page in pages if page.page_type == page_type],
        key=lambda page: (page.label.casefold(), page.path.as_posix()),
    )
    if not selected:
        lines.extend([f"- No {page_type} pages currently exist.", ""])
    for page in selected:
        category_suffix = ""
        if page.categories:
            category_suffix = " - " + ", ".join(f"`{category}`" for category in page.categories)
        lines.append(f"- {wiki_link(page.path, page.label)}{category_suffix}")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_dashboards(pages: list[Page]) -> None:
    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    dashboards = {
        "sources-by-category.md": render_sources_by_category(pages),
        "sources-by-biomolecule.md": render_sources_by_branch(
            "Sources By Biomolecule", "research/biomolecules/", pages
        ),
        "sources-by-method.md": render_sources_by_method(pages),
        "source-citation-links.md": render_source_citation_links(pages),
        "math-heavy-sources.md": render_math_heavy_sources(pages),
        "open-questions.md": render_open_questions(pages),
        "claims.md": render_pages_by_type("Claims", "claim", pages),
        "questions.md": render_pages_by_type("Questions", "question", pages),
        "tensions.md": render_pages_by_type("Tensions", "tension", pages),
    }
    for filename, text in dashboards.items():
        (DASHBOARD_DIR / filename).write_text(text, encoding="utf-8")


def remove_stale_categories(all_categories: set[str]) -> int:
    removed = 0
    expected = {category_path(category) for category in all_categories}
    for path in CATEGORY_DIR.rglob("*.md"):
        if path.name == "README.md" or path in expected:
            continue
        text = path.read_text(encoding="utf-8")
        if "\ngenerated: true\n" in text:
            path.unlink()
            removed += 1
    return removed


def main() -> int:
    CATEGORY_DIR.mkdir(parents=True, exist_ok=True)
    members, all_categories, pages = load_pages()
    removed = remove_stale_categories(all_categories)

    for category in sorted(all_categories):
        path = category_path(category)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.name == "README.md":
            continue
        path.write_text(render_category(category, members, all_categories), encoding="utf-8")

    build_dashboards(pages)
    print(f"Generated {len(all_categories)} category index pages and 9 dashboards.")
    if removed:
        print(f"Removed {removed} stale generated category pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
