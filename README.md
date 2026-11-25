# Skills

This repository holds the agent skills I share across my agents and projects.
Each skill is a folder in [`skills/`](skills/) with a `SKILL.md`.

## What's inside

### Find a skill or set up your agent

- `gosumode` picks the right skill when you describe what you are trying to do.
- `setup-gosumode` prompts you to set model tiers for your agents in
  `.agents/gosumode.toml`.

### Shape and ship work

**Think through an idea**

- `grilling` questions your plan or idea to find weak spots.
- `grill-with-docs` runs `grilling` on a design while updating the project
  glossary and architecture decision records.

**Take one step**

- `create-issue` turns an idea into a GitHub issue.
- `slice` limits an issue or stated scope to one pull request and files the
  remaining work as a new issue.
- `implement` builds a task in small steps and reviews each step with a
  subagent.

**Turn an issue into a pull request**

- `address-issue` runs an issue or stated scope through design questions,
  slicing, implementation, review, and a pull request.
- `yolo-issues` runs `address-issue` across a set of issues on one branch,
  accepts every recommendation, and opens a single pull request.

### Design the system or user interface

- `domain-modeling` maintains a project glossary and records hard-to-reverse
  architecture decisions.
- `prototype` builds a throwaway prototype to test application logic or
  interface design.
- `rehome` proposes a better location for a concept, module, pull request, or
  repository.
- `ui-design` designs or reviews web interfaces for layout, visual hierarchy,
  interaction, and usability.

### Review code or a pull request

- `correctness-review` checks a diff for functional bugs, security issues,
  intent fit, and weak tests.
- `thermo-nuclear-code-quality-review` runs a strict maintainability review for
  abstractions, large files, and complex conditionals.
- `review-pr` checks out a GitHub pull request to verify it and runs
  correctness and quality reviews in parallel. It posts a plain-language review
  after you confirm.
- `review-loop` fixes correctness findings in a loop, applies maintainability
  fixes, and reports what remains.
- `show-diff-in-browser` renders git diffs in a browser tab with word wrap and
  unified or split views.
- `explain-finding` explains a review finding in plain words with a short code
  example.

### Prevent repeat mistakes and maintain the repository

- `correct` finds mistakes agents repeat and prevents them with architecture,
  types, lint rules, or tests.
- `prune-tests` removes tests that guard no behavior.
- `tidy-up-agents-md` splits a long `AGENTS.md` into a short index with linked
  pages.

### Writing and handoffs

- `unslop` removes AI writing patterns from text.
- `bro` restates the last message in plain words without jargon.
- `handoff` writes a handoff file so another agent can continue your session.

I wrote 14 of these skills, and `tidy-up-agents-md` adapts a guide from
aihero.dev. Ten skills come from `mattpocock/skills`, `cursor/plugins`, and
`caldoai/skills`, and each includes a `source.json` file with its upstream URL.

## Install

Clone this repository and run `bin/install`. `bin/install` asks where to place
the skills: `~/.claude/skills` for Claude Code, `~/.agents/skills` for other
agents, `~/.gemini/antigravity-cli/skills` for Antigravity CLI, or all three.

```sh
git clone https://github.com/gosukiwi/skills.git ~/gosukiwi-skills
~/gosukiwi-skills/bin/install
```

`bin/install` symlinks or copies only the skills from this repository and does
not modify existing skills in the target directory, so running `bin/install`
again is safe. Run `bin/install --help` to see all options.

To update, run `git pull` in `~/gosukiwi-skills` and run `bin/install` again.

## Maintaining this repository

`bin/install` symlinks `skills/` into an agent's skills directory and removes
links whose source directory was deleted. `bin/update` downloads updates for
skills that have a `source.json` file. See [AGENTS.md](AGENTS.md).
