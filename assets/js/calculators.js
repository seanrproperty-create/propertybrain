/* ===== PropertyBrain.uk — Calculator Functions ===== */
'use strict';

// ===== Formatters =====
function fmt(n, dp) {
  dp = dp === undefined ? 0 : dp;
  if (n === null || n === undefined || isNaN(n)) return '—';
  return '£' + Math.abs(n).toLocaleString('en-GB', { minimumFractionDigits: dp, maximumFractionDigits: dp });
}
function fmtSigned(n, dp) {
  dp = dp === undefined ? 0 : dp;
  if (n === null || n === undefined || isNaN(n)) return '—';
  var prefix = n >= 0 ? '+£' : '-£';
  return prefix + Math.abs(n).toLocaleString('en-GB', { minimumFractionDigits: dp, maximumFractionDigits: dp });
}
function fmtPct(n, dp) {
  dp = dp === undefined ? 1 : dp;
  if (n === null || n === undefined || isNaN(n)) return '—';
  return n.toFixed(dp) + '%';
}
function fmtN(n, dp) {
  dp = dp === undefined ? 0 : dp;
  if (n === null || n === undefined || isNaN(n)) return '—';
  return n.toLocaleString('en-GB', { minimumFractionDigits: dp, maximumFractionDigits: dp });
}
function colorClass(n) {
  if (n > 0.001) return 'positive';
  if (n < -0.001) return 'negative';
  return '';
}
function v(id) {
  var el = document.getElementById(id);
  if (!el) return 0;
  return parseFloat(el.value) || 0;
}
function setEl(id, val, cls) {
  var el = document.getElementById(id);
  if (!el) return;
  el.textContent = val;
  if (cls !== undefined) {
    el.className = el.className.replace(/\b(positive|negative|accent)\b/g, '').trim();
    if (cls) el.className += ' ' + cls;
  }
}

// ===== SDLT / Stamp Duty =====
// country: 'england' | 'scotland' | 'wales'
// type: 'standard' | 'additional' | 'firsttime'
function calcSDLT(price, type, country) {
  if (!price || price <= 0) return { total: 0, effective: 0, breakdown: [] };
  var total = 0;
  var breakdown = [];
  country = country || 'england';
  type = type || 'standard';

  if (country === 'scotland') {
    var SDLT_SCOT_ADS_RATE = 8;
    var bands = [[0,145000,0],[145000,250000,0.02],[250000,325000,0.05],[325000,750000,0.10],[750000,Infinity,0.12]];
    bands.forEach(function(b) {
      if (price <= b[0]) return;
      var taxable = Math.min(price, b[1]) - b[0];
      var tax = taxable * b[2];
      breakdown.push({ band: (b[1]===Infinity ? fmt(b[0])+' and above' : fmt(b[0])+' – '+fmt(b[1])), rate: fmtPct(b[2]*100,0), amount: tax });
      total += tax;
    });
    if (type === 'additional') {
      var addl = price * (SDLT_SCOT_ADS_RATE / 100);
      breakdown.push({ band: 'Additional Dwelling Supplement (' + fmtPct(SDLT_SCOT_ADS_RATE,0) + ')', rate: fmtPct(SDLT_SCOT_ADS_RATE,0), amount: addl });
      total += addl;
    }
  } else if (country === 'wales') {
    // Higher residential rates (additional property) are NOT a flat surcharge on the
    // standard bands -- since 11 Dec 2024 they are their own separate band table with
    // different thresholds (gov.wales/land-transaction-tax-rates-and-bands).
    var bands = (type === 'additional')
      ? [[0,180000,0.05],[180000,250000,0.085],[250000,400000,0.10],[400000,750000,0.125],[750000,1500000,0.15],[1500000,Infinity,0.17]]
      : [[0,225000,0],[225000,400000,0.06],[400000,750000,0.075],[750000,1500000,0.10],[1500000,Infinity,0.12]];
    bands.forEach(function(b) {
      if (price <= b[0]) return;
      var taxable = Math.min(price, b[1]) - b[0];
      var tax = taxable * b[2];
      breakdown.push({ band: (b[1]===Infinity ? fmt(b[0])+' and above' : fmt(b[0])+' – '+fmt(b[1])), rate: fmtPct(b[2]*100,1), amount: tax });
      total += tax;
    });
  } else {
    // England / NI — SDLT
    var SDLT_ENG_FTB_NIL_RATE = 300000;
    var SDLT_ENG_FTB_CUTOFF = 500000;
    var SDLT_ENG_ADDITIONAL_SURCHARGE = 5;
    if (type === 'firsttime' && price <= SDLT_ENG_FTB_CUTOFF) {
      breakdown.push({ band: '£0 – ' + fmt(SDLT_ENG_FTB_NIL_RATE) + ' (FTB relief)', rate: '0%', amount: 0 });
      if (price > SDLT_ENG_FTB_NIL_RATE) {
        var tax = (Math.min(price, SDLT_ENG_FTB_CUTOFF) - SDLT_ENG_FTB_NIL_RATE) * 0.05;
        breakdown.push({ band: fmt(SDLT_ENG_FTB_NIL_RATE+1) + ' – ' + fmt(SDLT_ENG_FTB_CUTOFF), rate: '5%', amount: tax });
        total += tax;
      }
    } else {
      var sur = type === 'additional' ? SDLT_ENG_ADDITIONAL_SURCHARGE / 100 : 0;
      var SDLT_ENG_NIL_RATE_THRESHOLD = 125000;
      var SDLT_ENG_BAND2_CEILING = 250000;
      var SDLT_ENG_BAND3_CEILING = 925000;
      var bands = [
        [0, SDLT_ENG_NIL_RATE_THRESHOLD, 0 + sur],
        [SDLT_ENG_NIL_RATE_THRESHOLD, SDLT_ENG_BAND2_CEILING, 0.02 + sur],
        [SDLT_ENG_BAND2_CEILING, SDLT_ENG_BAND3_CEILING, 0.05 + sur],
        [SDLT_ENG_BAND3_CEILING, 1500000, 0.10 + sur],
        [1500000, Infinity, 0.12 + sur]
      ];
      bands.forEach(function(b) {
        if (price <= b[0]) return;
        var taxable = Math.min(price, b[1]) - b[0];
        var tax = taxable * b[2];
        breakdown.push({ band: (b[1]===Infinity ? fmt(b[0])+' and above' : fmt(b[0])+' – '+fmt(b[1])), rate: fmtPct(b[2]*100,0), amount: tax });
        total += tax;
      });
    }
  }

  return { total: total, effective: price > 0 ? (total / price) * 100 : 0, breakdown: breakdown };
}

