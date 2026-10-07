#!/usr/bin/env python3
"""Build data/ai-founders-curriculum.json: the AI for Founders draft curriculum, held in this repo until Vishen aligns.
Same schema as the E&A curriculum.json so it can be seeded into Airtable unchanged.

Source of the copy: scripts/aif/aif_modules.json (eight modules, two weeks each, lesson + lab every week), built on
Vykintas's curriculum proposal and Jaideep's launch brief of 5 Oct 2026. Calendar: programme starts Mon 16 Nov 2026
(the brief's date) with Vishen's opening; lessons Tuesday, labs Thursday, 9am Pacific; no sessions 22 and 29 Dec."""
import json, datetime as dt, pathlib, re
from zoneinfo import ZoneInfo
HERE=pathlib.Path(__file__).resolve().parent; R=HERE.parents[1]
SRC=json.load(open(HERE/'aif_modules.json'))
IMG={'Vishen':'vishen-lakhiani','Vykintas':'vykintas-glodenis'}
FULL={'Vishen':'Vishen Lakhiani','Vykintas':'Vykintas Glodenis'}
def spk(name):
    key=name.strip(); f=IMG.get(key) or re.sub(r'[^a-z]+','-',FULL.get(key,key).lower()).strip('-')
    return {'name':FULL.get(key,key),'image':('authors/'+f+'.jpg') if (R/'authors'/(f+'.jpg')).exists() else None}
def who(s): return [spk(x) for x in re.split(r'\s*\+\s*',s)]
PT=ZoneInfo('America/Los_Angeles')
def at(d,h=9,m=0): return dt.datetime(d.year,d.month,d.day,h,m,tzinfo=PT).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')

# week -> Tuesday. 16 weeks from Tue 17 Nov 2026, break 21 Dec to 3 Jan
starts={}; d=dt.date(2026,11,17); w=1
while w<=16:
    if d in (dt.date(2026,12,22),dt.date(2026,12,29)): d+=dt.timedelta(days=7); continue
    starts[w]=d; d+=dt.timedelta(days=7); w+=1
modules=[{'name':f"Module {m['n']}: {m['name']}",'short':m['short'],'order':m['n'],'problem':m['problem'],'installed':m['installed'],'changes':m['changes'],'weeks':m['weeks']} for m in SRC['modules']]
def mod(w): return next(x['name'] for x in modules if w in x['weeks'])

sessions=[]
def add(**k): sessions.append(k)
GAR=('Get AI-Ready: the shared floor before Week 1. Three layers, so no live lesson ever has to teach setup: optional pre-recorded base setup for '
     'founders starting from zero (signing up, which plan, starting a chat, adding files, voice, and a short guide for people coming from ChatGPT); '
     'required building blocks for everyone (prompt and context, skills, projects and instructions, connectors, scheduled tasks, cloud versus local), '
     'each with one thing set up in your own account; then the programme. The readiness checklist nudges, it does not gate: a paid plan, one project '
     'with instructions, one skill installed, one app connected. It also gives us the starting-level data the AI Mastery 2026 survey was missing.')
add(id='aif-ready-1',title='Get AI-Ready, call 1: your account, your first project, your first skill',type='Bonus',start=at(dt.date(2026,11,5)),duration_min=90,speakers=[spk('Vykintas')],module=None,
    description='Call 1, the first week after the summit, for early buyers: the building blocks walked live, questions answered, the checklist started. Recorded for late buyers.\n\n'+GAR)
add(id='aif-ready-2',title='Get AI-Ready, call 2: checklist, connectors and the questions from call 1',type='Bonus',start=at(dt.date(2026,11,12)),duration_min=90,speakers=[spk('Vykintas')],module=None,
    description='Call 2, the week before the start, for late buyers who watched the recording of call 1 and for anyone still stuck on setup. Nobody arrives at Week 1 wondering what a connector is.\n\n'+GAR)
add(id='aif-opening',title='Why Your Business Still Runs on You',type='Kick Off',start=at(dt.date(2026,11,16)),duration_min=90,speakers=[spk('Vishen'),spk('Vykintas')],module=None,
    description='The programme opens on Monday 16 November with Vishen. You built the business to be free; somewhere along the way it took the freedom. Vishen opens his own load map live: the years Mindvalley ran through him, and what AI runs there today. Then the ceiling every founder in the room shares: your business cannot grow faster than your calendar. Vykintas walks the sixteen weeks, the teacher on each, and the one measurement graduation is judged against: how many hours a week your business needs you today. You leave with the calendar in your hands and a number written down.')
