#!/usr/bin/env python3
"""Build deterministic semantic dashboards for flat concept pages."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
CONCEPT_DIR = WIKI_DIR / "concepts"
DASHBOARD_DIR = WIKI_DIR / "dashboards"
GENERATED_DATE = "2026-07-01"
SOURCE_ID_RE = re.compile(r"^SRC-\d{4}$")
HIGH_CONNECTIVITY_MIN_SCORE = 8
HIGH_CONNECTIVITY_LIMIT = 30
METHOD_PREFIXES = (
    "research/adaptive-sampling",
    "research/bioimage-analysis",
    "research/computer-vision",
    "research/computational-drug-discovery",
    "research/experimental-benchmarking",
    "research/high-performance-computing",
    "research/machine-learning",
    "research/molecular-simulation",
    "research/scientific-computing",
    "research/statistics",
)
BIOMOLECULE_PREFIX = "research/biomolecules/"


@dataclass(frozen=True)
class Page:
    path: Path
    page_type: str
    label: str
    categories: tuple[str, ...]
    tags: tuple[str, ...]
    related: tuple[str, ...]
    sources: tuple[str, ...]
    source_id: str = ""


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


def split_frontmatter(text: str) -> tuple[dict[str, Any], list[str]]:
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


def h1(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def page_label(path: Path, frontmatter: dict[str, Any], body: list[str]) -> str:
    for key in ("short_title", "display_title"):
        value = frontmatter.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    heading = h1(body)
    return heading or path.stem.replace("-", " ").title()


def wiki_pages() -> list[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if ".obsidian" not in path.parts
        and "categories" not in path.relative_to(WIKI_DIR).parts
        and "dashboards" not in path.relative_to(WIKI_DIR).parts
        and "graph" not in path.relative_to(WIKI_DIR).parts
    )


def load_pages() -> list[Page]:
    pages: list[Page] = []
    for path in wiki_pages():
        frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
        pages.append(
            Page(
                path=path,
                page_type=str(frontmatter.get("type", "")).strip(),
                label=page_label(path, frontmatter, body),
                categories=tuple(as_list(frontmatter.get("categories", []))),
                tags=tuple(as_list(frontmatter.get("tags", []))),
                related=tuple(as_list(frontmatter.get("related", []))),
                sources=tuple(as_list(frontmatter.get("sources", []))),
                source_id=str(frontmatter.get("source_id", "")).strip(),
            )
        )
    return pages


def concept_pages(pages: list[Page]) -> list[Page]:
    return sorted(
        [page for page in pages if page.page_type == "concept" and CONCEPT_DIR in page.path.parents],
        key=lambda page: (page.label.casefold(), page.path.as_posix()),
    )


def source_pages_by_id(pages: list[Page]) -> dict[str, Page]:
    return {
        page.source_id: page
        for page in pages
        if page.page_type == "source" and page.source_id
    }


def source_ids(page: Page) -> tuple[str, ...]:
    return tuple(source for source in page.sources if SOURCE_ID_RE.match(source))


def wiki_link(path: Path, label: str) -> str:
    target = path.relative_to(ROOT).with_suffix("").as_posix()
    return f"[[{target}|{label}]]"


def source_link(source_id: str, sources_by_id: dict[str, Page]) -> str:
    source_page = sources_by_id.get(source_id)
    if source_page:
        return wiki_link(source_page.path, source_id)
    return f"`{source_id}`"


def dashboard_header(title: str, dashboard_slug: str) -> list[str]:
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
        "  - concepts",
        "related:",
        "  - \"[[wiki/index]]\"",
        "sources: []",
        "sensitivity: public",
        "encryption: none",
        "graph_exclude: true",
        "generated: true",
        f"dashboard: {dashboard_slug}",
        "---",
        "",
        f"# {title}",
        "",
        "This dashboard is generated by `python3 tools/build_concept_indexes.py` from concept frontmatter. Keep concept files flat for link stability; edit concept metadata, then rerun the generator.",
        "",
    ]


def concept_line(page: Page, *, include_categories: bool = False) -> str:
    details: list[str] = []
    if include_categories and page.categories:
        details.append("categories: " + ", ".join(f"`{category}`" for category in page.categories))
    if page.tags:
        details.append("tags: " + ", ".join(f"`{tag}`" for tag in page.tags))
    ids = source_ids(page)
    if ids:
        details.append(f"{len(ids)} source IDs")
    suffix = f" - {'; '.join(details)}" if details else ""
    return f"- {wiki_link(page.path, page.label)}{suffix}"


def render_grouped_dashboard(
    title: str,
    slug: str,
    grouped: dict[str, list[Page]],
    *,
    empty_message: str,
    include_categories: bool = False,
) -> str:
    lines = dashboard_header(title, slug)
    if not grouped:
        lines.extend([f"- {empty_message}", ""])
        return "\n".join(lines).rstrip() + "\n"

    for group in sorted(grouped):
        lines.extend([f"## {group}", ""])
        for page in sorted(grouped[group], key=lambda item: (item.label.casefold(), item.path.as_posix())):
            lines.append(concept_line(page, include_categories=include_categories))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_concepts_by_category(concepts: list[Page]) -> str:
    grouped: dict[str, list[Page]] = defaultdict(list)
    uncategorized: list[Page] = []
    for page in concepts:
        if not page.categories:
            uncategorized.append(page)
            continue
        for category in page.categories:
            grouped[category].append(page)
    if uncategorized:
        grouped["No categories"].extend(uncategorized)
    return render_grouped_dashboard(
        "Concepts By Category",
        "concepts-by-category",
        grouped,
        empty_message="No concept pages currently exist.",
    )


def render_concepts_by_method(concepts: list[Page]) -> str:
    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in concepts:
        for category in page.categories:
            if category.startswith(METHOD_PREFIXES):
                grouped[category].append(page)
    return render_grouped_dashboard(
        "Concepts By Method",
        "concepts-by-method",
        grouped,
        empty_message="No concept pages currently use method-oriented category branches.",
        include_categories=True,
    )


def render_concepts_by_biomolecule(concepts: list[Page]) -> str:
    grouped: dict[str, list[Page]] = defaultdict(list)
    for page in concepts:
        for category in page.categories:
            if category.startswith(BIOMOLECULE_PREFIX):
                grouped[category].append(page)
    return render_grouped_dashboard(
        "Concepts By Biomolecule",
        "concepts-by-biomolecule",
        grouped,
        empty_message="No concept pages currently use biomolecule category branches.",
        include_categories=True,
    )


def dominant_source_category(page: Page, sources_by_id: dict[str, Page]) -> tuple[str, Counter[str]]:
    counts: Counter[str] = Counter()
    for source_id in source_ids(page):
        source_page = sources_by_id.get(source_id)
        if source_page:
            counts.update(source_page.categories)
    if counts:
        category = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0][0]
        return category, counts
    if source_ids(page):
        return "Unmatched source IDs", counts
    return "No source IDs", counts


def render_source_cluster_dashboard(concepts: list[Page], sources_by_id: dict[str, Page]) -> str:
    lines = dashboard_header("Concepts By Source Cluster", "concepts-by-source-cluster")
    lines.extend(
        [
            "Concepts are first grouped by the most frequent category among their cited source pages, with ties broken lexicographically. Shared source-ID groups list source IDs cited by multiple concept pages.",
            "",
            "## Dominant Source Category",
            "",
        ]
    )

    grouped: dict[str, list[tuple[Page, Counter[str]]]] = defaultdict(list)
    for page in concepts:
        category, counts = dominant_source_category(page, sources_by_id)
        grouped[category].append((page, counts))

    for category in sorted(grouped):
        lines.extend([f"### {category}", ""])
        for page, counts in sorted(grouped[category], key=lambda item: (item[0].label.casefold(), item[0].path.as_posix())):
            ids = source_ids(page)
            details = [f"{len(ids)} source IDs"]
            if counts:
                top = ", ".join(
                    f"`{name}` ({count})"
                    for name, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]
                )
                details.append(f"top source categories: {top}")
            lines.append(f"- {wiki_link(page.path, page.label)} - {'; '.join(details)}")
        lines.append("")

    source_to_concepts: dict[str, list[Page]] = defaultdict(list)
    for page in concepts:
        for source_id in source_ids(page):
            source_to_concepts[source_id].append(page)

    shared = {
        source_id: sorted(pages, key=lambda item: (item.label.casefold(), item.path.as_posix()))
        for source_id, pages in source_to_concepts.items()
        if len(pages) >= 2
    }
    lines.extend(["## Shared Source IDs", ""])
    if not shared:
        lines.extend(["- No source IDs are currently shared by multiple concept pages.", ""])
    for source_id in sorted(shared):
        lines.extend([f"### {source_link(source_id, sources_by_id)}", ""])
        for page in shared[source_id]:
            lines.append(concept_line(page, include_categories=True))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_high_connectivity_dashboard(concepts: list[Page]) -> str:
    lines = dashboard_header("High Connectivity Concepts", "high-connectivity-concepts")
    lines.extend(
        [
            f"Connectivity score is `related link count + source ID count`. This dashboard lists concepts with score >= {HIGH_CONNECTIVITY_MIN_SCORE}, capped at {HIGH_CONNECTIVITY_LIMIT} entries.",
            "",
        ]
    )
    scored = sorted(
        (
            (len(page.related) + len(source_ids(page)), len(page.related), len(source_ids(page)), page)
            for page in concepts
        ),
        key=lambda item: (-item[0], item[3].label.casefold(), item[3].path.as_posix()),
    )
    selected = [item for item in scored if item[0] >= HIGH_CONNECTIVITY_MIN_SCORE][:HIGH_CONNECTIVITY_LIMIT]
    if not selected:
        lines.extend(["- No concept pages currently meet the high-connectivity threshold.", ""])
    for score, related_count, source_count, page in selected:
        lines.append(
            f"- {wiki_link(page.path, page.label)} - score `{score}`; related links `{related_count}`; source IDs `{source_count}`"
        )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_dashboards(pages: list[Page]) -> None:
    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    concepts = concept_pages(pages)
    sources_by_id = source_pages_by_id(pages)
    dashboards = {
        "concepts-by-category.md": render_concepts_by_category(concepts),
        "concepts-by-method.md": render_concepts_by_method(concepts),
        "concepts-by-biomolecule.md": render_concepts_by_biomolecule(concepts),
        "concepts-by-source-cluster.md": render_source_cluster_dashboard(concepts, sources_by_id),
        "high-connectivity-concepts.md": render_high_connectivity_dashboard(concepts),
    }
    for filename, text in dashboards.items():
        (DASHBOARD_DIR / filename).write_text(text, encoding="utf-8")
    print(f"Generated {len(dashboards)} concept dashboards from {len(concepts)} concept pages.")


def main() -> int:
    build_dashboards(load_pages())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
