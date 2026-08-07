#!/usr/bin/env python3
"""Inserts a nav link to the new 2027 Property Tax calculator right after
the existing Section 24 nav link, across every page that has that nav
(86 files spanning en/zh/ar/hi). Idempotent - skips files that already
have the link. Also updates the two matching footer 'Calculators' columns
where present, using the same insert-after-Section-24 approach.
"""
import glob
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
NEW_HREF = '/property-income-tax-2027-calculator/'

LABELS = {
    'en': '2027 Tax',
    'zh': '2027税',
    'ar': 'ضريبة 2027',
    'hi': '2027 कर',
}

NAV_MARKER = '<a href="/section-24-calculator/">Section 24</a>'
FOOTER_MARKER = '<li><a href="/section-24-calculator/">Section 24</a></li>'


def lang_for(path):
    rel = os.path.relpath(path, ROOT).replace('\\', '/')
    if rel.startswith('zh/'):
        return 'zh'
    if rel.startswith('ar/'):
        return 'ar'
    if rel.startswith('hi/'):
        return 'hi'
    return 'en'


def main():
    files = set(glob.glob(os.path.join(ROOT, '*.html')))
    files |= set(glob.glob(os.path.join(ROOT, '**', 'index.html'), recursive=True))
    changed = 0
    skipped_new_page = 0
    for path in sorted(files):
        rel = os.path.relpath(path, ROOT).replace('\\', '/')
        if 'property-income-tax-2027-calculator' in rel:
            skipped_new_page += 1
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        if NAV_MARKER not in content:
            continue
        if NEW_HREF in content:
            continue

        lang = lang_for(path)
        label = LABELS[lang]
        nav_insert = NAV_MARKER + '\n        <a href="' + NEW_HREF + '">' + label + '</a>'
        content = content.replace(NAV_MARKER, nav_insert, 1)

        if FOOTER_MARKER in content:
            footer_insert = FOOTER_MARKER + '<li><a href="' + NEW_HREF + '">' + label + '</a></li>'
            content = content.replace(FOOTER_MARKER, footer_insert, 1)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        changed += 1
    print('updated', changed, 'files; skipped', skipped_new_page, 'new-page files')


if __name__ == '__main__':
    main()
