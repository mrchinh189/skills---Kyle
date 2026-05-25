#!/bin/bash
set -euo pipefail

# SessionStart hook: validate every skill (frontmatter + marketplace.json)
# so problems surface at session start rather than when a skill is invoked.
# Web-only by default; this repo has no runtime dependencies to install.

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

python3 .claude/hooks/validate_skills.py
