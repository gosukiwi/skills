# AGENTS.md

Working notes for this repo: how it's laid out, how the scripts behave, and
how skill changes are tested.

## What this repo is

A personal skill library. Skills live under `skills/` and sync to
`~/.agents/skills`. Source of truth is Markdown under `skills/` plus pressure
scenarios under `tests/`.

Human overview: `README.md`.

## Layout

```
skills/
  <skill-name>/
    SKILL.md
    source.json   (only for skills sourced from elsewhere)
    references/   (optional, skill-local)
  shared/
    <prompt>.md   (shared prompts, not skills)

tests/
  writing-skills.md
  scenarios/
    run-scenarios.sh
```

Each skill is a directory containing a `SKILL.md` (plus any supporting
files such as `references/` or `scripts/`). Sourced skills are kept as a
pristine mirror of their upstream directory — no local edits.

Owned skills (no `source.json`): `address-issue`, `correctness-review`,
`explain-finding`, `implement`, `plan`, `rehome`, `review-loop`,
`tidy-up-agents-md`, `use-simplified-english`, plus `shared/delegation.md`.
Scenario-test **only** these. Do not add scenarios for sourced skills.

## skills/shared

Prompts that several skills reuse. `shared/` holds plain markdown, not skills:
it has no `SKILL.md`, so agents never load it as a skill or expose it as a
slash command. Skills reach these files by path — see `shared/delegation.md`,
which is how one skill runs another.

## source.json

Skills sourced from elsewhere carry a `source.json` sidecar that records where
the `SKILL.md` came from:

```json
{
  "description": "Compact a conversation into a handoff doc.",
  "repo": "https://github.com/<user>/<repo>/blob/<branch>/path/to/SKILL.md"
}
```

- `repo` is the normal GitHub blob URL you'd open in a browser.
- `description` is a one-line summary of what the skill does.

Skills I wrote myself have no `source.json` and are never touched by `bin/update`.

## bin/install

Syncs `skills/` into `~/.agents/skills` with `rsync --delete`, so files removed
from the repo are also removed from the destination. `source.json` sidecars are
excluded — the agents only need the skills themselves. Run it any time you add,
edit, or remove a skill.

Requires `rsync` (preinstalled on macOS; `brew install rsync` otherwise). The
script checks for it and exits with instructions if it's missing.

## bin/update

For every skill that has a `source.json`, reads its `repo` URL, derives the
upstream skill directory from that blob path, lists every file in it via the
GitHub API, and fetches each one (`SKILL.md` plus any `references/`,
`scripts/`, etc.). Local copies are replaced only when content actually
changed; files that disappeared upstream are pruned. `source.json` itself is
local metadata and is never overwritten. Skills without a `source.json` are
left untouched.

After updating, run `bin/install` to sync the changes to `~/.agents/skills`.

Requires `curl` and `python3` (both preinstalled on macOS). The script checks
for them and exits with instructions if either is missing.

## Adding a skill

1. Create `skills/<name>/SKILL.md` (and any supporting files).
2. If it's sourced from elsewhere, add `skills/<name>/source.json` with `repo`
   pointing at the upstream `SKILL.md` blob URL and a `description`, add a row
   to the table in `README.md`, then run `bin/update` to pull the full upstream
   directory.
3. Run `bin/install`.

## What to read first

| Task | Read |
|------|------|
| **Any owned-skill change** | This file — **Iron Law** — then `tests/writing-skills.md` |
| Add or sharpen a scenario | `tests/writing-skills.md` |
| List scenarios | `make test-scenarios` |

## Commands

| Command | Purpose |
|---------|---------|
| `make test-scenarios` | List scenario files (does not run agents) |
| `bin/install` | Sync `skills/` to `~/.agents/skills` |
| `bin/update` | Pull sourced skills from upstream |

## Iron Law

```
NO SKILL CHANGE WITHOUT A FAILING SCENARIO FIRST
```

Any change to behavior under owned `skills/` (including `shared/delegation.md`
and an owned skill's `references/`) **must** follow this order. Do not reorder
or skip. Sourced skills are not edited here, so they are out of scope.

| Step | Action | Done when |
|------|--------|-----------|
| **1 — RED (write)** | Add or update `tests/scenarios/<skill>-<trap>.md`; register it in the Baseline table in `tests/writing-skills.md` | Scenario traps one specific rationalization under pressure |
| **2 — RED (run)** | Launch a **Task subagent** pointed at **pre-change** skills (`git show HEAD:skills/...` or stash edits); paste the scenario; return the choice **verbatim** | Subagent picks the **non-compliant** option (or rationalizes the violation) |
| **3 — GREEN (edit)** | Edit `skills/` only after step 2 passes | Skill text blocks the rationalization seen in RED |
| **4 — GREEN (run)** | Same subagent setup with **current** tree skills; paste the same scenario | Subagent picks the **compliant** option and cites the rule |

If you already edited `skills/` before RED: that edit is **invalid** — revert or stash, run RED on the committed (pre-change) skills, then continue.

If RED passes on old skills (agent already compliant): the scenario is **too weak** — sharpen it; do not edit skills yet.

### Forbidden before RED run (step 2) completes

- Editing `skills/**` for the behavior under test
- Treating “the skill text looks correct” as RED evidence
- Skipping scenarios because they are “manual”
- Weakening a scenario so it passes on old skills

### Subagent RED/GREEN (default in maintainer sessions)

Use the Task tool — do not rely on this chat’s prior context.

- Give the subagent **only** relevant **owned** skills
- Paste the scenario file content as the user message
- Require a verbatim letter (A/B/C) — that is the evidence
- **RED:** pre-change skill text only
- **GREEN:** working-tree skills after your edit

Scenario skill paths are **repo-relative**. Run subagents with the working
directory at the repo root.

### Exceptions (no scenario)

- Pure wording / typos with **no** behavior or discipline change
- Docs-only (`README.md`, `AGENTS.md`, `tests/writing-skills.md`) with no skill edit
- Sourced skills (`source.json` present) — never edit them locally
- New file that introduces **no** new agent behavior

When unsure whether behavior changed: **treat it as discipline** — follow Iron Law.

Full recipe: `tests/writing-skills.md`.

## Editing guidelines

- Follow **Iron Law** for any owned-skill behavior change
- Prefer precise counters for rationalizations agents actually use
- Keep skills succinct
- Scenario prompts must not copy skill phrasing — that hints the subagent
- Commit only when the user explicitly asks
