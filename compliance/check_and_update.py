#!/usr/bin/env python3
"""Weekly compliance sweep for this site's calculators.

For each constant in registry.json:
  1. Fetches its source_url.
  2. If extract_pattern is null, the constant has no verified automated
     source yet -- log a reminder and touch nothing.
  3. Otherwise, runs extract_pattern against the fetched text. If the
     pattern doesn't match, or the matched number isn't numeric, or it
     falls outside [plausible_min, plausible_max], the constant is
     skipped and NOTHING is edited -- a bad match must never reach a
     live calculator.
  4. If the extracted value differs from current_value, patches every
     listed file at its exact regex location, then updates the registry.
  5. Whether changed or confirmed unchanged, stamps "Last Verified: <date>"
     on every page tied to this constant -- only for constants that were
     actually checked this run, so the date is never faked.

Exits non-zero only on an unexpected internal error, never on a source
being temporarily unreachable (that's a WARN, not a failure) -- a flaky
gov.uk fetch shouldn't block the weekly run from completing.
"""
import datetime
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY_PATH = os.path.join(ROOT, "compliance", "registry.json")
TODAY = datetime.date.today().strftime("%-d %B %Y") if os.name != "nt" else datetime.date.today().strftime("%d %B %Y").lstrip("0")

UA = "Mozilla/5.0 (compatible; EIGHTFINITY-compliance-monitor/1.0; +https://eightfinity.net/)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse_number(raw):
    raw = raw.replace(",", "").replace("£", "").strip()
    return float(raw) if "." in raw else int(raw)


def stamp_timestamp(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, n = re.subn(r"Last Verified: [^<]*", "Last Verified: " + TODAY, content)
    if n:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def main():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry = json.load(f)

    changed_files = set()
    log = []

    for const in registry["constants"]:
        cid = const["id"]

        if not const.get("extract_pattern"):
            log.append("SKIP  %s: no verified source pattern yet -- needs manual check (see notes: %s)" % (cid, const.get("notes", "")))
            continue

        try:
            page = fetch(const["source_url"])
        except Exception as e:
            log.append("WARN  %s: fetch failed (%s) -- skipped, nothing changed" % (cid, e))
            continue

        m = re.search(const["extract_pattern"], page, re.DOTALL)
        if not m:
            log.append("WARN  %s: extract pattern not found on source page -- skipped, nothing changed" % cid)
            continue

        try:
            new_value = parse_number(m.group(1))
        except ValueError:
            log.append('WARN  %s: matched text "%s" not numeric -- skipped' % (cid, m.group(1)))
            continue

        if not (const["plausible_min"] <= new_value <= const["plausible_max"]):
            log.append("WARN  %s: extracted %s outside plausible range [%s, %s] -- skipped, nothing changed" % (cid, new_value, const["plausible_min"], const["plausible_max"]))
            continue

        if new_value == const["current_value"]:
            log.append("OK    %s: confirmed unchanged at %s" % (cid, new_value))
        else:
            log.append("DRIFT %s: %s -> %s  (source: %s)" % (cid, const["current_value"], new_value, const["source_url"]))
            for target in const["files"]:
                fpath = os.path.join(ROOT, target["path"])
                if not os.path.exists(fpath):
                    log.append("ERROR %s: file not found: %s" % (cid, target["path"]))
                    continue
                with open(fpath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                replacement = target["replace_template"].format(value=new_value)
                new_content, n = re.subn(target["pattern"], replacement, content, count=1)
                if n == 0:
                    log.append("ERROR %s: pattern not found in %s -- file NOT changed, needs manual fix" % (cid, target["path"]))
                    continue
                with open(fpath, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
                changed_files.add(target["path"])
            const["current_value"] = new_value

        const["last_verified"] = TODAY
        for target in const["files"]:
            fpath = os.path.join(ROOT, target["path"])
            if os.path.exists(fpath) and stamp_timestamp(fpath):
                changed_files.add(target["path"])

    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
        f.write("\n")

    print("\n".join(log))
    print("\nFiles touched: %d" % len(changed_files))

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a") as f:
            f.write("changed=%s\n" % ("true" if changed_files else "false"))
            drift_lines = [l for l in log if l.startswith("DRIFT") or l.startswith("ERROR")]
            f.write("summary=%s\n" % (" | ".join(drift_lines) if drift_lines else "no drift detected"))


if __name__ == "__main__":
    main()
