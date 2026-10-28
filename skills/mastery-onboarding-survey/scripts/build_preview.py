#!/usr/bin/env python3
"""Check a survey file against the skill's rules, time it, and render the student preview.

Usage:
    python build_preview.py survey.json [--out preview.html] [--check-only]

survey.json follows examples/aif-survey.json: programme, eyebrow, title, intro,
promise_minutes, badges, thanks {title, steps[{when, what}], note}, and sections
[{title, sub, qs[{id, type, q, req, opts, sub, max, ph, lo, hi, follow, why}]}].
Question types: text, email, tel, long, select, one, many, scale.

Exit code 1 if any FAIL. WARN lines are judgement calls to raise with the user.
"""
import json, re, sys, pathlib

# Seconds a student spends on each type, reading included. Pre-filled name and
# email cost nothing. Ticking a list takes longer than one tap, because people
# read every option before choosing.
SECONDS = {'one': 6, 'scale': 6, 'select': 8, 'many': 12, 'text': 25, 'email': 25, 'tel': 10, 'long': 45}
PREFILLED = {'name', 'email'}
CORE = ['name', 'email', 'phone', 'gender', 'age', 'country', 'income', 'history']
AGE = ['18–24', '25–34', '35–44', '45–54', '55–64', '65+']
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')
SHOUT = re.compile(r'\b[A-Z]{4,}\b')


def lint(s):
    fails, warns = [], []
    secs = s.get('sections', [])
    qs = [q for sec in secs for q in sec['qs']]
    ids = [q['id'] for q in qs]
    byid = {q['id']: q for q in qs}

    for k in ('programme', 'intro', 'promise_minutes', 'thanks'):
        if not s.get(k):
            fails.append(f'missing top-level "{k}"')
    if s.get('thanks') and not s['thanks'].get('steps'):
        warns.append('thank-you screen has no next steps; tell students what happens next and when')

    missing = [c for c in CORE if c not in ids]
    if missing:
        fails.append(f'core block missing: {", ".join(missing)}')
    if ids[:len(CORE)] != CORE and not missing:
        warns.append('core block is not first or not in DNA order')
    for c in ('phone', 'income'):
        if byid.get(c, {}).get('req'):
            fails.append(f'{c} must be optional (DNA)')
    if 'history' in byid and (byid['history']['type'] != 'many' or not byid['history'].get('req')):
        fails.append('programme history must be multi-select and required')
    if 'age' in byid and byid['age'].get('opts') != AGE:
        fails.append(f'age bands must be {" · ".join(AGE)}')

    for sec in secs:
        if re.match(r'(group|new group|section)\s*\d*$', sec['title'].strip(), re.I):
            fails.append(f'section title "{sec["title"]}" is an Airtable default')

    for q in qs:
        text = ' '.join([q['q'], q.get('sub', '')] + q.get('opts', []))
        if EMOJI.search(text):
            fails.append(f'{q["id"]}: emoji in question or options')
        if SHOUT.search(q['q']):
            warns.append(f'{q["id"]}: capitals for emphasis ("{SHOUT.search(q["q"]).group()}"); write it plainly')
        if q['id'] not in CORE and not q.get('why'):
            fails.append(f'{q["id"]}: no "why". Name who acts on the answer and when, or cut the question')
        if q['type'] in ('one', 'many') and any(o.lower() in ('other', 'something else') for o in q.get('opts', [])) and not q.get('follow'):
            fails.append(f'{q["id"]}: "Other" with no "please specify" follow-up')
        if q['type'] == 'many' and len(q.get('opts', [])) > 8 and not q.get('max') and q['id'] not in ('have', 'history', 'tools'):
            warns.append(f'{q["id"]}: {len(q["opts"])} options with no pick limit; "pick up to three" gives teachers a sharper signal')
        if len(q.get('opts', [])) > 12:
            warns.append(f'{q["id"]}: {len(q["opts"])} options is a wall; split or shorten')
        if re.search(r'desired income|want to earn', q['q'], re.I) and 'manifest' not in s.get('programme', '').lower():
            fails.append(f'{q["id"]}: desired income belongs to Manifesting only')

    opens = [q['id'] for q in qs if q['type'] == 'long' and q.get('req')]
    if len(opens) > 1:
        warns.append(f'{len(opens)} required long answers ({", ".join(opens)}); keep one')
    scales = [q for q in qs if q['type'] == 'scale']
    if not scales:
        warns.append('no 1 to 10 baseline; without one, graduation has no before-and-after number')

    req = sum(SECONDS[q['type']] for q in qs if q.get('req') and q['id'] not in PREFILLED)
    opt = sum(SECONDS[q['type']] for q in qs if not q.get('req') and q['id'] not in PREFILLED)
    promise = s.get('promise_minutes') or 0
    if promise and req > promise * 60 + 15:
        fails.append(f'required questions take about {req/60:.1f} min against a promise of {promise}; cut or change the promise')
    if len(qs) > 30:
        warns.append(f'{len(qs)} questions; above 30 completion drops')
    return fails, warns, len(qs), req, opt


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    src = pathlib.Path(args[0])
    s = json.loads(src.read_text())
    fails, warns, n, req, opt = lint(s)
    print(f'{s.get("programme")}: {n} questions. Required answers about {req/60:.1f} min, '
          f'with every optional one about {(req+opt)/60:.1f} min. Promise: {s.get("promise_minutes")} min.')
    for f in fails:
        print('FAIL', f)
    for w in warns:
        print('WARN', w)
    if '--check-only' not in args:
        out = pathlib.Path(args[args.index('--out') + 1]) if '--out' in args else src.with_suffix('.html')
        tpl = (pathlib.Path(__file__).parent.parent / 'assets' / 'preview-template.html').read_text()
        page = (tpl.replace('__PAGE_TITLE__', f'{s["programme"].replace(" Mastery", "")} Onboarding Survey')
                   .replace('__SURVEY_JSON__', json.dumps(s, ensure_ascii=False).replace('</', '<\\/')))
        out.write_text(page)
        print('preview:', out)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
