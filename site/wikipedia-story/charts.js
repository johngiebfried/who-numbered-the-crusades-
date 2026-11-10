(function () {
  const fmt = d3.format(',');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const C9 = 'var(--wk-9)', C8 = 'var(--wk-8)', C7 = 'var(--wk-7)', CDE = 'var(--wk-de)';
  const MUTED = 'var(--cds-chart-muted, #c9c7c1)', GRID = 'var(--cds-chart-grid, #ecebe7)', AXIS = 'var(--cds-text-secondary, #6b6a66)';
  const st = (id) => window.wkState[id] || {};
  const widthOf = (el) => Math.max(300, el.clientWidth || (el.closest('.wk-fig') || el).clientWidth - 30 || 600);
  const ym = (s) => { const [y, m, d] = String(s).split('-').map(Number); return new Date(Date.UTC(y, (m || 1) - 1, d || 1)); };
  const LANG = { en: 'English', de: 'German', fr: 'French', it: 'Italian', es: 'Spanish', ca: 'Catalan', pt: 'Portuguese', nl: 'Dutch', el: 'Greek',
    ar: 'Arabic', fa: 'Persian', he: 'Hebrew', tr: 'Turkish', pl: 'Polish', cs: 'Czech', ru: 'Russian', uk: 'Ukrainian', hu: 'Hungarian',
    sv: 'Swedish', da: 'Danish', no: 'Norwegian', fi: 'Finnish' };

  function mountSvg(el) {
    const svg = d3.select(el).append('svg');
    const tip = document.createElement('div'); tip.className = 'wk-tip'; tip.hidden = true; el.append(tip);
    const show = (ev, lines) => {
      tip.replaceChildren(...lines.map((l, i) => { const d = document.createElement('div'); if (i === 0) d.className = 'wk-tip-h'; d.textContent = l; return d; }));
      tip.hidden = false;
      const r = el.getBoundingClientRect();
      let x = ev.clientX - r.left + 12, y = ev.clientY - r.top + 12;
      if (x > r.width - 230) x = Math.max(4, ev.clientX - r.left - 240);
      if (y > r.height - 60) y = Math.max(4, ev.clientY - r.top - 60);
      tip.style.left = x + 'px'; tip.style.top = y + 'px';
    };
    const hide = () => { tip.hidden = true; };
    return { svg, show, hide };
  }
  function placeholder(m, d) {
    m.svg.selectAll('*').remove();
    m.svg.attr('viewBox', '0 0 600 60').append('text').attr('x', 8).attr('y', 30).style('fill', AXIS)
      .text(d.status === 'error' ? 'Failed to load' : '—');
  }
  const txt = (g, x, y, s, o = {}) => g.append('text').attr('x', x).attr('y', y).attr('text-anchor', o.anchor || 'start')
    .style('fill', o.fill || AXIS).style('font-size', (o.size || 11) + 'px').style('font-weight', o.weight || null).text(s);

  // ---------- Opening: edits per month ----------
  dash.draw('edits', {
    mount: mountSvg,
    update(el, m) {
      const d = dash.data('edits');
      if (d.status !== 'ok') return placeholder(m, d);
      const rows = d.data.map((r) => ({ month: r.month, t: ym(r.month), edits: Number(r.edits), editors: Number(r.editors) }));
      const W = widthOf(el), H = Math.round(Math.min(420, Math.max(280, W * 0.62)));
      const L = 40, R = 10, T = 30, B = 26;
      const x = d3.scaleBand().domain(['2001-09'].concat(rows.map((r) => r.month))).range([L, W - R]).paddingInner(0.15);
      const y = d3.scaleLinear().domain([0, d3.max(rows, (r) => r.edits) * 1.05]).nice().range([H - B, T]);
      m.svg.attr('viewBox', `0 0 ${W} ${H}`).selectAll('*').remove();
      const g = m.svg.append('g');
      y.ticks(5).forEach((t) => {
        g.append('line').attr('x1', L).attr('x2', W - R).attr('y1', y(t)).attr('y2', y(t)).style('stroke', GRID);
        txt(g, L - 6, y(t) + 4, fmt(t), { anchor: 'end', size: 10 });
      });
      ['2002', '2003', '2004', '2005', '2006', '2007', '2008'].forEach((yr) => {
        const xx = x(yr + '-01');
        g.append('line').attr('x1', xx).attr('x2', xx).attr('y1', T - 4).attr('y2', H - B).style('stroke', GRID);
        txt(g, xx + 2, H - 8, yr, { size: 10 });
      });
      g.selectAll('rect.b').data(rows).join('rect').attr('class', 'b')
        .attr('x', (r) => x(r.month)).attr('width', x.bandwidth())
        .attr('y', (r) => y(r.edits)).attr('height', (r) => y(0) - y(r.edits))
        .style('fill', (r) => (r.t < ym('2004-03') ? C8 : C9)).style('opacity', 0.9)
        .on('pointermove', (ev, r) => m.show(ev, [r.month, `${fmt(r.edits)} edits by ${fmt(r.editors)} editors`]))
        .on('pointerleave', m.hide);
      // 9/11 marker
      const x911 = x('2001-09') + x.bandwidth() / 2;
      g.append('line').attr('x1', x911).attr('x2', x911).attr('y1', T - 6).attr('y2', H - B).style('stroke', 'var(--color-bad)').style('stroke-dasharray', '3 3');
      txt(g, x911 + 4, T + 4, '11 Sept 2001', { fill: 'var(--color-bad)', size: 11, weight: 600 });
      txt(g, x911 + 4, T + 18, 'oldest surviving version, 28 Oct', { size: 10.5 });
      const peak = rows.reduce((a, b) => (b.edits > a.edits ? b : a));
      txt(g, x(peak.month) + x.bandwidth() / 2, y(peak.edits) - 6, `${fmt(peak.edits)}`, { anchor: 'middle', size: 11, weight: 600, fill: 'var(--color-fg)' });
      const sx = x('2004-01');
      txt(g, (L + sx) / 2, y(40), 'under ten a month', { anchor: 'middle', size: 11, fill: C8 });
    },
  });

  // ---------- Act I: counts by language ----------
  const ORDER = ['en', 'nl', 'pt', 'de', 'ar', 'el', 'pl', 'it', 'he', 'tr', 'es', 'fr', 'fa', 'ru', 'cs'];
  const fillN = (n) => (n >= 9 ? C9 : n === 8 ? C8 : n === 7 ? C7 : MUTED);
  dash.draw('counts', {
    mount: mountSvg,
    update(el, m) {
      const d = dash.data('wp_counts');
      if (d.status !== 'ok') return placeholder(m, d);
      const s = st('w1');
      const focus = (s.langs || '').split(',').filter(Boolean);
      const W = widthOf(el), narrow = W < 520;
      const L = narrow ? 70 : 84, R = 12, T = 24, rowH = narrow ? 20 : 25;
      const H = T + ORDER.length * rowH + 30;
      const x = d3.scaleLinear().domain([2003, 2027]).range([L, W - R]);
      m.svg.attr('viewBox', `0 0 ${W} ${H}`).selectAll('*').remove();
      const g = m.svg.append('g');
      const ticks = narrow ? [2005, 2010, 2015, 2020, 2025] : d3.range(2004, 2027, 2);
      ticks.forEach((t) => {
        g.append('line').attr('x1', x(t)).attr('x2', x(t)).attr('y1', T - 4).attr('y2', H - 24).style('stroke', GRID);
        txt(g, x(t), T - 10, String(t), { anchor: 'middle', size: 10 });
      });
      const yOf = (lang) => T + ORDER.indexOf(lang) * rowH;
      ORDER.forEach((lang) => {
        const on = !focus.length || focus.includes(lang);
        txt(g, L - 8, yOf(lang) + rowH / 2 + 4, LANG[lang], { anchor: 'end', size: narrow ? 10.5 : 12, fill: on ? 'var(--color-fg)' : AXIS, weight: on && focus.length ? 600 : null });
      });
      const segs = d.data.filter((r) => ORDER.includes(r.language)).map((r) => ({
        r, lang: r.language, a: Number(r.start), b: Number(r.end) + (Number(r.end) >= 2026 ? 0.9 : 1), n: Number(r.top), dbl: r.double === 'yes',
      }));
      const sel = g.selectAll('g.seg').data(segs).join('g').attr('class', 'seg')
        .style('opacity', (sg) => (!focus.length || focus.includes(sg.lang) ? 1 : 0.18))
        .on('pointermove', (ev, sg) => m.show(ev, [`${LANG[sg.lang]} box, ${sg.r.start === sg.r.end ? sg.r.start : sg.r.start + '–' + (Number(sg.r.end) >= 2026 ? 'now' : sg.r.end)}`,
          sg.dbl ? 'Highest number: 7, written "Siebter (Achter)"' : `Highest number: ${sg.n}`].concat(sg.r.note ? [sg.r.note] : [])))
        .on('pointerleave', m.hide);
      sel.append('rect').attr('x', (sg) => x(sg.a) + 0.5).attr('y', (sg) => yOf(sg.lang) + 3).attr('height', rowH - 6)
        .attr('width', (sg) => Math.max(2, x(sg.b) - x(sg.a) - 1)).attr('rx', 3)
        .style('fill', (sg) => (sg.dbl ? CDE : fillN(sg.n)));
      sel.append('text').attr('x', (sg) => x(sg.a) + 5).attr('y', (sg) => yOf(sg.lang) + rowH / 2 + 4)
        .style('fill', '#fff').style('font-size', '11px').style('font-weight', 600)
        .text((sg) => (x(sg.b) - x(sg.a) < (sg.dbl ? 40 : 14) ? '' : sg.dbl ? '7 (8)' : String(sg.n)));
      if (s.mark === '2019') {
        const xx = x(2019.88);
        g.append('line').attr('x1', xx).attr('x2', xx).attr('y1', T - 4).attr('y2', H - 24).style('stroke', 'var(--color-fg)').style('stroke-dasharray', '3 3');
        txt(g, Math.min(xx, W - 150), H - 8, '17 Nov 2019: "Ninth" renamed', { size: 11, fill: 'var(--color-fg)', weight: 600 });
      } else {
        txt(g, narrow ? 8 : L, H - 8, narrow ? 'German: old count, modern one in brackets' : 'German (green): "Siebter (Achter)", the old count with the modern one in brackets', { size: 10.5 });
      }
    },
  });

  // ---------- Act I: views ----------
  dash.draw('views', {
    mount: mountSvg,
    update(el, m) {
      const d = dash.data('ninth');
      if (d.status !== 'ok') return placeholder(m, d);
      const rows = d.data.map((r) => ({ year: r.year, ninth: Number(r.ninth_crusade), ed: Number(r.lord_edwards_crusade) }));
      const W = widthOf(el), H = Math.round(Math.min(400, Math.max(280, W * 0.6)));
      const L = 46, R = 10, T = 34, B = 26;
      const x = d3.scaleBand().domain(rows.map((r) => r.year)).range([L, W - R]).padding(0.25);
      const y = d3.scaleLinear().domain([0, d3.max(rows, (r) => r.ninth + r.ed)]).nice().range([H - B, T]);
      m.svg.attr('viewBox', `0 0 ${W} ${H}`).selectAll('*').remove();
      const g = m.svg.append('g');
      y.ticks(5).forEach((t) => {
        g.append('line').attr('x1', L).attr('x2', W - R).attr('y1', y(t)).attr('y2', y(t)).style('stroke', GRID);
        txt(g, L - 6, y(t) + 4, d3.format('~s')(t), { anchor: 'end', size: 10 });
      });
      const bars = g.selectAll('g.yr').data(rows).join('g').attr('class', 'yr')
        .on('pointermove', (ev, r) => m.show(ev, [r.year, `"Ninth Crusade": ${fmt(r.ninth)}`, `"Lord Edward's crusade": ${fmt(r.ed)}`]))
        .on('pointerleave', m.hide);
      bars.append('rect').attr('x', (r) => x(r.year)).attr('width', x.bandwidth()).attr('y', (r) => y(r.ninth)).attr('height', (r) => y(0) - y(r.ninth)).style('fill', C8);
      bars.append('rect').attr('x', (r) => x(r.year)).attr('width', x.bandwidth()).attr('y', (r) => y(r.ninth + r.ed)).attr('height', (r) => y(r.ninth) - y(r.ninth + r.ed)).style('fill', C9);
      rows.forEach((r) => txt(g, x(r.year) + x.bandwidth() / 2, H - 8, "'" + r.year.slice(2), { anchor: 'middle', size: 10 }));
      const xr = x('2019') + x.bandwidth() + x.step() * 0.12;
      g.append('line').attr('x1', xr).attr('x2', xr).attr('y1', T - 10).attr('y2', H - B).style('stroke', 'var(--color-fg)').style('stroke-dasharray', '3 3');
      txt(g, xr + 4, T - 14 + 8, 'rename', { size: 10.5, fill: 'var(--color-fg)' });
      g.append('rect').attr('x', L).attr('y', 4).attr('width', 10).attr('height', 10).style('fill', C8);
      txt(g, L + 14, 13, 'arrived via "Ninth Crusade"', { size: 11 });
      g.append('rect').attr('x', L + 190).attr('y', 4).attr('width', 10).attr('height', 10).style('fill', C9);
      txt(g, L + 204, 13, "via \"Lord Edward's crusade\"", { size: 11 });
    },
  });

  // ---------- Act II: links over time ----------
  dash.draw('links', {
    mount: mountSvg,
    update(el, m) {
      const d = dash.data('links'), e = dash.data('eras'), v = dash.data('events');
      if (d.status !== 'ok') return placeholder(m, d);
      const s = st('w2');
      const W = widthOf(el), narrow = W < 520;
      const H = Math.round(Math.min(440, Math.max(300, W * 0.7)));
      const L = 34, R = 12, T = 18, B = 66;
      const end = ym('2026-11');
      const x = d3.scaleUtc().domain([ym('2004-01'), end]).range([L, W - R]);
      const y = d3.scaleLinear().domain([0, 110]).range([H - B, T]);
      m.svg.attr('viewBox', `0 0 ${W} ${H}`).selectAll('*').remove();
      const g = m.svg.append('g');
      const win = (s.win || '').split(',');
      if (win.length === 2) {
        g.append('rect').attr('x', x(ym(win[0]))).attr('y', T).attr('width', x(ym(win[1])) - x(ym(win[0]))).attr('height', H - B - T)
          .style('fill', 'var(--color-warn)').style('opacity', 0.1);
      }
      [0, 25, 50, 75, 100].forEach((t) => {
        g.append('line').attr('x1', L).attr('x2', W - R).attr('y1', y(t)).attr('y2', y(t)).style('stroke', GRID);
        txt(g, L - 6, y(t) + 4, String(t), { anchor: 'end', size: 10 });
      });
      (narrow ? [2005, 2010, 2015, 2020, 2025] : d3.range(2004, 2027, 2)).forEach((yr) => txt(g, x(ym(yr + '-01')), H - B + 14, String(yr), { anchor: 'middle', size: 10 }));
      const series = ['en', 'de'].map((lang) => {
        const pts = d.data.filter((r) => r.language === lang).map((r) => ({ t: ym(r.month), n: Number(r.links), month: r.month }));
        pts.push({ t: end, n: pts[pts.length - 1].n, month: 'now' });
        return { lang, pts };
      });
      const line = d3.line().curve(d3.curveStepAfter).x((p) => x(p.t)).y((p) => y(p.n));
      series.forEach((se) => {
        g.append('path').attr('d', line(se.pts)).style('fill', 'none').style('stroke', se.lang === 'en' ? C9 : CDE).style('stroke-width', 2.2);
        const last = se.pts[se.pts.length - 1];
        txt(g, x(last.t) - 2, y(last.n) - 6, se.lang === 'en' ? 'English' : 'German', { anchor: 'end', size: 11, weight: 600, fill: se.lang === 'en' ? C9 : CDE });
      });
      const enPts = series[0].pts.slice(0, -1);
      g.selectAll('circle.pt').data(enPts).join('circle').attr('class', 'pt').attr('cx', (p) => x(p.t)).attr('cy', (p) => y(p.n)).attr('r', 6)
        .style('fill', 'transparent').on('pointermove', (ev, p) => m.show(ev, [p.month, `${p.n} links in the English box`])).on('pointerleave', m.hide);
      // events for this step
      if (v.status === 'ok') {
        const nAt = (t) => { let n = 0; enPts.forEach((p) => { if (p.t <= t) n = p.n; }); return n; };
        const evs = v.data.filter((r) => r.step === s.ev);
        evs.forEach((r, i) => {
          const t = ym(r.month), cx = x(t), cy = y(nAt(t));
          g.append('circle').attr('cx', cx).attr('cy', cy).attr('r', 4).style('fill', 'var(--color-panel)').style('stroke', 'var(--color-fg)').style('stroke-width', 1.5);
          const ly = T + 12 + i * 15;
          const right = cx > W * 0.55;
          g.append('line').attr('x1', cx).attr('x2', cx).attr('y1', cy - 5).attr('y2', ly + 3).style('stroke', 'var(--color-fg)').style('opacity', 0.35);
          txt(g, right ? cx - 4 : cx + 4, ly, r.label, { anchor: right ? 'end' : 'start', size: narrow ? 10 : 11, fill: 'var(--color-fg)' });
        });
      }
      // eras band
      if (e.status === 'ok') {
        const by = H - B + 36;
        txt(g, L, by - 5, 'How the English box was organized', { size: 10 });
        e.data.forEach((r, i) => {
          const a = x(ym(r.start)), b = x(ym(r.end));
          g.append('rect').attr('x', a).attr('y', by).attr('width', Math.max(1, b - a - 1)).attr('height', 18)
            .style('fill', i % 2 ? 'color-mix(in srgb, var(--wk-9) 28%, var(--color-panel))' : 'color-mix(in srgb, var(--wk-9) 14%, var(--color-panel))')
            .on('pointermove', (ev) => m.show(ev, [r.label, `${r.start} to ${r.end}`])).on('pointerleave', m.hide);
          if (b - a > r.label.length * 5.6) txt(g, (a + b) / 2, by + 13, r.label, { anchor: 'middle', size: 10, fill: 'var(--color-fg)' });
        });
      }
    },
  });

  // ---------- Act II: contested entries ----------
  const CROWS = ['Reconquista', 'Iberian battles', 'Nicopolis', 'Lepanto, Vienna, Armada', 'Popular crusades', 'Northern crusades', 'Crusades against heretics', 'Holy Leagues', 'Proto-crusades', 'Ideology and institutions', 'Reactionary crusades 1789–1939'];
  dash.draw('contested', {
    mount: mountSvg,
    update(el, m) {
      const d = dash.data('contested');
      if (d.status !== 'ok') return placeholder(m, d);
      const s = st('w2');
      const focus = (s.rows || '').split('|').filter(Boolean);
      const W = widthOf(el), narrow = W < 520;
      const L = narrow ? 120 : 170, R = 10, T = 22, rowH = narrow ? 24 : 30;
      const H = T + CROWS.length * rowH + 12;
      const x = d3.scaleUtc().domain([ym('2004-01'), ym('2026-11')]).range([L, W - R]);
      m.svg.attr('viewBox', `0 0 ${W} ${H}`).selectAll('*').remove();
      const g = m.svg.append('g');
      (narrow ? [2005, 2010, 2015, 2020, 2025] : d3.range(2004, 2027, 2)).forEach((yr) => {
        const xx = x(ym(yr + '-01'));
        g.append('line').attr('x1', xx).attr('x2', xx).attr('y1', T - 4).attr('y2', H - 8).style('stroke', GRID);
        txt(g, xx, T - 9, String(yr), { anchor: 'middle', size: 10 });
      });
      CROWS.forEach((name, i) => {
        const on = !focus.length || focus.includes(name);
        txt(g, L - 8, T + i * rowH + rowH / 2 + 4, name.replace(' 1789–1939', ''), { anchor: 'end', size: narrow ? 10 : 11.5, fill: on ? 'var(--color-fg)' : AXIS, weight: on && focus.length ? 600 : null });
      });
      const spans = d.data.map((r) => ({ name: r.item, a: ym(r.start), b: r.end ? ym(r.end) : ym('2026-11'), open: !r.end, start: r.start, end: r.end }));
      g.selectAll('rect.sp').data(spans).join('rect').attr('class', 'sp')
        .attr('x', (p) => x(p.a)).attr('width', (p) => Math.max(3, x(p.b) - x(p.a)))
        .attr('y', (p) => T + CROWS.indexOf(p.name) * rowH + 5).attr('height', rowH - 10).attr('rx', 3)
        .style('fill', (p) => (focus.length && focus.includes(p.name) ? C8 : C9))
        .style('opacity', (p) => (!focus.length || focus.includes(p.name) ? 0.95 : 0.2))
        .on('pointermove', (ev, p) => m.show(ev, [p.name, `in the box ${p.start} to ${p.end || 'now'}`])).on('pointerleave', m.hide);
    },
  });

  // ---------- Act II: Holy Land section ----------
  dash.draw('holy', {
    mount(el) { const box = document.createElement('div'); box.className = 'hl-grid'; el.append(box); return { box }; },
    update(el, m) {
      const d = dash.data('holyland');
      if (d.status !== 'ok') { m.box.textContent = '—'; return; }
      const rows = d.data.slice().sort((a, b) => Number(a.order) - Number(b.order));
      m.box.replaceChildren(...rows.map((r) => {
        const c = document.createElement('div');
        c.className = 'hl-chip' + (r.numbered === 'yes' ? ' is-num' : '');
        const n = document.createElement('span'); n.className = r.numbered === 'yes' ? 'hl-n' : ''; n.textContent = r.entry;
        const dd = document.createElement('span'); dd.className = 'hl-d'; dd.textContent = r.dates;
        c.append(n, dd); return c;
      }));
    },
  });

  // ---------- Act III: languages × kinds ----------
  const GLANGS = ['en', 'de', 'fr', 'it', 'es', 'ca', 'pt', 'nl', 'el', 'ar', 'fa', 'he', 'tr', 'pl', 'cs', 'ru', 'uk', 'hu', 'sv', 'da', 'no', 'fi'];
  const CATS = [['NUM', 'Numbered'], ['LEV', 'Other Holy Land'], ['POP', 'Popular'], ['IBER', 'Iberia'], ['NORTH', 'Baltic and north'], ['HER', 'Against heretics'],
    ['POLIT', 'Against Christian rulers'], ['LATE', 'After 1291'], ['PROTO', 'Proto-crusades'], ['MODERN', 'After 1789']];
  dash.draw('grid', {
    mount: mountSvg,
    update(el, m) {
      const d = dash.data('scope_grid');
      if (d.status !== 'ok') return placeholder(m, d);
      const s = st('w3');
      const cols = (s.cols || '').split(',').filter(Boolean), rsel = (s.rowsel || '').split(',').filter(Boolean);
      const W = widthOf(el), tall = W < 600;
      const cell = new Map(d.data.map((r) => [r.language + '|' + r.category, r]));
      const max = d3.max(d.data, (r) => Number(r.now)) || 1;
      const op = d3.scaleSqrt().domain([0, max]).range([0, 0.95]);
      // tall: languages down, kinds across. Wide: kinds down, languages across.
      const A = tall ? GLANGS : CATS.map((c) => c[0]);           // rows
      const Bk = tall ? CATS.map((c) => c[0]) : GLANGS;           // columns
      const catLabel = new Map(CATS);
      const L = tall ? 78 : 150, T = tall ? 96 : 74, R = 6;
      const cw = (W - L - R) / Bk.length, ch = tall ? Math.min(22, Math.max(15, cw * 0.9)) : Math.min(38, Math.max(24, cw * 1.45));
      const H = T + A.length * ch + 8;
      m.svg.attr('viewBox', `0 0 ${W} ${H}`).selectAll('*').remove();
      const g = m.svg.append('g');
      const isOn = (lang, cat) => (!cols.length || cols.includes(lang)) && (!rsel.length || rsel.includes(cat));
      Bk.forEach((k, j) => {
        const xx = L + j * cw + cw / 2;
        const lang = tall ? null : k, cat = tall ? k : null;
        const hot = tall ? rsel.includes(cat) : cols.includes(lang);
        if (tall) {
          g.append('text').attr('transform', `translate(${xx + 3},${T - 6}) rotate(-60)`).style('font-size', '10px')
            .style('fill', hot ? 'var(--color-fg)' : AXIS).style('font-weight', hot ? 600 : null).text(catLabel.get(cat));
        } else {
          g.append('text').attr('transform', `translate(${xx + 3},${T - 6}) rotate(-55)`).style('font-size', '10.5px')
            .style('fill', hot ? 'var(--color-fg)' : AXIS).style('font-weight', hot ? 600 : null).text(LANG[lang]);
        }
      });
      A.forEach((k, i) => {
        const yy = T + i * ch + ch / 2 + 4;
        const hot = tall ? cols.includes(k) : rsel.includes(k);
        txt(g, L - 6, yy, tall ? LANG[k] : catLabel.get(k), { anchor: 'end', size: tall ? 10.5 : 11.5, fill: hot ? 'var(--color-fg)' : AXIS, weight: hot ? 600 : null });
      });
      const cells = [];
      A.forEach((a, i) => Bk.forEach((b, j) => {
        const lang = tall ? a : b, cat = tall ? b : a;
        const r = cell.get(lang + '|' + cat);
        cells.push({ i, j, lang, cat, now: r ? Number(r.now) : 0, ever: r ? Number(r.ever) : 0, items: r ? r.items : '' });
      }));
      const focused = cols.length || rsel.length;
      const gc = g.selectAll('g.c').data(cells).join('g').attr('class', 'c')
        .style('opacity', (c) => (!focused || isOn(c.lang, c.cat) ? 1 : 0.22))
        .on('pointermove', (ev, c) => {
          const items = c.items ? c.items.split('; ') : [];
          const lines = [`${LANG[c.lang]} · ${catLabel.get(c.cat)}`, `${c.now} listed now` + (c.ever > c.now ? `, ${c.ever - c.now} more removed over the years` : '')];
          if (items.length) lines.push(items.slice(0, 8).join(', ') + (items.length > 8 ? ` and ${items.length - 8} more` : ''));
          m.show(ev, lines);
        })
        .on('pointerleave', m.hide);
      gc.append('rect').attr('x', (c) => L + c.j * cw + 1).attr('y', (c) => T + c.i * ch + 1).attr('width', cw - 2).attr('height', ch - 2).attr('rx', 2)
        .style('fill', (c) => (c.now ? `color-mix(in srgb, var(--wk-9) ${Math.round(op(c.now) * 100)}%, var(--color-panel))` : c.ever ? 'var(--color-panel)' : 'var(--cds-chart-grid, #ecebe7)'))
        .style('stroke', (c) => (!c.now && c.ever ? 'var(--wk-8)' : 'none')).style('stroke-dasharray', '2 2');
      gc.append('text').attr('x', (c) => L + c.j * cw + cw / 2).attr('y', (c) => T + c.i * ch + ch / 2 + 4).attr('text-anchor', 'middle')
        .style('font-size', cw < 20 ? '9px' : '10.5px').style('font-variant-numeric', 'tabular-nums')
        .style('fill', (c) => (op(c.now) > 0.55 ? '#fff' : 'var(--color-fg)'))
        .text((c) => (c.now ? String(c.now) : ''));
    },
  });

  // ---------- Act III: absences ----------
  dash.draw('absent', {
    mount(el) { const box = document.createElement('div'); box.className = 'ab-list'; el.append(box); return { box }; },
    update(el, m) {
      const d = dash.data('absences');
      if (d.status !== 'ok') { m.box.textContent = '—'; return; }
      m.box.replaceChildren(...d.data.map((r) => {
        const row = document.createElement('div'); row.className = 'ab-row'; row.setAttribute('role', 'listitem');
        const a = document.createElement('span'); a.className = 'ab-lang'; a.textContent = r.language_label;
        const b = document.createElement('span'); b.className = 'ab-miss'; b.textContent = r.missing;
        const n = document.createElement('span'); n.className = 'ab-note'; n.textContent = r.note; b.append(n);
        row.append(a, b); return row;
      }));
    },
  });
})();
