# Builds data/ledger/ledger.csv: print rows (scripts/ledger_code_corpus.py) plus Wikipedia navigation-box runs.
# Run from the repository root: python3 scripts/ledger_code_corpus.py && python3 scripts/build_ledger.py
import csv,re,json
WP='data/wikipedia/'
EXP=["H6","C","D","F","B","L1","L2","E"]
LN={'en':'English','de':'German','fr':'French','it':'Italian','es':'Spanish','nl':'Dutch','el':'Greek','ar':'Arabic','fa':'Persian','he':'Hebrew','pt':'Portuguese','pl':'Polish','tr':'Turkish','ru':'Russian','cs':'Czech','sv':'Swedish','hu':'Hungarian'}
def from_short(sh,unl):
    c={}
    for m in re.finditer(r'\b(H6|C|D|F|B|L1|L2|E)\s+(\d+)(?:\s*\((\d+)\))?',sh):
        c[m.group(1)]=m.group(2)+(f" ({m.group(3)})" if m.group(3) else "")
    for u in unl.split():
        if u in EXP and u not in c: c[u]='n'
    return c
def from_linked(lk):
    c={}
    for t in lk.split():
        k,_,n=t.partition(':')
        if k in EXP: c[k]=n if n else 'n'
    return c
rows=[]
NOTES={('pl',2007):'Frederick II absent: no article, no link. 2014 sample (only Alexandria linked) skipped as anomalous.',
 ('de',2005):'Modern count in brackets: "Fünfter (Sechster) Kreuzzug".',
 ('en',2020):'Ninth dropped 17 November 2019; Edward linked as "Lord Edward\'s crusade".',
 ('ar',2005):'Eighth until 4 December 2013, the last box to reach nine.'}
def runs(lang,page,samples,label):
    # samples: list of (year, cells)
    cur=None
    for y,cells in samples:
        key=tuple(cells.get(e,'') for e in EXP)
        if not any(key): cur=None; continue
        if cur and cur['key']==key and cur['end']>=y-2: cur['end']=y; continue
        cur={'key':key,'start':y,'end':y,'lang':lang,'page':label}; rows.append(cur)
yc=[x for x in csv.DictReader(open(WP+'yearly_counts.csv')) if x['page']=='navbox' and x['sample_date'].endswith('07-01')]
for lang in ['en','de','fr','it','es','nl','el','ar','fa','he']:
    s=sorted((int(x['sample_date'][:4]),from_short(x['numbering_shorthand'],x['unnumbered_linked'])) for x in yc if x['language']==lang)
    runs(lang,'navbox',s,'navigation box')
nb=list(csv.DictReader(open(WP+'navbox_new_languages.csv')))
for lang in ['pt','pl','tr','ru','cs']:
    s=sorted((int(x['sample_year']),from_linked(x['linked_codes'])) for x in nb if x['language']==lang and not (lang=='pl' and x['sample_year']=='2014'))
    runs(lang,'navbox',s,'navigation box')
out=[]
for r in rows:
    nine=r['key'][EXP.index('E')] not in ('','n')
    yl=f"{r['start']}–{r['end']}" if r['end']>r['start'] else str(r['start'])
    if r['end']>=2026: yl=f"{r['start']}–"
    out.append(dict(source=f"Wikipedia ({LN[r['lang']]}), {r['page']}",year_label=yl,year_sort=r['start'],year_end=r['end'],
        language=r['lang'],tradition='WP',kind='wikipedia',genre='Wikipedia',stated_count='',note=NOTES.get((r['lang'],r['start']),''),**dict(zip(EXP,r['key']))))
pr=[dict(x,year_end=x['year_sort']) for x in csv.DictReader(open('data/ledger/ledger_print.csv'))]
allr=pr+out
allr.sort(key=lambda x:(int(x['year_sort']),x['source']))
TL={'EARLY':'Early modern','EN':'English (Britain and US)','FR':'French','DE':'German','IT':'Italian','ES':'Spanish','EL':'Greek','NL':'Dutch','LIB':'Library catalogs','WP':'Wikipedia'}
seen=set()
for r in allr:
    base=re.sub(r'[^a-z0-9]+','-',(r['source']+' '+r['year_label']).lower()).strip('-')[:60]
    i=base;k=2
    while i in seen: i=f"{base}-{k}";k+=1
    seen.add(i); r['id']=i; r['tradition_label']=TL[r['tradition']]
cols=["id","source","year_label","year_sort","year_end","language","tradition","tradition_label","kind","genre","stated_count"]+EXP+["note"]
with open('data/ledger/ledger.csv','w',newline='') as f:
    w=csv.DictWriter(f,cols); w.writeheader(); [w.writerow({k:x[k] for k in cols}) for x in allr]
print(len(pr),len(out))

