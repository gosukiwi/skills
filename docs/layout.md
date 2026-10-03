# Repo layout

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

Each skill is a directory holding a `SKILL.md`, plus any supporting files such
as `references/` or `scripts/`.

## Owned vs sourced

**Owned** skills have no `source.json`. They are mine to edit, and the only ones
that get scenarios:

`address-issue`, `correctness-review`, `create-issue`, `explain-finding`,
`implement`, `slice`, `rehome`, `review-loop`, `tidy-up-agents-md`,
`use-simplified-english`.

**Sourced** skills are a pristine mirror of their upstream directory — never
edit them locally, and never add scenarios for them:

`bro`, `create-verification-skill`, `grilling`, `handoff`,
`maintain-verification-skill`, `thermo-nuclear-code-quality-review`.

## skills/shared

Prompts that several skills reuse. `shared/` holds plain markdown, not skills:
it has no `SKILL.md`, so agents never load it as a skill or expose it as a slash
command. Skills reach these files by path — see `shared/delegation.md`, which is
how one skill runs another.

`shared/delegation.md` and `shared/subagent-model-size.md` are owned, so both
fall under the Iron Law.

## source.json

Skills sourced from elsewhere carry a `source.json` sidecar recording where the
`SKILL.md` came from:

```json
{
  "description": "Compact a conversation into a handoff doc.",
  "repo": "https://github.com/<user>/<repo>/blob/<branch>/path/to/SKILL.md"
}
```

- `repo` is the normal GitHub blob URL you'd open in a browser.
- `description` is a one-line summary of what the skill does.

Skills I wrote myself have no `source.json` and are never touched by
`bin/update`.

## Adding a skill

1. Create `skills/<name>/SKILL.md` (and any supporting files).
2. If it's sourced from elsewhere, add `skills/<name>/source.json` with `repo`
   pointing at the upstream `SKILL.md` blob URL and a `description`, add it to
   the list in `README.md`, then run `bin/update` to pull the full upstream
   directory.
3. Run `bin/install` (see [`scripts.md`](scripts.md)).
