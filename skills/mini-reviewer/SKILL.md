---
name: mini-reviewer
description: >-
  Code review across security, correctness, style, refactor, and tests.
disable-model-invocation: true
---

# Mini Reviewer

## Overview

One agent. All lenses in a single pass. Concise report.

## Workflow

1. **Context** — determine diff and changed files:
   - `git status` — if staged/unstaged changes exist, use `git diff` and `git diff --cached`
   - otherwise diff against base branch: `git diff $(git merge-base HEAD main)..HEAD` (or `master`)
   - `git diff --name-only` for the file list
   - note any user focus areas (security-only, specific files, etc.)
2. **Review** — read the diff once. Apply each applicable lens (see below) in the same pass.
3. **Report** — merge findings, dedupe by location, sort block → should-fix → nit, assign final verdict.

## Lens routing

Skip lenses that don't apply to this diff.

| Lens | Run when |
|------|----------|
| security | code or config changed |
| correctness | code changed |
| style | code changed |
| refactor | non-trivial code changed |
| tests | source or test files changed |

## What to look for

Apply only the lenses that apply to this diff. Keep one finding per real issue — do not duplicate the same problem under multiple lenses.

**Security** — new exploitable risk introduced by this diff. >80% confidence only.
- Injection — SQL, command, XSS, template, path traversal, NoSQL
- AuthN/AuthZ — bypass, privilege escalation, session/JWT flaws, missing checks on new routes
- Unsafe execution — deserialization, eval/exec, user-controlled code paths
- Crypto/secrets — hardcoded keys/tokens, weak algorithms, cert validation bypass
- Data exposure — PII, secrets, or sensitive data in logs, errors, or API responses
- Skip: DoS, rate limiting, theoretical races, dependency nits, test files, docs.

**Correctness** — bugs in changed code, or existing code broken by the change.
- Backwards compatibility — broken callers, removed exports, changed APIs, altered defaults
- Logic errors — off-by-one, wrong operators, inverted conditions, overflow
- Missing null/undefined checks — property access on nullable values
- Unhandled states — missing switch cases, unhandled promise rejections
- Behavioral mismatch — code does something different from PR description or function name
- Type narrowing gaps — unsafe assertions, unchecked Any/dict payloads, mutable defaults
- Performance regressions — O(n²) or worse, N+1, unbounded growth, blocking main thread, missing pagination
- Be precise: say what breaks and under what input. Name the specific caller for compat issues.

**Style** — clarity and maintainability.
- Names — vague, too implementation-specific, or hiding side effects
- Complexity — oversized files/functions, too many responsibilities, deep nesting
- Duplication & magic values — unexplained literals; repeated knowledge (nit at 2, should-fix at 3+)
- Boundaries — validate external data at edges; keep vendor types out of domain code
- Type modeling — discriminated unions over optional-field bags
- React (.tsx only, not perf): effects for ordinary derivation; props/state mirroring; boolean prop explosions; missing loading/error/empty states
- Skip formatter nits or personal taste when nearby code follows the same pattern.

**Refactor** — structural simplification that deletes complexity.
- Code judo — reframe so branches, helpers, modes, or layers disappear
- Spaghetti growth — ad-hoc conditionals or special cases bolted onto unrelated flows
- File size — diff pushes a file past ~1k lines without decomposition
- Unearned abstractions — pass-through wrappers that spread complexity
- Wrong layer — feature logic in shared modules; bespoke helpers duplicating canonical utilities
- Missing model — repeated conditionals that want a typed union or dispatcher
- Prefer one high-conviction restructuring over many small nits.

**Tests** — coverage and test quality for changed behavior.
- Changed behavior without tests — new paths, modified conditionals, altered logic
- Removed or disabled tests — deleted or `.skip` covering live behavior
- Untested error paths — catch blocks, fallbacks, retry/timeout logic
- Critical paths without assertions — auth, payments, mutations, permissions
- Tests changed to match wrong implementation; weakened assertions; tests of mocks/markup not behavior
- Do not demand tests when the only practical path is expensive or low-signal — say what *would* be worth testing.

## Severity

| Level | Prefix | Meaning | Merge impact |
|-------|--------|---------|--------------|
| **block** | `B` | Must fix before merge | Request changes |
| **should-fix** | `F` | Real issue, non-blocking | Approve with notes |
| **nit** | `N` | Optional polish | Comment only |

**Final verdict:** Request changes if any block · Approve with notes if should-fix only · Approve if nits or clean.

**Finding IDs:** Number findings within each severity (`B1`, `B2`, `F1`, `N1`…) so users can reference them by ID (e.g. "fix B1 and F2").

## Dedup rules

When the same location surfaces under multiple lenses:

- security + correctness → keep **security**
- style + refactor → **refactor** if the fix is structural, **style** if local readability
- correctness already flagged → suppress style nits at that location

## Brevity

- **Summary** — 2–4 sentences max
- **Findings** — typically ≤8 total; cap nits at ~5 unless user asked for depth
- **Per finding** — one line when possible: `` **B1** `path:line` — issue. **Fix:** … ``
- **What looks good** — 1–3 bullets, or omit
- Skip empty severity sections

## Output template

```markdown
# Code review — [target]

## Verdict
[Approve | Approve with notes | Request changes]

## Findings

### Block
- **B1** `path:line` — issue. **Fix:** …

### Should-fix
- **F1** `path:line` — issue. **Fix:** …

### Nit
- **N1** `path:line` — issue. **Fix:** …

## What looks good
- …
```

## Rules

- Single pass — do not spawn sub-agents.
- Skip lenses that don't apply to the diff
- Verify block findings before requesting changes
- Prefer fewer, higher-signal findings — users can ask to expand any item
- Large diff (>20 files): cap merged output; lead with blocks and should-fix, trim nits
- Do not modify code
