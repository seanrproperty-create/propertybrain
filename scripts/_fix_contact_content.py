"""Add substantive content to /contact/ page — Brief 483 Task 3."""
import re

path = '/tmp/propertybrain/contact/index.html'
with open(path, encoding='utf-8') as f:
    html = f.read()

# Find the card__body section
OLD_BODY = (
    '      <h2>Get in touch</h2>\n'
    '      <p>For questions, feedback or business enquiries, please contact us via '
    '<a href="https://propertyalert.uk" target="_blank" rel="noopener">PropertyAlert.uk</a>.</p>\n'
    "      <p>If you've found a calculation error or would like to suggest a new calculator, we'd love to hear from you.</p>\n"
    '      <p style="margin-top:1.5rem"><a href="https://propertyalert.uk" class="btn btn--primary" target="_blank" rel="noopener">Visit PropertyAlert.uk →</a></p>'
)

NEW_BODY = (
    '      <h2>Get in touch</h2>\n'
    '      <p>Have a question about PropertyBrain&#8217;s calculators or property data? '
    'We&#8217;d love to hear from you &#8212; get in touch and we&#8217;ll respond within 1 business day.</p>\n'
    '      <p>PropertyBrain provides free UK property investment calculators covering buy-to-let yield, '
    'stamp duty, mortgage repayments, rental yield, SA/Airbnb cashflow, HMO yield, capital gains tax, '
    'property flip analysis, cashflow forecasting, refinance vs sell decisions and portfolio disposal '
    'modelling. All calculators are free to use, no sign-up required.</p>\n'
    '      <p>Common reasons to get in touch:</p>\n'
    '      <ul style="margin:0.75rem 0 1.25rem 1.25rem;">\n'
    '        <li>Report a calculation error or unexpected result</li>\n'
    '        <li>Suggest a new UK property investment calculator</li>\n'
    '        <li>Ask about property data sources or calculation methodology</li>\n'
    '        <li>Business enquiries or data partnerships</li>\n'
    '      </ul>\n'
    '      <p>For questions, feedback or business enquiries, please contact us via '
    '<a href="https://propertyalert.uk" target="_blank" rel="noopener">PropertyAlert.uk</a>.</p>\n'
    '      <p style="margin-top:1.5rem"><a href="https://propertyalert.uk" class="btn btn--primary" target="_blank" rel="noopener">Visit PropertyAlert.uk &rarr;</a></p>'
)

if OLD_BODY in html:
    html = html.replace(OLD_BODY, NEW_BODY, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Contact page content updated OK')
    # Word count check
    text = re.sub(r'<[^>]+>', ' ', html)
    m = re.search(r'</header>(.*?)<footer', html, re.DOTALL)
    if m:
        body_text = re.sub(r'<[^>]+>', ' ', m.group(1))
        words = [w for w in body_text.split() if len(w) > 2]
        print(f'Body word count after update: {len(words)}')
else:
    print('OLD_BODY not found. Current card__body content:')
    m = re.search(r'<div class="card__body">(.*?)</div>', html, re.DOTALL)
    if m:
        print(repr(m.group(1)[:500]))
    else:
        print('card__body section not found either')
