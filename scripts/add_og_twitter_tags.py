"""
One-off script: add complete Open Graph + Twitter Card meta tags to every
page. Derives og:title/og:description from existing og: tags if present,
else falls back to <title>/<meta name="description">. og:url always comes
fresh from the canonical link. Adds a shared og-image.png (1200x630) as
og:image/twitter:image on every page. Strips any existing og:*/twitter:*
tags first so re-running is idempotent and never duplicates tags.

Usage: python scripts/add_og_twitter_tags.py
"""
import glob
import html
import re

OG_IMAGE_URL = "https://propertybrain.uk/assets/og-image.png"

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)">')
CANONICAL_RE = re.compile(r'<link rel="canonical" href="(.*?)">')
OG_TITLE_RE = re.compile(r'<meta property="og:title" content="(.*?)">')
OG_DESC_RE = re.compile(r'<meta property="og:description" content="(.*?)">')
STRIP_OG_TWITTER_RE = re.compile(
    r'<meta (?:property="og:[^"]*"|name="twitter:[^"]*") content="[^"]*">\n?'
)
ICON_LINK_RE = re.compile(r'(<link rel="icon"[^>]*>)')


def escape_attr(text):
    text = html.unescape(text)
    return html.escape(text, quote=True)


def process(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    title_m = TITLE_RE.search(content)
    desc_m = DESC_RE.search(content)
    canonical_m = CANONICAL_RE.search(content)
    og_title_m = OG_TITLE_RE.search(content)
    og_desc_m = OG_DESC_RE.search(content)

    if not canonical_m:
        print("SKIP (no canonical):", path)
        return False

    og_title = og_title_m.group(1) if og_title_m else (title_m.group(1) if title_m else "PropertyBrain")
    og_desc = og_desc_m.group(1) if og_desc_m else (desc_m.group(1) if desc_m else "Free UK property investment calculators.")
    og_url = canonical_m.group(1)

    og_title = escape_attr(og_title)
    og_desc = escape_attr(og_desc)

    # Remove any existing og:*/twitter:* meta tags so this is idempotent.
    content = STRIP_OG_TWITTER_RE.sub("", content)

    block = (
        f'<meta property="og:title" content="{og_title}">\n'
        f'<meta property="og:description" content="{og_desc}">\n'
        f'<meta property="og:url" content="{og_url}">\n'
        f'<meta property="og:type" content="website">\n'
        f'<meta property="og:image" content="{OG_IMAGE_URL}">\n'
        f'<meta property="og:image:width" content="1200">\n'
        f'<meta property="og:image:height" content="630">\n'
        f'<meta name="twitter:card" content="summary_large_image">\n'
        f'<meta name="twitter:title" content="{og_title}">\n'
        f'<meta name="twitter:description" content="{og_desc}">\n'
        f'<meta name="twitter:image" content="{OG_IMAGE_URL}">\n'
    )

    if not ICON_LINK_RE.search(content):
        print("SKIP (no icon anchor):", path)
        return False

    content = ICON_LINK_RE.sub(block + r"\1", content, count=1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    files = sorted(glob.glob("**/index.html", recursive=True))
    files = [f for f in files if not f.startswith(".git")]
    changed = 0
    for f in files:
        if process(f):
            changed += 1
    print(f"Updated {changed}/{len(files)} pages")


if __name__ == "__main__":
    main()
