"""
One-off script: add the 5 EIGHTFINITY platforms that joined the network
after scripts/expand_our_network_footer.py ran (syllabustldr.com,
lawcheck.co.uk, legalroute.co.uk, ukimmigrationadvice.co.uk, eightfinity.net
itself) to the "Our Network" block on every page.

Anchored on the bestgiftsfor.net <li> since that script made it the last
entry everywhere. Idempotent: pages that already have syllabustldr.com are
skipped.

Usage: python scripts/add_law_syllabus_eightfinity_network.py
"""
import glob

BESTGIFTSFOR_LI = (
    '<li><a href="https://bestgiftsfor.net" target="_blank" rel="noopener">'
    'BestGiftsFor (AI-powered gift finder)</a></li>'
)

NEW_LIS = (
    '<li><a href="https://syllabustldr.com" target="_blank" rel="noopener">'
    'SyllabusTLDR (syllabus deadline extractor)</a></li>'
    '<li><a href="https://lawcheck.co.uk" target="_blank" rel="noopener">'
    'LawCheck (free UK legal calculators)</a></li>'
    '<li><a href="https://legalroute.co.uk" target="_blank" rel="noopener">'
    'LegalRoute (find a UK solicitor)</a></li>'
    '<li><a href="https://ukimmigrationadvice.co.uk" target="_blank" rel="noopener">'
    'UK Immigration Advice (visa quick check)</a></li>'
    '<li><a href="https://eightfinity.net" target="_blank" rel="noopener">'
    'EIGHTFINITY.net</a></li>'
)


def process(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if "syllabustldr.com" in content:
        print("SKIP (already complete):", path)
        return False
    if BESTGIFTSFOR_LI not in content:
        print("SKIP (anchor not found -- check manually):", path)
        return False

    content = content.replace(BESTGIFTSFOR_LI, BESTGIFTSFOR_LI + NEW_LIS, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Added 5 network entries:", path)
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
