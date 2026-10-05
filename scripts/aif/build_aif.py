#!/usr/bin/env python3
"""Build eam-repo/data/ai-founders-curriculum.json: the AI for Founders draft curriculum (held in HTML until Vishen aligns).
Same schema as the E&A curriculum.json so it can be seeded into Airtable unchanged."""
import json, datetime as dt, pathlib, re
HERE=pathlib.Path(__file__).resolve().parent; R=HERE.parents[1]; raw=json.load(open(HERE/'aif_weeks_raw.json'))
weeks={int(re.sub(r'\D','',r['label'])):r for r in raw if r['label'].startswith('WEEK')}
IMG={'Vishen':'vishen-lakhiani','Daniel':'daniel-priestley','Vykintas':'vykintas-glodenis','Noelle Russell':'noelle-russell','Shawn Kanungo':'shawn-kanungo','Alex Dogliotti':'alex-dogliotti','Natalie Ellis':'natalie-ellis','Callan Faulkner':'callan-faulkner','Maria Wendt':'maria-wendt'}
FULL={'Vishen':'Vishen Lakhiani','Daniel':'Daniel Priestley','Vykintas':'Vykintas Glodenis','Daniel Priestley':'Daniel Priestley'}
def spk(name):
    key=name.strip(); f=IMG.get(key) or IMG.get(FULL.get(key,key)) or re.sub(r'[^a-z]+','-',key.lower()).strip('-')
    return {'name':FULL.get(key,key),'image':('authors/'+f+'.jpg') if (R/'authors'/(f+'.jpg')).exists() else None}
def who(s):
    s=re.sub(r'^(Teach|Lab)\s*·\s*','',s); return [spk(x) for x in re.split(r'\s*\+\s*',s)]
PT=dt.timezone(dt.timedelta(hours=-8))  # PST from 1 Nov
def at(d,h=9,m=0): return dt.datetime(d.year,d.month,d.day,h,m,tzinfo=PT).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')
MODS=['Phase 1: The Foundation','Phase 2: The Growth System','Phase 3: The Delivery Engine','Phase 4: People & Performance']
def mod(w): return MODS[0] if w<=4 else MODS[1] if w<=8 else MODS[2] if w<=13 else MODS[3]
# week -> (lesson date). Tue lesson, Thu lab. Break 21 Dec to 3 Jan.
starts={}; d=dt.date(2026,11,10); w=1
while w<=18:
    if d==dt.date(2026,12,22) or d==dt.date(2026,12,29): d+=dt.timedelta(days=7); continue
    starts[w]=d; d+=dt.timedelta(days=7); w+=1
# roster edits (Gareth 25 Sep: Priestley stays; deck guests in; Marie Forleo out)
OVR={
 1:{'teach_who':'Vishen','teach_text':'The age-of-intelligence reset, opened by Vishen: why every business must be reinvented and Founder-Based AI as the method. The five pillars named, the promise made, and Vykintas introduced as the person who will build it with you every Thursday. Opens with a build, not a visioning session.'},
 2:{'teach_who':'Vykintas','teach_text':'From the Quest\u2019s personal SEED to the company SEED: mission, data, docs, meetings. Record-everything as an organisation, not a habit. Vykintas teaches the brain every pillar runs on, then builds it in the lab two days later.'},
 4:{'teach_who':'Vykintas','teach_text':'Skills as company assets. The authoring craft the Quest skipped: anatomy of a great skill, testing, versioning, sharing. Your expertise made executable, taught by the person who built the Skill Pack.'},
 5:{'teach_who':'Maria Wendt','teach_title':'Know Exactly Who It\u2019s For, Then Never Let Them Go Cold','teach_text':'Customer intelligence and automated nurture from the founder who built $21M on low-ticket products and shows her real numbers. The ICP found in your own data, then a nurture machine (ManyChat, Claude, automated sequences) that follows up while you sleep. Radical transparency: real conversion rates, not inflated claims.'},
 6:{'teach_who':'Maria Wendt','teach_title':'Signals Before Sales: The AI-Run Demand Engine','teach_text':'How demand is captured with AI at the centre: capacity, signals, assessments and lead magnets as tooling, and the automation stack that turns attention into a list. Maria\u2019s second week: the demand side of the machine she runs at scale.'},
 7:{'teach_who':'Callan Faulkner','teach_title':'The AI-Architected Launch','teach_text':'The architecture behind a $19.5M launch, told by the person who built the AI side of it: the systems, the agents and the hand-offs that let a small team run a very large campaign. AI as the mechanism of the launch, not a tool bolted on. Callan\u2019s first of three weeks, subject to her agreeing to teach.'},
 8:{'teach_who':'Maria Wendt','teach_text':'The sales pillar: qualification, nurture, proposals, follow-up. Where automation lifts conversion and where it kills trust, with a human in the loop at every closing moment. Maria closes the Growth System with the follow-up machine that made her low-ticket model work at volume.'},
 9:{'teach_who':'Vykintas','teach_text':'The first week after the Growth System switches on: reading the live signal data, tuning the machine, and the doctrine of iteration. What to touch, what to leave alone, what the numbers are telling you. Vykintas reviews every founder\u2019s running system before Phase 3 begins.'},
 12:{'teach_who':'Callan Faulkner','teach_text':'From vibe-coding to a real product: scope with user stories, build, ship, and put AI inside your offer, not just behind it. Callan teaches product-building the way she builds AI systems for clients, then Vykintas takes the cohort through a prototype in front of users.'},
 14:{'teach_who':'Callan Faulkner','teach_title':'The AI-Centred Company','teach_text':'The Uncommon Method: how Callan runs 150 AI employees alongside a 30-person human team with nobody let go. The modern org chart with AI systems at the centre and four human roles around it. Role by role, which work moves to an agent and which stays human.'},
 15:{'teach_who':'Noelle Russell','teach_title':'Bring Your Humans With You'},
 16:{'teach_who':'Shawn Kanungo','teach_text':'Founder finance with AI: cashflow visibility, pricing and unit economics, forecasts, the weekly founder brief. The pillar every other programme skips, taught by a CPA with a Deloitte background so it is credible rather than aspirational.'},
 17:{'teach_who':'Shawn Kanungo','teach_title':'The Bold Founder'},
 18:{'teach_who':'Vishen + Vykintas','teach_text':'Vishen and Vykintas close together: from momentum to market leadership, certification, success sharing and the cohort showcase. Vishen\u2019s third and final big session.'},
}
sessions=[]
def add(**k): sessions.append(k)
add(id='aif-bonus-skillpack',title='Founder OS Starter Kit and Skill Pack install',type='Bonus',start=at(dt.date(2026,11,5)),duration_min=120,speakers=[spk('Vykintas')],module=None,
    description='Before Week 1, every founder installs the Founder OS Starter Kit and the Skill Pack: one Claude skill per lesson, the project templates, connector guides and prompts the labs run on. Vykintas walks the install live so that on the first Thursday nobody is stuck on setup. This is the fix for the setup friction that ate labs in two earlier cohorts.\n\nYou’ll leave with:\n- The Starter Kit and Skill Pack installed and tested\n- Your first governed project created\n- A head start on Week 1 before it begins')
