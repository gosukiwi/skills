<div align="center">

# 🧠 Skills

**My personal skill library — shared across all my AI agents and projects.**

Skills live under [`skills/`](skills/) and sync to `~/.agents/skills`,
the shared location my agents read from.

</div>

---

## ✨ Skills

| Skill | Description | Source |
| --- | --- | --- |
| [`bro`](skills/bro/SKILL.md) | Restate the last message in plain human language, with no jargon. | [cursor/plugins](https://github.com/cursor/plugins/blob/main/pstack/skills/bro/SKILL.md) |
| [`create-verification-skill`](skills/create-verification-skill/SKILL.md) | Generate a project-local skill that drives the app the way a user does and proves behavior with evidence. | [cursor/plugins](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/SKILL.md) |
| [`flow-debug`](skills/flow-debug/SKILL.md) | Investigate bugs before fixing. Write a RED test that confirms the issue, then stop. | [gosukiwi/flow](https://github.com/gosukiwi/flow/blob/main/skills/flow-debug/SKILL.md) |
| [`flow-patch`](skills/flow-patch/SKILL.md) | Small bounded change with micro-spec, subagent TDD, and per-task review. | [gosukiwi/flow](https://github.com/gosukiwi/flow/blob/main/skills/flow-patch/SKILL.md) |
| [`flow-shared`](skills/flow-shared/SKILL.md) | Shared prompts and references for the flow skills. Not invoked directly. | [gosukiwi/flow](https://github.com/gosukiwi/flow/blob/main/skills/flow-shared/SKILL.md) |
| [`flow-spec`](skills/flow-spec/SKILL.md) | Spec + plan + subagent TDD tasks for multi-step features. | [gosukiwi/flow](https://github.com/gosukiwi/flow/blob/main/skills/flow-spec/SKILL.md) |
| [`grilling`](skills/grilling/SKILL.md) | Grill the user relentlessly about a plan, decision, or idea. | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) |
| [`handoff`](skills/handoff/SKILL.md) | Compact a conversation into a handoff doc for another agent. | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md) |
| [`maintain-verification-skill`](skills/maintain-verification-skill/SKILL.md) | Keep a project's verification skill and feature map honest with source and live coverage. | [cursor/plugins](https://github.com/cursor/plugins/blob/main/pstack/skills/maintain-verification-skill/SKILL.md) |
| [`pr-stabilization`](skills/pr-stabilization/SKILL.md) | Run adversarial red/blue self-review cycles on a change until only nits remain, before asking for human review. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/pr-stabilization/SKILL.md) |
| [`review-loop`](skills/review-loop/SKILL.md) | Clear correctness blockers in a loop, then report leftover findings and a refactor review. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/review-loop/SKILL.md) |
| [`thermo-nuclear-code-quality-review`](skills/thermo-nuclear-code-quality-review/SKILL.md) | Run an extremely strict maintainability review for abstraction quality, giant files, and spaghetti-condition growth. | [cursor/plugins](https://github.com/cursor/plugins/blob/21327bee99f30a73758c99f6c6459571bc9f6e98/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md) |

## Usage

```sh
bin/install   # sync skills to ~/.agents/skills
bin/update    # pull the latest version of sourced skills
```

See [AGENTS.md](AGENTS.md) for how the repo is laid out and how the scripts work.
