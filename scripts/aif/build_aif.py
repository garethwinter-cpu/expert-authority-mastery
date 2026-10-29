#!/usr/bin/env python3
"""Build data/ai-founders-curriculum.json: the AI for Founders draft curriculum, held in this repo until Vishen aligns.
Same schema as the E&A curriculum.json so it can be seeded into Airtable unchanged.

Source of the copy: scripts/aif/aif_modules.json (eight modules, seventeen lessons and a graduation, lesson + lab every week),
built on Vykintas's post-call draft and Jaideep's decision deck of 14 Oct 2026. Calendar: week 1 is Tue 17 Nov 2026; lessons
Tuesday, labs Thursday, 7am Pacific (3pm London, 2pm London 16 to 25 March); no sessions 22 and 29 Dec; graduation Tue 30 Mar 2027."""
import json, datetime as dt, pathlib, re
from zoneinfo import ZoneInfo
HERE=pathlib.Path(__file__).resolve().parent; R=HERE.parents[1]
SRC=json.load(open(HERE/'aif_modules.json'))
IMG={'Vishen':'vishen-lakhiani','Vykintas':'vykintas-glodenis'}
FULL={'Vishen':'Vishen Lakhiani','Vykintas':'Vykintas Glodenis'}
def spk(name):
    key=name.strip(); f=IMG.get(key) or re.sub(r'[^a-z]+','-',FULL.get(key,key).lower()).strip('-')
    return {'name':FULL.get(key,key),'image':('authors/'+f+'.jpg') if (R/'authors'/(f+'.jpg')).exists() else None}
def who(s): return [] if s.strip().upper()=='TBD' else [spk(x) for x in re.split(r'\s*\+\s*',s)]
PT=ZoneInfo('America/Los_Angeles')
def at(d,h=7,m=0): return dt.datetime(d.year,d.month,d.day,h,m,tzinfo=PT).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')

# week -> Tuesday. 17 lesson weeks and a graduation week from Tue 17 Nov 2026, break 21 Dec to 3 Jan
WEEKS=max(c['week'] for m in SRC['modules'] for c in m['calls'])
starts={}; d=dt.date(2026,11,17); w=1
while w<=WEEKS:
    if d in (dt.date(2026,12,22),dt.date(2026,12,29)): d+=dt.timedelta(days=7); continue
    starts[w]=d; d+=dt.timedelta(days=7); w+=1
modules=[{'name':f"Module {m['n']}: {m['name']}",'short':m['short'],'order':m['n'],'problem':m['problem'],'installed':m['installed'],'changes':m['changes'],'weeks':m['weeks']} for m in SRC['modules']]
def mod(w): return next(x['name'] for x in modules if w in x['weeks'])

sessions=[]
def add(**k): sessions.append(k)
GAR=SRC['onboarding']['text']
add(id='aif-fast-action',title='What to Automate First, Built With Vishen',type='Bonus',start=at(dt.date(2026,11,4)),duration_min=90,speakers=[spk('Vishen'),spk('Vykintas')],module=None,
    description='Fast action bonus call for early buyers, live on Wednesday 4 November: each founder looks at their own week, finds the work that eats the most hours, chooses the one thing to hand to AI first, and sees it built live. The bridge from the summit to kickoff; the recording follows in BlinkLearn.')
add(id='aif-ready-1',title='Get AI-Ready 1 (pre-recorded): setup, your first pack, your hours log',type='Bonus',start=at(dt.date(2026,11,5)),duration_min=90,speakers=[spk('Vykintas')],module=None,
    description='Pre-recorded, ready from 5 November: Claude Code set up on a folder, the first AI skills installed, talking instead of typing, the basics of how AI works, hosting ready so publishing is one sentence, and the 30-minute hours log started.\n\n'+GAR)
add(id='aif-ready-2',title='Get AI-Ready 2 (pre-recorded): the go-live walkthrough',type='Bonus',start=at(dt.date(2026,11,12)),duration_min=90,speakers=[spk('Vykintas')],module=None,
    description='Pre-recorded, ready from 12 November: hosting set up step by step, so publishing is one sentence from week 1. For late buyers and anyone stuck; anyone who still cannot publish goes live in the week 1 lab.\n\n'+GAR)
