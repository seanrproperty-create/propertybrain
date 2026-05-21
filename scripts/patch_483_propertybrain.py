"""
Brief 483 — propertybrain.uk GSC: fix "Discovered — not indexed" for 16 pages.

Root cause: inner pages had truncated footers with only 4-8 links; /contact/ and
/cookies/ were not linked from ANY inner page, so Googlebot had no referring path.

Fix: replace every page's footer with a complete footer containing all 20 sitemap
pages, ensuring every page on the site links to every other page.

Run: python3 scripts/patch_483_propertybrain.py
     (No --prod flag — deploys via git push to Cloudflare Pages)
"""
import os, re, sys

BASE = '/tmp/propertybrain'

# ── The canonical complete footer for all pages ───────────────────────────────
NEW_FOOTER = '''\
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="footer-brand__name">Property<span>Brain</span></div>
        <p>Free UK property investment calculators. For informational purposes only — not financial advice.</p>
      </div>
      <div class="footer-links">
        <h4>Calculators</h4>
        <ul>
          <li><a href="/buy-to-let-calculator/">Buy-to-Let</a></li>
          <li><a href="/stamp-duty-calculator/">Stamp Duty</a></li>
          <li><a href="/mortgage-calculator/">Mortgage</a></li>
          <li><a href="/rental-yield-calculator/">Rental Yield</a></li>
          <li><a href="/sa-airbnb-calculator/">SA / Airbnb</a></li>
          <li><a href="/hmo-yield-calculator/">HMO Yield</a></li>
          <li><a href="/cashflow-calculator/">Cashflow</a></li>
          <li><a href="/property-roi-calculator/">Property ROI</a></li>
          <li><a href="/capital-gains-tax-calculator/">CGT Calculator</a></li>
          <li><a href="/property-flip-calculator/">Property Flip</a></li>
          <li><a href="/refinance-vs-sell-calculator/">Refinance vs Sell</a></li>
          <li><a href="/portfolio-disposal-calculator/">Portfolio Disposal</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4>Resources</h4>
        <ul>
          <li><a href="/guide/">Investment Guide</a></li>
          <li><a href="/downloads/">Free Downloads</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacy/">Privacy Policy</a></li>
          <li><a href="/terms/">Terms of Use</a></li>
          <li><a href="/cookies/">Cookie Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 PropertyBrain.uk &#8212; For informational purposes only. Not financial advice.</span>
      <span>Data powered by <a href="https://propertyalert.uk">PropertyAlert.uk</a></span>
    </div>
  </div>
</footer>'''

# All 20 links that every page's footer should now contain
REQUIRED_LINKS = [
    '/buy-to-let-calculator/', '/stamp-duty-calculator/', '/mortgage-calculator/',
    '/rental-yield-calculator/', '/sa-airbnb-calculator/', '/hmo-yield-calculator/',
    '/cashflow-calculator/', '/property-roi-calculator/', '/capital-gains-tax-calculator/',
    '/property-flip-calculator/', '/refinance-vs-sell-calculator/', '/portfolio-disposal-calculator/',
    '/guide/', '/downloads/', '/about/', '/contact/', '/privacy/', '/terms/', '/cookies/',
]

def update_page(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Match <footer ...>...</footer> (greedy is fine; only one footer per page)
    m = re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
    if not m:
        print(f'  [SKIP] no footer found: {path}')
        return False

    old_footer = m.group(0)

    # Verify the new footer will have the required links
    for link in REQUIRED_LINKS:
        assert link in NEW_FOOTER, f'BUG: required link missing from NEW_FOOTER: {link}'

    new_html = html[:m.start()] + NEW_FOOTER + html[m.end():]

    # Sanity: confirm all required links present in new HTML
    for link in REQUIRED_LINKS:
        assert link in new_html, f'Missing link after replacement in {path}: {link}'

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    # Report what changed
    old_links = set(re.findall(r'href="(/[^"]+)"', old_footer))
    new_links = set(re.findall(r'href="(/[^"]+)"', NEW_FOOTER))
    added = new_links - old_links
    return added


# ── Process all pages ─────────────────────────────────────────────────────────
all_pages = ['index.html']
for d in sorted(os.listdir(BASE)):
    candidate = os.path.join(BASE, d, 'index.html')
    if os.path.isfile(candidate):
        all_pages.append(os.path.join(d, 'index.html'))

print(f'Processing {len(all_pages)} pages in {BASE}')
updated = 0
for rel in all_pages:
    path = os.path.join(BASE, rel)
    added = update_page(path)
    if added is not False:
        added_list = ', '.join(sorted(added)) if added else 'none'
        print(f'  [OK] {rel}  (+{len(added)} links: {added_list})')
        updated += 1

print(f'\nDone — {updated}/{len(all_pages)} pages updated.')
print()
print('Verify — check /contact/ footer for all required links:')

# Spot-check contact page
with open(os.path.join(BASE, 'contact/index.html'), 'r', encoding='utf-8') as f:
    check = f.read()
for link in ['/contact/', '/cookies/', '/cashflow-calculator/', '/capital-gains-tax-calculator/', '/portfolio-disposal-calculator/']:
    status = 'OK' if link in check else 'MISSING'
    print(f'  [{status}] {link}')
