# Skills

My personal skill folder, used across all my AI agents and projects.

Skills live under `skills/` in this repo and are synced to `~/.agents/skills`,
the shared location my agents read from.

## Layout

```
skills/
  <skill-name>/
    SKILL.md
```

Each skill is a directory containing a `SKILL.md` (plus any supporting files).

## Install

Sync this repo's `skills/` into `~/.agents/skills`:

```sh
bin/install
```

This mirrors the folder with `rsync --delete`, so files removed from the repo
are also removed from `~/.agents/skills`. Run it again any time you add, edit,
or remove a skill.

### Requirements

`rsync` must be installed. On macOS:

```sh
brew install rsync
```

The install script checks for `rsync` and exits with instructions if it's
missing.
