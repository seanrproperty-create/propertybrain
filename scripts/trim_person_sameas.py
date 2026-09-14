"""
One-off script: trim the founder Person schema sameAs list to LinkedIn only,
per the 2026-09-13 seo-audit skill update (Snapchat/Mastodon excluded
portfolio-wide; TikTok/Facebook optional-only-if-active; Sean confirmed
PropertyBrain should drop TikTok/Snapchat/Mastodon for consistency).

Applies across all 4 language About pages (en/ar/hi/zh). Idempotent: if the
old sameAs array isn't found (already trimmed), the file is skipped.

Usage: python scripts/trim_person_sameas.py
"""
import re

OLD_SAMEAS = (
    '"sameAs":["https://www.linkedin.com/in/sean-ramdin-736880413/",'
    '"https://www.tiktok.com/@seanr1970","https://www.snapchat.com/add/sean700918",'
    '"https://mastodon.social/@sean70"]'
)
NEW_SAMEAS = '"sameAs":["https://www.linkedin.com/in/sean-ramdin-736880413/"]'

FILES = [
    "about/index.html",
    "ar/about/index.html",
    "hi/about/index.html",
    "zh/about/index.html",
]


def main():
    changed = 0
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            content = f.read()
        if OLD_SAMEAS not in content:
            print("SKIP (already trimmed or not found):", path)
            continue
        content = content.replace(OLD_SAMEAS, NEW_SAMEAS)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        changed += 1
        print("Trimmed:", path)
    print(f"Updated {changed}/{len(FILES)} pages")


if __name__ == "__main__":
    main()
