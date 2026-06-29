#!/usr/bin/env sh
set -eu

TMP_FILE="$(mktemp /tmp/import-source-smoke-XXXXXX.md)"
trap 'rm -f "$TMP_FILE"' EXIT

cat > "$TMP_FILE" <<'MD'
# Example Import Title

Body text.
MD

python3 tools/import_source.py "$TMP_FILE" --dry-run | grep 'slug_source: markdown_heading'
python3 tools/import_source.py "$TMP_FILE" --title 'Training a force field for proteins and small molecules from scratch' --dry-run | grep 'SRC-[0-9][0-9][0-9][0-9]-training-a-force-field-for-proteins-and-small.md'
python3 tools/import_source.py "$TMP_FILE" --slug 'garnet-force-field' --dry-run | grep 'SRC-[0-9][0-9][0-9][0-9]-garnet-force-field.md'
