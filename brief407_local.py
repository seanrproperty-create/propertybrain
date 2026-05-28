import os

BASE = r"C:\Users\Sean\Documents\Claude\Code\propertybrain"
AD_SLOT_MARKER = '<div class=\"ad-slot\"'

TRUSTPILOT = '''<section style="background:#f0fdf4;padding:2.5rem 0;text-align:center;border-top:1px solid #e2e8f0;">
  <div class="container">
    <p style="font-size:1rem;color:#475569;margin-bottom:0.75rem;">Found our calculators useful?</p>
    <a href="https://www.trustpilot.com/review/propertyalert.uk"
       target="_blank" rel="noopener"
       style="display:inline-flex;align-items:center;gap:0.5rem;background:#00b67a;color:#fff;padding:0.65rem 1.5rem;border-radius:6px;font-weight:600;text-decoration:none;font-size:0.95rem;">
      &#9733; Leave a review on Trustpilot
    </a>
    <p style="font-size:0.8rem;color:#94a3b8;margin-top:0.5rem;">Your feedback helps other property investors find us</p>
  </div>
</section>'''

CTA_1ST_FORMATIONS = '''  <div class="cta-box" style="background:#fff7ed;border:1px solid #fed7aa">
    <h2 style="font-size:1.1rem">Setting up a limited company for BTL?</h2>
    <p>1st Formations makes it quick and easy to incorporate a property investment company &mdash; from &pound;12.99.</p>
    <a href="https://1st-formations-limited.sjv.io/R0bxE7" class="btn btn--outline" target="_blank" rel="noopener sponsored">Form Your Company with 1st Formations &rarr;</a>
  </div>
'''

CTA_READYSTEADYBED = '''  <div class="cta-box" style="background:#f0f9ff;border:1px solid #bae6fd">
    <h2 style="font-size:1.1rem">Need SA furniture packages?</h2>
    <p>ReadySteadyBed supplies complete furniture packs for short-let and serviced accommodation properties across the UK.</p>
    <a href="https://tidd.ly/4tQKwAg" class="btn btn--outline" target="_blank" rel="noopener sponsored">Shop SA Furniture Packs at ReadySteadyBed &rarr;</a>
  </div>
'''

CTA_MAKE_A_WILL = '''  <div class="cta-box" style="background:#fdf4ff;border:1px solid #e9d5ff">
    <h2 style="font-size:1.1rem">Protect your property portfolio with a Will</h2>
    <p>Make a Will Online helps property investors write a legally-binding Will from home &mdash; starting from &pound;29.99.</p>
    <a href="https://tidd.ly/4dA1lbP" class="btn btn--outline" target="_blank" rel="noopener sponsored">Write Your Will with Make a Will Online &rarr;</a>
  </div>
'''

CTA_LNC_TODO = '  <!-- AFFILIATE TODO: L&C Mortgages CTA -->\n'
CTA_MUVE_TODO = '  <!-- AFFILIATE TODO: Muve Conveyancing CTA -->\n'
CTA_PROVESTOR_TODO = '  <!-- AFFILIATE TODO: Provestor CTA -->\n'

def insert_before_ad_slot(filepath, cta_html, label):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'AFFILIATE TODO' in content or 'tidd.ly' in content or '1st-formations-limited' in content:
        print('  SKIP (already patched): ' + label)
        return
    if AD_SLOT_MARKER not in content:
        print('  WARN: no ad-slot in ' + label)
        return
    content = content.replace(AD_SLOT_MARKER, cta_html + AD_SLOT_MARKER, 1)
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print('  OK: ' + label)

# Task 3: Trustpilot on homepage
idx = os.path.join(BASE, 'index.html')
with open(idx, 'r', encoding='utf-8') as f:
    content = f.read()
if 'trustpilot.com' in content:
    print('Task 3: SKIP (already present)')
else:
    content = content.replace('</main>', TRUSTPILOT + '\n</main>', 1)
    with open(idx, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print('Task 3: Trustpilot inserted')

# Task 4: Affiliates
print('Task 4:')
insert_before_ad_slot(BASE + r'\buy-to-let-calculator\index.html', CTA_1ST_FORMATIONS, 'buy-to-let')
insert_before_ad_slot(BASE + r'\hmo-yield-calculator\index.html', CTA_1ST_FORMATIONS, 'hmo-yield')
insert_before_ad_slot(BASE + r'\sa-airbnb-calculator\index.html', CTA_READYSTEADYBED, 'sa-airbnb')
insert_before_ad_slot(BASE + r'\guide\index.html', CTA_MAKE_A_WILL, 'guide')
insert_before_ad_slot(BASE + r'\mortgage-calculator\index.html', CTA_LNC_TODO, 'mortgage')
insert_before_ad_slot(BASE + r'\refinance-vs-sell-calculator\index.html', CTA_LNC_TODO, 'refinance-vs-sell')
insert_before_ad_slot(BASE + r'\stamp-duty-calculator\index.html', CTA_MUVE_TODO, 'stamp-duty')
insert_before_ad_slot(BASE + r'\property-flip-calculator\index.html', CTA_MUVE_TODO, 'property-flip')
insert_before_ad_slot(BASE + r'\cashflow-calculator\index.html', CTA_PROVESTOR_TODO, 'cashflow')
insert_before_ad_slot(BASE + r'\capital-gains-tax-calculator\index.html', CTA_PROVESTOR_TODO, 'capital-gains-tax')
insert_before_ad_slot(BASE + r'\portfolio-disposal-calculator\index.html', CTA_PROVESTOR_TODO, 'portfolio-disposal')
print('Done')
