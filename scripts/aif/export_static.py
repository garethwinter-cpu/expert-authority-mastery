#!/usr/bin/env python3
"""Export the AI for Founders pages as a self-contained static site (for garethwinter-cpu/ai-founder-mastery).

The source of truth stays here: scripts/aif/ -> build_aif.py -> data/ai-founders-curriculum.json, served by server.js.
This writes index.html (front door) and pack.html with the curriculum JSON inlined, the JSON itself,
and the author headshots the data references, so the pages work from any static host or straight from disk.
curriculum.html is not exported: the static repo builds its own student-facing page from the Airtable snapshot
(scripts/build_curriculum.py there), so an export never overwrites it.
Usage: python3 scripts/aif/export_static.py /path/to/ai-founder-mastery"""
import json, pathlib, re, shutil, sys
R = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(sys.argv[1]).resolve()
LIVE = 'https://expert-authority-mastery-1f30-jdtcvngavq-as.a.run.app'
PAGES = {'ai-founders-home.html': 'index.html', 'ai-founders-pack.html': 'pack.html'}
LINKS = {'/ai-founders/curriculum': 'curriculum.html', '/ai-founders/pack': 'pack.html', '/ai-founders/outline': 'curriculum.html',
         '/ai-founders/proposal': LIVE + '/ai-founders/proposal', '/ai-founders': 'index.html', '/api/ai-founders': 'data/ai-founders-curriculum.json',
         '/positioning': LIVE + '/positioning', '/expert-authority': LIVE + '/expert-authority', '/': LIVE + '/'}
D = json.loads((R / 'data' / 'ai-founders-curriculum.json').read_text(encoding='utf-8'))
if D.get('source', {}).get('url', '').startswith('/'): D['source']['url'] = LINKS.get(D['source']['url'], LIVE + D['source']['url'])
data = json.dumps(D, indent=1, ensure_ascii=False)
ASSETS = set()
def link(path, frag=''):
    if path in LINKS: return LINKS[path] + frag
    f = R / path.lstrip('/')
    if path != '/' and f.is_file(): ASSETS.add(path.lstrip('/')); return path.lstrip('/') + frag   # ship the asset with the site
    return LIVE + path + frag
for src, dst in PAGES.items():
    h = (R / src).read_text(encoding='utf-8')
    h = h.replace('__CURRICULUM_JSON__', data.replace('</', '<\\/'))
    h = re.sub(r'(href|src)="(/[^"#]*)(#[^"]*)?"', lambda m: '%s="%s"' % (m.group(1), link(m.group(2), m.group(3) or '')), h)
    h = h.replace('href="' + LIVE + '/ai-founders/curriculum"', 'href="curriculum.html"')
    h = h.replace("'<img src=\"/'+esc(p.image)", "'<img src=\"'+esc(p.image)")
    left = re.findall(r'(?:src|href)="/[^"]*"', h)
    if left: sys.exit(f'{dst}: root-relative references left: {left[:5]}')
    (OUT / dst).write_text(h, encoding='utf-8')
(OUT / 'data').mkdir(exist_ok=True)
(OUT / 'data' / 'ai-founders-curriculum.json').write_text(data, encoding='utf-8')
for a in sorted(ASSETS):
    (OUT / a).parent.mkdir(parents=True, exist_ok=True); shutil.copy(R / a, OUT / a)
    if a.endswith('.css'):
        for u in re.findall(r'url\((["\']?)(/[^)"\']+)\1\)', (R / a).read_text(encoding='utf-8')): print('note: css references', u[1])
imgs = {s['image'] for x in D['sessions'] for s in x['speakers'] if s.get('image')}
(OUT / 'authors').mkdir(exist_ok=True)
for i in sorted(imgs): shutil.copy(R / i, OUT / i)
print('exported', ', '.join(PAGES.values()), '+ data + %d headshots + assets %s to' % (len(imgs), sorted(ASSETS)), OUT)
