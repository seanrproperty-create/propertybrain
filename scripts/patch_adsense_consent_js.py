#!/usr/bin/env python3
"""Wires the existing #cookie-banner Accept/Decline buttons to real Google
Consent Mode v2 signals. Previously they only set a localStorage flag and
hid the banner -- gtag never learned about the visitor's choice, so
GA fired unconditionally regardless of Accept/Decline. Patches both the
source and pre-minified JS (no build step in this repo, both are
hand-maintained). Idempotent.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC_OLD = """function initCookieBanner() {
  var banner = document.getElementById('cookie-banner');
  if (!banner) return;
  if (localStorage.getItem('pb_cookies')) { banner.style.display = 'none'; return; }
  document.getElementById('cookie-accept').onclick = function() { localStorage.setItem('pb_cookies','1'); banner.style.display='none'; };
  document.getElementById('cookie-decline').onclick = function() { localStorage.setItem('pb_cookies','0'); banner.style.display='none'; };
}"""

SRC_NEW = """function updateConsent(granted) {
  if (typeof gtag !== 'function') return;
  var state = granted ? 'granted' : 'denied';
  gtag('consent', 'update', {
    'ad_storage': state,
    'ad_user_data': state,
    'ad_personalization': state,
    'analytics_storage': state
  });
}

function initCookieBanner() {
  var banner = document.getElementById('cookie-banner');
  if (!banner) return;
  var stored = localStorage.getItem('pb_cookies');
  if (stored) {
    banner.style.display = 'none';
    updateConsent(stored === '1');
    return;
  }
  document.getElementById('cookie-accept').onclick = function() { localStorage.setItem('pb_cookies','1'); banner.style.display='none'; updateConsent(true); };
  document.getElementById('cookie-decline').onclick = function() { localStorage.setItem('pb_cookies','0'); banner.style.display='none'; updateConsent(false); };
}"""

MIN_OLD = "function initCookieBanner(){var banner=document.getElementById('cookie-banner');if(!banner)return;if(localStorage.getItem('pb_cookies')){banner.style.display='none';return;}\ndocument.getElementById('cookie-accept').onclick=function(){localStorage.setItem('pb_cookies','1');banner.style.display='none';};document.getElementById('cookie-decline').onclick=function(){localStorage.setItem('pb_cookies','0');banner.style.display='none';};}"

MIN_NEW = "function updateConsent(g){if(typeof gtag!=='function')return;var s=g?'granted':'denied';gtag('consent','update',{'ad_storage':s,'ad_user_data':s,'ad_personalization':s,'analytics_storage':s});}\nfunction initCookieBanner(){var banner=document.getElementById('cookie-banner');if(!banner)return;var stored=localStorage.getItem('pb_cookies');if(stored){banner.style.display='none';updateConsent(stored==='1');return;}\ndocument.getElementById('cookie-accept').onclick=function(){localStorage.setItem('pb_cookies','1');banner.style.display='none';updateConsent(true);};document.getElementById('cookie-decline').onclick=function(){localStorage.setItem('pb_cookies','0');banner.style.display='none';updateConsent(false);};}"

def patch(path, old, new, label):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "updateConsent" in content:
        print(f"{label}: already patched, skipping")
        return
    if old not in content:
        raise SystemExit(f"{label}: expected block not found -- aborting to avoid a bad patch")
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{label}: patched")

patch(os.path.join(ROOT, "assets", "js", "calculators.js"), SRC_OLD, SRC_NEW, "calculators.js")
patch(os.path.join(ROOT, "assets", "js", "calculators.min.js"), MIN_OLD, MIN_NEW, "calculators.min.js")
