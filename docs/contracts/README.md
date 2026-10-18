# Contracts

API and event contracts are the boundary between services and stacks. They are written
before implementation (contract-first) and owned by the Architect.

- `openapi/<service>.yaml` — synchronous HTTP APIs (OpenAPI 3.1)
- `asyncapi/<service>.yaml` — events and messages (AsyncAPI 3)

CI runs contract tests against these files. Changing a contract is a high-risk change.
