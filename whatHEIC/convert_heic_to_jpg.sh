#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-.}"

find "$TARGET_DIR" -type f \( -iname "*.heic" -o -iname "*.heif" \) -print0 |
while IFS= read -r -d '' file; do
  dir="$(dirname "$file")"
  base="$(basename "$file")"
  name="${base%.*}"
  output="$dir/$name.jpg"

  if [[ -e "$output" ]]; then
    echo "Skip: already exists -> $output"
    continue
  fi

  echo "Convert: $file -> $output"

  magick "$file" \
    -quality 95 \
    -sampling-factor 4:4:4 \
    -strip \
    "$output"
done

echo "Done."