// ===== Mortgage =====
function calcMortgage(principal, annualRate, termYears, interestOnly) {
  if (!principal || !annualRate || !termYears) return { monthly: 0, totalRepaid: 0, totalInterest: 0 };
  if (interestOnly) {
    var mo = principal * (annualRate / 100) / 12;
    return { monthly: mo, totalRepaid: mo * termYears * 12 + principal, totalInterest: mo * termYears * 12 };
  }
  var r = annualRate / 100 / 12;
  var n = termYears * 12;
  if (r === 0) { var mo = principal / n; return { monthly: mo, totalRepaid: principal, totalInterest: 0 }; }
  var mo = principal * (r * Math.pow(1+r, n)) / (Math.pow(1+r, n) - 1);
  return { monthly: mo, totalRepaid: mo * n, totalInterest: mo * n - principal };
}

function buildAmortisation(principal, annualRate, termYears, interestOnly) {
  var r = annualRate / 100 / 12;
  var mo = calcMortgage(principal, annualRate, termYears, interestOnly).monthly;
  var balance = principal;
  var rows = [];
  for (var yr = 1; yr <= Math.min(termYears, 30); yr++) {
    var yInt = 0, yPrin = 0;
    for (var m = 0; m < 12; m++) {
      var interest = balance * r;
      var princ = interestOnly ? 0 : Math.min(mo - interest, balance);
      yInt += interest; yPrin += princ; balance -= princ;
    }
    rows.push({ year: yr, interest: yInt, principal: yPrin, balance: Math.max(0, balance) });
  }
  return rows;
}

// ===== Rental Yield =====
function calcYield(price, monthlyRent, annualCosts) {
  annualCosts = annualCosts || 0;
  if (!price || !monthlyRent) return { gross: 0, net: 0 };
  var annual = monthlyRent * 12;
  return { gross: annual / price * 100, net: (annual - annualCosts) / price * 100, monthlyNet: (annual - annualCosts) / 12 };
}

