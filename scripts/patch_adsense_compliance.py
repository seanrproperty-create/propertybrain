#!/usr/bin/env python3
"""AdSense compliance sweep across every static page:
1. Consent Mode v2 default-denied block, inserted right after <head>.
2. Footer operator line ("PropertyBrain.uk is operated by EIGHTFINITY LTD...").
   Handles two observed footer shapes: pages with an existing
   .footer-bottom div (append a new line there) and pages without one
   (insert a new .footer-bottom div right before </footer>'s closing tag).
Idempotent -- safe to re-run. Does NOT touch the cookie-banner markup
itself (already present on every page) or assets/js/calculators*.js
(patched separately, see patch_adsense_consent_js.py).
"""
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONSENT_BLOCK = '''<head>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('consent','default',{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied','analytics_storage':'denied'});</script>'''

OPERATOR_LINE = 'PropertyBrain.uk is operated by EIGHTFINITY LTD, a registered company in the United Kingdom.'

changed_files = []
skipped_files = []

for path in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
    if ".tmp.driveupload" in path:
        continue
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    original = html
    notes = []

    # --- 1. Consent Mode v2 default block ---
    if "gtag('consent','default'" not in html and "gtag('consent', 'default'" not in html:
        if "<head>" in html:
            html = html.replace("<head>", CONSENT_BLOCK, 1)
            notes.append("consent-default")
        else:
            notes.append("SKIPPED consent-default: no <head> tag found")

    # --- 2. Footer operator line ---
    if "operated by EIGHTFINITY LTD" not in html:
        if '<div class="footer-bottom">' in html:
            # Existing footer-bottom div: prepend a new line inside it.
            marker = '<div class="footer-bottom">'
            html = html.replace(
                marker,
                marker + f'\n      <span>{OPERATOR_LINE}</span>',
                1,
            )
            notes.append("footer-line (appended to existing footer-bottom)")
        elif "</footer>" in html:
            # No footer-bottom div on this page's footer -- add one just
            # before the footer closes. Handles both the multi-line and
            # single-line-squished footer markup styles seen across pages.
            html = html.replace(
                "</footer>",
                f'  <div class="footer-bottom"><span>{OPERATOR_LINE}</span></div>\n</footer>',
                1,
            )
            notes.append("footer-line (new footer-bottom div inserted)")
        else:
            notes.append("SKIPPED footer-line: no </footer> found")

    if html != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        rel = os.path.relpath(path, ROOT)
        changed_files.append((rel, notes))
    elif any("SKIPPED" in n for n in notes):
        rel = os.path.relpath(path, ROOT)
        skipped_files.append((rel, notes))

print(f"Patched {len(changed_files)} file(s):")
for rel, notes in changed_files:
    print(f"  {rel}: {', '.join(notes)}")

if skipped_files:
    print(f"\nSKIPPED / needs manual review ({len(skipped_files)}):")
    for rel, notes in skipped_files:
        print(f"  {rel}: {', '.join(notes)}")
