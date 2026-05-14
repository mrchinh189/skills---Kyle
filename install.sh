#!/usr/bin/env bash
# Install all skills in this repo as user-level skills for Claude Code CLI.
# Creates symlinks under ~/.claude/skills/ pointing at this repo's skills/*.
#
# Usage:
#   ./install.sh           # symlink (default; updates auto when you `git pull`)
#   ./install.sh --copy    # copy instead of symlink (skills won't auto-update)
#   ./install.sh --uninstall

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
SKILLS_DST="${CLAUDE_HOME:-$HOME/.claude}/skills"

mode="symlink"
case "${1:-}" in
  --copy)      mode="copy" ;;
  --uninstall) mode="uninstall" ;;
  -h|--help)
    sed -n '2,9p' "$0"
    exit 0
    ;;
  "") ;;
  *) echo "Unknown arg: $1" >&2; exit 2 ;;
esac

if [ ! -d "$SKILLS_SRC" ]; then
  echo "skills/ not found at $SKILLS_SRC" >&2
  exit 1
fi

mkdir -p "$SKILLS_DST"

count=0
for src in "$SKILLS_SRC"/*/; do
  name="$(basename "$src")"
  dst="$SKILLS_DST/$name"

  if [ "$mode" = "uninstall" ]; then
    if [ -L "$dst" ] || [ -d "$dst" ]; then
      rm -rf "$dst"
      echo "removed: $dst"
      count=$((count + 1))
    fi
    continue
  fi

  if [ -e "$dst" ] || [ -L "$dst" ]; then
    rm -rf "$dst"
  fi

  if [ "$mode" = "symlink" ]; then
    ln -s "${src%/}" "$dst"
    echo "linked:  $dst -> ${src%/}"
  else
    cp -R "${src%/}" "$dst"
    echo "copied:  $dst"
  fi
  count=$((count + 1))
done

echo
if [ "$mode" = "uninstall" ]; then
  echo "Uninstalled $count skill(s) from $SKILLS_DST"
else
  echo "Installed $count skill(s) into $SKILLS_DST (mode: $mode)"
  echo "Restart Claude Code to pick them up."
fi
