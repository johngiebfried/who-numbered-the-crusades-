// Scroll steps, plates, inline numbers and calcs.
window.wkState = {};

dash.calc('holy_counts', {
  inputs: ['holyland'],
  title: 'Holy Land section, numbered vs. not',
  description: 'How many entries the Holy Land section of the English box has, and how many of them are numbered.',
  fn: (holyland) => [{ total: holyland.length, numbered: holyland.filter((r) => r.numbered === 'yes').length }],
});

dash.calc('box_totals', {
  inputs: ['scope_grid'],
  title: 'Expeditions in each box',
  description: 'Expeditions listed in each language\'s crusade box in November 2026, summed over the kinds.',
  fn: (scope_grid) => {
    const by = new Map();
    scope_grid.forEach((r) => by.set(r.language, (by.get(r.language) || 0) + Number(r.now)));
    return Array.from(by, ([language, items]) => ({ language, items }));
  },
});

(function () {
  const fmt = d3.format(',');
  function rowFor(el, rows) {
    if (el.dataset.row != null) return rows[Number(el.dataset.row)];
    const conds = (el.dataset.where || '').split('&').filter(Boolean).map((c) => c.split('=').map(decodeURIComponent));
    return rows.find((r) => conds.every(([k, v]) => String(r[k]) === v));
  }
  dash.draw('val', (el) => {
    const d = dash.data(el.dataset.source);
    if (d.status !== 'ok' || !Array.isArray(d.data)) { el.textContent = '—'; return; }
    const r = rowFor(el, d.data);
    const v = r ? Number(r[el.dataset.field]) : NaN;
    el.textContent = Number.isFinite(v) ? fmt(v) : '—';
  });

  // Image plates: base64 WebP text attached as datasets.
  dash.draw('plate', {
    mount(el) { const img = document.createElement('img'); img.alt = ''; img.decoding = 'async'; el.append(img); return { img }; },
    update(el, m) {
      const d = dash.data(el.dataset.source);
      if (d.status !== 'ok') return;
      let s = d.data;
      if (s && typeof s === 'object' && !Array.isArray(s)) s = s.text || s.content || '';
      if (Array.isArray(s)) s = s.map((r) => (typeof r === 'string' ? r : Object.values(r).join(''))).join('');
      s = String(s || '').replace(/\s+/g, '');
      if (!s || m.src === s.length) return;
      m.src = s.length;
      m.img.src = 'data:image/webp;base64,' + s;
    },
  });
})();

// Scroll steps choose what each sticky figure shows. Only class, hidden and style are written here.
document.querySelectorAll('.wk-wrap').forEach((wrap) => {
  const steps = Array.from(wrap.querySelectorAll('.wk-step'));
  const fig = wrap.querySelector('.wk-fig');
  if (!steps.length || !fig) return;
  function activate(step, initial) {
    steps.forEach((s) => s.classList.toggle('is-active', s === step));
    const panel = step.dataset.panel;
    window.wkState[wrap.id] = Object.assign({}, step.dataset);
    fig.querySelectorAll('[data-panel-for]').forEach((p) => { p.hidden = p.dataset.panelFor !== panel; });
    fig.querySelectorAll('[data-cap]').forEach((c) => { c.hidden = c.dataset.cap !== panel; });
    ['all', 'eight', 'rep'].forEach((h) => fig.classList.toggle('hl-' + h, step.dataset.hl === h));
    if (!initial) dash.draw(panel);
  }
  activate(steps[0], true);
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) activate(en.target); });
  }, { root: document, rootMargin: '-48% 0px -48% 0px', threshold: 0 });
  steps.forEach((s) => io.observe(s));
});
