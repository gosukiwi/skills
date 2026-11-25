# Skills

My personal collection of agent skills, shared across my AI agents and
projects. Each skill is a folder in [`skills/`](skills/) with a `SKILL.md`.

## What's inside

### Find a skill or set up your agent

- `gosumode` — describe what you're trying to do; it points you at the right skill.
- `setup-gosumode` — choose model tiers for your harnesses through a short setup wizard.

### Shape and ship work

**Think through an idea**

- `grilling` — push back hard on a plan or idea.
- `grill-with-docs` — push back on a design and write the glossary and ADRs as you go.

**Take one step**

- `create-issue` — turn an idea into a GitHub issue.
- `slice` — cut an issue or stated scope down to one pull request and file the rest as a new issue.
- `implement` — build a task in small steps, each one reviewed.

**Go from issue to pull request**

- `address-issue` — take an issue or stated scope from first discussion through to a pull request.
- `yolo-issues` — run `address-issue` over a set of issues into one review branch, then open a single PR, accepting every recommendation.

### Design the system or UI

- `domain-modeling` — keep a project glossary and record hard-to-reverse decisions (ADRs).
- `prototype` — build a throwaway prototype to answer a question about application logic or UI design.
- `rehome` — suggest a better home for a concept, module, or repo.
- `ui-design` — design, refine, or review web interfaces for layout, visual hierarchy, interaction, and usability.

### Review code or a pull request

- `correctness-review` — look over your changes for real bugs and weak tests.
- `thermo-nuclear-code-quality-review` — a very strict review for code that's hard to maintain.
- `review-pr` — verify a GitHub PR, run parallel correctness and quality reviews, and post a confirmed plain-language review.
- `review-loop` — fix the bugs a review finds in a loop, then the cleanups worth doing.
- `show-diff-in-browser` — render git diffs in the browser with word wrap and unified/split views.
- `explain-finding` — explain a review finding in plain words, with code.

### Prevent repeat mistakes and maintain the repo

- `correct` — find mistakes agents keep repeating and prevent them with architecture, types, lint, or tests.
- `prune-tests` — prune tests that guard no behavior.
- `tidy-up-agents-md` — split a bloated AGENTS.md into a short index plus linked pages.

### Write, explain, or hand off

- `unslop` — cut AI tells from any writing.
- `bro` — restate the last message in plain words.
- `handoff` — write a note so another agent can pick up where you left off.

Most skills are mine. A few are mirrored from other repos — mattpocock/skills,
cursor/plugins, caldoai/skills, and a guide from aihero.dev — and each mirrored
skill has a `source.json` showing where it came from.

## Install

Clone the repo, then run the install script — it asks where to put the skills:
Claude Code's `~/.claude/skills`, other agents' `~/.agents/skills`,
Antigravity CLI's `~/.gemini/antigravity-cli/skills`, or all of them.

```sh
git clone https://github.com/gosukiwi/skills.git ~/gosukiwi-skills
~/gosukiwi-skills/bin/install
```

It only touches the skills it installs and leaves everything else alone, so
running it again is safe. Run `bin/install --help` for the options.

To update, `git pull` in the clone and run it again.

## Maintaining this repo

`bin/install` links `skills/` into an agent's skills directory, touching only
the skills it installed. `bin/update` refreshes the skills that come from other
people. See [AGENTS.md](AGENTS.md).