for m in SRC['modules']:
    for c in m['calls']:
        w=c['week']; d=starts[w]
        if c['type'] in ('lesson','graduation'):
            add(id=f'aif-w{w:02d}-lesson',title=c['title'],type='Lesson' if c['type']=='lesson' else 'Graduation',start=at(d),duration_min=90,speakers=who(c['who']),module=mod(w),description=c['text'],brief=c.get('brief'),team=c.get('team'),week=w)
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
 # The snapshot was refreshed from Airtable on 14 Oct and already carries the John Lee rotation and Marisha Lakhiani's
 # Paid Advertising and Funnel Design workshops, so those overlay rows were removed: re-applying them moved Vishen's
 # Membership lesson to 17 Nov and counted Vykintas twice on 20 Nov. One held decision of 5 Oct (STATUS.md) is still not in
 # Airtable: Regan Hillyer teaching Membership, Continuity & Superfans in Vishen's place.
 {'title':'Membership, Continuity & Superfans','type':'Lesson','if_speaker':'Vishen Lakhiani','speaker':'Regan Hillyer'},
]
def ea_sessions():
    out=[]
    for s in ea['sessions']:
        m=re.match(r'\s*(\d+)',str(s.get('slot') or '')); slot=int(m.group(1)) if m else None
        names=[p['name'] for p in s['speakers']]; moved=False
        for o in EA_OVERLAY:
            if 'slot' in o and o['slot']!=slot: continue
            if 'title' in o and not s['title'].startswith(o['title']): continue
            if 'type' in o and o['type']!=s['type']: continue
            if o['if_speaker'] not in names: continue
            if 'speaker' in o: names=[o['speaker'] if n==o['if_speaker'] else n for n in names]
            if 'to_slot' in o: slot=o['to_slot']; moved=True
        start=s.get('start')                                 # the 14 Oct snapshot is Airtable as it stands: trust its dates and times
        if moved: start=at(ea_slot_date(slot),9)            # an overlay that moves a session uses E&A's rule: 9am Pacific
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
load_basis=('Computed against the Expert & Authority calendar as read from Airtable on 14 October 2026 (Tuesday lessons, Friday workshops, 9am Pacific, '
            'no Thanksgiving break, graduation Tuesday 23 February; the John Lee rotation and Marisha Lakhiani\u2019s two workshops are in it), with one decision held on 5 October '
            'applied on top because it is not yet in Airtable: Regan Hillyer teaching Membership on 26 January in place of Vishen.')
