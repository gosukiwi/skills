# TDD RED-GREEN

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

## Cycle

1. **RED** — one minimal test for one behavior
2. **Verify RED** — run it; fails for the right reason (missing behavior, not a typo)
3. **GREEN** — minimal code to pass
4. **Verify GREEN** — suite green
5. **REFACTOR** — clean up; stay green

## What to test

**TDD applies:** logic, API contracts, data mutations, UI behavior (validation, show/hide, errors).

**Skip new tests** (document a quick manual check instead): pure presentation (CSS, spacing, copy), static markup with unchanged behavior.

## Choose the regression check before RED

- Identify the contract and the specific regression each test guards. Use the
  smallest entry point whose callers rely on that contract. Assert the result or
  side effect they depend on. Private state, helper calls, and internal call
  order can change during a refactor that preserves behavior.
- Derive the expected result from the contract. Use a known result for the
  fixture so the test can catch a mistake in the production calculation.
  Exercise real code under test and assert behavior the app owns.
- Check existing coverage first. Run an existing test for RED if it already
  exposes the regression. Extend its cases or update its expectation if that
  expresses the changed contract. Add a test only if it catches a regression
  the suite would otherwise miss. Another layer earns its own test when it
  guards distinct behavior, such as request mapping or response serialization.

## Evidence

Report fail-before and pass-after output. If an automated test is impractical, say why and use the closest substitute (script, repro command) — still broken-then-fixed.