// ===== BTL Full Analysis =====
function calcBTL(p) {
  var deposit = p.price * (p.depositPct / 100);
  var loan = p.price - deposit;
  var sdlt = calcSDLT(p.price, p.isAdditional ? 'additional' : 'standard', p.country || 'england');
  var purchaseCosts = deposit + sdlt.total + (p.legalFees || 2000) + (p.surveyFees || 800);

  var mortResult = calcMortgage(loan, p.rate, p.term, p.interestOnly);
  var mortMonthly = mortResult.monthly;
  var annInterest = p.interestOnly ? mortMonthly * 12 : (mortMonthly * 12 - loan / p.term);

  var voidFactor = 1 - (p.voidWeeks || 0) / 52;
  var effectiveRent = p.monthlyRent * voidFactor;
  var annualRent = effectiveRent * 12;

  var mgmtCost = annualRent * ((p.managementPct || 0) / 100);
  var maintCost = annualRent * ((p.maintenancePct || 0) / 100);
  var totalOpex = mgmtCost + maintCost + (p.insurance || 0);
  var grossProfit = annualRent - totalOpex;

  var BTL_LTD_CORP_TAX_RATE = 19; // small profits rate up to £50k -- see section-24-calculator's S24_RELIEF_CREDIT_RATE for the mortgage-interest relief constant this file also uses
  var S24_RELIEF_CREDIT_RATE = 20;
  var taxable, taxPayable;
  if (p.isLtdCo) {
    taxable = Math.max(0, grossProfit - annInterest);
    taxPayable = taxable * (BTL_LTD_CORP_TAX_RATE / 100);
  } else {
    taxable = Math.max(0, grossProfit);
    var grossTax = taxable * ((p.taxBand || 20) / 100);
    var s24Relief = annInterest * (S24_RELIEF_CREDIT_RATE / 100);
    taxPayable = Math.max(0, grossTax - s24Relief);
  }

  var netAnnual = grossProfit - mortMonthly * 12 - taxPayable;
  var netMonthly = netAnnual / 12;
  var grossYield = p.monthlyRent * 12 / p.price * 100;
  var netYield = (annualRent - totalOpex - mortMonthly * 12 - taxPayable) / p.price * 100;
  var cashOnCash = purchaseCosts > 0 ? netAnnual / purchaseCosts * 100 : 0;

  return {
    deposit: deposit, loan: loan, sdlt: sdlt.total, purchaseCosts: purchaseCosts,
    mortMonthly: mortMonthly, annInterest: annInterest,
    effectiveRent: effectiveRent, annualRent: annualRent,
    mgmtCost: mgmtCost, maintCost: maintCost, totalOpex: totalOpex,
    grossProfit: grossProfit, taxPayable: taxPayable,
    netAnnual: netAnnual, netMonthly: netMonthly,
    grossYield: grossYield, netYield: netYield, cashOnCash: cashOnCash,
    annInterest: annInterest
  };
}

function buildBTLProjection(price, loan, monthlyRent, mortMonthly, voidWeeks, mgmtPct, maintPct, insurance) {
  var rows = [];
  var val = price; var rent = monthlyRent; var balance = loan;
  for (var yr = 1; yr <= 5; yr++) {
    val *= 1.04; rent *= 1.03;
    var annRent = rent * (1 - (voidWeeks||0)/52) * 12;
    var opex = annRent * ((mgmtPct+maintPct)/100) + insurance;
    var equity = val - balance;
    var cf = (annRent - opex - mortMonthly*12) / 12;
    rows.push({ year: yr, value: val, equity: equity, rent: rent, cashflow: cf });
  }
  return rows;
}

function buildStressTest(loan, currentRate, monthlyRent, term, interestOnly) {
  var rows = [];
  for (var r = currentRate; r <= currentRate + 4.01; r += 0.5) {
    var mo = calcMortgage(loan, r, term, interestOnly).monthly;
    var icr = mo > 0 ? monthlyRent / mo : 99;
    rows.push({ rate: r, monthly: mo, icr: icr, ok: icr >= 1.25 });
  }
  return rows;
}

// ===== SA / Airbnb =====
function calcSA(nightly, occupancyPct, platformPct, mgmtPct, cleaningPer, staysPm, mortgage) {
  var annualRev = nightly * (occupancyPct/100) * 365;
  var monthlyRev = annualRev / 12;
  var platform = monthlyRev * (platformPct/100);
  var mgmt = monthlyRev * (mgmtPct/100);
  var cleaning = cleaningPer * staysPm;
  var costs = platform + mgmt + cleaning;
  var grossMo = monthlyRev - costs;
  var netMo = grossMo - mortgage;

  var sensitivity = [];
  for (var occ = 40; occ <= 90; occ += 10) {
    var rev = nightly * (occ/100) * 365 / 12;
    var c = rev * ((platformPct+mgmtPct)/100) + cleaning;
    sensitivity.push({ occ: occ, gross: rev - c, net: rev - c - mortgage });
  }
  return { annualRev: annualRev, monthlyRev: monthlyRev, platform: platform, mgmt: mgmt, cleaning: cleaning, costs: costs, grossMo: grossMo, netMo: netMo, sensitivity: sensitivity };
}

