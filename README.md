<div align="center">

# 🧠 Skills

**My personal skill library — shared across all my AI agents and projects.**

Skills live under [`skills/`](skills/) and sync to `~/.agents/skills`,
the shared location my agents read from.

</div>

---

## ✨ Skills

### Ship

Take a GitHub issue from scope to a PR — the full pipeline, or one stage of it.

| Skill | Description | Source |
| --- | --- | --- |
| [`address-issue`](skills/address-issue/SKILL.md) | Take a GitHub issue from grilling through plan, implementation, review, and PR. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/address-issue/SKILL.md) |
| [`plan`](skills/plan/SKILL.md) | Scope one PR from a GitHub issue or this session — open a GitHub issue for that PR, and a leftover issue if needed. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/plan/SKILL.md) |
| [`implement`](skills/implement/SKILL.md) | Break a scope into TDD tasks and implement with subagent review. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/implement/SKILL.md) |

### Review

Inspect a branch or diff. `review-loop` also fixes what those reviews find.

| Skill | Description | Source |
| --- | --- | --- |
| [`correctness-review`](skills/correctness-review/SKILL.md) | Review a diff for functional bugs, security, intent fit, and whether tests actually prove the change. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/correctness-review/SKILL.md) |
| [`review-loop`](skills/review-loop/SKILL.md) | Fix correctness findings in a loop via `correctness-review`, then fix the refactor findings worth fixing and report what's left. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/review-loop/SKILL.md) |
| [`thermo-nuclear-code-quality-review`](skills/thermo-nuclear-code-quality-review/SKILL.md) | Run an extremely strict maintainability review for abstraction quality, giant files, and spaghetti-condition growth. | [cursor/plugins](https://github.com/cursor/plugins/blob/21327bee99f30a73758c99f6c6459571bc9f6e98/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md) |

### Verify

Generate and keep honest a project-local skill that drives the app the way a user does.

| Skill | Description | Source |
| --- | --- | --- |
| [`create-verification-skill`](skills/create-verification-skill/SKILL.md) | Generate a project-local skill that drives the app the way a user does and proves behavior with evidence. | [cursor/plugins](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/SKILL.md) |
| [`maintain-verification-skill`](skills/maintain-verification-skill/SKILL.md) | Keep a project's verification skill and feature map honest with source and live coverage. | [cursor/plugins](https://github.com/cursor/plugins/blob/main/pstack/skills/maintain-verification-skill/SKILL.md) |

### Communicate

How the session thinks with you, how it writes, and how it hands off.

| Skill | Description | Source |
| --- | --- | --- |
| [`grilling`](skills/grilling/SKILL.md) | Grill the user relentlessly about a plan, decision, or idea. | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) |
| [`handoff`](skills/handoff/SKILL.md) | Compact a conversation into a handoff doc for another agent. | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md) |
| [`bro`](skills/bro/SKILL.md) | Restate the last message in plain human language, with no jargon. | [cursor/plugins](https://github.com/cursor/plugins/blob/main/pstack/skills/bro/SKILL.md) |
| [`use-simplified-english`](skills/use-simplified-english/SKILL.md) | Make the session respond in Simplified Technical English (ASD-STE100). | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/use-simplified-english/SKILL.md) |

### Docs

| Skill | Description | Source |
| --- | --- | --- |
| [`tidy-up-agents-md`](skills/tidy-up-agents-md/SKILL.md) | Refactor an `AGENTS.md` into a minimal root file plus linked topic docs, following progressive disclosure. | [aihero.dev](https://www.aihero.dev/a-complete-guide-to-agents-md) |

## Usage

```sh
bin/install   # sync skills to ~/.agents/skills
bin/update    # pull the latest version of sourced skills
```

See [AGENTS.md](AGENTS.md) for how the repo is laid out and how the scripts work.
