---
name: architecture-review
description: Propose a better software design for a named module, subsystem, or concept — current homes versus proposed homes, what moves, and why the next similar change is cheaper. Use when the user wants an architecture or design pass. Not a code review, correctness review, or implementation.
disable-model-invocation: true
---

# Architecture Review

Requires a named area: a module, subsystem, or concept. If the caller did not pass one, ask and stop. Never implement.

If the named area is too big to hold one design, cut to the one concept whose missing or cramped home is costing the most, and say that's the cut.

# Job

Propose a better **place** for the concept. Ignore correctness, style, naming-as-taste, and local cleanup.

A one-off that works for a single instance is not a design. The test: when the next similar thing shows up, does it have a home, or does someone bolt on another special case?

Authorization as a single `if` in a handler is a one-off. A `policies/` module — role + action in, allow/deny out — is a home. Propose the second shape, not a cleaner `if`.

# Current

Read enough to see where the concept lives today. Do not audit lines.

# Proposed

One design. A second only if another home is genuinely close.

What moves is modules and responsibilities, not functions. Callers that do not care about the new instance should not have to change.

# Output

```markdown
## Current
Where it lives. Why the next instance is expensive.

## Proposed
The home. What moves. Why the next instance is cheaper.
```

If a second home was close, add `## Also considered` with why not.

No code. No patches. No `file:line` notes. No catalog of nits.

# Stop

Report the design. Do not branch, implement, or open a PR.
