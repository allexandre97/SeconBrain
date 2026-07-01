#!/usr/bin/env python3
"""Report conservative citation matches between ingested source pages."""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "wiki" / "sources"
GRAPH_DIR = ROOT / "wiki" / "graph"
REPORT_JSON = GRAPH_DIR / "source_citation_candidates.json"
SOURCE_ID_RE = re.compile(r"^SRC-\d{4}$")
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
ARXIV_RE = re.compile(r"(?:arXiv:)?(\d{4}\.\d{4,5}(?:v\d+)?|[a-z-]+/\d{7}(?:v\d+)?)", re.IGNORECASE)
REFERENCE_HEADINGS = {"references", "bibliography", "citation links"}


@dataclass(frozen=True)
class SourcePage:
    path: Path
    source_id: str
    display_title: str
    short_title: str
    aliases: tuple[str, ...]
    authors: tuple[str, ...]
    year: str
    doi: str
    arxiv: str
    references_text: str


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


def normalized_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.casefold()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_doi(value: str) -> str:
    value = value.strip().strip(".").lower()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    value = re.sub(r"^doi:\s*", "", value)
    return value.strip()


def normalize_arxiv(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^https?://arxiv\.org/(?:abs|pdf)/", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^arxiv:\s*", "", value, flags=re.IGNORECASE)
    return value.lower().removesuffix(".pdf")


def title_values(source: SourcePage) -> list[str]:
    values = [source.display_title, source.short_title]
    values.extend(source.aliases)
    return [
        value
        for value in dict.fromkeys(values)
        if value and not SOURCE_ID_RE.match(value) and len(normalized_text(value).split()) >= 3
    ]


def first_author_surname(source: SourcePage) -> str:
    if not source.authors:
        return ""
    first = source.authors[0].strip()
    if "," in first:
        return normalized_text(first.split(",", 1)[0])
    parts = normalized_text(first).split()
    return parts[-1] if parts else ""


def section_text(body: list[str], heading: str) -> str:
    wanted = heading.casefold()
    collected: list[str] = []
    active = False
    for line in body:
        if line.startswith("## "):
            title = line[3:].strip().casefold()
            if active and title not in REFERENCE_HEADINGS:
                break
            active = title == wanted
            continue
        if active:
            collected.append(line)
    return "\n".join(collected).strip()


def collect_references_text(frontmatter: dict[str, Any], body: list[str]) -> str:
    chunks: list[str] = []
    for key in ("references_text",):
        value = frontmatter.get(key)
        if isinstance(value, str):
            chunks.append(value)
        elif isinstance(value, list):
            chunks.extend(str(item) for item in value)
    for heading in sorted(REFERENCE_HEADINGS):
        text = section_text(body, heading)
        if text:
            chunks.append(text)
    return "\n\n".join(chunks).strip()


def load_sources() -> list[SourcePage]:
    sources: list[SourcePage] = []
    for path in sorted(SOURCE_DIR.glob("*.md")):
        frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
        if str(frontmatter.get("type", "")).strip() != "source":
            continue
        source_id = str(frontmatter.get("source_id", "")).strip()
        if not source_id:
            continue
        sources.append(
            SourcePage(
                path=path,
                source_id=source_id,
                display_title=str(frontmatter.get("display_title", "")).strip(),
                short_title=str(frontmatter.get("short_title", "")).strip(),
                aliases=tuple(as_list(frontmatter.get("aliases", []))),
                authors=tuple(as_list(frontmatter.get("authors", []))),
                year=str(frontmatter.get("year", "")).strip(),
                doi=normalize_doi(str(frontmatter.get("doi", "")).strip()),
                arxiv=normalize_arxiv(str(frontmatter.get("arxiv", "")).strip()),
                references_text=collect_references_text(frontmatter, body),
            )
        )
    return sources


def evidence_window(text: str, needle: str) -> str:
    lower = text.casefold()
    index = lower.find(needle.casefold())
    if index < 0:
        return ""
    start = max(0, index - 80)
    end = min(len(text), index + len(needle) + 160)
    return re.sub(r"\s+", " ", text[start:end]).strip()


def reference_chunks(text: str) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        if re.match(r"^\s*(?:[-*]|\[\d+\]|\(\d+\)|\d+[.)])\s+", line) and current:
            chunks.append(" ".join(current))
            current = [line]
        elif line.strip():
            current.append(line)
    if current:
        chunks.append(" ".join(current))
    return chunks or [text]


def best_fuzzy_title_match(source: SourcePage, ref_text: str) -> tuple[float, str, str]:
    best_score = 0.0
    best_title = ""
    best_chunk = ""
    for title in title_values(source):
        norm_title = normalized_text(title)
        if len(norm_title) < 20:
            continue
        for chunk in reference_chunks(ref_text):
            norm_chunk = normalized_text(chunk)
            if not norm_chunk:
                continue
            score = SequenceMatcher(None, norm_title, norm_chunk).ratio()
            title_tokens = set(norm_title.split())
            chunk_tokens = set(norm_chunk.split())
            if title_tokens:
                score = max(score, len(title_tokens & chunk_tokens) / len(title_tokens))
            if score > best_score:
                best_score = score
                best_title = title
                best_chunk = re.sub(r"\s+", " ", chunk).strip()
    return best_score, best_title, best_chunk


def add_match(matches: dict[tuple[str, str], dict[str, str]], item: dict[str, str]) -> None:
    key = (item["citing_source_id"], item["cited_source_id"])
    current = matches.get(key)
    rank = {"candidate": 0, "strong": 1}
    if current is None or rank[item["confidence"]] > rank[current["confidence"]]:
        matches[key] = item


def match_sources(sources: list[SourcePage]) -> list[dict[str, str]]:
    matches: dict[tuple[str, str], dict[str, str]] = {}
    for citing in sources:
        if not citing.references_text:
            continue
        ref_text = citing.references_text
        norm_refs = normalized_text(ref_text)
        dois_in_refs = {normalize_doi(match.group(0)) for match in DOI_RE.finditer(ref_text)}
        arxivs_in_refs = {normalize_arxiv(match.group(1)) for match in ARXIV_RE.finditer(ref_text)}
        for cited in sources:
            if cited.source_id == citing.source_id:
                continue
            if cited.doi and cited.doi in dois_in_refs:
                add_match(
                    matches,
                    {
                        "citing_source_page": citing.path.relative_to(ROOT).as_posix(),
                        "citing_source_id": citing.source_id,
                        "cited_source_page": cited.path.relative_to(ROOT).as_posix(),
                        "cited_source_id": cited.source_id,
                        "match_type": "doi-exact",
                        "evidence": evidence_window(ref_text, cited.doi) or cited.doi,
                        "confidence": "strong",
                    },
                )
                continue
            if cited.arxiv and cited.arxiv in arxivs_in_refs:
                add_match(
                    matches,
                    {
                        "citing_source_page": citing.path.relative_to(ROOT).as_posix(),
                        "citing_source_id": citing.source_id,
                        "cited_source_page": cited.path.relative_to(ROOT).as_posix(),
                        "cited_source_id": cited.source_id,
                        "match_type": "arxiv-exact",
                        "evidence": evidence_window(ref_text, cited.arxiv) or cited.arxiv,
                        "confidence": "strong",
                    },
                )
                continue
            exact_title = next((title for title in title_values(cited) if normalized_text(title) in norm_refs), "")
            if exact_title:
                add_match(
                    matches,
                    {
                        "citing_source_page": citing.path.relative_to(ROOT).as_posix(),
                        "citing_source_id": citing.source_id,
                        "cited_source_page": cited.path.relative_to(ROOT).as_posix(),
                        "cited_source_id": cited.source_id,
                        "match_type": "title-exact",
                        "evidence": evidence_window(ref_text, exact_title) or exact_title,
                        "confidence": "strong",
                    },
                )
                continue
            surname = first_author_surname(cited)
            has_author_year = bool(surname and cited.year and surname in norm_refs and cited.year in ref_text)
            score, fuzzy_title, fuzzy_chunk = best_fuzzy_title_match(cited, ref_text)
            if score >= 0.82 and has_author_year:
                add_match(
                    matches,
                    {
                        "citing_source_page": citing.path.relative_to(ROOT).as_posix(),
                        "citing_source_id": citing.source_id,
                        "cited_source_page": cited.path.relative_to(ROOT).as_posix(),
                        "cited_source_id": cited.source_id,
                        "match_type": "title-author-year",
                        "evidence": fuzzy_chunk[:260] or fuzzy_title,
                        "confidence": "strong",
                    },
                )
            elif score >= 0.82:
                add_match(
                    matches,
                    {
                        "citing_source_page": citing.path.relative_to(ROOT).as_posix(),
                        "citing_source_id": citing.source_id,
                        "cited_source_page": cited.path.relative_to(ROOT).as_posix(),
                        "cited_source_id": cited.source_id,
                        "match_type": "title-fuzzy",
                        "evidence": fuzzy_chunk[:260] or fuzzy_title,
                        "confidence": "candidate",
                    },
                )
            elif has_author_year:
                add_match(
                    matches,
                    {
                        "citing_source_page": citing.path.relative_to(ROOT).as_posix(),
                        "citing_source_id": citing.source_id,
                        "cited_source_page": cited.path.relative_to(ROOT).as_posix(),
                        "cited_source_id": cited.source_id,
                        "match_type": "author-year",
                        "evidence": f"{surname} and {cited.year} appear in reference text",
                        "confidence": "candidate",
                    },
                )
    return sorted(
        matches.values(),
        key=lambda item: (
            item["citing_source_id"],
            item["confidence"],
            item["cited_source_id"],
            item["match_type"],
        ),
    )


def main() -> int:
    sources = load_sources()
    matches = match_sources(sources)
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps({"matches": matches}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("citing source page\tcandidate cited existing source\tmatch type\tconfidence\tevidence")
    for item in matches:
        print(
            "\t".join(
                [
                    item["citing_source_page"],
                    item["cited_source_page"],
                    item["match_type"],
                    item["confidence"],
                    item["evidence"],
                ]
            )
        )
    print(f"Wrote {REPORT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
