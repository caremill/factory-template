"""Fail if any source file is missing from the coverage report.

A file that no test imports may be left out of the report entirely. Coverage
thresholds and diff-cover then never see it, so untested code passes silently.
"""

from __future__ import annotations

import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPORT = Path("coverage/cobertura-coverage.xml")
PATTERNS = ["src/**/*.ts", "src/*.ts"]
IGNORE_SUFFIXES = (".d.ts", ".test.ts", ".spec.ts")


def source_files() -> set[str]:
    out = subprocess.run(
        ["git", "ls-files", "--", *PATTERNS], capture_output=True, text=True, check=True
    ).stdout
    return {f for f in out.splitlines() if f and not f.endswith(IGNORE_SUFFIXES)}


def reported_files(report: Path, repo_root: Path) -> set[str]:
    root = ET.parse(report).getroot()
    bases = [Path(s.text.strip()) for s in root.iter("source") if s.text and s.text.strip()]
    bases = bases or [repo_root]
    found: set[str] = set()
    for cls in root.iter("class"):
        name = cls.get("filename")
        if not name:
            continue
        for base in bases:
            path = (base / name) if not Path(name).is_absolute() else Path(name)
            try:
                found.add(path.resolve().relative_to(repo_root).as_posix())
            except ValueError:
                continue
    return found


def main() -> int:
    if not REPORT.exists():
        print(f"::error::{REPORT} not found; run the coverage step first.")
        return 1
    repo_root = Path.cwd().resolve()
    missing = sorted(source_files() - reported_files(REPORT, repo_root))
    for path in missing:
        print(f"::error file={path}::{path} is not in the coverage report (no test imports it).")
    if not missing:
        print("All source files appear in the coverage report.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())