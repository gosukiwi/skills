# AGENTS.md

Working notes for this repo: how it's laid out and how the scripts behave.

## Layout

```
skills/
  <skill-name>/
    SKILL.md
    source.json   (only for skills sourced from elsewhere)
  shared/
    <prompt>.md   (shared prompts, not skills)
```

Each skill is a directory containing a `SKILL.md` (plus any supporting
files such as `references/` or `scripts/`). Sourced skills are kept as a
pristine mirror of their upstream directory — no local edits.

## skills/shared

Prompts that several skills reuse. `shared/` holds plain markdown, not skills:
it has no `SKILL.md`, so agents never load it as a skill or expose it as a
slash command. Skills reach these files by path — see `shared/delegation.md`,
which is how one skill runs another.

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
upstream skill directory from that blob path, lists every file in it via the
GitHub API, and fetches each one (`SKILL.md` plus any `references/`,
`scripts/`, etc.). Local copies are replaced only when content actually
changed; files that disappeared upstream are pruned. `source.json` itself is
local metadata and is never overwritten. Skills without a `source.json` are
left untouched.

After updating, run `bin/install` to sync the changes to `~/.agents/skills`.

Requires `curl` and `python3` (both preinstalled on macOS). The script checks
for them and exits with instructions if either is missing.

## Adding a skill

1. Create `skills/<name>/SKILL.md` (and any supporting files).
2. If it's sourced from elsewhere, add `skills/<name>/source.json` with `repo`
   pointing at the upstream `SKILL.md` blob URL and a `description`, add a row
   to the table in `README.md`, then run `bin/update` to pull the full upstream
   directory.
3. Run `bin/install`.