add(id='aif-kickoff',title='The Room, the Blueprint and Your Before Picture',type='Kick Off',start=at(dt.date(2026,11,9)),duration_min=75,speakers=[spk('Vishen'),spk('Vykintas')],module=None,
    description='One live call between the summit and Week 1. Vishen and Vykintas read the room back to itself from the onboarding survey, walk the 18 weeks with the teacher on each, and take the one measurement graduation is judged against: how many hours a week your business needs you today. You leave with the calendar in your hands and a number written down.')
for w in range(1,19):
    r=weeks[w]; teach=[c for c in r['calls'] if not c['lab']][0]; lab=[c for c in r['calls'] if c['lab']]
    o=OVR.get(w,{}); d=starts[w]
    tw=o.get('teach_who',teach['who']); tt=o.get('teach_title',teach['title']); tx=o.get('teach_text',teach['text'])
    lid=f'aif-w{w:02d}-lesson'
    add(id=lid,title=tt if w!=18 else 'Graduation: Designing Your Next 12 Months',type='Lesson' if w!=18 else 'Graduation',start=at(d),duration_min=90,speakers=who(tw),module=mod(w),description=tx,week=w)
    if lab and w!=18:
        l=lab[0]; ltext=l['text']+(('\n\n**The win:** '+re.sub(r'^Win:\s*','',l['win'])) if l['win'] else '')
        add(id=f'aif-w{w:02d}-lab',title=o.get('lab_title',l['title']),type='Workshop',start=at(d+dt.timedelta(days=2)),duration_min=90,speakers=who(l['who']),module=mod(w),description=ltext,week=w,pair=lid)
    else:
        add(id=f'aif-w{w:02d}-lab',title='Certification showcase and cohort demo day',type='Workshop',start=at(d+dt.timedelta(days=2)),duration_min=90,speakers=[spk('Vykintas')],module=mod(w),description='Every founder demonstrates one running system per pillar. Certification is awarded on systems in production, not videos watched. The cohort showcase closes the programme.',week=w,pair=lid)
# Q&A calls: Vishen with Vykintas, own Zoom webinar, Fridays
for i,d in enumerate([dt.date(2026,12,4),dt.date(2027,1,15),dt.date(2027,2,12),dt.date(2027,3,12)],1):
    add(id=f'aif-qa-{i}',title=f'Office hours {i}: open Q&A with Vykintas'+(' and Vishen' if i in (1,4) else ''),type='Q&A Call',start=at(d),duration_min=60,speakers=([spk('Vishen')] if i in (1,4) else [])+[spk('Vykintas')],module=None,
        description='A dedicated Zoom webinar, not folded into a lesson. Bring the system you are stuck on. The summit data showed the dedicated Q&A held 94 percent of the room and was where sign-ups and the hardest questions clustered, so the Mastery gets one a month.')
