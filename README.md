# Skills

My personal collection of agent skills, shared across my AI agents and
projects. Each skill is a folder in [`skills/`](skills/) with a `SKILL.md`.

## What's inside

**Plan and ship**

- `create-issue` — turn an idea into a GitHub issue.
- `address-issue` — take an issue from first discussion through to a pull request.
- `slice` — cut an issue down to one pull request and file the rest as a new issue.
- `implement` — build a task in small steps, each one reviewed.

**Review code**

- `correctness-review` — look over your changes for real bugs and weak tests.
- `explain-finding` — explain a review finding in plain words, with code.
- `review-loop` — fix the bugs a review finds in a loop, then the cleanups worth doing.
- `thermo-nuclear-code-quality-review` — a very strict review for code that's hard to maintain.

**Design**

- `rehome` — suggest a better home for a concept, module, or repo.

**Verify**

- `create-verification-skill` — build a project skill that drives your app the way a user would.
- `maintain-verification-skill` — keep that skill and its feature list up to date.

**Talk and write**

- `grilling` — push back hard on a plan or idea.
- `handoff` — write a note so another agent can pick up where you left off.
- `bro` — restate the last message in plain words.
- `use-simplified-english` — make replies use Simplified Technical English.

**Docs**

- `tidy-up-agents-md` — split a bloated AGENTS.md into a short index plus linked pages.

Most skills are mine. A few are mirrored from other repos — mattpocock/skills,
cursor/plugins, and a guide from aihero.dev — and each mirrored skill has a
`source.json` showing where it came from.

## Install

Clone the repo, then run the setup script:

```sh
git clone https://github.com/gosukiwi/skills.git ~/gosukiwi-skills
~/gosukiwi-skills/bin/setup-gosukiwi
```

It asks where to put the skills — `~/.claude/skills` for Claude Code, or
`~/.agents/skills` for other agents — then links them in. Running it again is
safe: it only touches the skills it added, and leaves yours alone. Run
`bin/setup-gosukiwi --help` for the options.

To update, `git pull` in the clone and run the script again.

## Maintaining this repo

`bin/install` mirrors `skills/` into `~/.agents/skills` on my own machines, and
deletes anything else there. `bin/update` refreshes the skills that come from
other people. See [AGENTS.md](AGENTS.md).