for m in SRC['modules']:
    for c in m['calls']:
        w=c['week']; d=starts[w]
        if c['type'] in ('lesson','graduation'):
            add(id=f'aif-w{w:02d}-lesson',title=c['title'],type='Lesson' if c['type']=='lesson' else 'Graduation',start=at(d),duration_min=90,speakers=who(c['who']),module=mod(w),description=c['text'],week=w)
        else:
            text=c['text']+(('\n\n**The win:** '+c['win']) if c.get('win') else '')
            add(id=f'aif-w{w:02d}-lab',title=c['title'],type='Workshop',start=at(d+dt.timedelta(days=2)),duration_min=90,speakers=who(c['who']),module=mod(w),description=text,week=w,pair=f'aif-w{w:02d}-lesson')
sessions.sort(key=lambda s:s['start'])

# diary load. The E&A snapshot (data/curriculum.json, 23 Sep) is stale: it still skips Thanksgiving and lands lessons on
# Fridays from December. E&A's rule, confirmed against live Airtable on 5 Oct 2026: slot 1 is Tue 6 Oct, odd slots are Tuesday
# lessons, even slots the Friday workshop of the same week, 9am Pacific, no Thanksgiving break, no sessions on 22 and 29 Dec.
# Dates come from that rule; titles, types and speakers from the snapshot; EA_OVERLAY carries what the snapshot has not caught
# up with. Each overlay row applies only while the snapshot still shows the pre-change state, so a refreshed snapshot no-ops it.
ea=json.load(open(R/'data'/'curriculum.json'))
EA_START=dt.date(2026,10,6); EA_SKIP={dt.date(2026,12,22),dt.date(2026,12,29)}
def ea_slot_date(n):
    tue=EA_START; week=1
    while week<(n+1)//2:
        tue+=dt.timedelta(days=7)
        if tue in EA_SKIP: continue
        week+=1
    return tue if n%2 else tue+dt.timedelta(days=3)
EA_OVERLAY=[
 # in Airtable since the snapshot: Marisha Lakhiani runs the Paid Advertising and Funnel Design workshops
 {'slot':18,'if_speaker':'Vykintas Glodenis','speaker':'Marisha Lakhiani'},
 {'slot':20,'if_speaker':'Vykintas Glodenis','speaker':'Marisha Lakhiani'},
 # held decisions of 5 Oct (STATUS.md), not yet in Airtable: the John Lee three-way rotation ...
 {'slot':13,'if_speaker':'John Lee','to_slot':25},{'slot':14,'if_speaker':'John Lee','to_slot':26},
 {'slot':29,'if_speaker':'Vishen Lakhiani','to_slot':13},{'slot':30,'if_speaker':'Vykintas Glodenis','to_slot':14},
 {'slot':25,'if_speaker':'Vishen Lakhiani','to_slot':29},{'slot':26,'if_speaker':'Vykintas Glodenis','to_slot':30},
 # ... and Regan Hillyer teaching Membership, Continuity & Superfans in Vishen's place
 {'title':'Membership, Continuity & Superfans','type':'Lesson','if_speaker':'Vishen Lakhiani','speaker':'Regan Hillyer'},
]
def ea_sessions():
    out=[]
    for s in ea['sessions']:
        m=re.match(r'\s*(\d+)',str(s.get('slot') or '')); slot=int(m.group(1)) if m else None
        names=[p['name'] for p in s['speakers']]
        for o in EA_OVERLAY:
            if 'slot' in o and o['slot']!=slot: continue
            if 'title' in o and not s['title'].startswith(o['title']): continue
            if 'type' in o and o['type']!=s['type']: continue
            if o['if_speaker'] not in names: continue
            if 'speaker' in o: names=[o['speaker'] if n==o['if_speaker'] else n for n in names]
            if 'to_slot' in o: slot=o['to_slot']
        start=s['start']
        if slot: start=at(ea_slot_date(slot))              # slot 0 (the bonus) keeps its own date
        elif s.get('start'): start=s['start']               # a refreshed snapshot carries no slot; trust its dates
        if start: out.append({'start':start,'type':s['type'],'title':s['title'],'speakers':names})
    return out