notes=[
 'Teachers, allocation D, agreed with Vykintas on 29 October and entered in the AIF Airtable base: Vishen opens week 1 and teaches weeks 2, 7, 8 and 16; Vykintas teaches weeks 1, 3, 5, 9, 11 and 17, every lab and both pre-recorded Get AI-Ready sessions; Noelle Russell weeks 6 and 15 (weeks 3 and 6 swapped on 29 October after team feedback); Ajit Nawalkha weeks 4 and 10; Marisha Lakhiani week 12; Sara Davison and Tyler Fisk week 13; Joe Stolte week 14; Vishen and Vykintas host the fast action bonus call on 4 November and co-host graduation. Labs, Vykintas\u2019s lessons, week 1, graduation and the pre-recorded sessions are Confirmed in Airtable; Vishen\u2019s and the guests\u2019 lessons are Proposed. Before contracts: Joe, Sara and Tyler have no Mindvalley ratings until the summit.',
 '14 October, after the team call (Vykintas, Jaideep, Marisha, Gareth), Vykintas\u2019s post-call draft and Jaideep\u2019s decision deck, with Gareth\u2019s decisions on the deck: seventeen lessons and a graduation (eighteen calls, as agreed in the call); the company brain in week 4 and inbox triage straight after it in week 5, because the brain gives AI the context to prioritise and draft (Vykintas, later on 14 October, who asked for the brain in lesson 3 to 5), with the longest privacy segment in the inbox lab; hosting in onboarding with a go-live clinic; owner pages, a test week and graduation as the ending; Meta ads kept in the core so paid and organic are both taught; software building as an elective. Every lesson installs an AI team, a head and three members, as Vykintas proposed. Teachers are mapped once the curriculum is settled, five or six at most.',
 'Rebuilt on 5 October from three sources: Vykintas Glodenis’s curriculum proposal (eight modules, one business pillar each, the problem / management idea / installed system / observable change pattern, and the Get AI-Ready onboarding layer), Jaideep’s launch brief (16 weeks from Monday 16 November, two sessions per module, the summit on 30 October to 1 November), and the AI for Founders quiz (812 answers: operations, marketing and sales are where the pain is; solo founders start with marketing, founders with teams with operations; data safety and sounding like me are the unprogrammed worries).',
 'Team direction, 26 September (Jaideep, Marijana, Marta): Vishen leads the summit and takes only the big Mastery sessions; Vykintas leads the Mastery curriculum and every implementation lab; roughly one guest teacher per pillar; at least one more woman on the roster. Every guest here is placed where they are most authentic, from the names in consideration on 5 October, and none is confirmed for the Mastery until the team says so.',
 'Cadence, decided 5 October, hour set 7 October: Tuesday lesson, Thursday lab, 7am Pacific (3pm London; 2pm London from 16 to 25 March), Tuesday 17 November 2026 to graduation on Tuesday 30 March 2027, with a break from 21 December to 3 January. Expert & Authority runs Tuesday and Friday; this programme deliberately does not match it. Vykintas leads every lab here and already holds '+str(len(vyk_fridays))+' of Expert & Authority’s Friday workshops at 9am Pacific inside this run ('+', '.join(fmt(d) for d in vyk_fridays)+'), so a Friday lab would put him in two rooms on the same morning on each of those dates.',
 'The separate Monday opening on 16 November is folded into week 1, as Jaideep\u2019s deck proposes: Vishen opens the first lesson on Tuesday 17 November for about twenty minutes, then Vykintas builds. That saves Vishen one call; his other Mastery session is graduation. It is a two-programme morning: his Expert & Authority Email Marketing lesson starts at 9am Pacific the same day, so his twenty minutes at 7am leave room, but the diary should hold both.',
 'Thanksgiving, decided 5 October and checked against the day on 7 October: the Week 2 lab stays on Thursday 26 November, Thanksgiving Day in the US. Expert & Authority’s 2025 reading was that the week holds, and it kept its Friday 27 November workshop. The 2025 Mastery records confirm the week and sharpen the day: AI Mastery’s sessions the day before (422 against 454 and 447 the Wednesdays either side) and the day after (307 against 274 and 313) showed no dip; the one session that ran on Thanksgiving Day itself, Entrepreneurship Mastery’s Thursday lesson, kept 214 of a usual 300, about 70 percent, and its recording was watched more that week than any other Thursday’s that month. So the lab runs, Vykintas-led and recorded, and the Tuesday 1 December lesson picks up anyone who missed it. Wednesday 25 November is the alternative if the team prefers not to run on the day; the day before showed no dip.',
 'Time slot, set 7 October: 7am Pacific, which is 3pm London except from 16 to 25 March 2027, when it is 2pm (US clocks change on 14 March, UK clocks on 28 March); graduation on 30 March is back at 3pm London. Janja set the hour for team capacity and schedule; the data supports it. Attendance across five Mastery bases shows no hour effect between 7am and 10am Pacific (Entrepreneurship Mastery moved from 5pm to 3pm London mid-cohort and attendance did not move), Manifesting and Speaking & Influence Mastery run at 3pm London with the highest live rates in the set, and the final hour-by-hour preference was for 9am because about 60 percent of students are in North America; that was never a hill to die on. Students are told the Pacific time; London is the derived time. Evidence in briefs/AIF-TIME-SLOT-EVIDENCE.md.',
 'What this programme leaves to AI Mastery: how models work, prompting in depth, image and video generation, writing skills from scratch, building apps (the one exception is the software elective, offered outside the core seventeen). Where both touch the same tool the angle differs: the brain in AI Mastery is your personal knowledge; here it is the company’s, shared with the team. Neither is the advanced one.',
 'Outside the lessons: the fast action bonus call, live on Wednesday 4 November with Vishen and Vykintas, and two pre-recorded Get AI-Ready sessions, ready from 5 and 12 November, the second being the go-live walkthrough for hosting. Office hours and an alumni reunion were removed on 7 October, and the Monday opening was folded into week 1 on 14 October. Software building is an elective; its format, recorded or an extra live call, is not yet decided.',
 'Summit learnings applied: a live build directly before every offer; every session leaves something built; written topic lock for every Vishen session two weeks ahead and no previews of unreleased tools; a sound check at every speaker handoff; untested builders get a paid webinar or Highlights slot before the summit; Shawn never follows Vykintas in the same event.',
]
promise={'can':['The founder moves from doing to orchestrating','A leaner team gets more done','Hours back every week','Every lead answered and followed up','The books off the founder\u2019s desk','A business designed for AI'],
         'cannot':['Fully autonomous systems that run with no human trigger or review: AI does the work, the founder or team approves; fully autonomous builds are outside this programme','Integration with every founder\u2019s own software beyond what existing connectors cover: we do not teach specific CRMs or SaaS tools','Hours measured by time tracking: the 30-minute hours log in week 0, counted again at graduation, is the measure, plus Demo Day, a showcase of what is running'],
         'line':'Ambitious, in words people will not take literally. \u201cYour business runs without you\u201d sets the expectation that agents do everything; that will not happen, and refunds follow.'}
