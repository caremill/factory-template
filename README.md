# factory-template

Template for every product repository built by the AI software factory.
Create new product repos from this template, then adjust `AGENTS.md` and the stack.

## Structure

| Path                      | Purpose                                           | Owner                  |
| ------------------------- | ------------------------------------------------- | ---------------------- |
| `AGENTS.md`               | Conventions every agent follows                   | Architect              |
| `docs/spec/`              | Requirements with `REQ-` IDs                      | Requirements Analyst   |
| `docs/adr/`               | Architecture decision records                     | Architect              |
| `docs/contracts/`         | OpenAPI / AsyncAPI contracts                      | Architect              |
| `docs/design/`, `design/` | Design system, screens, prototypes                | Designer               |
| `docs/glossary.md`        | Domain terms                                      | Requirements Analyst   |
| `docs/risk.md`            | Privacy, accessibility and security risk register | Architect              |
| `src/`                    | Application code                                  | Developer              |
| `tests/unit/`             | Unit tests                                        | Developer              |
| `tests/acceptance/`       | Acceptance tests from the spec (protected)        | QA                     |
| `.github/`                | CI, CODEOWNERS, templates (protected)             | DevOps + product owner |

## Branches

`feat/*` → `stage` (integration, auto-merge for low-risk PRs) → `main` (weekly release).
See `docs/adr/0001-operating-model.md`.

## Local checks

```bash
npm ci
npm run format:check && npm run lint && npm run typecheck && npm run test:coverage
```
