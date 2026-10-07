#!/usr/bin/env python3
"""Fee guard. Run before every push: no author compensation on any served page or data file.
Exit 1 on a hit. Add a phrase to ALLOW only when it is curriculum copy, never a real fee."""
import re, sys, pathlib
R = pathlib.Path(__file__).resolve().parents[1]
FILES = ['expert-authority.html', 'data/curriculum.json', 'index.html', 'ai-founders-proposal.html',
         'data/ai-founders-curriculum.json', 'ai-founders.html', 'ai-founders-home.html', 'ai-founders-outline.html', 'briefs/AIF-CURRICULUM-OUTLINE.md', 'ai-founders-pack.html', 'briefs/AIF-SURVEY.md', 'scripts/aif/aif_survey.json', 'scripts/aif/aif_emails.json', 'expert-authority-guild.html',
         'ai-founders-guild.html', 'positioning.html', 'live.html', 'CURRICULUM-BRIEF.md',
         'data/learnings.json', 'ONBOARDING-SURVEY.md', 'STATUS.md']
WORDS = re.compile(r'compensation:|% of programme revenue|fee table|fee allocation|fee.alignment|\bfees?\b|'
                   r'per.class|/class|hospitality|royalt|speaker.budget|\bpackages?\b|headroom|guest spend', re.I)
ALLOW = ['roughly one skill per class', 'from vague idea to compelling package',
         'command premium fees and create life-changing results',
         'Speaking fees: when to charge, when to speak for free', '$100K → $3K',
         'generates millions in royalties from Udemy', 'generating millions in royalty income',
         'privacy, royalties and subscription', 'Packaged and One Committed',
         'no fees or compensation', 'check-no-fees', 'package.json']
bad = 0
for f in FILES:
    p = R / f
    if not p.exists():
        continue
    t = p.read_text()
    if '<!-- ACCEL-START -->' in t:
        t = t[:t.index('<!-- ACCEL-START -->')] + t[t.index('<!-- ACCEL-END -->'):]
    for a in ALLOW:
        t = t.replace(a, '')
    for m in WORDS.finditer(t):
        bad += 1
        s = max(0, m.start() - 70)
        print(f'  HIT {f}: …{t[s:m.end() + 70]!r}…')
print('FEE GUARD', 'OK 0 matches' if not bad else f'FAIL {bad} matches')
sys.exit(1 if bad else 0)
