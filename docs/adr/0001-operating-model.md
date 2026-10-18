# ADR-0001: AI software factory operating model

- **Status:** Accepted
- **Date:** 2026-10-17
- **Decider:** Product owner

## Context

Products are built by AI agents coordinated by an orchestrator, with one human product owner
whose review time is the system's bottleneck. We need rules that keep quality high, keep the
product owner's effort bounded, and stop agents from verifying their own work.

## Decision

1. **Branching:** feature branches → `stage` (integration) → `main` (releases). Feature PRs are
   squash-merged into `stage`; `stage` is merged into `main` on a weekly release cadence.
2. **Gates owned by the product owner:** G1 spec sign-off, G2 architecture and design approval,
   G3 release (`stage` → `main`), G4 production deploy (GitHub `production` environment).
3. **Risk classes:** changes to paths listed in `.github/CODEOWNERS` (specs, ADRs, CI, acceptance
   tests, dependencies, infrastructure, sensitive modules) need the product owner's review.
   All other PRs auto-merge into `stage` once every required check passes.
4. **Deterministic gates first:** formatting, linting, type checks, tests with coverage
   (80% overall, 80% changed lines, 90% critical modules), secret scanning and dependency review
   run before any agent review.
5. **Independent verification:** QA writes acceptance tests from the spec before implementation;
   developers cannot modify them. A reviewer agent with fresh context reviews each diff.
6. **Agents propose, pipelines apply:** no agent can merge, deploy, or change Azure resources.

## Consequences

- The product owner reviews only gate decisions and high-risk PRs, batched daily.
- Low-risk work flows without waiting for a human, which depends on CI being trustworthy;
  weakening CI is therefore itself a high-risk change.
- Adding a sensitive module requires adding its path to `CODEOWNERS`.
