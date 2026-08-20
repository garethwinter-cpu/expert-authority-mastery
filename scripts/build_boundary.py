#!/usr/bin/env python3
"""Render the E&A / AI-for-Founders boundary from data/boundary.json.

One source, three outputs:
  - injected into expert-authority.html   (perspective: ea)
  - injected into ai-founders.html        (perspective: aif)
  - positioning.html generated whole      (perspective: neutral)

Injection targets the markers <!-- boundary:auto --> ... <!-- /boundary:auto -->.
Anything hand-edited between them is overwritten. Edit data/boundary.json instead.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = json.load(open(os.path.join(ROOT, 'data', 'boundary.json'), encoding='utf-8'))

START, END = '<!-- boundary:auto -->', '<!-- /boundary:auto -->'

def card(key, own):
    p = B['programmes'][key]
    tint = ' tint' if own else ''
    tag = ' · this proposal' if own else ''
    return f'''      <div class="card{tint}">
        <div class="kicker">{p['name']}{tag}</div>
        <h3>{p['pain']}</h3>
        <p class="body-md" style="margin-top:10px">{p['diagnosis']}</p>
        <div class="covers"><strong>Outcome:</strong> {p['outcome']}. Proof: <em>{p['proof']}.</em><br><strong>Graduating artefact:</strong> {p['artefact']}<br><strong>Led by:</strong> {p['led_by']}</div>
      </div>'''

def render(perspective):
    own = perspective if perspective in ('ea', 'aif') else None
    order = ['ea', 'aif'] if perspective != 'aif' else ['aif', 'ea']
    cards = '\n'.join(card(k, k == own) for k in order)
    rows = '\n'.join(
        f'        <tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td></tr>'
        for r in B['comparison'])
    return f'''{START}
  <!-- GENERATED from data/boundary.json by scripts/build_boundary.py — do not hand-edit. -->
  <section>
    <div class="section-head">
      <div class="overline">The boundary that matters most</div>
      <h2>{B['headline_ea_first']}</h2>
      <p class="body-lg">{B['intro']}</p>
      <p class="small" style="margin-top:8px">{B['generated_note']}</p>
    </div>
    <div class="grid g2" style="margin-bottom:18px">
{cards}
    </div>
    <div class="callout dark" style="margin-bottom:18px">
      <div class="ic">▸</div>
      <div>
        <p><strong>The one-question router.</strong> {B['router']['question']}</p>
        <p>{B['router']['answer']}</p>
      </div>
    </div>
    <div class="tbl-scroll" style="margin-bottom:18px">
    <table class="tbl">
      <thead><tr><th>&nbsp;</th><th>Expert &amp; Authority Mastery</th><th>AI for Founders Mastery</th></tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
    </div>
    <div class="grid g2">
      <div class="card" style="border-left:4px solid var(--orange)">
        <div class="kicker" style="color:var(--orange-content)">The three overlap rules</div>
        <p class="body-md">{B['overlap_rules']}</p>
      </div>
      <div class="card" style="border-left:4px solid var(--green)">
        <div class="kicker" style="color:var(--green)">Why the boundary is a retention mechanism</div>
        <p class="body-md">{B['retention']}</p>
      </div>
    </div>
  </section>
  {END}'''

def inject(path, perspective):
    s = open(path, encoding='utf-8').read()
    a, b = s.find(START), s.find(END)
    assert a >= 0 and b > a, f'{path}: boundary markers not found'
    out = s[:a] + render(perspective) + s[b + len(END):]
    open(path, 'w', encoding='utf-8').write(out)
    print(f'injected {perspective:3} -> {os.path.basename(path)}')

def standalone():
    tpl = open(os.path.join(ROOT, 'shared', 'positioning.template.html'), encoding='utf-8').read()
    assert '{{BOUNDARY}}' in tpl
    out = tpl.replace('{{BOUNDARY}}', render('neutral'))
    open(os.path.join(ROOT, 'positioning.html'), 'w', encoding='utf-8').write(out)
    print('generated    -> positioning.html')

if __name__ == '__main__':
    inject(os.path.join(ROOT, 'expert-authority.html'), 'ea')
    inject(os.path.join(ROOT, 'ai-founders.html'), 'aif')
    standalone()
    print('ok')
