# AGENTS.md

A personal library of agent skills. Each skill is a folder in `skills/` holding
a `SKILL.md`; the scripts in `bin/` install them into an agent's skills
directory. Human overview: [`README.md`](README.md).

## Iron Law

```
NO SKILL CHANGE WITHOUT A FAILING SCENARIO FIRST
```

Applies to any behaviour change under an owned skill, `shared/delegation.md`,
`shared/subagent-model-size.md`, or an owned skill's `references/`. Full process
and exceptions: [`tests/writing-skills.md`](tests/writing-skills.md).

## Commands

| Command | Purpose |
|---------|---------|
| `make test-scenarios` | List scenario files (does not run agents) |
| `bin/install` | Install `skills/` into an agent dir (non-destructive) |
| `bin/update` | Pull sourced skills from upstream |

Commit only when the user explicitly asks.

## Where to look

| Topic | File |
|-------|------|
| Repo layout, `shared/`, `source.json`, adding a skill | [`docs/layout.md`](docs/layout.md) |
| What each script does | [`docs/scripts.md`](docs/scripts.md) |
| Writing and running scenarios, the Iron Law steps | [`tests/writing-skills.md`](tests/writing-skills.md) |
