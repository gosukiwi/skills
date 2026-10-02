<div align="center">

# 🧠 Skills

**My personal skill library — shared across all my AI agents and projects.**

Skills live under [`skills/`](skills/) and sync to `~/.agents/skills`,
the shared location my agents read from.

</div>

---

## ✨ Skills

### Ship

Turn an idea into a GitHub issue, then take it from scope to a PR — the full pipeline, or one stage of it.

| Skill | Description | Source |
| --- | --- | --- |
| [`create-issue`](skills/create-issue/SKILL.md) | Explore an idea with the user and draft a GitHub issue ready for `address-issue`. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/create-issue/SKILL.md) |
| [`address-issue`](skills/address-issue/SKILL.md) | Take a GitHub issue from grilling through slice, implementation, review, and PR. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/address-issue/SKILL.md) |
| [`slice`](skills/slice/SKILL.md) | Scope a GitHub issue to one PR: file a slice spec, peel leftover work onto a new issue, close the original pointing at both. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/slice/SKILL.md) |
| [`implement`](skills/implement/SKILL.md) | Break a scope into TDD tasks and implement with subagent review. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/implement/SKILL.md) |

### Review

Inspect a branch or diff. `review-loop` also fixes what those reviews find.

| Skill | Description | Source |
| --- | --- | --- |
| [`correctness-review`](skills/correctness-review/SKILL.md) | Review a diff for functional bugs, security, intent fit, and whether tests actually prove the change. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/correctness-review/SKILL.md) |
| [`explain-finding`](skills/explain-finding/SKILL.md) | Explain a review finding in a short, simple way, using code examples. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/explain-finding/SKILL.md) |
| [`review-loop`](skills/review-loop/SKILL.md) | Fix correctness findings in a loop via `correctness-review`, then fix the refactor findings worth fixing and report what's left. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/review-loop/SKILL.md) |
| [`thermo-nuclear-code-quality-review`](skills/thermo-nuclear-code-quality-review/SKILL.md) | Run an extremely strict maintainability review for abstraction quality, giant files, and spaghetti-condition growth. | [cursor/plugins](https://github.com/cursor/plugins/blob/21327bee99f30a73758c99f6c6459571bc9f6e98/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md) |

### Design

Find the concept that has no good home, and propose one.

| Skill | Description | Source |
| --- | --- | --- |
| [`rehome`](skills/rehome/SKILL.md) | Propose one better home for a concept, given a concept, a module, a PR, or a whole repo: where it lives now, where it should live, what moves. | [gosukiwi/skills](https://github.com/gosukiwi/skills/blob/main/skills/rehome/SKILL.md) |

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

## Install these skills

These are personal skills, but you're welcome to use them. The
non-destructive way is to clone the repo and symlink each skill into the
skills directory your agent reads — nothing already there is touched, and a
single `git pull` updates everything.

Claude Code reads personal skills from `~/.claude/skills/`; Codex, Cursor and
the other agents in this repo's setup read the shared `~/.agents/skills/`. Use
whichever your agent loads.

```sh
git clone https://github.com/gosukiwi/skills.git ~/src/skills

REPO="$HOME/src/skills"
DEST="$HOME/.claude/skills"   # or ~/.agents/skills
mkdir -p "$DEST"

for entry in "$REPO"/skills/*; do
  name="$(basename "$entry")"
  if [ -e "$DEST/$name" ] || [ -L "$DEST/$name" ]; then
    echo "skip  $name (already exists)"
  else
    ln -s "$entry" "$DEST/$name"
  fi
done
```

`skills/shared/` has to be linked alongside the skills: `address-issue`,
`review-loop` and `implement` read `shared/delegation.md` and
`shared/subagent-model-size.md` from your skills directory.

Update later with:

```sh
git -C ~/src/skills pull
```

The symlinks point into the clone, so the new files are picked up with no
re-copying. If your setup can't follow symlinks, copy instead
(`cp -R "$REPO"/skills/* "$DEST"/`) and re-run it after each pull.

**Name clashes.** The loop skips any skill whose name already exists in the
destination, so your own skills are never overwritten. To take the repo's
version instead, remove or rename your copy first. Note that under Claude Code
a personal (`~/.claude/skills/`) skill already wins over a project skill of the
same name, so both can coexist — the personal one is the one that runs.

## Maintainer scripts

`bin/install` is how *this* machine stays in sync. It uses `rsync --delete`,
so it makes `~/.agents/skills` an exact mirror of `skills/` and **deletes
anything else** in that directory. Don't hand it to someone else — give them
the install steps above instead.

```sh
bin/install   # mirror skills/ to ~/.agents/skills (destructive)
bin/update    # pull the latest version of sourced skills
```

See [AGENTS.md](AGENTS.md) for how the repo is laid out and how the scripts work.
