#!/usr/bin/env python3
"""Check customer-facing lesson descriptions against the Mastery house style.

Usage:
    python check_descriptions.py descriptions.json

descriptions.json is a list of {"title": ..., "type": ..., "description": ...}
("id" and other keys are ignored). Types: Lesson, Workshop (or Lab), Bonus,
Graduation, Kick Off, Q&A Call, Community.

Exit code 1 if any FAIL. WARN lines are judgement calls.
"""
import json, re, sys

HEAD = {'Lesson': "You'll learn:"}
DEFAULT_HEAD = "You'll leave with:"
INTERNAL = [r'\bHead of\b', r'\bthe guide\b', r'\bthe line with\b', r'\binternal\b', r'\bTBD\b', r'\bTBC\b',
            r'\[', r'\bteam call\b', r'\bdeck\b', r'\bAirtable\b', r'\bslot\b', r'\bcohort report\b']
# payment words, assembled so this file does not itself contain them
PAYMENT_WORDS = r'\b' + 'pack' + r'ages?\b|\b' + 'fe' + r'es?\b|\bper ' + 'cla' + r'ss\b'
DASH = '—–'
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')


def words(s): return len(re.findall(r"[\w'’]+", s))


def check(item):
    fails, warns = [], []
    t = item.get('type', 'Lesson')
    t = 'Workshop' if t.lower() in ('lab', 'workshop') else t
    text = item.get('description', '').replace('\r', '')
    head = HEAD.get(t, DEFAULT_HEAD)
    if head not in text:
        fails.append(f'missing the "{head}" line')
        return fails, warns
    intro, rest = text.split(head, 1)
    intro = intro.strip()
    bullets = [l.strip() for l in rest.strip().splitlines() if l.strip()]
    if '\n\n' in intro: warns.append('intro is more than one paragraph')
    n = words(intro)
    lo, hi = (40, 110) if t in ('Lesson', 'Workshop') else (25, 110)
    if not lo <= n <= hi: fails.append(f'intro is {n} words (aim {lo} to {hi})')
    if not all(b.startswith('- ') for b in bullets): fails.append('every line after the heading must be a "- " bullet')
    if not 2 <= len(bullets) <= 6: fails.append(f'{len(bullets)} bullets (aim 2 to 6)')
    for b in bullets:
        if b.endswith('.'): warns.append(f'bullet ends with a full stop: "{b[:40]}"')
        if words(b) > 16: warns.append(f'long bullet ({words(b)} words): "{b[:40]}"')
    if not re.search(r"\byou(r|'ll|'re|'ve)?\b", intro, re.I): fails.append('intro never speaks to the student as "you"')
    if t == 'Workshop' and 'lesson' not in intro.split('.')[0].lower():
        warns.append('workshop does not open from the lesson ("The lesson gave you..." / "Vishen\'s lesson showed you...")')
    for pat in INTERNAL:
        m = re.search(pat, text)
        if m: fails.append(f'internal wording: "{m.group()}"')
    m = re.search(PAYMENT_WORDS, text, re.I)
    if m: fails.append(f'money wording: "{m.group()}"')
    if any(c in text for c in DASH): fails.append('dash used; use a comma, colon or full stop')
    if EMOJI.search(text): fails.append('emoji')
    if re.search(r'\bweek \d+ (lab|lesson)\b.*\bweek \d+\b.*\bweek \d+\b', text, re.I): warns.append('many week references; students read one lesson at a time')
    return fails, warns


def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    items = json.load(open(sys.argv[1], encoding='utf-8'))
    nf = 0
    for i, it in enumerate(items, 1):
        f, w = check(it)
        label = it.get('title') or it.get('id') or f'#{i}'
        for x in f: print(f'FAIL {label}: {x}'); nf += 1
        for x in w: print(f'WARN {label}: {x}')
    print(f'{len(items)} descriptions checked, {nf} failures')
    sys.exit(1 if nf else 0)


if __name__ == '__main__':
    main()
