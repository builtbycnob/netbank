/* ==========================================================================
   NetBank — interactive product demo · behaviour
   Navigation · scripted product moments · guided tour
   All data is illustrative / synthetic. Market stats use blessed numbers only.
   ========================================================================== */
(() => {
'use strict';

const $  = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const viewport = $('#viewport');
const appSmall = $('#appSmall');
const appTitle = $('#appTitle');
const appBack  = $('#appBack');
const tabbar   = $('#tabbar');

const state = { view: 'home', payer: 'acme', distress: false, truthsShown: false, touring: false };

/* tiny inline icons reused by JS-built markup */
const ICON = {
  check: '<svg class="chk" viewBox="0 0 24 24" fill="none"><path d="m5 13 4 4L19 7"/></svg>',
  lock:  '<svg viewBox="0 0 24 24" fill="none"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
};

/* ----------------------------------------------------------------------------
   VIEW REGISTRY + NAVIGATION
---------------------------------------------------------------------------- */
const VIEWS = {
  home:      { title: 'Atlas Studio',     small: 'Good morning',          tab: 'home' },
  money:     { title: 'Money',            small: 'Accounts & cards',      tab: 'money' },
  scan:      { title: 'Scan · Pay',       small: 'Captured just now',     tab: 'scan' },
  financing: { title: 'Financing',        small: 'Safe to borrow',        tab: 'financing' },
  bridge:    { title: 'Request a bridge', small: 'Agentic underwriting',  tab: 'financing', back: 'financing' },
  more:      { title: 'More',             small: 'Everything else',       tab: 'more' },
  invoices:  { title: 'Invoices',         small: 'AR · AP · Radar',       tab: 'more', back: 'more' },
  payer:     { title: 'Payer detail',     small: 'Per-client reliability', tab: 'more', back: 'invoices' },
  services:  { title: 'Services',         small: 'Vetted partners',       tab: 'more', back: 'more' },
  pricing:   { title: 'Plans',            small: 'Tax-Sweep+',            tab: 'more', back: 'more' },
  about:     { title: 'About this demo',  small: 'What is real',          tab: 'more', back: 'more' },
};

function navigate(view) {
  const target = viewport.querySelector(`[data-view="${view}"]`);
  if (!target) return;
  if (view === 'payer') renderPayer(state.payer);

  $$('.view', viewport).forEach((v) => v.classList.remove('active'));
  target.classList.add('active');
  target.scrollTop = 0;

  const meta = VIEWS[view] || {};
  appSmall.textContent = meta.small || '';
  appTitle.textContent = view === 'payer' ? payerData(state.payer).name : (meta.title || '');
  appBack.style.display = meta.back ? '' : 'none';
  appBack.onclick = meta.back ? () => navigate(meta.back) : null;

  $$('[data-go]', tabbar).forEach((t) => t.classList.toggle('on', t.dataset.go === meta.tab));
  $$('.jump').forEach((j) => j.classList.toggle('on', j.dataset.go === view));
  state.view = view;
}

/* global click delegation for navigation triggers */
document.addEventListener('click', (e) => {
  const payerEl = e.target.closest('[data-payer]');
  if (payerEl) { e.preventDefault(); state.payer = payerEl.dataset.payer; navigate('payer'); return; }
  const go = e.target.closest('[data-go]');
  if (go) { e.preventDefault(); navigate(go.dataset.go); }
});

/* ----------------------------------------------------------------------------
   MOMENT 1 · the three-truths reveal ("the balance was lying")
---------------------------------------------------------------------------- */
function revealTruths() {
  if (state.truthsShown) return;
  state.truthsShown = true;
  const truths = $('#truths');
  truths.hidden = false;
  $$('.truth', truths).forEach((t, i) => setTimeout(() => t.classList.add('in'), i * 130));
  const v = $('#lyingValue'); v.style.transition = 'opacity .5s, color .5s'; v.style.opacity = '.3';
  const hint = $('#lyingCard .hintline');
  hint.innerHTML = '✓ the truth — three live balances, not one';
  hint.style.color = 'var(--mint)'; hint.style.borderColor = 'rgba(127,231,166,.4)';
}
$('#lyingCard').addEventListener('click', revealTruths);

/* ----------------------------------------------------------------------------
   MOMENT 2 · Tax-Sweep+ auto-sweep animation
---------------------------------------------------------------------------- */
function flyCoin(fromEl, toEl, label) {
  const screen = $('.screen');
  const sr = screen.getBoundingClientRect();
  const a = fromEl.getBoundingClientRect();
  const b = toEl.getBoundingClientRect();
  const coin = document.createElement('div');
  coin.className = 'coin'; coin.textContent = label;
  coin.style.left = a.left - sr.left + a.width / 2 - 24 + 'px';
  coin.style.top  = a.top - sr.top + 'px';
  coin.style.transition = 'transform 0.85s cubic-bezier(.4,.1,.2,1), opacity .85s';
  screen.appendChild(coin);
  // force reflow then move to the tax pot
  void coin.offsetWidth;
  const dx = (b.left - sr.left + b.width / 2 - 24) - (a.left - sr.left + a.width / 2 - 24);
  const dy = (b.top - sr.top + b.height / 2 - 14) - (a.top - sr.top);
  coin.style.transform = `translate(${dx}px, ${dy}px) scale(.7)`;
  coin.style.opacity = '0.2';
  setTimeout(() => coin.remove(), 900);
}

function showToast(iconSvg, title, sub, tag) {
  const screen = $('.screen');
  $('.toast', screen)?.remove();
  const t = document.createElement('div');
  t.className = 'toast';
  t.innerHTML =
    `<div class="t-ic">${iconSvg}</div>` +
    `<div class="t-b"><b>${title}</b><small>${sub}</small></div>` +
    (tag ? `<span class="est">${tag}</span>` : '');
  screen.appendChild(t);
  void t.offsetWidth; t.classList.add('show');
  setTimeout(() => { t.classList.remove('show'); setTimeout(() => t.remove(), 350); }, 3400);
}

let swept = false;
$('#simulatePayment').addEventListener('click', (e) => {
  const btn = e.currentTarget;
  const pot = $('#taxPot');
  const potVal = $('#taxPotVal');
  flyCoin(btn, potVal, '+€420');
  setTimeout(() => {
    pot.classList.add('flash');
    const next = swept ? 3180 : 2760;
    potVal.textContent = '€' + next.toLocaleString('en-US');
    swept = true;
    setTimeout(() => pot.classList.remove('flash'), 1100);
    showToast(
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
      '€420 set aside for IVA',
      '€2,000 from Studio Vermell landed · the rest is yours',
      'estimate'
    );
  }, 760);
});

/* ----------------------------------------------------------------------------
   MOMENT 3 · Concurso Radar distress flip + bridge interlock
---------------------------------------------------------------------------- */
$('#simulateDistress').addEventListener('click', (e) => {
  state.distress = true;
  const light = $('#caixaLight');
  light.classList.remove('g'); light.classList.add('r');
  $('#clientCaixa').classList.add('flipping');
  $('#caixaSub').innerHTML = 'BORME pre-concurso filing · 11 days ago';
  $('#caixaSub').style.color = 'var(--red)';
  const badge = $('#clientVermell')?.closest('.card')?.querySelector('.radar-head .badge');
  if (badge) { badge.className = 'badge risk'; badge.innerHTML = '<i class="dot"></i>2 green · 1 risk'; }
  const e2 = $('#recvCaixaE'); if (e2) { e2.textContent = "won't bridge — distress"; e2.className = 'e risk'; }
  showToast(
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/></svg>',
    'Caixa Studio flagged',
    'Public filing matched by NIF — any bridge against them is gated',
    'about your client'
  );
  e.currentTarget.disabled = true;
  e.currentTarget.style.opacity = '.5';
  e.currentTarget.querySelector('span') || (e.currentTarget.innerHTML = 'Distress detected — bridge gated');
});

/* ----------------------------------------------------------------------------
   PAYER DETAIL (parametric) + MOMENT 4 · the closed-loop flywheel
---------------------------------------------------------------------------- */
const PAYERS = {
  acme: {
    name: 'ACME S.L.', nif: 'CIF B-12345678', observed: 14, flag: 'green',
    summaryHTML: 'Pays <b>~18 days late</b> on average — and that is <b>steady</b>, so it is predictable.',
    comps: [['Avg days late', '+18d', 42, 'amber'], ['Consistency', 'steady', 78, ''], ['Paid on-time', '64%', 64, ''], ['Paid &gt;30d late', '12%', 12, 'amber']],
    spark: [-2, 6, 18, 12, 20, 16, 22, 14, 18, 11, 19, 15, 18, null], expected: 18,
    why: ['Mean days-late <b>+18</b> with <b>low volatility</b> (their strongest signals)', 'No public-distress filing on their NIF (BORME / RAI clean)', '14 invoices observed — <b>enough history</b> to trust it'],
    loop: { pred: '~12 Aug ±4', real: '10 Aug' },
  },
  vermell: {
    name: 'Studio Vermell', nif: 'CIF B-87654321', observed: 22, flag: 'green',
    summaryHTML: 'Pays <b>96% on-time</b> — your most reliable client, about <b>+6 days</b>.',
    comps: [['Avg days late', '+6d', 18, ''], ['Consistency', 'very steady', 92, ''], ['Paid on-time', '96%', 96, ''], ['Paid &gt;30d late', '1%', 2, 'amber']],
    spark: [2, -1, 1, 6, 4, 8, 3, 5, 6, 2, 7, 5, 6, null], expected: 6,
    why: ['Mean days-late <b>+6</b>, <b>very low volatility</b>', '<b>No distress filing</b> · long clean history', '22 invoices observed — <b>high confidence</b>'],
    loop: { pred: '~9 Jun ±2', real: '8 Jun' },
  },
  caixa: {
    name: 'Caixa Studio', nif: 'CIF B-44556677', observed: 9, flag: 'risk',
    summaryHTML: 'Was steady at <b>~+31 days</b> — but a <b>public distress filing</b> just changed the picture.',
    comps: [['Avg days late', '+31d', 62, 'amber'], ['Trend', 'slowing', 40, 'amber'], ['Paid on-time', '38%', 38, 'amber'], ['Paid &gt;60d late', '22%', 22, 'amber']],
    spark: [20, 28, 25, 31, 30, 38, 42, 55, 68, null], expected: 55,
    feed: [['red', 'Concurso pre-filing', 'BORME · 11 days ago'], ['amber', 'Annual accounts overdue', 'Registro Mercantil · 2 mo ago']],
    why: ['A <b>concurso pre-filing</b> on their NIF (BORME) — a weeks-early warning', 'Days-late <b>trending up</b> over the last 4 invoices', 'Only 9 invoices observed — <b>treat with caution</b>'],
    loop: { pred: '~5 Jul ±9', real: null },
  },
};

function payerData(id) {
  const p = { ...PAYERS[id] };
  if (id === 'caixa' && !state.distress) {
    p.flag = 'green';
    p.summaryHTML = 'Pays <b>~+31 days</b> — slow, but steady so far.';
    p.feed = null;
    p.comps = [['Avg days late', '+31d', 62, 'amber'], ['Consistency', 'steady', 66, ''], ['Paid on-time', '52%', 52, ''], ['Paid &gt;60d late', '8%', 8, 'amber']];
    p.why = ['Days-late <b>+31</b>, fairly steady', '<b>No distress filing</b> on their NIF yet', 'Only 9 invoices — <b>modest confidence</b>'];
  }
  return p;
}

const flagBadge = (flag) =>
  flag === 'risk'
    ? '<span class="badge risk"><i class="dot"></i>distress</span>'
    : '<span class="badge"><i class="dot"></i>green</span>';

function renderPayer(id) {
  const p = payerData(id);
  const view = viewport.querySelector('[data-view="payer"]');
  const comps = p.comps.map(([k, v, w, cls]) =>
    `<div class="crow"><span class="ck">${k}</span><span class="ctrack ${cls}"><i style="width:${w}%"></i></span><span class="cv">${v}</span></div>`).join('');
  const feed = p.feed
    ? `<div class="eyebrow">Concurso Radar · public filings <span class="ai predict">monitored</span></div>
       <div class="card"><div class="feed">${p.feed.map(([c, t, s]) =>
         `<div class="fev ${c}"><b>${t}</b><small>${s}</small></div>`).join('')}</div>
       <p style="color:var(--text-3);font-size:11px;font-family:var(--mono);margin-top:8px">This is about your <b style="color:var(--text-2)">client</b>, not you.</p></div>`
    : '';
  const whyList = p.why.map((w) => `<li>${w}</li>`).join('');
  const realKnown = !!p.loop.real;

  view.innerHTML = `
    <div class="payer-hero" data-tour="payerhero">
      <div class="pn">${p.name} ${flagBadge(p.flag)}</div>
      <div class="pnif">client · ${p.nif} · ${p.observed} invoices observed</div>
      <div class="psum">${p.summaryHTML}</div>
      <div class="pobs">Reliability sharpens every time they pay · scores your <b>client</b>, never you.</div>
    </div>

    <div class="eyebrow">How they pay · transparent, not a black box</div>
    <div class="card comp">${comps}</div>

    <div class="eyebrow">Payment history · each dot is one invoice</div>
    <div class="card">
      <div class="spark" id="spark"><div class="base"></div><div class="baselbl">due date</div></div>
      <p style="color:var(--text-3);font-size:10.5px;font-family:var(--mono);text-align:center">above = paid late · below = paid early · blue = next, expected</p>
    </div>

    <div class="why-row" id="whyRow">
      <div class="wh"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--blue)" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/></svg>Why this estimate?<span class="ai predict">predict</span><span class="arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></span></div>
      <div class="wb"><div class="wb-inner"><ul>${whyList}</ul>
        <p style="margin-top:8px;color:var(--text-3)">Drawn from interpretable model coefficients — the same explanation a human reviewer sees (GDPR Art. 22).</p></div></div>
    </div>

    ${feed}

    <div class="eyebrow">The closed loop</div>
    <div class="card loop-card" data-tour="flywheel">
      <div style="display:flex;align-items:center;gap:8px"><b style="font-size:13.5px">A past invoice</b><span class="ai predict" style="margin-left:auto">predicted</span></div>
      <div class="loop-vs">
        <div class="pv"><div class="k">Predicted</div><div class="d">${p.loop.pred}</div></div>
        <div class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
        <div class="pv real" id="realCell" style="opacity:.3"><div class="k">Actually paid</div><div class="d" id="realDate">—</div></div>
      </div>
      ${realKnown
        ? `<button class="btn outline sm" id="markPaid">Mark this invoice paid</button>
           <div class="loop-tick" id="loopTick" style="display:none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9"/><path d="M3 4v5h5"/></svg>Model updated · next prediction tightened · logged append-only</div>`
        : `<p style="color:var(--text-3);font-size:11.5px;font-family:var(--mono);text-align:center;margin-top:4px">Still open — its real pay-date will retrain the model when it lands.</p>`}
    </div>`;

  renderSpark($('#spark', view), p.spark, p.expected);
  $('#whyRow', view).querySelector('.wh').addEventListener('click', () => $('#whyRow', view).classList.toggle('open'));
  const mp = $('#markPaid', view);
  if (mp) mp.addEventListener('click', () => {
    $('#realCell', view).style.opacity = '1';
    $('#realDate', view).textContent = p.loop.real;
    $('#loopTick', view).style.display = 'flex';
    mp.textContent = '✓ logged — model retrained';
    mp.disabled = true; mp.style.opacity = '.7';
  });
}

function renderSpark(el, arr, expected) {
  $$('.dot', el).forEach((d) => d.remove());
  const n = arr.length;
  arr.forEach((v, i) => {
    const dot = document.createElement('div');
    const x = n > 1 ? (i / (n - 1)) * 90 + 5 : 50;
    const val = v === null ? expected : v;
    let y = 50 - val * 1.05; y = Math.max(11, Math.min(89, y));
    dot.className = 'dot ' + (v === null ? 'next' : v < 0 ? 'early' : v > 30 ? 'vlate' : 'late');
    dot.style.left = x + '%'; dot.style.top = y + '%';
    dot.title = v === null ? `next — expected ~+${expected}d` : v < 0 ? `${-v}d early` : `+${v}d late`;
    el.appendChild(dot);
  });
}

/* ----------------------------------------------------------------------------
   MOMENT 5 · the nine-agent bridge sequence ending at the human gate
---------------------------------------------------------------------------- */
const AGENTS = [
  { mode: 'act', name: 'Onboarding', run: 'Connecting your linked accounts and resolving Acme Studios by NIF…', done: 'Acme Studios S.L. matched · CIF B-12345678' },
  { mode: 'predict', name: 'Identity & Fraud', padlock: 'aml', run: 'Sanctions, PEP &amp; synthetic-ID checks — fraud lane only, kept separate from credit.', done: 'Clear. If flagged, this routes to an AML officer — a different person, a different law.' },
  { mode: 'predict', name: 'Reliability', asof: true, run: 'Acme pays ~18 days late, steady. No public-distress filing on their NIF.', done: 'P(paid late) modest · expected +18d · top drivers explained.', sub: 'I predict and explain — I never decide.' },
  { mode: 'predict', name: 'Safe-to-Borrow', gauge: 65, run: 'After VAT/IRPF set-aside and committed outflows…', done: 'You can safely bridge up to <b>€6,500</b> today · tightest day 12 Jul.' },
  { mode: 'recommend', name: 'Credit Decision', padlock: 'grant', run: 'Your €8,400 ask vs the €6,500 safe ceiling…', done: 'Above safe capacity — a reduced offer is <b>adverse</b>, so it goes to a human.', chip: 'Sent to credit reviewer' },
];
const POST_AGENTS = [
  ['Offer &amp; Pricing', '€6,500 @ 1.4% on the named receivable · “why this rate” explained'],
  ['Disbursement', 'Funds move after you sign + SCA · schedule pegged to Acme’s pay-date'],
  ['Servicing &amp; Early-Warning', 'Keeps watching Acme · offers a re-date if they slow (you confirm)'],
  ['Repayment &amp; Limit', 'Auto-settles when Acme pays · logs predicted-vs-realized · retrains'],
];

function buildAgents() {
  const mount = $('#agents');
  if (mount.dataset.built) return;
  mount.dataset.built = '1';
  mount.innerHTML =
    AGENTS.map((a, i) => `
      <div class="agent ${a.mode}" data-n="${i}">
        ${a.padlock ? `<div class="padlock ${a.padlock}" title="human gate — never automated">${ICON.lock}</div>` : ''}
        <div class="node"><span class="num">${i + 1}</span></div>
        <div class="acard">
          <div class="atop"><b>${a.name}</b><span class="ai ${a.mode}">${a.mode}</span></div>
          <div class="acopy js-copy">${a.run}${a.asof ? '<span class="asof">_asof</span>' : ''}</div>
          ${a.gauge ? '<div class="gauge"><i></i></div>' : ''}
          ${a.sub ? `<div class="asub">${a.sub}</div>` : ''}
          <div class="js-chip"></div>
        </div>
      </div>`).join('') +
    POST_AGENTS.map((a, i) => `
      <div class="agent" data-post="1" style="opacity:.32">
        <div class="node"><span class="num">${i + 6}</span></div>
        <div class="acard">
          <div class="atop"><b>${a[0]}</b><span class="badge" style="margin-left:auto">after a human signs</span></div>
          <div class="acopy">${a[1]}</div>
        </div>
      </div>`).join('');
}

let agentsRan = false;
async function runAgents(btn) {
  if (agentsRan) return; agentsRan = true;
  btn.disabled = true; btn.style.opacity = '.55';
  btn.innerHTML = '<span>Agents working…</span>';
  const nodes = $$('#agents .agent:not([data-post])');
  for (let i = 0; i < AGENTS.length; i++) {
    const el = nodes[i]; const a = AGENTS[i];
    el.classList.add('seen', 'active');
    if (a.gauge) setTimeout(() => { const g = $('.gauge i', el); if (g) g.style.width = a.gauge + '%'; }, 120);
    await sleep(900);
    el.classList.remove('active');
    if (a.mode !== 'recommend') { el.classList.add('done'); $('.node', el).innerHTML = ICON.check; }
    $('.js-copy', el).innerHTML = a.done + (a.asof ? '<span class="asof">_asof &lt; issue</span>' : '');
    if (a.chip) $('.js-chip', el).innerHTML = `<span class="badge warn" style="margin-top:8px"><i class="dot"></i>${a.chip}</span>`;
    await sleep(420);
  }
  revealGate();
}

function revealGate() {
  const mount = $('#gateMount');
  mount.innerHTML = `
    <div class="gate">
      <div class="glock">${ICON.lock}</div>
      <b>Awaiting human review</b>
      <p>A credit reviewer is checking your reduced-offer packet — typically under 2 hours. You'll see exactly <b>why €6,500</b> and <b>why 1.4%</b>, and can dispute it with one tap.</p>
      <div class="legal">AI sizes &amp; warns — a human signs every loan · Annex III §5(b) + GDPR Art. 22</div>
    </div>
    <p style="text-align:center;color:var(--text-3);font-size:11px;font-family:var(--mono);margin-top:12px">The sequence stops here on purpose. The agents sized &amp; warned — the adverse call is a person's.</p>`;
  mount.scrollIntoView({ block: 'end', behavior: 'smooth' });
}

$('#runAgents').addEventListener('click', (e) => runAgents(e.currentTarget));
buildAgents();

/* ----------------------------------------------------------------------------
   GUIDED TOUR
---------------------------------------------------------------------------- */
const coach = $('#coach');
const spot = $('#spot');
const TOUR = [
  { view: 'home', target: 'verdict', title: 'Are we okay?', body: 'A calm bank opens with one answer, not a feed. The home screen says you are <b>covered through ~22 Jul</b>, with the next tight spot flagged early.' },
  { view: 'home', target: 'lying', action: 'reveal', title: 'One balance lies', body: 'A single number blends three different kinds of money. Watch it <b>split into three live truths</b> — mine, the tax office\'s, and not-here-yet.' },
  { view: 'home', target: 'truths', title: 'Three live truths', body: 'This is the whole product in one card: money that is <b>genuinely yours</b>, the slice the <b>tax office</b> already owns, and revenue <b>owed but not arrived</b> — forecast from how each client actually pays.' },
  { view: 'money', target: 'sweep', action: 'sweep', title: 'Tax-Sweep+', body: 'When a client pays, the VAT/IRPF slice <b>sweeps itself</b> into a locked sub-account. The best screen is sometimes no screen — money is just where it should be.' },
  { view: 'invoices', target: 'radar', title: 'Concurso Radar', body: 'Every client is matched daily against public distress registries (BORME, RAI) by tax ID — and it stays <b>silent while everything is green.</b>' },
  { view: 'invoices', target: 'distress', action: 'distress', title: 'A weeks-early warning', body: 'A pre-concurso filing lands on Caixa Studio. It flips red <b>weeks before</b> they would miss a payment — and any bridge against them is gated. This is about your <b>client</b>, not you.' },
  { view: 'payer', payer: 'acme', target: 'payerhero', title: 'The Payer is the object', body: 'Tap a client and you see <b>per-Payer reliability</b> in transparent components — average days-late, its volatility, on-time rate — never a black-box score.' },
  { view: 'payer', payer: 'acme', target: 'flywheel', action: 'markpaid', title: 'The closed loop', body: 'Reality lands: predicted vs actual pay-date is <b>logged and retrains the model</b>. Every realized payment sharpens the next bridge price. That loop is the moat.' },
  { view: 'financing', target: 'dontborrow', title: 'The honest answer', body: 'Here is the part an engagement-driven bank won\'t copy: when your cash is genuinely coming, we tell you <b>not to borrow.</b> We win when you borrow less.' },
  { view: 'bridge', target: 'run', action: 'run', title: 'Nine agents, one human gate', body: 'When you do bridge a named invoice, nine agents <b>size and warn</b> — then deliberately <b>stop at a human</b>. A person signs every loan (Annex III §5(b) + GDPR Art. 22).' },
  { view: 'about', target: null, title: 'What\'s real', body: 'The data here is illustrative; the <b>thesis and the numbers are evidenced</b>. One object, one loop, one objective — that\'s NetBank. Explore freely from here.' },
];
let step = 0;

function positionSpot(target) {
  if (!target) { spot.classList.remove('show'); return; }
  const r = target.getBoundingClientRect();
  const pad = 8;
  spot.style.left = r.left - pad + 'px';
  spot.style.top = r.top - pad + 'px';
  spot.style.width = r.width + pad * 2 + 'px';
  spot.style.height = r.height + pad * 2 + 'px';
  spot.classList.add('show');
}

async function runStep(i) {
  step = i;
  const s = TOUR[i];
  if (s.payer) state.payer = s.payer;
  navigate(s.view);
  // coach content
  $('#coachStep').textContent = `Step ${i + 1} / ${TOUR.length}`;
  $('#coachBar').style.width = ((i + 1) / TOUR.length) * 100 + '%';
  $('#coachTitle').innerHTML = s.title;
  $('#coachBody').innerHTML = s.body;
  $('#coachBack').style.visibility = i === 0 ? 'hidden' : 'visible';
  $('#coachNext').textContent = i === TOUR.length - 1 ? 'Finish ✓' : 'Next →';
  spot.classList.remove('show');
  await sleep(380);
  // fire the demonstrated action
  if (s.action === 'reveal') revealTruths();
  if (s.action === 'sweep' && !swept) $('#simulatePayment').click();
  if (s.action === 'distress' && !state.distress) $('#simulateDistress').click();
  if (s.action === 'run' && !agentsRan) $('#runAgents').click();
  if (s.action === 'markpaid') { await sleep(200); const mp = $('#markPaid'); if (mp && !mp.disabled) mp.click(); }
  await sleep(s.action ? 520 : 120);
  // spotlight the target
  const target = s.target ? viewport.querySelector(`.view.active [data-tour="${s.target}"]`) : null;
  if (target) target.scrollIntoView({ block: 'center' });
  await sleep(260);
  positionSpot(target);
}

function startTour() {
  state.touring = true;
  document.body.classList.add('touring');
  coach.classList.add('show');
  runStep(0);
}
function endTour() {
  state.touring = false;
  document.body.classList.remove('touring');
  coach.classList.remove('show');
  spot.classList.remove('show');
}

$('#startTour').addEventListener('click', startTour);
$('#coachExit').addEventListener('click', endTour);
$('#coachBack').addEventListener('click', () => step > 0 && runStep(step - 1));
$('#coachNext').addEventListener('click', () => {
  if (step < TOUR.length - 1) runStep(step + 1); else endTour();
});
document.addEventListener('keydown', (e) => {
  if (!state.touring) return;
  if (e.key === 'Escape') endTour();
  if (e.key === 'ArrowRight') $('#coachNext').click();
  if (e.key === 'ArrowLeft') $('#coachBack').click();
});
window.addEventListener('resize', () => {
  if (!state.touring) return;
  const s = TOUR[step];
  const target = s.target ? viewport.querySelector(`.view.active [data-tour="${s.target}"]`) : null;
  positionSpot(target);
});

/* boot */
navigate('home');
})();
