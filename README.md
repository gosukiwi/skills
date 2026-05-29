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

## Install

Sync this repo's `skills/` into `~/.agents/skills`:

```sh
bin/install
```

This mirrors the folder with `rsync --delete`, so files removed from the repo
are also removed from `~/.agents/skills`. `source.json` sidecars are excluded —
the agents only need the skills themselves. Run it again any time you add, edit,
or remove a skill.

> [!NOTE]
> Requires `rsync` (preinstalled on macOS). If it's missing: `brew install rsync`.
> The script checks for it and exits with instructions.

## Layout

```
skills/
  <skill-name>/
    SKILL.md
    source.json   (only for skills sourced from elsewhere)
```

Each skill is a directory containing a `SKILL.md` (plus any supporting files).
`SKILL.md` is kept as a pristine mirror of its upstream — no local edits.

Skills sourced from elsewhere carry a `source.json` sidecar that records where
the `SKILL.md` came from:

```json
{
  "description": "Compact a conversation into a handoff doc.",
  "repo": "https://github.com/<user>/<repo>/blob/<branch>/path/to/SKILL.md"
}
```

`repo` is the normal GitHub page you'd open in a browser, and `description` is a
one-line summary of what the skill does. `bin/update` uses `repo` to pull in
upstream changes (see below). Skills I wrote myself have no `source.json`.

## Update

Pull the latest upstream version of each skill:

```sh
bin/update
```

For every skill that has a `source.json`, this reads its `repo` URL, derives the
matching raw URL, fetches the latest `SKILL.md`, and replaces the local copy
only if the content actually changed. Skills without a `source.json` are left
untouched.

> [!TIP]
> After updating, run `bin/install` to sync the changes to `~/.agents/skills`.
