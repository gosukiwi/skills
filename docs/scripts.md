# Scripts

Two scripts in `bin/`. Both only touch the skills that come from this repo and
leave everything else in the destination alone.

## bin/install

Installs every entry in `skills/` (including `shared/`) into an agent's skills
directory. The default destination is `~/.agents/skills`; `--claude` is
shorthand for `~/.claude/skills`, and `--dest DIR` picks anywhere else.
`--copy` copies instead of symlinking, and `--update` runs `git pull --ff-only`
first.

Safe to re-run. It refreshes what it installed, skips any name it didn't create,
and prunes links whose source has disappeared from the repo — nothing else in
the destination is touched. `--force` replaces whatever sits at a matching name;
use it once to migrate a destination that the old `rsync`-based install filled
with real copies.

Links point into the checkout, so `git pull` updates them. `--copy` snapshots
instead and records what it installed in `<dest>/.install-skills-manifest`, so a
re-run can refresh and prune those copies too.

Requires `ln` (or `cp` with `--copy`); `--update` additionally requires `git`.

## bin/update

For every skill that has a `source.json`, reads its `repo` URL, derives the
upstream skill directory from that blob path, lists every file in it via the
GitHub API, and fetches each one (`SKILL.md` plus any `references/`, `scripts/`,
etc.). Local copies are replaced only when content actually changed; files that
disappeared upstream are pruned. `source.json` itself is local metadata and is
never overwritten. Skills without a `source.json` are left untouched.

After updating, run `bin/install` to sync the changes.

Requires `curl` and `python3` (both preinstalled on macOS). The script checks
for them and exits with instructions if either is missing.
