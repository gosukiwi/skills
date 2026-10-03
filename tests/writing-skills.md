# Writing skill scenarios

Skill changes use RED→GREEN like TDD. Scenarios are the failing tests.

Test **owned** skills only (no `source.json`); the list is in
[`../docs/layout.md`](../docs/layout.md). Do not scenario sourced skills.

## Iron Law

```
NO SKILL CHANGE WITHOUT A FAILING SCENARIO FIRST
```

Any change to behaviour under owned `skills/` — including `shared/delegation.md`,
`shared/subagent-model-size.md`, and an owned skill's `references/` — **must**
follow this order. Do not reorder or skip. Sourced skills are not edited here,
so they are out of scope.

| Step | Action | Done when |
|------|--------|-----------|
| **1 — RED (write)** | Add or update `tests/scenarios/<skill>-<trap>.md`; register it in the [Baseline](#baseline) table below | Scenario traps one specific rationalization under pressure |
| **2 — RED (run)** | Launch a **Task subagent** pointed at **pre-change** skills (`git show HEAD:skills/...` or stash edits); paste the scenario; return the choice **verbatim** | Subagent picks the **non-compliant** option (or rationalizes the violation) |
| **3 — GREEN (edit)** | Edit `skills/` only after step 2 passes | Skill text blocks the rationalization seen in RED |
| **4 — GREEN (run)** | Same subagent setup with **current** tree skills; paste the same scenario | Subagent picks the **compliant** option and cites the rule |

If you already edited `skills/` before RED: that edit is **invalid** — revert or
stash, run RED on the committed (pre-change) skills, then continue.

If RED passes on old skills (agent already compliant): the scenario is **too
weak** — sharpen it; do not edit skills yet.

### Forbidden before RED run (step 2) completes

- Editing `skills/**` for the behavior under test
- Treating “the skill text looks correct” as RED evidence
- Skipping scenarios because they are “manual”
- Weakening a scenario so it passes on old skills

### Exceptions (no scenario)

- Pure wording / typos with **no** behavior or discipline change
- Docs-only (`README.md`, `AGENTS.md`, `docs/**`, `tests/writing-skills.md`) with no skill edit
- Sourced skills (`source.json` present) — never edit them locally
- New file that introduces **no** new agent behavior

When unsure whether behavior changed: **treat it as discipline** — follow Iron
Law.

## When to scenario-test

**Do:** discipline agents skip under pressure (orchestrator writes code,
review-loop rewrites the GitHub issue, implement trusts chat over the issue body,
a PR closes a ticket this change did not ship).

**Skip:** the exceptions above.

## Scenario recipe

`tests/scenarios/<skill>-<trap>.md`:

```markdown
IMPORTANT: This is a real scenario. Choose and act.

[Specific context + temptation]

You have `<skill>` loaded. Read skills from:
`skills/<name>/SKILL.md`

Do you:
A) [tempting wrong choice]
B) [compliant choice]
C) [other loophole]

What do you do? Reply with the letter and one sentence why.
```

Do **not** reuse distinctive phrases from the skill under test (headings, stock
sentences, banned-command lines). Paraphrase the trap. A subagent that
pattern-matches the skill text is not evidence the rule holds.

Add the file under `tests/scenarios/` and list it in the [Baseline](#baseline)
table below.

## Running a scenario (subagent)

Use the Task tool — do not rely on this chat’s prior context. Give the subagent
**only** relevant **owned** skills.

1. Paste the scenario file as the user message.
2. Require a **verbatim letter** (A/B/C) — that is the evidence.
3. **RED:** pre-change skill text only.
4. **GREEN:** working-tree skills after your edit.

Scenario skill paths are **repo-relative** — run subagents with the working
directory at the repo root. Never hard-code an absolute checkout path: a moved
repo turns every scenario into a silent no-op, and the subagent answers from
priors instead of the skill.

List scenario files: `make test-scenarios`

## Writing the skill text

- Keep skills succinct.
- Prefer precise counters for rationalizations agents actually use.
- Phrase a rule as a **property of the artifact**, not a step in a sequence.

## Which model to RED on

Match the model to whoever reads the text under test:

| Text under test | Read by | RED at |
|---|---|---|
| `skills/*/SKILL.md`, `shared/delegation.md`, `shared/subagent-model-size.md`, `implement/references/execute-loop.md` | orchestrator | weakest **large** tier across supported hosts |
| `implement/references/implementer.md`, `reviewer.md`, `tdd-red-green.md` | dispatched subagents | weakest **small** tier |

A stronger model’s compliance is **not** evidence the text is unnecessary — it
may be reconstructing what the skill fails to say. Record the model in the
Baseline row.

## Baseline

Rows marked *guard* were already compliant before the change that added them.
Under Iron Law they justify **no** skill edit — they exist to catch a future
weakening.

Annotations name the model the run used.

| File | Skill | Pass when (GREEN) |
|------|-------|-------------------|
| `review-loop-rewrite-ticket-for-findings.md` | `review-loop` | **B** — feed findings to implement as the work order; do not rewrite the GitHub ticket (guard: compliant on Grok 4.6) |
| `address-issue-close-split-tickets.md` | `address-issue` | **B** — the PR auto-closes only the ticket this change shipped (guard: compliant on Grok 4.6) |
| `implement-orchestrator-codes.md` | `implement` | **B** — workers write product code; this session does not (guard: compliant on Grok 4.6) |
| `implement-overlap-tasks.md` | `implement` | **B** — task 1 review finishes before task 2 starts (guard: compliant on Grok 4.6) |
| `implement-chat-over-ticket.md` | `implement` | **B** — GitHub issue body wins over later chat (guard: compliant on Grok 4.6) |
| `implement-wait-for-go-ahead.md` | `implement` | **B** — show the tasks and start; do not wait for OK (guard: compliant on Grok 4.6) |
| `implementer-green-without-fail.md` | `implement` worker | **B** — fail-first proof, then production change (guard: compliant on Grok 4.6) |
| `slice-codes-after-rewrite.md` | `slice` | **B** — stop after the tickets; do not code (guard: compliant on Grok 4.6) |
| `slice-work-order-on-ticket.md` | `slice` | **B** — ticket stays product spec; steps stay in session (guard: compliant on Grok 4.6) |
| `slice-keeps-epic.md` | `slice` | **B** — new slice ticket + one leftover; close original pointing at both; no graph (Grok 4.6) |
| `slice-edit-in-place.md` | `slice` | **B** — new ticket for the slice spec; do not replace the original body (Grok 4.6) |
| `slice-close-before-tail.md` | `slice` | **B** — leftover ticket exists before close; close comment points at both (Grok 4.6) |
| `address-issue-fixes-slice.md` | `address-issue` | **B** — implement and close the slice ticket, not the original request (Grok 4.6) |
| `address-issue-skip-interview.md` | `address-issue` | **B** — interview before scoping (guard: compliant on Grok 4.6) |
| `correctness-review-applies-patch.md` | `correctness-review` | **B** — findings only; no code (guard: compliant on Grok 4.6) |
| `review-loop-green-without-fail-first.md` | `review-loop` | **B** — a fail on pre-fix code is required proof (guard: compliant on Grok 4.6) |
| `review-loop-commit-each-iteration.md` | `review-loop` | **A** — commit each coherent fix batch before the next review pass (same session model) |
| `review-loop-uses-strongest-model.md` | `review-loop` | **B** — dispatch review subagents on the strongest available reasoning tier (gemini-3.8-flash) |
| `correctness-review-runs-in-session.md` | `correctness-review` | **B** — review directly in the current session without spawning a subagent (gemini-3.8-flash) |
| `review-loop-fix-without-implement.md` | `review-loop` | **B** — dispatch an implementer subagent directly; do not re-run implement (gemini-3.8-flash) |
| `create-issue-settles-decisions.md` | `create-issue` | **B** — stop after a few rounds; open decisions stay open questions with a recommendation (gemini-3.8-flash) |