EA=ea_sessions()
def load_for(name):
    rows=[('E&A',s['start'],s['type'],s['title']) for s in EA if name in s['speakers']]
    rows+=[('AIF',s['start'],s['type'],s['title']) for s in sessions if any(p['name']==name for p in s['speakers'])]
    weeks={}
    for prog,start,typ,title in rows:
        wk=dt.date.fromisoformat(start[:10]); wk=wk-dt.timedelta(days=wk.weekday()); weeks.setdefault(wk,[]).append(prog)
    heavy=sorted([ (k,v) for k,v in weeks.items() if len(v)>=3 ])
    both=sorted([k for k,v in weeks.items() if 'E&A' in v and 'AIF' in v])
    clashes=[{'start':a[1],'ea':a[3],'aif':b[3]} for a in rows if a[0]=='E&A' for b in rows if b[0]=='AIF' and a[1]==b[1]]
    return {'name':name,'ea':sum(1 for r in rows if r[0]=='E&A'),'aif':sum(1 for r in rows if r[0]=='AIF'),
            'weeks_on_both':len(both),'first_overlap':both[0].isoformat() if both else None,'last_overlap':both[-1].isoformat() if both else None,
            'peak_per_week':max(len(v) for v in weeks.values()),'weeks_3plus':len(heavy),'clashes':sorted(clashes,key=lambda c:c['start'])}
load=[load_for('Vishen Lakhiani'),load_for('Vykintas Glodenis')]
ea_dated=sorted(s['start'][:10] for s in EA if s['type']!='Bonus')
ea_range={'first':ea_dated[0],'last':ea_dated[-1]}
aif_first,aif_last=min(s['start'][:10] for s in sessions if s.get('week')),max(s['start'][:10] for s in sessions if s.get('week'))
vyk_fridays=sorted(s['start'][:10] for s in EA if 'Vykintas Glodenis' in s['speakers'] and dt.date.fromisoformat(s['start'][:10]).weekday()==4 and aif_first<=s['start'][:10]<=aif_last)
fmt=lambda iso: dt.date.fromisoformat(iso).strftime('%-d %b')
load_basis=('Computed against the Expert & Authority calendar as read from Airtable on 5 October 2026 (Tuesday lessons, Friday workshops, 9am Pacific, '
            'no Thanksgiving break, graduation Tuesday 23 February), with the two decisions held on 5 October applied on top because they are not yet in Airtable: '
            'the John Lee rotation (Platforms to 12 and 15 January, Speaking to 17 and 20 November, Membership to 26 and 29 January) and Regan Hillyer teaching Membership in place of Vishen.')
