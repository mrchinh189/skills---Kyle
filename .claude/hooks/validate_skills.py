#!/usr/bin/env python3
"""Validate every skill in this repo.

Checks each skills/*/SKILL.md and template/SKILL.md for:
  - valid YAML frontmatter delimited by ---
  - required fields: name, description
  - name is lowercase-with-hyphens and matches its directory
  - description is non-trivial (length sanity)
And validates .claude-plugin/marketplace.json:
  - parses as JSON
  - every referenced skill path exists and has a SKILL.md

Exit code 0 when clean, 1 when any error is found. Warnings never fail.
Pure stdlib; uses PyYAML if available for robust parsing, otherwise a
minimal frontmatter parser.
"""
from __future__ import annotations
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(os.environ.get("CLAUDE_PROJECT_DIR", Path(__file__).resolve().parents[2]))

try:
    import yaml  # type: ignore
    _HAVE_YAML = True
except Exception:
    _HAVE_YAML = False

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict | None:
    """Return the frontmatter mapping, or None if no valid block."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    block = parts[1]
    if _HAVE_YAML:
        try:
            data = yaml.safe_load(block)
            return data if isinstance(data, dict) else None
        except Exception:
            return None
    # Minimal fallback: single-line `key: value` pairs, strips quotes.
    out: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if m:
            val = m.group(2).strip()
            if len(val) >= 2 and val[0] in "\"'" and val[-1] == val[0]:
                val = val[1:-1]
            out[m.group(1)] = val
    return out or None


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    checked = 0

    skill_md_files = sorted((REPO / "skills").glob("*/SKILL.md"))
    template = REPO / "template" / "SKILL.md"
    if template.exists():
        skill_md_files.append(template)

    for md in skill_md_files:
        checked += 1
        rel = md.relative_to(REPO)
        fm = parse_frontmatter(md.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{rel}: missing or unparseable YAML frontmatter")
            continue
        name = fm.get("name")
        desc = fm.get("description")
        if not name:
            errors.append(f"{rel}: frontmatter missing required field 'name'")
        if not desc:
            errors.append(f"{rel}: frontmatter missing required field 'description'")
        # template uses a placeholder name; skip name-shape checks for it
        is_template = md.parent.name == "template"
        if name and not is_template:
            if not NAME_RE.match(str(name)):
                errors.append(f"{rel}: name '{name}' must be lowercase-with-hyphens")
            if str(name) != md.parent.name:
                warnings.append(
                    f"{rel}: name '{name}' does not match directory '{md.parent.name}'"
                )
        if desc and not is_template and len(str(desc)) < 30:
            warnings.append(
                f"{rel}: description is very short ({len(str(desc))} chars) — "
                "weak triggering signal"
            )

    # marketplace.json
    mk = REPO / ".claude-plugin" / "marketplace.json"
    if mk.exists():
        try:
            data = json.loads(mk.read_text(encoding="utf-8"))
            for plugin in data.get("plugins", []):
                for sp in plugin.get("skills", []):
                    p = (REPO / sp).resolve()
                    if not (p / "SKILL.md").exists():
                        errors.append(
                            f".claude-plugin/marketplace.json: plugin "
                            f"'{plugin.get('name')}' references '{sp}' "
                            "but no SKILL.md found there"
                        )
        except json.JSONDecodeError as e:
            errors.append(f".claude-plugin/marketplace.json: invalid JSON ({e})")
    else:
        warnings.append(".claude-plugin/marketplace.json not found")

    # report
    print(f"[validate-skills] checked {checked} SKILL.md file(s) "
          f"(PyYAML={'yes' if _HAVE_YAML else 'no, using fallback'})")
    for w in warnings:
        print(f"  ⚠️  {w}")
    if errors:
        for e in errors:
            print(f"  ❌ {e}")
        print(f"[validate-skills] FAILED with {len(errors)} error(s).")
        return 1
    print(f"[validate-skills] OK — all skills valid"
          f"{f', {len(warnings)} warning(s)' if warnings else ''}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
