# AGENTS.md

Working notes for this repo: how it's laid out and how the scripts behave.

## Layout

```
skills/
  <skill-name>/
    SKILL.md
    source.json   (only for skills sourced from elsewhere)
```

Each skill is a directory containing a `SKILL.md` (plus any supporting files).
`SKILL.md` is kept as a pristine mirror of its upstream — no local edits.

## source.json

Skills sourced from elsewhere carry a `source.json` sidecar that records where
the `SKILL.md` came from:

```json
{
  "description": "Compact a conversation into a handoff doc.",
  "repo": "https://github.com/<user>/<repo>/blob/<branch>/path/to/SKILL.md"
}
```

- `repo` is the normal GitHub blob URL you'd open in a browser.
- `description` is a one-line summary of what the skill does.

Skills I wrote myself have no `source.json` and are never touched by `bin/update`.

## bin/install

Syncs `skills/` into `~/.agents/skills` with `rsync --delete`, so files removed
from the repo are also removed from the destination. `source.json` sidecars are
excluded — the agents only need the skills themselves. Run it any time you add,
edit, or remove a skill.

Requires `rsync` (preinstalled on macOS; `brew install rsync` otherwise). The
script checks for it and exits with instructions if it's missing.

## bin/update

For every skill that has a `source.json`, reads its `repo` URL, derives the
matching raw URL (`github.com/.../blob/...` → `raw.githubusercontent.com/...`),
fetches the latest `SKILL.md`, and replaces the local copy only if the content
actually changed. Skills without a `source.json` are left untouched.

After updating, run `bin/install` to sync the changes to `~/.agents/skills`.

Requires `curl` (preinstalled on macOS). The script checks for it and exits with
instructions if it's missing.

## Adding a skill

1. Create `skills/<name>/SKILL.md`.
2. If it's sourced from elsewhere, add `skills/<name>/source.json` with `repo`
   and `description`, and add a row to the table in `README.md`.
3. Run `bin/install`.
