import json, collections, re, html as H
rows=json.load(open('quiz/all_norm.json'))
N=len(rows)
def C(k): return collections.Counter(r[k] for r in rows if r[k])
T,NN,R,B,S=C('T'),C('N'),C('R'),C('B'),C('S')
q=[(r['q6'].strip(),r) for r in rows if r['q6'] and len(r['q6'].strip())>2]
nq=len(q)
THEMES={
 'A system I can follow, start to finish': r"\b(how to|don't know how|dont know how|where to start|roadmap|strategy|plan|steps|guidance|mentor|structure|system|knowledge|skills?|learn|know[- ]?how|framework)\b",
 'Selling, pricing and making an offer': r"\b(sell|sale|selling|money|price|pricing|charge|offer|monet|revenue|income|paying|clients?|customers?|convert|conversion|funnel|launch|product)\b",
 'Being seen and growing an audience': r"\b(visib|seen|audience|reach|follow|marketing|social media|instagram|content|post|platform|algorithm|exposure|brand|known|attention|traffic|grow|linkedin|youtube|tiktok)\b",
 'Clarity, niche and putting it into words': r"\b(clarity|clear|niche|focus|direction|position|what i do|message|messaging|too many|scattered|which idea|too broad|articulate|define|defin|identity|who i am|jack of all)\b",
 'Time, overwhelm and consistency': r"\b(time|busy|overwhelm|consisten|discipline|job|full[- ]time|energy|burnout|juggl|balance|kids|family|hours|too much|priorit)\b",
 'Money, tools and tech': r"\b(funds|funding|capital|budget|afford|cash|invest|no money|resources|tech|technology|website|tools|systems?|automation|ai\b)\b",
 'Credibility and proof': r"\b(credib|credential|qualif|certif|degree|experience|proof|testimon|track record|authority|legitim|too young|too old|age)\b",
 'Network and not doing it alone': r"\b(network|community|support|alone|lonely|connections?|team|accountab|mentor|peers?|tribe|partner)\b",
 'Fear, confidence and self-doubt': r"\b(fear|afraid|scared|confiden|imposter|impostor|self[- ]?doubt|doubt|not good enough|worth|courage|brave|anxiety|anxious|insecur|shy|judg|criticis|rejection|perfection|procrastinat|vulnerab|comparison)\b",
 'Mindset and old stories': r"\b(mindset|belief|block|limiting|trauma|past|story|self[- ]?sabotag|subconscious|inner|healing|worthiness|permission|deserve)\b",
}
TH=collections.Counter()
for t,r in q:
    for k,p in THEMES.items():
        if re.search(p,t.lower()): TH[k]+=1
uncoded=sum(1 for t,r in q if not any(re.search(p,t.lower()) for p in THEMES.values()))
PH={'"without me", "trading time", "while I sleep", "passive"':r"without me|trading (my )?time|time for money|while i sleep|passive|scal|automat|runs itself|not (be|being) always available",
 'a course, programme or digital product':r"\bcourse|online product|digital product|programme|program\b|membership",
 'pricing, charging, premium, worth':r"pric|charg|premium|worth|undercharg|rates?\b",
 'a book, speaking, a stage, a podcast':r"\bbook|author|speak|stage|podcast|keynote",
 'fear, courage, shy, self-doubt':r"fear|afraid|courage|shy|doubt|confiden|imposter|impostor|scared|dare",
 'a funnel, a website, tech, AI':r"funnel|website|landing|tech|automation|\bai\b",
 'leaving a job or employment':r"\bjob\b|employ|9 ?to ?5|corporate|leaving|quit|transition",
 'what to post, consistency, showing up':r"what to post|what to say|content idea|consisten|show up|posting",
 'my story, my message, articulating it':r"my story|tell my story|storytell|articulat|put .* into words|message",
 'the right rooms, network, connections':r"network|right rooms?|connections?|contacts|introduc|partnership",
 'where to start, step by step, a blueprint':r"where to start|where do i start|step[- ]by[- ]step|blueprint|roadmap|start to finish|dummies|simple system|the how",
 'testimonials, proof, a credibility gap':r"testimon|proof|credib|track record|case stud"}
PHC={k:sum(1 for t,r in q if re.search(p,t.lower())) for k,p in PH.items()}
goodat=sum(1 for t,r in q if re.search(r"(good at what i do|know my stuff|great (coach|at)|expert in|i know (i can|a lot|my)|i have (the )?knowledge)",t.lower()))
hi=[r for r in rows if r['R'] in ('$100K–$500K','$500K–$1M','Over $1M')]
nrev=sum(R.values())
def xt(a,b,arow,bcols):
    out={}
    for av in arow:
        sub=[r for r in rows if r[a]==av and r[b]]
        n=len(sub); c=collections.Counter(r[b] for r in sub)
        out[av]=(n,[c.get(bv,0)/n if n else 0 for bv in bcols])
    return out
