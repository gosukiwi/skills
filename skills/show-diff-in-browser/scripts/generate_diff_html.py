#!/usr/bin/env python3
"""
Generate a clean, standalone HTML diff viewer using diff2html with line-wrapping
and a Unified/Split view toggle.

Usage:
    git diff | python3 generate_diff_html.py
    python3 generate_diff_html.py [git diff arguments...]
    python3 generate_diff_html.py --output /tmp/custom.html HEAD~1 HEAD
    python3 generate_diff_html.py --title "My Changes" path/to/file.md
"""

import sys
import os
import argparse
import subprocess
import json

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/diff2html/bundles/css/diff2html.min.css" />
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/diff2html/bundles/js/diff2html-ui.min.js"></script>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 24px 32px;
      background-color: #f6f8fa;
      color: #1f2328;
    }}
    .header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 16px;
      border-bottom: 1px solid #d0d7de;
    }}
    .header h1 {{
      font-size: 20px;
      margin: 0 0 4px 0;
      font-weight: 600;
    }}
    .header .meta {{
      font-size: 13px;
      color: #656d76;
    }}
    .btn-group {{
      display: inline-flex;
      background: #eef1f4;
      border-radius: 6px;
      padding: 2px;
      border: 1px solid #d0d7de;
    }}
    .btn {{
      border: none;
      background: transparent;
      padding: 5px 12px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      border-radius: 4px;
      color: #57606a;
    }}
    .btn.active {{
      background: #ffffff;
      color: #1f2328;
      box-shadow: 0 1px 2px rgba(0,0,0,0.12);
    }}
    /* Clean wrapping rules for readable prose & code */
    .d2h-code-line,
    .d2h-code-side-line {{
      white-space: normal !important;
      display: block !important;
      line-height: 1.5 !important;
    }}
    .d2h-code-line-ctn {{
      white-space: pre-wrap !important;
      word-break: break-word !important;
      display: inline !important;
    }}
    .d2h-file-side-diff {{
      width: 50% !important;
    }}
    /* Offline fallback styling */
    pre.raw-diff {{
      background: white;
      border: 1px solid #d0d7de;
      border-radius: 6px;
      padding: 16px;
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
      font-size: 13px;
      line-height: 1.5;
      white-space: pre-wrap;
      word-break: break-word;
    }}
    .diff-add {{ background-color: #e6ffec; color: #1a7f37; }}
    .diff-del {{ background-color: #ffebe9; color: #cf222e; }}
  </style>
</head>
<body>
  <div class="header">
    <div>
      <h1>{title}</h1>
      <div class="meta">{subtitle}</div>
    </div>
    <div class="btn-group">
      <button id="btn-unified" class="btn active" onclick="setMode('line-by-line')">Unified</button>
      <button id="btn-split" class="btn" onclick="setMode('side-by-side')">Split</button>
    </div>
  </div>
  <div id="diff-ui"></div>
  <script id="diff-raw" type="text/plain">{diff_content}</script>
  <script>
    let currentMode = "line-by-line";
    const raw = document.getElementById("diff-raw").textContent;
    const targetElement = document.getElementById("diff-ui");

    function renderDiff() {{
      if (typeof Diff2HtmlUI !== "undefined") {{
        targetElement.innerHTML = "";
        const configuration = {{
          drawFileList: false,
          matching: "words",
          outputFormat: currentMode,
          highlight: true,
          renderNothingWhenEmpty: false
        }};
        const diff2htmlUi = new Diff2HtmlUI(targetElement, raw, configuration);
        diff2htmlUi.draw();
        diff2htmlUi.highlightCode();
      }} else {{
        const lines = raw.split("\\n").map(l => {{
          let cls = "";
          if (l.startsWith("+") && !l.startsWith("+++")) cls = "diff-add";
          else if (l.startsWith("-") && !l.startsWith("---")) cls = "diff-del";
          const safe = l.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
          return cls ? `<div class="${{cls}}">${{safe}}</div>` : `<div>${{safe || "&nbsp;"}}</div>`;
        }}).join("");
        targetElement.innerHTML = `<pre class="raw-diff">${{lines}}</pre>`;
      }}
    }}

    function setMode(mode) {{
      currentMode = mode;
      document.getElementById("btn-unified").classList.toggle("active", mode === "line-by-line");
      document.getElementById("btn-split").classList.toggle("active", mode === "side-by-side");
      renderDiff();
    }}

    if (document.readyState === "loading") {{
      document.addEventListener("DOMContentLoaded", renderDiff);
    }} else {{
      renderDiff();
    }}
  </script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(
        description="Generate an HTML diff viewer with line-wrap and split/unified toggles."
    )
    parser.add_argument(
        "-o", "--output",
        default="/tmp/diff.html",
        help="Path to output HTML file (default: /tmp/diff.html)"
    )
    parser.add_argument(
        "-t", "--title",
        default="Diff Viewer",
        help="Title shown on the diff page"
    )
    parser.add_argument(
        "git_args",
        nargs=argparse.REMAINDER,
        help="Arguments to pass to 'git diff' if diff is not piped via stdin"
    )

    args = parser.parse_args()

    # Determine if input is from pipe or git command
    if not sys.stdin.isatty():
        diff_text = sys.stdin.read()
        subtitle = "Piped diff stream"
    else:
        git_cmd = ["git", "diff"] + args.git_args
        try:
            diff_text = subprocess.check_output(git_cmd, text=True)
            subtitle = "git " + " ".join(args.git_args) if args.git_args else "Working directory changes (git diff)"
        except subprocess.CalledProcessError as e:
            sys.stderr.write(f"Error running git diff: {e}\n")
            sys.exit(e.returncode)

    if not diff_text.strip():
        diff_text = "(No changes detected)"
        subtitle = "Empty diff"

    html = HTML_TEMPLATE.format(
        title=args.title,
        subtitle=subtitle,
        diff_content=diff_text
    )

    output_path = os.path.abspath(args.output)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    # Output file URI
    print(f"file://{output_path}")


if __name__ == "__main__":
    main()
