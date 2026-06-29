#!/usr/bin/env python3
"""Import a local file into raw/sources/ with a normalized source ID."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_SOURCES = ROOT / "raw" / "sources"
SOURCE_RE = re.compile(r"^SRC-(\d{4})-")
MAX_SLUG_WORDS = 8
TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".text"}
TITLE_RE = re.compile(rb"/Title\s*\((.*?)\)", re.DOTALL)
HEX_TITLE_RE = re.compile(rb"/Title\s*<([0-9A-Fa-f]+)>")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def next_source_id() -> str:
    highest = 0
    if RAW_SOURCES.exists():
        for path in RAW_SOURCES.iterdir():
            match = SOURCE_RE.match(path.name)
            if match:
                highest = max(highest, int(match.group(1)))
    return f"SRC-{highest + 1:04d}"


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    words = re.findall(r"[a-z0-9]+", ascii_text.lower())
    slug = "-".join(words[:MAX_SLUG_WORDS])
    return slug or "source"


def meaningful_line(line: str) -> str:
    return line.strip().strip("# ").strip()


def is_title_like(line: str) -> bool:
    if not line or len(line) > 160:
        return False
    if line.endswith(('.', ',', ';', ':')):
        return False
    words = re.findall(r"[A-Za-z0-9]+", line)
    return 2 <= len(words) <= 18


def infer_markdown_title(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            title = meaningful_line(line)
            if title:
                return title
    return None


def infer_text_title(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        candidate = meaningful_line(line)
        if candidate and is_title_like(candidate):
            return candidate
    return None


def decode_pdf_title(raw: bytes) -> str | None:
    if raw.startswith(b"\xfe\xff"):
        try:
            return raw[2:].decode("utf-16-be").strip()
        except UnicodeDecodeError:
            return None
    try:
        return raw.decode("latin-1").encode("latin-1").decode("unicode_escape").strip()
    except UnicodeDecodeError:
        return None


def infer_pdf_title(path: Path) -> str | None:
    data = path.read_bytes()[:1024 * 1024]
    match = TITLE_RE.search(data)
    if match:
        title = decode_pdf_title(match.group(1))
        if title:
            return title
    match = HEX_TITLE_RE.search(data)
    if match:
        try:
            title = bytes.fromhex(match.group(1).decode("ascii")).decode("utf-16-be").strip()
        except (ValueError, UnicodeDecodeError):
            return None
        return title or None
    return None


def infer_title(path: Path) -> tuple[str, str]:
    suffix = path.suffix.lower()
    title = None
    source = "filename"
    if suffix in {".md", ".markdown"}:
        title = infer_markdown_title(path)
        source = "markdown_heading" if title else source
    elif suffix in {".txt", ".text"}:
        title = infer_text_title(path)
        source = "text_first_line" if title else source
    elif suffix == ".pdf":
        title = infer_pdf_title(path)
        source = "pdf_metadata" if title else source

    if title:
        return title, source
    return path.stem, "filename"


def choose_slug(path: Path, explicit_slug: str | None, explicit_title: str | None) -> tuple[str, str]:
    if explicit_slug:
        return slugify(explicit_slug), "explicit_slug"
    if explicit_title:
        return slugify(explicit_title), "explicit_title"
    title, slug_source = infer_title(path)
    return slugify(title), slug_source


def unique_destination(source_id: str, slug: str, suffix: str) -> Path:
    destination = RAW_SOURCES / f"{source_id}-{slug}{suffix}"
    if not destination.exists():
        return destination

    counter = 2
    while True:
        destination = RAW_SOURCES / f"{source_id}-{slug}-{counter}{suffix}"
        if not destination.exists():
            return destination
        counter += 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy a local source file into raw/sources/ as SRC-XXXX-short-slug.ext."
    )
    parser.add_argument("path", help="Local file to import")
    parser.add_argument("--title", help="Document title to slugify if --slug is not provided")
    parser.add_argument("--slug", help="Custom short slug for the imported filename")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned import details without copying the file.",
    )
    args = parser.parse_args()

    source = Path(args.path).expanduser().resolve()
    if not source.is_file():
        print(f"ERROR: source file not found: {source}", file=sys.stderr)
        return 1

    RAW_SOURCES.mkdir(parents=True, exist_ok=True)
    source_id = next_source_id()
    slug, slug_source = choose_slug(source, args.slug, args.title)
    destination = unique_destination(source_id, slug, source.suffix.lower())
    file_hash = sha256(source)

    if not args.dry_run:
        shutil.copy2(source, destination)
        file_hash = sha256(destination)

    print(f"source_id: {source_id}")
    print(f"original_path: {source}")
    print(f"imported_path: {destination.relative_to(ROOT).as_posix()}")
    print(f"slug_source: {slug_source}")
    print(f"sha256: {file_hash}")
    if args.dry_run:
        print("dry_run: true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