agenda=json.load(open(R/'scripts'/'aif'/'summit_agenda.json',encoding='utf-8'))
summit={'name':'AI for Founders Summit','note':'name confirmed by Vishen, 6 Oct, over the brief\u2019s \u201cRun on AI\u201d recommendation','dates':'Friday 30 October to Sunday 1 November 2026','line':'Find out what to automate first in your business, then build it live, step by step.','role':'The launch event. Free, three days, the offer opens here.','agenda':agenda}
difference=[['Organised by','AI capability','Business function'],['Each lesson starts from','A capability, for example connectors','A business problem, for example leads going cold'],['You leave with','The ability to build your own solutions','Proven systems installed and running in your business'],['Depth','Deep on applied AI','Deep on the business, lighter on AI'],['Management content','None','Core: how a founder thinks and decides with AI'],['Your role','Builder','Orchestrator'],['The question it answers','What can AI do, and how do I use it?','How should my business run in the age of AI?'],['Buying trigger','I am falling behind on AI','I am the bottleneck in my own business']]
artefact={'name':'The Founder Operating System','short':'Founder OS','parts':['Company brain','Storefront, funnel and traffic teams','Sales, operations and finance teams','The founder\u2019s cockpit'],'line':'What a founder leaves with: the systems built week by week, running as one, in their own business.'}
SESSION_NOTES={'aif-w02-lab':'Thanksgiving Day in the US. The lab runs as scheduled and is recorded; the Week 3 lesson on Tuesday 1 December picks up anyone who misses it.',
               'aif-w16-lesson':'2pm London this week, not 3pm: US clocks changed on 14 March, UK clocks change on 28 March.',
               'aif-w16-lab':'2pm London this week, not 3pm: US clocks changed on 14 March, UK clocks change on 28 March.',
               'aif-w17-lesson':'2pm London this week, not 3pm: US clocks changed on 14 March, UK clocks change on 28 March.',
               'aif-w17-lab':'2pm London this week, not 3pm: US clocks changed on 14 March, UK clocks change on 28 March.',
               'aif-w18-lesson':'3pm London again: UK clocks changed on 28 March.'}
for s in sessions:
    if s['id'] in SESSION_NOTES: s['note']=SESSION_NOTES[s['id']]
slot={'pt':'7am Pacific','london':'3pm London','london_final':'2pm London from 16 to 25 March 2027',
      'line':'7am Pacific, 3pm London (2pm London from 16 to 25 March, between the US and UK clock changes)',
      'anchor':'Pacific is the anchor; London is the derived time','decided':'2026-10-07','decided_by':'Janja, for team capacity and schedule'}
