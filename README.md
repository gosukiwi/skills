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
| [`handoff`](skills/handoff/SKILL.md) | Compact a conversation into a handoff doc for another agent. | [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md) |
| [`succinct`](skills/succinct/SKILL.md) | Provide a short answer that keeps the same level of detail while being terse and consise. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/succinct/SKILL.md) |
| [`thermo-nuclear-code-quality-review`](skills/thermo-nuclear-code-quality-review/SKILL.md) | Run an extremely strict maintainability review for abstraction quality, giant files, and spaghetti-condition growth. | [cursor/plugins](https://github.com/cursor/plugins/blob/21327bee99f30a73758c99f6c6459571bc9f6e98/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md) |
| [`mini-reviewer`](skills/mini-reviewer/SKILL.md) | Code review across security, correctness, style, refactor, and tests in a single pass. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/mini-reviewer/SKILL.md) |

## Usage

```sh
bin/install   # sync skills to ~/.agents/skills
bin/update    # pull the latest version of sourced skills
```

See [AGENTS.md](AGENTS.md) for how the repo is laid out and how the scripts work.