// ===== HMO =====
function calcHMO(price, rooms, roomRent, bills, mgmtPct, maintPct, mortgage) {
  var totalRent = rooms * roomRent;
  var annualRent = totalRent * 12;
  var mgmt = totalRent * (mgmtPct/100);
  var maint = totalRent * (maintPct/100);
  var opex = mgmt + maint + bills;
  var grossMo = totalRent - opex;
  var netMo = grossMo - mortgage;
  var grossYield = annualRent / price * 100;
  var netYield = (netMo * 12) / price * 100;
  return { totalRent: totalRent, annualRent: annualRent, mgmt: mgmt, maint: maint, opex: opex, grossMo: grossMo, netMo: netMo, grossYield: grossYield, netYield: netYield };
}

// ===== Cashflow =====
function calcCashflow(rent, mortgage, mgmt, maint, insurance, groundRent, serviceCharge, other, voidPct) {
  var voidAmt = rent * (voidPct/100);
  var effective = rent - voidAmt;
  var expenses = mortgage + mgmt + maint + insurance + groundRent + serviceCharge + other;
  var net = effective - expenses;
  return { voidAmt: voidAmt, effective: effective, expenses: expenses, net: net };
}

// ===== ROI =====
function calcROI(purchaseCosts, annualCashflow, currentValue, purchasePrice, yearsHeld) {
  var capitalGain = currentValue - purchasePrice;
  var totalCfReturn = annualCashflow * yearsHeld;
  var totalReturn = capitalGain + totalCfReturn;
  var roi = purchaseCosts > 0 ? totalReturn / purchaseCosts * 100 : 0;
  var ann = purchaseCosts > 0 && yearsHeld > 0 ? (Math.pow(1 + totalReturn/purchaseCosts, 1/yearsHeld) - 1)*100 : 0;
  return { capitalGain: capitalGain, totalCfReturn: totalCfReturn, totalReturn: totalReturn, roi: roi, annualised: ann };
}

// ===== UI Helpers =====
function updateConsent(granted) {
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
}

function initTabs() {
  document.querySelectorAll('.tab-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var group = btn.closest('.tab-group');
      group.querySelectorAll('.tab-btn').forEach(function(b){ b.classList.remove('active'); });
      group.querySelectorAll('.tab-panel').forEach(function(p){ p.classList.remove('active'); });
      btn.classList.add('active');
      var panel = group.querySelector('#'+btn.dataset.tab);
      if (panel) panel.classList.add('active');
    });
  });
}

function initTogglePills() {
  document.querySelectorAll('.toggle-group').forEach(function(grp) {
    grp.querySelectorAll('.toggle-pill').forEach(function(pill) {
      pill.addEventListener('click', function() {
        grp.querySelectorAll('.toggle-pill').forEach(function(p){ p.classList.remove('active'); });
        pill.classList.add('active');
        var inp = pill.querySelector('input[type="radio"]');
        if (inp) { inp.checked = true; inp.dispatchEvent(new Event('change', { bubbles: true })); }
        // Trigger calc
        var calcFn = window[grp.dataset.calc];
        if (calcFn) calcFn();
      });
    });
  });
}

function initRanges() {
  document.querySelectorAll('input[type="range"]').forEach(function(r) {
    var out = r.dataset.out ? document.getElementById(r.dataset.out) : null;
    var update = function() {
      if (out) out.textContent = (r.dataset.prefix||'') + r.value + (r.dataset.suffix||'');
    };
    r.addEventListener('input', update);
    update();
  });
}

document.addEventListener('DOMContentLoaded', function() {
  initCookieBanner();
  initTabs();
  initTogglePills();
  initRanges();
  // Mark active nav link
  var path = location.pathname;
  document.querySelectorAll('.site-nav a').forEach(function(a) {
    if (a.getAttribute('href') === path || a.getAttribute('href') === path + '/') {
      a.classList.add('active');
    }
  });
});
