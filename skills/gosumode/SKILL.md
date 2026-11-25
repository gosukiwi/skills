---
name: gosumode
description: Pick the right skill for what you're trying to do. A router over this repo's skills.
argument-hint: "What are you trying to do?"
disable-model-invocation: true
---

# Gosumode

Say what you're trying to do. This picks the skill to start with. If the invocation names no goal, ask for one.

Read the chosen skill's `SKILL.md` before invoking it. The lines below orient you; they are not a substitute for the skill.

## Main flow: idea → merged PR

1. **Rough idea to explore, no ticket** → `create-issue`. Explores with you and drafts a GitHub issue.
2. **GitHub issue, or concrete scope for the full flow** → `address-issue`. Runs the whole path: grilling, slice, implement, review, PR.
   - Too big for one PR → `slice` first.
   - A set of issues, unattended, one PR → `yolo-issues`.
   - Only the code, no grilling or PR → `implement` with the issue.
3. **Already-scoped brief, code only (no grilling or PR)** → `implement`. TDD tasks, each reviewed; no PR.
4. **Built branch, not reviewed** → `review-loop`. Fixes correctness findings, then the maintainability findings worth fixing.

## Standalone

### Design & explore

- **Stress-test a plan, decision, or idea** → `grilling`.
- **Stress-test a design and record glossary terms and ADRs as you go** → `grill-with-docs`.
- **Define domain terminology (`GLOSSARY.md`) or record an ADR** → `domain-modeling`.
- **Build a throwaway prototype to test logic or explore UI variations** → `prototype`.
- **Design, refine, or critique a web interface** → `ui-design`.
- **Find a better home for a concept, module, or repo** → `rehome`.

### Review & inspect

- **Review a GitHub PR and post feedback** → `review-pr`.
- **Review a diff for bugs, no fixes** → `correctness-review`.
- **Harsh maintainability pass** → `thermo-nuclear-code-quality-review`.
- **Render a git diff in the browser** → `show-diff-in-browser`.
- **Explain a review finding** → `explain-finding`.

### Prevent mistakes & maintain

- **Prevent repeated agent mistakes with architecture, types, lint, or tests** → `correct`.
- **Remove or rewrite tests that guard no behavior** → `prune-tests`.
- **Split a bloated `AGENTS.md`** → `tidy-up-agents-md`.

### Write, explain, & session

- **Cut AI tells from writing** → `unslop`.
- **Restate the last message plainly** → `bro`.
- **Move context to a fresh session** → `handoff`.
- **Set up or change worker model tiers** → `setup-gosumode`.

## Route

1. Match the request to one entry. If two fit, pick the earlier step in the main flow: starting too early costs a round; starting too late leaves an issue or a review missing.
2. No fit? Say so in one line and answer or ask for the missing goal. Do not force a skill.
3. Invoke the chosen skill and pass the user's words plus any scope they named: issue number, branch, file, or diff.
4. Do not do the work here. Route, then stop.
