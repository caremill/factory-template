"""Check that a PR links at least one requirement and one issue (traceability).

Exempt: dependency bots and release PRs (stage -> main).
Inputs come from environment variables set by the workflow. The PR body is untrusted
text: it is only matched against patterns, never executed or interpolated into a shell.
"""

from __future__ import annotations

import os
import re
import sys

EXEMPT_AUTHORS = {"dependabot[bot]", "renovate[bot]"}
REQ_PATTERN = re.compile(r"\bImplements\s+(REQ-\d+(?:\s*,\s*REQ-\d+)*)", re.IGNORECASE)
ISSUE_PATTERN = re.compile(r"\b(?:Closes|Fixes|Resolves)\s+#\d+", re.IGNORECASE)


def check(body: str, author: str, base: str, head: str) -> list[str]:
    """Return a list of problems; an empty list means the PR passes."""
    if author in EXEMPT_AUTHORS:
        return []
    if base == "main" and head == "stage":
        return []
    problems = []
    if not REQ_PATTERN.search(body):
        problems.append("PR body must contain 'Implements REQ-<number>' (one or more IDs).")
    if not ISSUE_PATTERN.search(body):
        problems.append("PR body must contain 'Closes #<issue>'.")
    return problems


def main() -> int:
    problems = check(
        body=os.environ.get("PR_BODY", ""),
        author=os.environ.get("PR_AUTHOR", ""),
        base=os.environ.get("BASE_REF", ""),
        head=os.environ.get("HEAD_REF", ""),
    )
    for problem in problems:
        print(f"::error::{problem}")
    if not problems:
        print("PR conventions satisfied.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
