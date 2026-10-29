#!/usr/bin/env python3
"""Check Mastery session titles against the house rules.

Usage:
    python check_titles.py titles.json [--allow "word,word"]

titles.json is a list of {"title": ..., "type": ..., "teachers": [...]} ("id", "old_title" and other keys are
ignored). Types: Lesson, Workshop (or Lab), Bonus, Graduation, Kick Off, Q&A Call, Community.
--allow takes words from the jargon list that this programme has already taught its students.

Exit code 1 if any FAIL. WARN lines are judgement calls: fix them, or keep them on purpose.
"""
import json, re, sys

MAX, SOFT = 72, 58
SMALL = {'a', 'an', 'the', 'and', 'or', 'but', 'for', 'nor', 'to', 'of', 'in', 'on', 'at', 'by', 'as', 'vs', 'from', 'into', 'with', 'per'}
# words a student has not learned when they read the title; a named concept may lead a lesson title only with a promise after it
JARGON = ['offer book', 'answer hub', 'owner page', 'owner pages', 'monday brief', 'ai team', 'head of', 'chief of staff',
          'skill pack', 'the pack', 'clinic', 'agentic', 'context engineering', 'mcp', 'api']
CONCEPTS = ['company brain', 'brand kit', 'voice file', 'lead magnet', 'funnel']
GENERIC = [r'^community (session|call)', r'^q&a\b', r'^introduction to\b', r'^intro to\b', r'^overview\b', r'^session \d', r'^week \d', r'^module \d']
HYPE = ['revolutionary', 'game-changing', 'game changer', 'ultimate', 'insane', 'explosive', 'guaranteed', 'skyrocket', 'secret sauce', 'hack']
LAB_VERBS = {'build', 'launch', 'set', 'create', 'make', 'write', 'publish', 'put', 'score', 'send', 'switch', 'turn', 'run',
             'automate', 'design', 'map', 'rewrite', 'give', 'assign', 'test', 'plan', 'connect', 'record', 'find', 'fix', 'ship', 'draft'}
PAYMENT_WORDS = r'\b' + 'pack' + r'ages?\b|\b' + 'fe' + r'es?\b|\bper ' + 'cla' + r'ss\b|\bprice of\b|\$\d'
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')


def norm_type(t):
    t = (t or 'Lesson').strip()
    return 'Workshop' if t.lower() in ('lab', 'workshop') else t


def title_case_issues(title):
    words = re.findall(r"[\w][\w'’-]*", title)
    out = []
    for i, w in enumerate(words):
        if i and w.lower() in SMALL:
            continue
        if w[0].islower() and not re.search(r'\d', w):
            out.append(w)
    return out


def check(item, allow, seen):
    fails, warns = [], []
    title = item.get('title', '').strip()
    low = title.lower()
    t = norm_type(item.get('type'))
    if not title:
        return ['empty title'], []
    if low in seen:
        fails.append('duplicate of another title in this programme')
    seen.add(low)
    n = len(title)
    if n > MAX: fails.append(f'{n} characters (limit {MAX}); too long to scan in a calendar')
    elif n > SOFT: warns.append(f'{n} characters; under {SOFT} reads in one glance')
    if any(c in title for c in '—–'): fails.append('dash; use a colon between topic and promise')
    if ' - ' in title: fails.append('hyphen used as a dash; use a colon')
    if '!' in title: fails.append('exclamation mark')
    if EMOJI.search(title): fails.append('emoji')
    if re.search(r'\b[A-Z]{4,}\b', title) and not re.search(r'\b(ChatGPT|LinkedIn|YouTube|TikTok)\b', title):
        fails.append('capitals for emphasis')
    m = re.search(PAYMENT_WORDS, title, re.I)
    if m: fails.append(f'money wording: "{m.group()}"')
    for name in item.get('teachers') or []:
        for part in [name] + name.split()[:1]:
            if len(part) > 2 and re.search(r'\b' + re.escape(part) + r'\b', title):
                fails.append(f'teacher name "{part}" in the title; the platform shows the teacher, and teachers change')
                break
    if re.search(r'\bpart\s*#?\d|\(\s*part', low): warns.append('"Part N" titles fade; give each part its own promise')
    for pat in GENERIC:
        if re.search(pat, low): fails.append('generic label; name what the student gets')
    for w in HYPE:
        if re.search(r'\b' + re.escape(w) + r'\b', low): warns.append(f'hype word "{w}"; make the promise concrete instead')
    for j in JARGON:
        if j in allow: continue
        if re.search(r'\b' + re.escape(j) + r'\b', low): fails.append(f'jargon a student has not learned yet: "{j}"')
    if re.search(r'\bAI\b', title) and not re.search(r'AI-Ready', title) and 'ai' not in allow:
        warns.append('"AI" in the title; past Masteries pulled less with it. Name the business outcome unless AI itself is the topic')
    if re.search(r'\bwith AI\b', title): fails.append('"... with AI" is the weakest pattern in the benchmark; lead with the outcome')
    bad_case = title_case_issues(title)
    if bad_case: warns.append('not in title case: ' + ', '.join(bad_case[:4]))

    topic, _, promise = title.partition(':')
    if t == 'Lesson':
        if not promise:
            fails.append('lesson needs "Topic: Promise", a plain topic the student recognises, then the outcome')
        else:
            if len(topic.split()) > 4: warns.append(f'topic "{topic}" is {len(topic.split())} words; keep it to one to four')
            if len(promise.split()) < 3: warns.append('promise is under three words; say what changes for them')
    elif t == 'Workshop':
        first = title.split()[0].lower()
        if re.match(r'^(lab|workshop)\b', low):
            warns.append('type label in the title; leave it out where the platform already shows the session type')
            first = (title.split(':', 1)[1].split() or [''])[0].lower() if ':' in title else first
        if first not in LAB_VERBS:
            warns.append(f'lab starts with "{first}"; open with what they build ("Build", "Launch", "Set Up", "Write")')
        if not re.search(r'\byour\b', low): warns.append('lab title does not say "your"; name the thing they leave with')
    elif t == 'Graduation' and 'graduation' not in low:
        fails.append('graduation title should say Graduation')
    for c in CONCEPTS:
        if c in allow: continue
        if c in promise.lower() and t == 'Lesson' and c not in topic.lower():
            warns.append(f'"{c}" in the promise; a named concept belongs in the topic, explained by the promise')
    return fails, warns


def main():
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    allow = set()
    if '--allow' in args:
        allow = {w.strip().lower() for w in args[args.index('--allow') + 1].split(',') if w.strip()}
    items = json.load(open(args[0], encoding='utf-8'))
    seen, nf = set(), 0
    for i, it in enumerate(items, 1):
        f, w = check(it, allow, seen)
        label = it.get('title') or it.get('id') or f'#{i}'
        for x in f: print(f'FAIL {label}: {x}'); nf += 1
        for x in w: print(f'WARN {label}: {x}')
    firsts = [it.get('title', '').split(':')[0].split()[0].lower() for it in items if it.get('title')]
    for a, b, it in zip(firsts, firsts[1:], items[1:]):
        if a == b: print(f'WARN {it.get("title")}: starts with the same word as the title before it; vary the run')
    print(f'{len(items)} titles checked, {nf} failures')
    sys.exit(1 if nf else 0)


if __name__ == '__main__':
    main()
