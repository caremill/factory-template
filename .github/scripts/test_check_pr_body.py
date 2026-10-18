"""Unit tests for check_pr_body (run with: python -m pytest .github/scripts)."""

from check_pr_body import check


def test_passes_with_requirement_and_issue():
    body = "Adds the checklist.\n\nImplements REQ-012, REQ-014\nCloses #45"
    assert check(body, "factory-developer[bot]", "stage", "feat/45-checklist") == []


def test_fails_without_requirement():
    problems = check("Closes #45", "someone", "stage", "feat/45-x")
    assert len(problems) == 1
    assert "REQ" in problems[0]


def test_fails_without_issue():
    problems = check("Implements REQ-001", "someone", "stage", "feat/1-x")
    assert len(problems) == 1
    assert "Closes" in problems[0]


def test_dependabot_is_exempt():
    assert check("", "dependabot[bot]", "stage", "dependabot/npm/x") == []


def test_release_pr_is_exempt():
    assert check("", "factory-orchestrator[bot]", "main", "stage") == []
