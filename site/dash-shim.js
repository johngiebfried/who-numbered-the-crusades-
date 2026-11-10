// Local stand-in for the dashboard runtime (development and the repo's standalone pages).
(function(){
  const store = window.__DASH_DATA__ || {};
  const calcs = {}, draws = [], listeners = [];
  let params = {};
  function parseCSV(t){ const rows=d3.csvParse(t); rows.forEach(r=>{for(const k in r) if(r[k]==='') r[k]=null;}); return rows; }
  const cache = {};
  function data(id){
    if (calcs[id]) { const c=calcs[id]; const ins=c.inputs.map(i=>data(i).data); return {status:'ok', data:c.fn(...ins)}; }
    if (!(id in store)) return {status:'missing', data:[]};
    if (!cache[id]) { const r=parseCSV(store[id]); cache[id]={status:'ok', data:r}; cache[id].data.columns=r.columns; }
    return cache[id];
  }
  function runAll(){ listeners.forEach(f=>f()); draws.forEach(d=>document.querySelectorAll('[data-draw="'+d.name+'"]').forEach(el=>{
      if (el.closest('[hidden]')) return;
      if (typeof d.fn==='function') d.fn(el); else { if(!el.__m){el.replaceChildren(); el.__m=d.fn.mount?d.fn.mount(el):{};} d.fn.update&&d.fn.update(el,el.__m);} })); }
  window.dash = {
    data, colors:['var(--c1)','var(--c2)','var(--c3)','var(--c4)','var(--c5)'],
    onData(fn){ listeners.push(fn); },
    calc(id,o){ calcs[id]=o; }, loader(){},
    draw(name,fn){ if(fn===undefined){ const d=draws.find(x=>x.name===name); d&&document.querySelectorAll('[data-draw="'+name+'"]').forEach(el=>{ if(el.closest('[hidden]'))return; if(typeof d.fn==='function'){d.fn(el);return;} if(!el.__m){el.replaceChildren(); el.__m=d.fn.mount?d.fn.mount(el):{};} d.fn.update(el,el.__m);}); return; } draws.push({name,fn}); },
    params(){ return {...params}; }, setParams(p){ params={...params,...p}; for(const k in params) if(params[k]==null) delete params[k]; runAll(); }, resetParams(){ params={}; runAll(); },
    setLink(){}, refresh(){}
  };
  let t; window.addEventListener('resize',()=>{clearTimeout(t);t=setTimeout(runAll,100);});
  document.addEventListener('DOMContentLoaded',()=>setTimeout(runAll,0));
})();
