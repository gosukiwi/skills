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

Skills sourced from elsewhere end their `SKILL.md` with a `## Source` table:

```
## Source

| Name | Description | Repo |
| --- | --- | --- |
| handoff | Compact a conversation into a handoff doc. | https://github.com/<user>/<repo>/blob/<branch>/path/to/SKILL.md |
```

The `Repo` URL is the normal GitHub page you'd open in a browser, and the
`Description` is a one-line summary of what the skill does. `bin/update` uses
the URL to pull in upstream changes (see below).

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

## Update

Pull the latest upstream version of each skill:

```sh
bin/update
```

For every `skills/*/SKILL.md`, this reads the GitHub URL from the `## Source`
table, derives the matching raw URL, fetches the latest content, and writes it
back — re-appending the local `## Source` table so it survives the update.
Skills without a `## Source` table (i.e. ones I wrote myself) are skipped.

After updating, run `bin/install` to sync the changes to `~/.agents/skills`.

### Requirements

`curl` must be installed (it ships with macOS). The script checks for it and
exits with instructions if it's missing.