notes=[
 'Rebuilt on 5 October from three sources: Vykintas Glodenis’s curriculum proposal (eight modules, one business pillar each, the problem / management idea / installed system / observable change pattern, and the Get AI-Ready onboarding layer), Jaideep’s launch brief (16 weeks from Monday 16 November, two sessions per module, the summit on 30 October to 1 November), and the AI for Founders quiz (812 answers: operations, marketing and sales are where the pain is; solo founders start with marketing, founders with teams with operations; data safety and sounding like me are the unprogrammed worries).',
 'Team direction, 26 September (Jaideep, Marijana, Marta): Vishen leads the summit and takes only the big Mastery sessions; Vykintas leads the Mastery curriculum and every implementation lab; roughly one guest teacher per pillar; at least one more woman on the roster. Every guest here is placed where they are most authentic, from the names in consideration on 5 October, and none is confirmed for the Mastery until the team says so.',
 'Cadence, decided 5 October: Tuesday lesson, Thursday lab, 9am Pacific, Tuesday 17 November 2026 to Thursday 18 March 2027, with a break from 21 December to 3 January. Expert & Authority runs Tuesday and Friday; this programme deliberately does not match it. Vykintas leads every lab here and already holds '+str(len(vyk_fridays))+' of Expert & Authority’s Friday workshops at 9am Pacific inside this run ('+', '.join(fmt(d) for d in vyk_fridays)+'), so a Friday lab would put him in two rooms at once on each of those dates.',
 'The opening is Monday 16 November, the start date in the brief, with Vishen. It also keeps him clear of his Expert & Authority lesson at the same hour on Tuesday 17 November once the John Lee rotation is applied.',
 'Thanksgiving, decided 5 October: the Week 2 lab stays on Thursday 26 November. Expert & Authority looked at its 2025 cohort data, saw no attendance drop over Thanksgiving week, and kept its Friday 27 November workshop; the same reasoning applies here. The lab is Vykintas-led and recorded. Caveat: the 2025 evidence covers the week, not Thanksgiving Day itself, so the live number on the day is the test for the next cohort.',
 'What we promise, in Vykintas’s words: the founder moves from doing to orchestrating; a leaner team gets more done; hours back every week; every lead answered and followed up; new hires productive in days; a business designed for AI. What we do not promise: fully autonomous systems with no human trigger or review (that depth belongs in the Guild), integration with every founder’s own software beyond existing connectors, or hours measured by time tracking. The founder load map, filled in at Module 1 and again at Module 8, is the measure, plus a showcase of what is running.',
 'What this programme leaves to AI Mastery: how models work, prompting in depth, image and video generation, writing skills from scratch, building apps. Where both touch the same tool the angle differs: the brain in AI Mastery is your personal knowledge; here it is the company’s, shared with the team. Neither is the advanced one.',
 'Outside the modules there are only three sessions, all before Week 1: Get AI-Ready calls 1 and 2, which are Vykintas\u2019s and in his proposal as written (the content of each call is a first pass), and the Monday opening with Vishen, the kickoff from the earlier draft moved to the start date in the brief. Office hours and an alumni reunion were in the earlier draft and were removed on 7 October: Vishen\u2019s diary cannot carry extra calls, and continuity after graduation is the Guild\u2019s job, not the Mastery\u2019s. Expert & Authority\u2019s own Airtable holds only lessons, workshops, one bonus and the graduation.',
 'Summit learnings applied: a live build directly before every offer; every session leaves something built; written topic lock for every Vishen session two weeks ahead and no previews of unreleased tools; a sound check at every speaker handoff; untested builders get a paid webinar or Highlights slot before the summit; Shawn never follows Vykintas in the same event.',
]
promise={'can':['The founder moves from doing to orchestrating','A leaner team gets more done','Hours back every week','Every lead answered and followed up','New hires productive in days','A business designed for AI'],
         'cannot':['Fully autonomous systems that run with no human trigger or review: AI does the work, the founder or team approves; fully autonomous builds belong in the Guild','Integration with every founder\u2019s own software beyond what existing connectors cover: we do not teach specific CRMs or SaaS tools','Hours measured by time tracking: the founder load map, filled in at Module 1 and again at Module 8, is the measure, plus a showcase of what is running'],
         'line':'Ambitious, in words people will not take literally. \u201cYour business runs without you\u201d sets the expectation that agents do everything; that will not happen, and refunds follow.'}
summit={'name':'AI for Founders Summit','note':'name confirmed by Vishen, 6 Oct, over the brief\u2019s \u201cRun on AI\u201d recommendation','dates':'Friday 30 October to Sunday 1 November 2026','line':'Find out what to automate first in your business, then build it live, step by step.','role':'The launch event. Free, three days, the offer opens here.'}
difference=[['Organised by','AI capability','Business function'],['Each lesson starts from','A capability, for example connectors','A business problem, for example leads going cold'],['You leave with','The ability to build your own solutions','Proven systems installed and running in your business'],['Depth','Deep on applied AI','Deep on the business, lighter on AI'],['Management content','None','Core: how a founder thinks and decides with AI'],['Your role','Builder','Orchestrator'],['The question it answers','What can AI do, and how do I use it?','How should my business run in the age of AI?'],['Buying trigger','I am falling behind on AI','I am the bottleneck in my own business']]
out={'programme':'AI for Founders Mastery','source':{'label':'Draft curriculum held in this page until aligned with Vishen, then seeded into Airtable','url':'/ai-founders/proposal'},'promise':promise,'summit':summit,'difference':difference,'start':'2026-11-16','end':'2027-03-18','break':['2026-12-21','2027-01-03'],
     'mode':'draft','synced_at':dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'),
     'aligned':False,'cadence':'Monday 16 November opening · Tuesday lesson · Thursday lab · 9am Pacific · Vishen leads the summit, Vykintas leads the Mastery',
     'basis':SRC['basis'],'pattern':SRC['pattern'],
     'modules':modules,'labels':{'Workshop':'Lab'},'load':load,'load_basis':load_basis,'ea_range':ea_range,'roster':SRC['roster'],'notes':notes,'sessions':sessions}
(R/'data'/'ai-founders-curriculum.json').write_text(json.dumps(out,indent=1,ensure_ascii=False))
print('sessions',len(sessions)); print(json.dumps(load,indent=1)); print('E&A range',ea_range,'| Vykintas E&A Fridays in run:',vyk_fridays)
for s in sessions: print(s['start'][:10],s['type'],'|',s['title'][:52],'|',', '.join(p['name'] for p in s['speakers']))
