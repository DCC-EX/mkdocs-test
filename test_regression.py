from pathlib import Path
import re
import sys

html_path = Path("site/products/ex-commandstation/exrail/cookbooks/driving-trains/passing-loop/index.html")
css_path = Path("site/_static/css/dccex_theme.css")

if not html_path.exists():
    print(f"Missing expected page: {html_path}")
    sys.exit(1)
if not css_path.exists():
    print(f"Missing expected stylesheet: {css_path}")
    sys.exit(1)

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Ensure the first rendered code block is still multiline in generated HTML.
match = re.search(r'<div class="language-\w+ highlight"><pre><span></span><code>(.*?)</code></pre></div>', html, re.DOTALL)
if not match:
    print("Could not locate a rendered fenced code block in passing-loop page")
    # Let's look for what we actually have
    highlight_match = re.search(r'<div class="highlight">(.*?)</div>', html, re.DOTALL)
    if highlight_match:
        print("\nFound highlight div with content (first 500 chars):")
        content = highlight_match.group(1)[:500]
        print(content)
        print("\n...")
    else:
        print("\nNo highlight divs found at all")
    sys.exit(1)
if "\n" not in match.group(1):
    print("Rendered fenced code block no longer contains line breaks")
    sys.exit(1)

# Ensure our CSS safeguard that preserves preformatted line breaks is present.
if "white-space: pre !important;" not in css:
    print("Missing white-space safeguard for code blocks in compiled CSS")
    sys.exit(1)

print("Regression checks passed: multiline code block and CSS safeguard present")