TYPES=['The Expert','The Founder','The Creator','The Established Expert']
REVS=['Nothing yet','Under $25K','$25K–$100K','$100K–$500K','$500K–$1M','Over $1M']
BRK=['Nobody knows I exist',"I can't put what I do into words","People follow me but don't buy","I'm known, but I've plateaued",'One offer, nowhere for customers to go next']
SUC=['My first paying clients','Fully booked at premium rates','A product line that sells without trading hours','Being THE name in my niche','A room of peers at my level']
TEN=['Under 1 year','1–2 years','2–5 years','5–10 years','10+ years']
tr=xt('T','R',TYPES,REVS); tb=xt('T','B',TYPES,BRK); ts=xt('T','S',TYPES,SUC); rb=xt('R','B',REVS,BRK); rs=xt('R','S',REVS,SUC); nr=xt('N','R',TEN,REVS)
days=collections.Counter(r['created'][:10] for r in rows)
upsell=C('upsell'); vip=sum(1 for r in rows if r['vip'])
nonen=sum(1 for r in rows if r['tenure'] and r['tenure'] not in ('More than 10 years','Less than a year','2–5 years','5–10 years','1–2 years'))

def pct(x,n): return f'{x/n:.0%}'
def bars(counter, order=None, total=None, label_w=300):
    items=[(k,counter[k]) for k in (order or [k for k,_ in counter.most_common()])]
    total=total or sum(counter.values()); mx=max(v for _,v in items)
    out=['<div class="bars">']
    for k,v in items:
        out.append(f'<div class="bar"><div class="bl">{H.escape(k)}</div><div class="bt"><div class="bf" style="width:{v/mx*100:.1f}%"></div></div><div class="bv">{v/total:.0%}<span>{v:,}</span></div></div>')
    out.append('</div>'); return '\n'.join(out)
def heat(xtab, rowlabel, cols, note):
    out=[f'<div class="tbl-scroll"><table class="heat"><thead><tr><th>{rowlabel}</th>']
    for c in cols: out.append(f'<th>{H.escape(c)}</th>')
    out.append('<th class="n">n</th></tr></thead><tbody>')
    for rk,(n,vals) in xtab.items():
        out.append(f'<tr><th>{H.escape(rk)}</th>')
        for v in vals:
            a=min(1,v/0.7)
            out.append(f'<td style="--a:{a:.2f}">{v:.0%}</td>')
        out.append(f'<td class="n">{n:,}</td></tr>')
    out.append(f'</tbody></table></div><p class="cap">{note}</p>'); return '\n'.join(out)

topN=lambda c:c.most_common(1)[0]
nothing=R['Nothing yet']; expert=T['The Expert']; nobody=B['Nobody knows I exist']; ten=NN['10+ years']
vet_nothing=sum(1 for r in rows if r['N']=='10+ years' and r['R']=='Nothing yet'); vet_n=sum(1 for r in rows if r['N']=='10+ years' and r['R'])
hi_plateau=sum(1 for r in hi if r['B']=="I'm known, but I've plateaued"); hi_b=sum(1 for r in hi if r['B'])
hi_name=sum(1 for r in hi if r['S']=='Being THE name in my niche'); hi_s=sum(1 for r in hi if r['S'])
u25=[r for r in rows if r['R']=='Under $25K' and r['B']]; u25_follow=sum(1 for r in u25 if r['B']=="People follow me but don't buy")
m1=[r for r in rows if r['R']=='Over $1M' and r['S']]; m1_peers=sum(1 for r in m1 if r['S']=='A room of peers at my level')
creators=[r for r in rows if r['T']=='The Creator' and r['B']]; cr_words=sum(1 for r in creators if r['B']=="I can't put what I do into words")
oneoffer=[r for r in rows if r['B']=='One offer, nowhere for customers to go next' and r['S']]; oo_line=sum(1 for r in oneoffer if r['S']=='A product line that sells without trading hours')

