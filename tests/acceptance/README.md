# Acceptance tests

Owned by QA and protected by CODEOWNERS. Written from the spec **before** implementation.

- One `.feature` file per spec area, Given/When/Then scenarios.
- Every scenario carries the tag of the requirement it verifies, for example `@REQ-012`.
- Developers must not edit these files. A disputed scenario is a _spec conflict_ resolved by
  the Analyst and QA through a spec change.

Example:

```gherkin
@REQ-012
Feature: Onboarding checklist

  Scenario: Newcomer sees the Anmeldung step first
    Given a newcomer who has not completed any step
    When they open the checklist
    Then the first step is "Register your address (Anmeldung)"
```