survey=json.load(open(R/'scripts'/'aif'/'aif_survey.json',encoding='utf-8'))
survey.setdefault('url',None); survey.setdefault('note','Survey link to follow')
emails=json.load(open(R/'scripts'/'aif'/'aif_emails.json',encoding='utf-8'))
out={'programme':'AI for Founders Mastery','artefact':artefact,'source':{'label':'Draft curriculum held in this page until aligned with Vishen, then seeded into Airtable','url':'/ai-founders/proposal'},'promise':promise,'summit':summit,'difference':difference,'start':'2026-11-17','end':'2027-03-30','break':['2026-12-21','2027-01-03'],
     'mode':'draft','synced_at':dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'),
     'aligned':False,'cadence':'Seventeen lessons and a graduation · Tuesday lesson · Thursday lab · 7am Pacific, 3pm London (2pm London 16 to 25 March) · graduation Tuesday 30 March 2027','slot':slot,'survey':survey,'emails':emails,
     'basis':SRC['basis'],'pattern':SRC['pattern'],'lab_format':SRC['lab_format'],'onboarding':SRC['onboarding'],'changelog':SRC['changelog'],'changelog_title':SRC['changelog_title'],'electives':SRC['electives'],'tools':SRC['tools'],
     'modules':modules,'labels':{'Workshop':'Lab'},'load':load,'load_basis':load_basis,'ea_range':ea_range,'roster':SRC['roster'],'notes':notes,'sessions':sessions}
(R/'data'/'ai-founders-curriculum.json').write_text(json.dumps(out,indent=1,ensure_ascii=False))
print('sessions',len(sessions)); print(json.dumps(load,indent=1)); print('E&A range',ea_range,'| Vykintas E&A Fridays in run:',vyk_fridays)
for s in sessions: print(s['start'][:10],s['type'],'|',s['title'][:52],'|',', '.join(p['name'] for p in s['speakers']))

# The outline for the survey invitation: module, lesson, lab, one line on the lesson. No teachers, no dates, no times.
byid={s['id']:s for s in sessions}
md=['# AI for Founders Mastery: the curriculum outline','',
    'Seventeen lessons and a graduation, eight modules, one department of the business at a time. Every lesson has a lab, where the system is installed in your own business. This is the draft before it is finished. Read it as a partner: what is missing, where should we go deeper, what would you skip?','']
for mod in modules:
    mname=re.sub(r'^Module \\d+: ','',mod['name'])
    md.append(f"## {mod['order']}. {mname}"); md.append(f"*{mod['problem']}*"); md.append('')
    for w in mod['weeks']:
        L=byid.get(f'aif-w{w:02d}-lesson'); Bb=byid.get(f'aif-w{w:02d}-lab')
        if L: md.append(f"**{'Graduation' if L['type']=='Graduation' else 'Lesson'}: {L['title']}**  "); md.append(L.get('brief') or '')
        if L and L.get('team'): md.append(''); md.append('*Your AI team: '+', '.join([L['team']['head']]+[m['name'] for m in L['team']['members']])+'*')
        if Bb: md.append(f"**Lab: {Bb['title']}**"); md.append('')
md+=['## Three questions for you','','1. What is missing that you expected to see?','2. Where should we go deeper?','3. What would you skip?','','*Survey link to follow.*','']
(R/'briefs'/'AIF-CURRICULUM-OUTLINE.md').write_text('\n'.join(md))
print('outline written', len(md),'lines')

sm=['# AI for Founders: the co-creation survey','',survey['intro'],'']
for sec in survey['sections']:
    sm.append(f"## {sec['title']}"); sm.append(sec.get('lead','')); sm.append('')
    for q in sec['questions']:
        sm.append(f"**{q['n']}. {q['text']}**  "); sm.append(f"_{q['type']}{' · required' if q.get('required') else ' · optional'}{(' · '+q['step']) if q.get('step') else ''}_")
        for o in q.get('options',[]): sm.append(f"- {o}")
        if q.get('rows'): sm.append('Rows: '+'; '.join(q['rows']))
        if q.get('scale'): sm.append('Scale: '+' / '.join(q['scale']))
        for k,v in (q.get('variants') or {}).items(): sm.append(f'- {k} version: {v}')
        sm.append(f"*Why we ask: {q['why']}*"); sm.append('')
sm+=['## What the quiz already told us','']+[f'- {x}' for x in survey.get('quiz_insights',[])]+['','## How this answers the 6 October brief','']+[f"- **{b['ask']}** {b['how']}" for b in survey.get('brief_map',[])]+['','## Thank-you page','',survey['thanks'],'','## Design notes','']+[f"- {n}" for n in survey['design_notes']]+['','## What we do with the answers','']+[f"- {n}" for n in survey['analysis']]
(R/'briefs'/'AIF-SURVEY.md').write_text('\n'.join(sm))
print('survey written')
