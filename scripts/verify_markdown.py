#!/usr/bin/env python3
"""Lightweight repository checks for Markdown docs.

This is intentionally small. Milestone 0 needs a sanity check, not a documentation framework.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".worktrees", "worktrees", ".venv", "venv", "__pycache__"}


def iter_markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
            continue
        yield path


def check_file(path: Path) -> list[str]:
    rel = path.relative_to(ROOT)
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    fence_count = 0

    for i, line in enumerate(lines, 1):
        if "	" in line:
            errors.append(f"{rel}:{i}: tab character")
        if line.strip().startswith("```"):
            fence_count += 1

    if fence_count % 2:
        errors.append(f"{rel}: unbalanced fenced code blocks ({fence_count})")

    return errors


def main() -> int:
    errors: list[str] = []
    files = list(iter_markdown_files())

    for path in files:
        errors.extend(check_file(path))

    if errors:
        print("Markdown verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Markdown verification passed: {len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
