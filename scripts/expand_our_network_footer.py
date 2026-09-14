"""
One-off script: make the "Our Network" footer block genuinely site-wide.

Prior state: the block existed on only 1 of 100 pages (the homepage), despite
earlier records describing it as site-wide. This adds it to every other page's
footer (99 files), and adds a bestgiftsfor.net entry to the network list
everywhere (it was missing even from the homepage's existing block).

Network links are absolute external URLs, so the same markup is valid at any
folder depth (en/ar/hi/zh, any subfolder) -- no relative-path handling needed.

Idempotent: pages that already have "Our Network" are left alone except for
the bestgiftsfor.net addition, which is itself skipped if already present.

Usage: python scripts/expand_our_network_footer.py
"""
import glob
import re

FOOTER_LINKS_RE = re.compile(r'<div class="footer-links">.*?</div>', re.S)

NETWORK_BLOCK = (
    '<div class="footer-links"><h4>Our Network</h4><ul>'
    '<li><a href="https://propertyalert.uk" target="_blank" rel="noopener">'
    'PropertyAlert (off-market property deal alerts)</a></li>'
    '<li><a href="https://howmuchismyhomeworth.uk" target="_blank" rel="noopener">'
    'HowMuchIsMyHomeWorth (instant home valuation)</a></li>'
    '<li><a href="https://groundlayer.co.uk" target="_blank" rel="noopener">'
    'Groundlayer (structural trade specialist directory)</a></li>'
    '<li><a href="https://bestgiftsfor.net" target="_blank" rel="noopener">'
    'BestGiftsFor (AI-powered gift finder)</a></li>'
    '</ul></div>'
)

BESTGIFTSFOR_LI = (
    '<li><a href="https://bestgiftsfor.net" target="_blank" rel="noopener">'
    'BestGiftsFor (AI-powered gift finder)</a></li>'
)

# Anchor for adding bestgiftsfor.net to an EXISTING Our Network block
# (only the homepage has one going in).
GROUNDLAYER_LI = (
    '<li><a href="https://groundlayer.co.uk" target="_blank" rel="noopener">'
    'Groundlayer (structural trade specialist directory)</a></li>'
)


def process(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if "Our Network" in content:
        if "bestgiftsfor.net" in content:
            print("SKIP (already complete):", path)
            return False
        if GROUNDLAYER_LI not in content:
            print("SKIP (Our Network present but anchor not found -- check manually):", path)
            return False
        content = content.replace(GROUNDLAYER_LI, GROUNDLAYER_LI + BESTGIFTSFOR_LI, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Added bestgiftsfor.net to existing Our Network block:", path)
        return True

    matches = list(FOOTER_LINKS_RE.finditer(content))
    if not matches:
        print("SKIP (no footer-links div found):", path)
        return False

    insert_at = matches[-1].end()
    content = content[:insert_at] + NETWORK_BLOCK + content[insert_at:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Added Our Network block:", path)
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
