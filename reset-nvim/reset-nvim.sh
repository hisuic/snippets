#!/usr/bin/env bash

set -e

echo "== Neovim Reset Script =="

CONFIG_DIR="$HOME/.config/nvim"
DATA_DIR="$HOME/.local/share/nvim"
CACHE_DIR="$HOME/.cache/nvim"
STATE_DIR="$HOME/.local/state/nvim"

echo ""
echo "[1] Checking config..."
if [ ! -d "$CONFIG_DIR" ]; then
  echo "⚠️  Config not found: $CONFIG_DIR"
  echo "   Aborting to avoid wiping everything blindly."
  exit 1
fi

echo "✔ Config found: $CONFIG_DIR"

echo ""
echo "Choose reset mode:"
echo "1) Full reset (plugins + cache + state)"
echo "2) Plugin-only reset (~/.local/share/nvim/lazy)"
echo "3) Cache-only reset"
read -rp "Select [1-3]: " MODE

case "$MODE" in
  1)
    echo "🔥 Full reset..."
    rm -rf "$DATA_DIR"
    rm -rf "$CACHE_DIR"
    rm -rf "$STATE_DIR"
    ;;
  2)
    echo "🔁 Plugin-only reset..."
    rm -rf "$DATA_DIR/lazy"
    ;;
  3)
    echo "🧽 Cache-only reset..."
    rm -rf "$CACHE_DIR"
    ;;
  *)
    echo "❌ Invalid option"
    exit 1
    ;;
esac

echo ""
echo "✔ Reset complete."

echo ""
echo "Next steps:"
echo "  - Run: nvim"
echo "  - Then: :Lazy sync"
echo "  - Then: :TSUpdate"

echo ""
echo "Done."