add(id='aif-alumni',title='Alumni reunion and OS upgrade call',type='Community',start=at(dt.date(2027,5,6)),duration_min=60,speakers=[spk('Vishen'),spk('Vykintas')],module=None,description='Six weeks after graduation: what broke, what compounded, and the quarterly upgrade to the Founder Operating System.')
sessions.sort(key=lambda s:s['start'])
# diary load, computed against the E&A Airtable snapshot
ea=json.load(open(R/'data'/'curriculum.json'))
def load_for(name):
    rows=[]
    for s in ea['sessions']:
        if any(p['name']==name for p in s['speakers']) and s.get('start'): rows.append(('E&A',s['start'][:10],s['type']))
    for s in sessions:
        if any(p['name']==name for p in s['speakers']): rows.append(('AIF',s['start'][:10],s['type']))
    weeks={}
    for prog,day,typ in rows:
        wk=dt.date.fromisoformat(day); wk=wk-dt.timedelta(days=wk.weekday()); weeks.setdefault(wk,[]).append(prog)
    heavy=sorted([ (k,v) for k,v in weeks.items() if len(v)>=3 ])
    both=sorted([k for k,v in weeks.items() if 'E&A' in v and 'AIF' in v])
    return {'name':name,'ea':sum(1 for r in rows if r[0]=='E&A'),'aif':sum(1 for r in rows if r[0]=='AIF'),
            'weeks_on_both':len(both),'first_overlap':both[0].isoformat() if both else None,'last_overlap':both[-1].isoformat() if both else None,
            'peak_per_week':max(len(v) for v in weeks.values()),'weeks_3plus':len(heavy)}
load=[load_for('Vishen Lakhiani'),load_for('Vykintas Glodenis')]
notes=[
 'Team direction, 26 September (Jaideep, Marijana, Marta): Vishen leads the summit and takes only the big Mastery sessions; Vykintas leads the Mastery curriculum and every implementation lab; six speakers at about three classes each; Daniel Priestley is not the lead here and is being looked at for Social Media instead; Natalie Ellis is not a fit; Noelle Russell is in; at least one more woman on the roster.',
 'Allocation of the 18 lessons: Vishen 3 (Weeks 1, 13, 18), Vykintas 4 as curriculum lead (Weeks 2, 4, 9, 11) plus co-closing Week 18, Noelle Russell 3 (Weeks 3, 10, 15), Maria Wendt 3 (Weeks 5, 6, 8), Callan Faulkner 3 (Weeks 7, 12, 14), Shawn Kanungo 2 (Weeks 16, 17). Three of the six are women.',
 'Callan Faulkner runs a competing programme and may decline. If she does, her three weeks go to an AI coach or AI consultant with a track record at scale, to be found by Author Relations. The weeks are written so a substitute can take them without redesign.',
 'Proven names open the programme to protect the refund window: Vishen in Week 1, Vykintas in Week 2, Noelle in Week 3. New names arrive from Week 5, after the summit has given a second data point on each.',
 'The three-day weekend intensive is folded into the Tuesday and Thursday mainline, as was done for Expert & Authority. Week 9 is the switch-on review.',
 'Cadence: Tuesday lesson, Thursday lab, 9am Pacific, from Tuesday 10 November 2026 to Thursday 25 March 2027, with a break from 21 December to 3 January. The Week 3 lab falls on US Thanksgiving, 26 November, and should move.',
 'Expert & Authority conventions carried across: a dated Skill Pack bonus before Week 1, a kickoff call, four monthly office-hours calls on their own Zoom webinar led by Vykintas with Vishen on the first and last, an alumni reunion six weeks after graduation.',
 'Summit learnings applied: written topic lock for every Vishen session two weeks ahead and no previews of unreleased tools; a sound check at every speaker handoff; Callan takes a free trial session before her paid slot; Shawn never closes and never follows Vykintas in the same event.',
]
out={'programme':'AI for Founders Mastery','source':{'label':'Draft curriculum held in this page until aligned with Vishen, then seeded into Airtable','url':'/ai-founders-proposal'},
     'mode':'draft','synced_at':dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'),
     'aligned':False,'cadence':'Tuesday lesson · Thursday lab · 9am Pacific · Vishen leads the summit, Vykintas leads the Mastery',
     'modules':[{'name':m,'short':m.split(': ',1)[1],'order':i+1} for i,m in enumerate(MODS)],
     'labels':{'Workshop':'Lab'},'load':load,'notes':notes,'sessions':sessions}
(R/'data'/'ai-founders-curriculum.json').write_text(json.dumps(out,indent=1,ensure_ascii=False))
print('sessions',len(sessions)); print(json.dumps(load,indent=1))
for s in sessions: print(s['start'][:10],s['type'],'|',s['title'][:50],'|',', '.join(p['name'] for p in s['speakers']))