page=f'''<title>The Room, Measured</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{{--brand:#7A12D4;--brand-content:#6810B4;--brand-light:#F6EEFD;--brand-border:#E4D2F8;--brand-dark:#44087A;
--ink:#0F131A;--text:#0F131A;--muted:#595E67;--subtle:#71767F;--bg:#FFFFFF;--surface:#FFFFFF;--grey-100:#F9F9F9;--grey-200:#F3F4F6;--border:#DFE1E5;
--green:#159F65;--green-light:#E8F8F1;--orange:#ED6325;--orange-light:#FFF4E9;--orange-content:#C9541F;
--hero-bg:#0F131A;--hero-text:#FFFFFF;--hero-muted:#CDB2EE;
--sh-light:0 4px 15px rgba(0,0,0,.05);--sh-med:0 5px 20px rgba(0,0,0,.10)}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--brand:#B47CF0;--brand-content:#C99AF5;--brand-light:#22162F;--brand-border:#3D2757;--brand-dark:#E4D2F8;
--ink:#F3F4F6;--text:#F3F4F6;--muted:#B9BEC9;--subtle:#979CA5;--bg:#0F131A;--surface:#161B24;--grey-100:#1B212B;--grey-200:#222937;--border:#2C3441;
--green:#3FCF8E;--green-light:#0F2A1E;--orange:#F5905C;--orange-light:#2E1A10;--orange-content:#F5905C;--hero-bg:#080A0E;--sh-light:none;--sh-med:none}}}}
:root[data-theme="dark"]{{--brand:#B47CF0;--brand-content:#C99AF5;--brand-light:#22162F;--brand-border:#3D2757;--brand-dark:#E4D2F8;
--ink:#F3F4F6;--text:#F3F4F6;--muted:#B9BEC9;--subtle:#979CA5;--bg:#0F131A;--surface:#161B24;--grey-100:#1B212B;--grey-200:#222937;--border:#2C3441;
--green:#3FCF8E;--green-light:#0F2A1E;--orange:#F5905C;--orange-light:#2E1A10;--orange-content:#F5905C;--hero-bg:#080A0E;--sh-light:none;--sh-med:none}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:"Google Sans","Segoe UI",system-ui,sans-serif;background:var(--bg);color:var(--text);font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1120px;margin:0 auto;padding-inline:24px}}
h1,h2,h3,h4{{text-wrap:balance;line-height:1.15;letter-spacing:-.02em}}
h1{{font-size:clamp(34px,5vw,56px);font-weight:700}} h2{{font-size:clamp(24px,3vw,34px);font-weight:700}} h3{{font-size:19px;font-weight:700;line-height:1.3}}
p{{text-wrap:pretty}} .lead{{font-size:18px;color:var(--muted);max-width:68ch}} .body{{color:var(--muted);max-width:68ch}}
.over{{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--brand-content)}}
.hero{{background:var(--hero-bg);color:var(--hero-text);padding-block:64px 72px}}
.hero .over{{color:var(--hero-muted)}} .hero .lead{{color:#E6D8F8}} .hero h1{{margin:12px 0 18px;max-width:20ch}}
.facts{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:40px}}
.qf{{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);border-radius:16px;padding:18px 20px}}
.qf .n{{font-size:30px;font-weight:700;letter-spacing:-.02em;font-variant-numeric:tabular-nums}} .qf .l{{font-size:13px;color:var(--hero-muted);margin-top:4px;line-height:1.4}}
section{{padding-block:56px}} section+section{{border-top:1px solid var(--border)}}
.head{{max-width:820px;margin-bottom:28px}} .head p{{margin-top:10px}}
.grid{{display:grid;gap:18px}} .g2{{grid-template-columns:1fr 1fr}} .g3{{grid-template-columns:repeat(3,1fr)}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px;box-shadow:var(--sh-light)}}
.card h3{{margin-bottom:6px}} .card .body{{font-size:15px}}
.kick{{font-size:12px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--brand-content);margin-bottom:10px}}
.bars{{display:grid;gap:9px;margin-top:14px}}
.bar{{display:grid;grid-template-columns:minmax(150px,40%) 1fr 84px;gap:12px;align-items:center;font-size:14px}}
.bl{{color:var(--text);line-height:1.3}} .bt{{height:12px;background:var(--grey-200);border-radius:4px;overflow:hidden}} .bf{{height:100%;background:var(--brand);border-radius:0 4px 4px 0}}
.bv{{font-weight:700;font-variant-numeric:tabular-nums;text-align:right}} .bv span{{display:block;font-weight:400;font-size:12px;color:var(--subtle)}}
.cap{{font-size:13px;color:var(--subtle);margin-top:10px;max-width:70ch}}
.tbl-scroll{{overflow-x:auto}}
table.heat{{width:100%;border-collapse:separate;border-spacing:0;font-size:13.5px;min-width:640px;border:1px solid var(--border);border-radius:16px;overflow:hidden}}
.heat th{{text-align:left;font-weight:600;padding:10px 12px;background:var(--grey-100);color:var(--muted);font-size:12px;line-height:1.3;vertical-align:bottom}}
.heat tbody th{{color:var(--text);font-weight:600;font-size:13.5px;background:var(--surface)}}
.heat td{{padding:10px 12px;font-variant-numeric:tabular-nums;text-align:right;border-top:1px solid var(--border);background:color-mix(in oklab,var(--brand) calc(var(--a)*55%),var(--surface));color:var(--text)}}
.heat td.n,.heat th.n{{text-align:right;color:var(--subtle);background:var(--surface)}}
.insight{{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:32px;align-items:start;padding-block:32px}} .insight+.insight{{border-top:1px dashed var(--border)}}
.insight .num{{font-size:12px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--subtle);margin-bottom:8px}}
.insight h3{{font-size:22px;margin-bottom:10px}} .insight .body{{font-size:15.5px}}
.big{{font-size:44px;font-weight:700;letter-spacing:-.02em;color:var(--brand);line-height:1;font-variant-numeric:tabular-nums;margin:6px 0 2px}}
.rec{{display:grid;grid-template-columns:56px 1fr;gap:18px;padding:22px 0;border-top:1px solid var(--border)}} .rec:last-child{{border-bottom:1px solid var(--border)}}
.rec .wk{{font-size:12px;font-weight:700;letter-spacing:.06em;color:var(--brand-content);background:var(--brand-light);border:1px solid var(--brand-border);border-radius:12px;padding:8px 6px;text-align:center;line-height:1.25;align-self:start}}
.rec h3{{font-size:18px;margin-bottom:6px}} .rec .body{{font-size:15px}} .rec .ev{{font-size:13px;color:var(--subtle);margin-top:8px}}
.rec .ev b{{color:var(--brand-content);font-weight:700}}
.quote{{border-left:3px solid var(--brand-border);padding:2px 0 2px 14px;font-size:14px;color:var(--muted);font-style:italic;margin-top:10px}}
.callout{{border-radius:16px;padding:22px 26px;background:var(--brand-light);border:1px solid var(--brand-border);color:var(--text);font-size:15px}}
.callout.warn{{background:var(--orange-light);border-color:transparent}} .callout strong{{color:var(--text)}}
.pill{{display:inline-block;font-size:11px;font-weight:700;padding:3px 9px;border-radius:128px;background:var(--grey-200);color:var(--muted);white-space:nowrap}}
.pill.g{{background:var(--green-light);color:var(--green)}} .pill.o{{background:var(--orange-light);color:var(--orange-content)}} .pill.b{{background:var(--brand-light);color:var(--brand-content)}}
footer{{padding-block:32px;color:var(--subtle);font-size:13px;border-top:1px solid var(--border)}}
@media(max-width:900px){{.facts,.g3{{grid-template-columns:1fr 1fr}}.insight{{grid-template-columns:1fr}}}}
@media(max-width:600px){{.facts,.g2,.g3{{grid-template-columns:1fr}}.bar{{grid-template-columns:1fr}}.bv{{text-align:left}}.bv span{{display:inline;margin-left:8px}}.rec{{grid-template-columns:1fr}}.rec .wk{{justify-self:start;padding:6px 10px}}}}
</style>

<header class="hero"><div class="wrap">
  <div class="over">Expert to Authority Quiz · {N:,} responses · 6 to 15 September 2026</div>
  <h1>The Room, Measured</h1>
  <p class="lead">Every answer from the quiz on the summit thank-you page, read as a brief for the Expert &amp; Authority Mastery. Six closed questions are counted exhaustively. The open question, {nq:,} answers in the registrants&rsquo; own words, is coded by theme and quoted directly.</p>
  <div class="facts">
    <div class="qf"><div class="n">{expert/sum(T.values()):.0%}</div><div class="l">call themselves The Expert. Founders {T['The Founder']/sum(T.values()):.0%}, Creators {T['The Creator']/sum(T.values()):.0%}, Established {T['The Established Expert']/sum(T.values()):.0%}</div></div>
    <div class="qf"><div class="n">{nothing/nrev:.0%}</div><div class="l">have never sold anything from their expertise. Another {R['Under $25K']/nrev:.0%} earn under $25K</div></div>
    <div class="qf"><div class="n">{nobody/sum(B.values()):.0%}</div><div class="l">say the thing that breaks is &ldquo;nobody knows I exist&rdquo;</div></div>
    <div class="qf"><div class="n">{ten/sum(NN.values()):.0%}</div><div class="l">have been at their craft for more than ten years. One in three of them has never sold</div></div>
  </div>
</div></header>

<section><div class="wrap">
  <div class="head"><div class="over">The shape of the room</div><h2>Experienced, unseen, and not yet paid for what they know</h2>
  <p class="lead">This is not a beginners&rsquo; room. It is a room of people with a decade of craft and no product, no audience and no price.</p></div>
  <div class="grid g2">
    <div class="card"><div class="kick">Q1 · Which type are you</div>{bars(T,TYPES)}<p class="cap">Answered by {sum(T.values()):,}. &ldquo;The Established Expert&rdquo; is the renamed &ldquo;Stagnating Expert&rdquo;; one legacy response is folded in. A further 447 answered the original Q1 wording before the question was replaced.</p></div>
    <div class="card"><div class="kick">Q2 · How long have you been at it</div>{bars(NN,TEN)}<p class="cap">Answered by {sum(NN.values()):,}. Two peaks: a fifth just starting, a third with more than a decade behind them.</p></div>
    <div class="card"><div class="kick">Q3 · Revenue from expertise, last 12 months</div>{bars(R,REVS)}<p class="cap">Answered by {sum(R.values()):,}. {len(hi):,} people, {len(hi)/nrev:.0%}, earn $100K or more. That is the Guild room, and it is larger than one cohort can hold.</p></div>
    <div class="card"><div class="kick">Q4 · Where it breaks down</div>{bars(B,BRK)}<p class="cap">Answered by {sum(B.values()):,}. The two visibility answers, unseen and unable to say what they do, are {(B['Nobody knows I exist']+B["I can't put what I do into words"])/sum(B.values()):.0%} between them.</p></div>
  </div>
  <div class="card" style="margin-top:18px"><div class="kick">Q5 · Twelve months from now, what would make you say this worked</div>{bars(S,SUC)}<p class="cap">Answered by {sum(S.values()):,}. The product line beats every other definition of success, in every revenue band and every type.</p></div>
</div></section>

<section><div class="wrap">
  <div class="head"><div class="over">Seven insights</div><h2>What the answers say when you cross them</h2><p class="lead">Single counts describe the room. Crossing them describes the rooms inside it, and that is what a curriculum has to be built for.</p></div>

  <div class="insight"><div><div class="num">Insight 1</div><h3>Tenure does not buy revenue. A decade in, a third have still never sold.</h3>
    <p class="body">Of the {vet_n:,} people with more than ten years&rsquo; experience, {vet_nothing:,} have never sold anything from it. Only the under-one-year group is meaningfully greener. This is the whole thesis of the programme in one row: expertise is not the bottleneck, the machine around it is.</p></div>
    <div>{heat(nr,'Tenure',REVS,'Row percentages. Each row is one tenure band; cells are the share of that band in each revenue band. Darker is higher.')}</div></div>

  <div class="insight"><div><div class="num">Insight 2</div><h3>Four types, and they are genuinely different rooms.</h3>
    <p class="body">Creators are the least monetised ({tr['The Creator'][1][0]:.0%} never sold) and the most likely to say they cannot put what they do into words ({cr_words/len(creators):.0%}). Founders are the most likely to have followers who do not buy ({tb['The Founder'][1][2]:.0%}). Established Experts are a different species: {tr['The Established Expert'][1][3]+tr['The Established Expert'][1][4]+tr['The Established Expert'][1][5]:.0%} earn six figures or more and {tb['The Established Expert'][1][3]:.0%} name the plateau, not invisibility, as the problem.</p></div>
    <div>{heat(tb,'Type',BRK,'Q1 against Q4. The Expert and Founder rows are dominated by invisibility; the Established row flips to the plateau.')}</div></div>

  <div class="insight"><div><div class="num">Insight 3</div><h3>The pain moves with the money, in a predictable order.</h3>
    <p class="body">At zero revenue, {rb['Nothing yet'][1][0]:.0%} say nobody knows they exist. Under $25K, &ldquo;people follow me but don&rsquo;t buy&rdquo; jumps to {rb['Under $25K'][1][2]:.0%}, its peak. From $100K up, the plateau takes over and reaches {rb['Over $1M'][1][3]:.0%} above $1M. That is the same left-to-right walk as the curriculum: Be Seen, then Architecture, then Show Up and stay chosen. The sequence is right. The question is whether each stage is weighted for the people actually in it.</p></div>
    <div>{heat(rb,'Revenue',BRK,'Q3 against Q4. Read down the columns: invisibility falls as revenue rises, the plateau rises to replace it.')}</div></div>

  <div class="insight"><div><div class="num">Insight 4</div><h3>Success moves too: first clients, then fully booked, then a product line, then the name.</h3>
    <p class="body">A third of the never-sold want their first paying client. By $25K that collapses to {rs['$25K–$100K'][1][0]:.0%} and &ldquo;fully booked at premium rates&rdquo; peaks at {rs['Under $25K'][1][1]:.0%}. From $100K the answer becomes the product line and the name, and above $1M one in eight wants the room of peers, more than double any other band. The Guild is the right answer for that top band, and the quiz already routes them there.</p></div>
    <div>{heat(rs,'Revenue',SUC,'Q3 against Q5. Success is a ladder in the registrants&rsquo; own answers, and it matches the product ladder the programme teaches.')}</div></div>

  <div class="insight"><div><div class="num">Insight 5</div><h3>In their own words, the biggest ask is a system they can follow.</h3>
    <p class="body">{nq:,} people answered the open question. Two in five ask, in some form, for the how: a roadmap, a structure, a step-by-step, someone to tell them where to start. A third talk about selling, pricing and making an offer. A quarter talk about being seen. Only {TH['Fear, confidence and self-doubt']/nq:.0%} name fear, even though {nobody/sum(B.values()):.0%} chose invisibility as the thing that breaks. People describe the symptom, not the wound.</p>
    <p class="quote">&ldquo;Giving a blueprint or system from start to finish like a dummies version.&rdquo;</p><p class="quote">&ldquo;I know I can but I don&rsquo;t know how to structure a product, an offer, and how to have automatic sales.&rdquo;</p></div>
    <div><div class="card"><div class="kick">Q6 themes · share of {nq:,} open answers · one answer can carry several</div>{bars(TH)}<p class="cap">{uncoded:,} answers ({uncoded/nq:.0%}) matched no theme: single words, a job title, a URL, or a wish too general to code. Coding is keyword-based and was validated against a read sample of about sixty answers.</p></div></div></div>

  <div class="insight"><div><div class="num">Insight 6</div><h3>&ldquo;I&rsquo;m good at what I do, but.&rdquo;</h3>
    <p class="body">{goodat:,} people wrote a version of that sentence unprompted. The recurring vocabulary underneath it is the vocabulary of leverage: without me, trading time, while I sleep, a course, a product. That is the product line answer from Q5, said as a feeling. It is also the strongest possible endorsement of the programme&rsquo;s graduating artefact.</p>
    <p class="quote">&ldquo;How to turn a 1:1 service based business into one that runs without me and makes more revenue than I do now.&rdquo;</p><p class="quote">&ldquo;I&rsquo;m good at what I do but I don&rsquo;t know how to turn my knowledge into money without trading money for hours.&rdquo;</p></div>
    <div><div class="card"><div class="kick">Recurring phrases · mentions in the open answers</div>{bars(collections.Counter(PHC),None,nq)}<p class="cap">Share of the {nq:,} open answers containing the phrase family. Books, speaking and stages appear in one answer in seven, mostly as the thing the person wants to be known for.</p></div></div></div>

  <div class="insight"><div><div class="num">Insight 7</div><h3>The Guild room is already here, and it is {len(hi):,} people.</h3>
    <div class="big">{len(hi):,}</div><p class="body">registrants earn $100K or more. Their problem is the plateau ({hi_plateau/hi_b:.0%}) and their definition of success is the product line or being the name ({(sum(1 for r in hi if r['S']=='A product line that sells without trading hours')+hi_name)/hi_s:.0%} between them). {T['The Established Expert']:,} people picked the Established Expert type, but {sum(1 for r in hi if r['T']=='The Expert'):,} six-figure earners still call themselves The Expert. The type question under-counts the top of the room. Of the {sum(upsell.values()):,} responses the routing has processed so far, {upsell['Guild']:,} were sent to the Guild and {upsell['Mastery']:,} to the Mastery.</p></div>
    <div>{heat(ts,'Type',SUC,'Q1 against Q5. The Established row wants the name and the product line; the Creator row wants first clients and the product line.')}</div></div>
</div></section>

<section><div class="wrap">
  <div class="head"><div class="over">Recommendations</div><h2>How I would strengthen the curriculum from this</h2><p class="lead">Nine moves, each tied to the evidence above and to the week it lands in. None of them changes the spine. The sequence the quiz describes is the sequence Version 3 already teaches.</p></div>

  <div class="rec"><div class="wk">W1<br>to<br>W17</div><div><h3>Make the Authority Blueprint the weekly tracker, not a summit slide.</h3><p class="body">The single largest ask in the open answers is a system to follow, start to finish. The summit shows thirteen Blueprint pieces on Day 1 and promises them finished in the Mastery. Hand every student a one-page Blueprint on Day 1 of Week 1 with the thirteen pieces and the week each is built, and open every Tuesday by marking the next one. It costs one slide a week and answers the question two in five people asked.</p><div class="ev"><b>Evidence</b> · {TH['A system I can follow, start to finish']:,} open answers ({TH['A system I can follow, start to finish']/nq:.0%}) ask for the how · &ldquo;where to start&rdquo; and &ldquo;blueprint&rdquo; named outright by {PHC['where to start, step by step, a blueprint']}</div></div></div>

  <div class="rec"><div class="wk">W14<br>W15</div><div><h3>Give pricing and the ask a full clinic, not a lab afternoon.</h3><p class="body">Pricing and charging appear in the open answers as often as fear, courage and self-doubt combined. &ldquo;Fully booked at premium rates&rdquo; is the second most chosen definition of success and peaks in exactly the band that has started selling and stalled. Ajit&rsquo;s pricing hour on the Week 14 build day should become a named pricing clinic with a price set and defended out loud by every student, and the Week 15 enrolment conversation should end with each student having asked one real person for real money, on tape.</p><div class="ev"><b>Evidence</b> · pricing family {PHC['pricing, charging, premium, worth']} mentions ({PHC['pricing, charging, premium, worth']/nq:.0%}) · &ldquo;fully booked&rdquo; chosen by {S['Fully booked at premium rates']:,} ({S['Fully booked at premium rates']/sum(S.values()):.0%}), {rs['Under $25K'][1][1]:.0%} of the under-$25K band · &ldquo;follow but don&rsquo;t buy&rdquo; peaks at {u25_follow/len(u25):.0%} in the same band</div></div></div>

  <div class="rec"><div class="wk">W14<br>W16<br>W17</div><div><h3>Name leverage as an outcome and audit for it.</h3><p class="body">&ldquo;Without me&rdquo;, &ldquo;trading time&rdquo;, &ldquo;while I sleep&rdquo; is the emotional centre of the open answers, and the product line wins Q5 in every revenue band. Weeks 14 to 17 already build the ladder and the cadence. Add a ten-minute leverage audit to the Week 17 cadence class: for each rung, does it run without you, and if not, what is the one change that would make it. Then say the word on stage. The room used it; the curriculum should too.</p><div class="ev"><b>Evidence</b> · product line is the top success answer in all six revenue bands ({S['A product line that sells without trading hours']/sum(S.values()):.0%} overall) · leverage phrase family {PHC['"without me", "trading time", "while I sleep", "passive"']} mentions · {oo_line/len(oneoffer):.0%} of &ldquo;one offer, nowhere to go next&rdquo; want the product line</div></div></div>

  <div class="rec"><div class="wk">W1</div><div><h3>Put the one-sentence exercise in Week 1, before the first post.</h3><p class="body">One in five chose &ldquo;I can&rsquo;t put what I do into words&rdquo; and it is the Creator&rsquo;s top answer after invisibility. Week 3 names the edge and Week 4 crowns the belief, which is right, but two weeks is a long time to post without a sentence. The onboarding survey already asks for the one sentence. Have Week 1&rsquo;s identity sabbatical end with a rough version of it, so the Week 1 video has words in it, and let Weeks 3 and 4 sharpen rather than invent.</p><div class="ev"><b>Evidence</b> · {B["I can't put what I do into words"]:,} chose it ({B["I can't put what I do into words"]/sum(B.values()):.0%}) · {cr_words/len(creators):.0%} of Creators · clarity theme in {TH['Clarity, niche and putting it into words']:,} open answers</div></div></div>

  <div class="rec"><div class="wk">W9<br>W10</div><div><h3>Send students out of Week 10 with thirty days of posts, not a hook bank.</h3><p class="body">&ldquo;I struggle with what to post, so I&rsquo;m not posting at all&rdquo; is the visibility wound in operational clothing. The summit sells a 30-day content plan built live from one idea. The Mastery should deliver it as the Week 10 artefact: each student leaves the lab with thirty scheduled posts generated from their named method, not a bank of hooks to draw on later. Consistency was named by {PHC['what to post, consistency, showing up']} people as the thing they lack.</p><div class="ev"><b>Evidence</b> · visibility theme {TH['Being seen and growing an audience']:,} open answers ({TH['Being seen and growing an audience']/nq:.0%}) · {nobody:,} chose &ldquo;nobody knows I exist&rdquo; · summit Session &ldquo;The Free Product Content Machine&rdquo; already promises the 30-day plan</div></div></div>

  <div class="rec"><div class="wk">W3<br>W11<br>W12</div><div><h3>Give the Established Experts their own thread, and the Guild bridge earlier.</h3><p class="body">Eight hundred people earn six figures and their problem is not being seen, it is being stuck. For them Weeks 1 and 2 are review, Weeks 3 and 4 (the edge, the belief) are the real work, and Weeks 11 and 12 (the fireside, the long-form advantage) are where they break the plateau. Pod them together from the onboarding survey&rsquo;s revenue question, brief the Week 3 and Week 12 sessions to speak to the plateau explicitly, and put the Guild invitation in front of them in Week 12 rather than at graduation. Above $1M, the peer room is the success answer for one in eight.</p><div class="ev"><b>Evidence</b> · {len(hi):,} at $100K+ · plateau is {hi_plateau/hi_b:.0%} of their Q4 · {m1_peers/len(m1):.0%} of the $1M+ band want peers vs {S['A room of peers at my level']/sum(S.values()):.0%} overall · {sum(1 for r in hi if r['T']=='The Expert'):,} six-figure earners still self-select as The Expert, so the pod cannot rely on Q1 alone</div></div></div>

  <div class="rec"><div class="wk">W5<br>to<br>W8</div><div><h3>Keep the first rung early. It is the proof the job-leavers need.</h3><p class="body">{PHC['leaving a job or employment']} people wrote about leaving employment, and {PHC['a course, programme or digital product']} named a course or digital product as the thing they want to build. Half the room has never sold. Module 2 puts a $49 product live by Week 8 and that is exactly right: the first rung is not a revenue event, it is the moment a person with a job becomes a person with a product. Do not let anything push it later.</p><div class="ev"><b>Evidence</b> · {nothing:,} never sold ({nothing/nrev:.0%}) · {rs['Nothing yet'][1][0]:.0%} of them want their first paying client · course/product named {PHC['a course, programme or digital product']} times</div></div></div>

  <div class="rec"><div class="wk">W16</div><div><h3>Signpost the book and the stage, without teaching them.</h3><p class="body">One open answer in seven mentions a book, speaking, a stage or a podcast. That is Speaking &amp; Influence territory and the three-programme boundary should hold. But the room is telling us where it wants to be known, so the Week 16 Get Booked thread should say so plainly: your book and your talk are rungs on this ladder, here is where they sit, and here is the programme that builds them. A boundary the student can see is a referral. One they cannot see is a disappointment.</p><div class="ev"><b>Evidence</b> · {PHC['a book, speaking, a stage, a podcast']} mentions ({PHC['a book, speaking, a stage, a podcast']/nq:.0%}) · Week 16 already carries a 30-minute Get Booked thread</div></div></div>

  <div class="rec"><div class="wk">W1<br>W2</div><div><h3>Do not add a mindset week. The room named symptoms, and Weeks 1 and 2 already treat the wound.</h3><p class="body">Only {TH['Fear, confidence and self-doubt']/nq:.0%} of open answers name fear, self-doubt or confidence, and {TH['Mindset and old stories']/nq:.0%} name mindset. Yet {nobody/sum(B.values()):.0%} chose invisibility. The gap is diagnostic: people do not experience the visibility wound as fear, they experience it as &ldquo;I don&rsquo;t know what to post&rdquo; and &ldquo;nobody knows I exist&rdquo;. Week 1 names the wound for them and Week 2 gives Marisa the identity shift. That is the right dose. Adding more mindset would be teaching to a complaint the room did not make.</p><div class="ev"><b>Evidence</b> · fear theme {TH['Fear, confidence and self-doubt']:,} answers · mindset theme {TH['Mindset and old stories']:,} · &ldquo;imposter&rdquo; appears {sum(1 for t,r in q if 'impost' in t.lower())} times in {nq:,} answers</div></div></div>
</div></section>

<section><div class="wrap">
  <div class="head"><div class="over">Data hygiene</div><h2>Three things to fix in the quiz itself</h2></div>
  <div class="grid g3">
    <div class="card"><h3>Browser-translated answers split the counts</h3><p class="body">{nonen} responses arrived with the option text in Spanish, Portuguese, German, Italian, Polish, Russian and a dozen others, because the quiz was submitted through a translated browser. The tenure question alone produced forty variant strings. Every figure on this page is normalised, but the Airtable is not. Lock the option values at ingest or map them in a formula field.</p></div>
    <div class="card"><h3>Q1 changed mid-flight</h3><p class="body">447 people answered the original &ldquo;which sounds most like you&rdquo; before it was replaced with the four types, and {N-sum(T.values())-447:,} more answered neither. The four-type question is answered by {sum(T.values())/N:.0%} of the table. If the types drive routing, the old answers need mapping or the routing has a blind spot.</p></div>
    <div class="card"><h3>The type question under-reads the top of the room</h3><p class="body">{sum(1 for r in hi if r['T']=='The Expert'):,} people earning six figures or more still chose &ldquo;The Expert&rdquo;. Revenue is the more reliable signal for routing to the Guild and for podding Established Experts in the Mastery. Treat Q3 as the primary fork and Q1 as flavour.</p></div>
  </div>
  <div class="callout" style="margin-top:18px"><strong>Method.</strong> {N:,} records read in full from the quiz table on 15 September 2026. Closed questions are counted exhaustively after normalising translated option text. The open question was coded with a keyword taxonomy, multi-label, and checked against a read sample of about sixty answers across the four types; {uncoded/nq:.0%} of answers matched no theme and are reported as such. Percentages are of those who answered each question, not of the whole table. {vip} respondents are flagged VIP. Submissions ran from 6 to 15 September, peaking at {max(days.values()):,} on {max(days,key=days.get)}.</div>
</div></section>

<footer><div class="wrap">Expert &amp; Authority Mastery · quiz analysis for the curriculum team · built from the Expert to Authority Quiz 2026 table, base appnHZYcirCg1VqUP</div></footer>
'''
open('quiz-report.html','w').write(page)
print('written', len(page), 'chars')
