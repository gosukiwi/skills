---
name: show-diff-in-browser
description: Render git diffs (working tree, staged, commits, or specific files) in a standalone browser tab with syntax highlighting, word wrap, and unified/split views. Opens via system open or a connected browser tool.
disable-model-invocation: true
---

Render a clean, formatted Git diff in the browser without pushing to GitHub or needing external services.

# When to Use

- When the user asks to "show the diff in the browser", "view diff", or inspect changes visually.
- Reviewing local changes before committing or opening a PR.
- Comparing prose, markdown, or large code changes where terminal diffs are awkward to read.

# Workflow

## 1. Determine the Diff Target

Parse what the user wants to compare:
- **Unstaged changes** (default): `git diff`
- **Staged changes**: `git diff --staged`
- **Latest commit**: `git diff HEAD~1 HEAD`
- **Specific commit**: `git diff <commit>~1 <commit>`
- **Branch comparison**: `git diff <target-branch>...HEAD`
- **Specific file or path**: `git diff [args] -- <path>`

## 2. Generate the Diff HTML

Run the embedded generator script from this skill's directory:

```bash
python3 scripts/generate_diff_html.py --title "<Title>" [git diff arguments...]
```

Or pipe custom diff content directly:

```bash
git diff [args] | python3 scripts/generate_diff_html.py --title "<Title>"
```

The script outputs the file URL (defaulting to `file:///tmp/diff.html`).

Features included in the generated HTML:
- **Unified & Split view toggles** (defaults to Unified for readable prose and code).
- **Line wrapping** enabled so long paragraphs or code lines never require horizontal scrolling.
- **Diff2Html formatting** with GitHub syntax highlighting, plus standalone fallback if offline.

## 3. Open in Browser

Follow this precedence:

1. **System Command**:
   - Run `open /tmp/diff.html` (macOS) or `xdg-open /tmp/diff.html` (Linux).
   - If that succeeds, confirm to the user that the diff was opened in their default browser.
2. **Connected Browser MCP** (if system command fails or environment is sandboxed):
   - Use `create_tab` or `navigate_to_url` (Safari, Chrome, Playwright) with `file:///tmp/diff.html`.
   - Confirm to the user that the tab was opened/refreshed.
3. **Fallback Link**:
   - Always print the clickable Markdown link: `[View Diff in Browser](file:///tmp/diff.html)`.
