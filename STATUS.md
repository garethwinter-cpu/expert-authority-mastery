# Status and held decisions

Internal working file. Not served by any route. Read this first in any new session.
House rules: no fees or compensation on any page or data file (run `python3 scripts/check-no-fees.py`
before every push); push to `main` (auto-deploys) and to `claude/expert-authority-mastery-proposal-3en6ld`;
bump `package.json` on every ship.
Live site: `https://expert-authority-mastery-1f30-jdtcvngavq-as.a.run.app` (Google sign-in). Cloud Run redeploys from `main` in a few minutes.

## AI for Founders Mastery: teacher allocation D (29 Oct 2026, 1.3.35)

- D is committed and in the AIF Airtable base (`app7lhR1V9Fts0mNc`). Order: storefront weeks 1 to 4 (answer hub moved to
  week 4, Ajit), brain 5, inbox 6, brand and funnel 7 to 9, content 10 and 11, Meta ads 12, then finance, sales, cockpit as before.
  Teachers: Vishen 1 (opens), 2, 7, 8, 16; Vykintas 1, 3, 5, 9, 11, 17 and every lab; Noelle 6 and 15 (weeks 3 and 6 swapped 29 Oct after Marta and Marijana's feedback; Ajit kept on content); Ajit 4 and 10; Marisha 12;
  Sara and Tyler 13; Joe 14; Vishen and Vykintas host graduation and the fast action bonus call (Wed 4 Nov, 7am PT).
  Get AI-Ready 1 and 2 are pre-recorded.
- `scripts/aif/aif_modules.json`, `build_aif.py`, the survey, the front door, the pack, positioning and the proposal's led-by
  line all follow D. No Vishen clash with Expert & Authority.
- The static repo `garethwinter-cpu/ai-founder-mastery` builds its own student-facing `curriculum.html` from an Airtable
  snapshot (`scripts/build_curriculum.py` there); `export_static.py` ships only the front door, the pack and the data.
- Open: the Schedule table's Year tag reads 2025; spare slots 36 and 37 after graduation.

## Expert & Authority Mastery: held decisions (updated 21 Oct 2026)

Proposed by Gareth to the team, Marta and Marijana. Both items are applied in Airtable (John Lee 8 Oct, Regan 21 Oct). Airtable is the source of truth: base `appnHZYcirCg1VqUP`, Lessons table.
Cadence rule: lessons on Tuesdays, workshops on Fridays, 9am PT. Vishen does not teach Fridays.

### 1. John Lee: both his weeks in January (confirmed by his team, 8 Oct) — APPLIED in Airtable 8 Oct

John's team confirmed Tue 5 Jan, Fri 8 Jan, Tue 12 Jan and Fri 15 Jan (Marta, 8 Oct). He teaches
both lessons and runs both workshops himself, live. This replaces the 5 Oct three-way rotation.

Edits, all in the Slot column of the Lessons table:

| Row | Slot now | Change to | New date |
|---|---|---|---|
| Content Machine (John Lee) | 11 (2026) | 23 (2026) | Tue 5 Jan |
| Workshop, Content Machine (John Lee) | 12 (2026) | 24 (2026) | Fri 8 Jan |
| Platforms, Reels & Algorithmic Growth (John Lee) | 13 (2026) | 25 (2026) | Tue 12 Jan |
| Workshop, Platforms (John Lee) | 14 (2026) | 26 (2026) | Fri 15 Jan |
| Speaking & Stages (Vishen) | 29 (2026) | 11 (2026) | Tue 10 Nov |
| Workshop, Speaking (Vykintas) | 30 (2026) | 12 (2026) | Fri 13 Nov |
| Email Marketing (Vishen) | 23 (2026) | 13 (2026) | Tue 17 Nov |
| Workshop, Email (Vykintas) | 24 (2026) | 14 (2026) | Fri 20 Nov |
| Membership, Continuity & Superfans | 25 (2026) | 29 (2026) | Tue 26 Jan |
| Workshop, Membership (Vykintas) | 26 (2026) | 30 (2026) | Fri 29 Jan |

Applied and audited 8 Oct (all 36 slots: one lesson each, Tuesdays lessons, Fridays workshops, Vishen Tuesdays only,
every workshop follows its own lesson, nothing 21 Dec to 3 Jan). Rollback values: `data/airtable-backups/2026-10-08-john-lee-swap.json`.
Also done: John's four rows Checking to Confirmed; Module on the Speaking and Email rows (lesson and
workshop) to Pillar 2; check slots 11 to 14, 23 to 26, 29 and 30 each hold exactly one lesson.
Vykintas moves from Fri 8 and 15 Jan to Fri 13 and 20 Nov: confirm with him.

Why this order: Speaking (a platform) and Email (the audience you own) join Pillar 2 in November;
Email on 17 Nov builds the list that Daniel's Oversubscribed waitlist lesson needs on 24 Nov.
Watch: Vishen teaches no lessons in January (John, John, Ajit, Regan); his next is Tue 2 Feb.

### 2. Regan Hillyer: her own lesson, Tue 26 Jan — CONFIRMED and APPLIED 21 Oct

Regan's team confirmed on 20 Oct (via Marijana): Tue 26 Jan 2027, 9am Pacific / 5pm London, Zoom, 90 min
(60 min content + 30 min Q&A). She teaches **Membership, Continuity & Superfans: Build Revenue That Renews Itself**
on her own (not a fireside). Vishen's title and outline are kept; her team's working title was "Membership,
Continuity & Super Fans: Build a Community That Stays".

Applied in the E&A base: Regan Hillyer added to Speakers (Lessons) (`recaRF6roiUewECIP`: Confirmed, Zoom email,
photo); she replaces Vishen on the Membership lesson, now Confirmed, with the confirmation in Internal Notes; the
Fri 29 Jan workshop description now reads "Regan's lesson". Page snapshot refreshed and live.

Not done (no edit access): her row in the Author Relations base (Author x Event, `recNpgTpDftiJxZ5Z`) still has
Speaking Slot Confirmed and Sessions blank. Those fields sync into the E&A Speaker Engagements table, so Marta or
Marijana set them at source. Her Speakers record has no Mastery Unique link (Zoom panelist link) yet.

### Other E&A state

- Marisha Lakhiani: Confirmed, Paid Advertising workshop Fri 4 Dec and Funnel Design workshop Fri 11 Dec.
- No Thanksgiving break (2025 data showed no drop). Christmas break 21 Dec to 3 Jan; graduation Tue 23 Feb.
- `data/curriculum.json` is the 23 Sep snapshot and is stale (it predates the no-Thanksgiving-break calendar and Marisha's two
  workshops); refresh with `scripts/sync-curriculum.js`. Note that script writes `slot` as null; see the AIF load-panel note below.
- `AIRTABLE_TOKEN` is not set on Cloud Run yet, so the live page serves the snapshot.

## AI for Founders Mastery: the curriculum rebuilt on Vykintas's draft v4 and Jaideep's deck (14 Oct, 1.3.24)

- **Reordered later on 14 Oct (1.3.26), Vykintas on WhatsApp:** the inbox needs the brain's context to prioritise and
  draft, and week 8 was too late for later lessons to build on the brain; he asked for the brain in lesson 3 to 5. Now:
  1 Storefront (1 to 3), 2 Company brain (4), 3 Operations, the sorted inbox (5), 4 Brand and funnel (6 to 8), then
  Traffic 9 to 12, Finance 13, Sales 14 and 15, Cockpit 16 to 18 as before. The inbox still lands before the Christmas
  break (15 and 17 Dec). Survey questions 8 to 10, the front door diagram and the hub chapter follow the new order.
  The shape line below describes the first 1.3.24 order.
- **Decisions (Gareth, 14 Oct, on Jaideep's decision deck):** seventeen lessons plus a graduation, eighteen calls, as
  agreed in the call; inbox triage in week 4 on condition that weeks 1 to 3 leave it the offer book, the copy and the
  voice file, and that its lab carries the longest privacy segment; hosting in onboarding with a go-live clinic; the
  deck's ending (owner pages, a test week, graduation and Demo Day); Meta ads kept in the core so paid and organic are
  both taught (Marisha). Software building is an elective (deck), format undecided.
- **Shape:** 1 Storefront (weeks 1 to 3: website, offer and pricing, copy plus voice file), 2 Operations (week 4 sorted
  inbox), 3 Brand and funnel (5 to 7), 4 Company brain (8), 5 Traffic (9 to 12: AI search, a month of content, weekly
  content, Meta ads), 6 Finance (13 bookkeeping agent), 7 Sales (14 and 15), 8 Cockpit and handover (16 dashboard, 17
  owners and the week you only decide, 18 graduation). Every lesson carries Vykintas's AI team (`team`: dept, head,
  members, scheduled flags). Week 0 onboarding is optional, under two hours, with the hours log; the week 1 lab is the
  safety net for hosting, the tracking pack and the hours log.
- **Calendar:** Tue 17 Nov 2026 to graduation Tue 30 Mar 2027, 7am Pacific. London is 2pm from 16 to 25 March (weeks 16
  and 17, notes on each session) and 3pm again at graduation. The Monday 16 Nov opening is folded into week 1 (Vishen
  opens for about twenty minutes); Vishen has two Mastery sessions, week 1 and graduation. Thanksgiving is the week 2 lab.
- **Pages:** one curriculum page (AI team box on every lesson, week 0 block, how every week runs, the stack, electives,
  "What changed on 14 October"); front door diagram redrawn for the new departments; pack outline lists each lesson's AI
  team, and the pack's changelog card is marked "for the team, not for the community". Survey questions 8 to 10 and the
  intro now name the new modules and week 4. Hub chapter, positioning row and boundary data say 17 lessons + graduation.
- **Bug fixed in the diary check:** the E&A snapshot refreshed from Airtable on 14 Oct already carries the John Lee
  rotation and Marisha's workshops; the build was re-applying the rotation (Vishen's Membership lesson moved to 17 Nov,
  Vykintas counted twice on 20 Nov) and was placing E&A sessions at 7am instead of 9am Pacific since the 7 Oct slot
  change. Now it trusts the snapshot's times and keeps only the Regan Hillyer overlay. Result: no clashes.
- **Open, needs Airtable or a person:** the summit's Day 2 offer session is still titled "Your Business, Rebuilt in 16
  Weeks" in the AIF base (flagged on the front door; not edited, base is read-only until Vishen aligns); the elective's
  format; Vishen's twenty minutes on 17 Nov sit two hours before his E&A Email Marketing lesson; teachers for the 15
  unassigned lessons, five or six at most; whether the community survey goes out before or after this version.
- **Static mirror (14 Oct, Gareth: flush it and fill it with this):** `garethwinter-cpu/ai-founder-mastery` now holds only
  the current curriculum as a static site (index, curriculum, pack, JSON, headshots, favicons, wellness.css); the August
  proposal is gone from the tree but kept in its history. Refresh it with `scripts/aif/export_static.py <clone>` after
  every build. Links to the proposal, positioning and E&A point at the live site, which needs Google sign-in.
- Audit scripts used: data audit (counts, Tuesday/Thursday pairing, 7am PT, break, London-hour notes, decisions, wording)
  and a render audit (six pages at 1280 and 390 px, script errors, overflow, diagram labels, links, redirect, API).

## AI for Founders Mastery: version two of the curriculum (14 Oct, local build, awaiting Gareth's review before push)

- **What changed.** The order now follows a customer's journey: 1 Front door (weeks 1–2: website live on Thursday of
  week 1; brand voice then funnel in week 2), 2 Marketing engine (3–4: answer, amplify, ask; AEO articles on
  the founder's own site, each cut into carousels, posts, reels and a newsletter; both routes to traffic, organic and
  one ad attached to a sale), 3 Sales (5–6), 4 Company brain (7–8, once its absence is felt; Monday page v1 in week 8),
  5 Operations and delivery (9–10, Automation Hub page), 6 Team: people and AI (11–12), 7 Finance and the founder's
  cockpit (13–14, dashboard that recommends), 8 Product and scale (15 the week you only decide, 16 Demo Day). The
  word certification is retired. Every lab runs one fixed format (`lab_format`) with a pre-recorded twin. Get AI-Ready
  is optional and pre-recorded with two drop-in calls (`onboarding`). The load map is homework from the Monday opening.
  Week 1 installs two reusable skills, copywriting and website building. The full list is `changelog` in
  `scripts/aif/aif_modules.json` and renders on the curriculum, outline and pack pages.
- **Sources.** Team call 14 Oct (Marisha, Vykintas, Gareth: website before sales page; copywriting and website skills;
  brand voice before funnel; AEO; write once and cut into carousels, posts and ads (our own three-move frame, answer, amplify, ask, rather than a borrowed one); show ads and content but stay one lesson on
  producing content, not a social media programme), Jaideep's curriculum review (14 Oct), Vykintas's proposals (5 and
  8 Oct), the quiz (907 rows).
- **Authors (28 Oct, Gareth: put the teacher map into Airtable and align).** From the teacher map of 21 Oct: Vykintas
  weeks 1, 3, 4, 8, 10, 11, every lab and both drop-ins; Vishen opens week 1 and teaches 2, 6, 7, 9, 15, 16; Noelle 5
  and 17; Marisha 12; Sara Davison and Tyler Fisk 13; Joe Stolte 14; Vishen and Vykintas co-host graduation. Teachers
  now show on the curriculum page. AIF Airtable base: 9 Modules created, Lessons 1 to 35 filled (title, teacher, type,
  status, 90 min, module, description, reason in Internal Notes), two drop-in slots added (0.1 and 0.2), slots 36 and
  37 (1 and 6 April) labelled spare, not deleted. Open in Airtable: every Schedule slot carries Year 2025 and the
  "2026 | Schedule" view filters on 2025; the Fast Action Bonus Call (slot 0) has no date.
- **Jaideep's framework diagram** is kept and redrawn as inline SVG on the front door (`#framework`, figure with
  caption): company brain at the centre, AI workspace and Automation Hub ring, six engines in build order with their
  weeks, labelled flow arrows, dashed spokes for reads and writes, the founder at the bottom (Monday page down,
  decisions up). Week numbers on the blocks are the only addition to his structure.
- **One curriculum page, no outline (14 Oct, Gareth: "just one").** `/ai-founders/outline` 301s to
  `/ai-founders/curriculum`; `ai-founders-outline.html` is deleted; the dated/outline toggle tried in 1.3.21 is gone.
  The curriculum page is the single view: dates, briefs, labs and wins, with teachers switched off until 28 Oct (now shown) (`.who` hidden, no
  teachers count, hero and banner say teachers are mapped once the curriculum is settled). The home page module cards
  list the week's lesson titles instead of teacher chips. The pack keeps its outline tab because it is the marketing
  artefact. Authors are mapped later, by Gareth's instruction.
- **Week 3 renamed (14 Oct, Gareth).** "Short form, long form, lead form" is Daniel Priestley's framework and he is not
  on this programme, so the lesson is now "Write It Once. Get Found Everywhere." with our own three moves: answer
  (articles on your site that answer what buyers ask, AEO), amplify (each article cut into carousels, posts, reels, a
  newsletter), ask (every piece points at the funnel).
- Pushed 14 Oct as 1.3.20 (version two) and 1.3.21 (outline merge, week 3 rename). Push goes to `main` and the proposal branch; bump to 1.3.20;
  then rebuild the pack artefact fragment and republish https://claude.ai/artifact/TSVY9rk4uHY7VRXzT9SDMG.

## AI for Founders Mastery: state after the 5 Oct session (second pass)

- Draft page `/ai-founders`, rendered from `data/ai-founders-curriculum.json` (mode draft, not aligned). Rebuild with
  `python3 scripts/aif/build_aif.py`. All copy lives in `scripts/aif/aif_modules.json` (eight modules, the calls, the
  teacher map); the E&A calendar for the load panel is in the script's `EA_OVERLAY` (see "The load panel" below).
- Routes live under one namespace. `/ai-founders` is the **front door** (`ai-founders-home.html`: calendar, the eight
  modules with their teachers, who it is for, the promise, the boundary against AI Mastery, the people, links to every
  AIF page). `/ai-founders/curriculum` is the dated draft. `/ai-founders/proposal` is the August proposal (deep links
  `#programme`, `#programme-w5`, `#authors` intact), `/ai-founders/guild` the Guild, `/api/ai-founders` the JSON. Both
  pages render the same JSON on every request, so they cannot disagree. The old flat routes 301. Same repo, same
  Cloud Run service: the anti-drift architecture (shared authors, boundary, learnings, design system) is the reason not
  to split. A separate hostname later is a Kessel domain mapping, not a code change. The old
  `garethwinter-cpu/ai-founder-mastery` repo (last pushed 20 Aug) should be archived with a pointer here; it could not be
  opened this session.
- The hub (`/`) chapter for AI for Founders was updated to the rebuild (16 weeks, eight modules, Vishen with Vykintas,
  the placed roster, Priestley off). Its pricing lozenge still reads the August figure and the brief proposes a
  different one; left for Vishen to lock, not changed here.
- Do not seed the AIF Airtable base (`app7lhR1V9Fts0mNc`) until Vishen has aligned. Reading it is fine: the quiz, summit
  agenda and speaker tables were read on 5 Oct. Seeding later is a copy of the JSON, same schema as E&A.
- Sources absorbed 5 Oct: Jaideep's launch brief (claude.ai artifact, ten tabs), Vykintas's curriculum proposal
  (Google Doc `1PY6N7uNqGRWk7Rh540IDIqNFrDyKDhXCxntHrOEvlvg`), the AI for Founders quiz (812 rows, 669 written answers),
  the AIF Summit Agenda (36 rows, already tagged M1 to M8) and Speaker Engagements.

### The curriculum as rebuilt 5 Oct

Vykintas's eight modules, two weeks each, lesson Tuesday and lab Thursday at 7am PT, 3pm London (hour set by Janja 7 Oct; Gareth, 5 Oct: two sessions a week,
same as E&A). Opening Monday 16 November with Vishen (the brief's start date). Weeks run Tue 17 Nov to Thu 18 Mar, break
21 Dec to 3 Jan. Get AI-Ready calls Thu 5 Nov and Thu 12 Nov in the sales window. 35 live sessions. Office hours and
the alumni reunion were removed on 7 Oct (Gareth): Vishen's diary cannot carry extra calls, and post-graduation
continuity is the Guild's job.

| Module | Weeks | Lessons |
|---|---|---|
| 1 Strategy: find the bottleneck | 1 to 2 | Vykintas (load map), Nate Herk (what to hand to AI first) |
| 2 Company brain | 3 to 4 | Vykintas (the brain), Noelle Russell (governance, data safety) |
| 3 Marketing | 5 to 6 | Sabrina Ramonov (one-person marketing team), Ruben Hassid (content to a list) |
| 4 Sales | 7 to 8 | Liam Ottley (the lead that never goes cold), Nick Saraev (outbound) |
| 5 Operations and delivery | 9 to 10 | Noelle Russell (delivery agents), Nate Herk (operations brain) |
| 6 Team: people and AI | 11 to 12 | Callan Faulkner (first AI employees), Alex Dogliotti (how Mindvalley's team works with agents) |
| 7 Finance and the cockpit | 13 to 14 | Shawn Kanungo (finance cockpit), Vishen (the orchestrator's week) |
| 8 Product and scale | 15 to 16 | Matt Gray (founder operating rhythm), Vishen + Vykintas (graduation) |

Teacher placement rule: each guest sits where they are most authentic against the module's problem, from the names on
Gareth's 5 Oct screenshot (In consideration: Natalie Ellis, Alex Dogliotti, Sabrina Ramonov, Ruben Hassid, Nick Saraev,
Nate Herk, Oren John, Dave Katague, Liam Ottley, Matt Gray; Outreach done: Callan Faulkner). Alternates and the not-placed
list, with reasons, are on the page and in `aif_modules.json` under `roster`. Airtable showed Not Approved for Matt Gray,
Dave Katague, Ruben Hassid, Oren John and Alex Dogliotti at 16:40 UTC on 5 Oct; the screenshot shows In consideration, so
the screenshot is treated as current. Nobody is confirmed for the Mastery.

Still open on the curriculum:
- Vishen alignment, then the Airtable seed.
- Shawn Kanungo is Can't make it for the summit; the Mastery date (Tue 23 Feb) is a separate ask. Callan Faulkner may
  decline; Week 11 is written so a substitute can take it.
- Dave Katague is placed as an alternate on his Airtable title only; nothing else verified.
- The promise line. The brief keeps "Your business scales beyond you" for the offer; Vykintas rules out "runs without
  you" and "fully automated". The page uses Vykintas's list of what we can and cannot promise (notes). The summit agenda's
  Day 3 "founder-free week" sits on the wrong side of that line; flag to Jaideep.
- Daniel Priestley: out of this draft. `/ai-founders/proposal` keeps its August header as history, under a banner that
  says the curriculum it describes was superseded on 5 Oct.

### Decided 5 Oct (the three items held over from the last session)

1. **Cadence stays Tuesday lesson / Thursday lab.** AIF does not match E&A's Tuesday / Friday. Vykintas leads every AIF lab
   and, after the John Lee rotation, holds eight E&A Friday workshops at 9am PT inside the AIF run (20 and 27 Nov, 18 Dec,
   8 and 29 Jan, 5, 12 and 19 Feb). A Friday lab would double-book him on each.
2. **The Thanksgiving lab stays, Thu 26 Nov** (now Week 2). Same logic as E&A: 2025 data showed no attendance drop over
   Thanksgiving week, so E&A kept Fri 27 Nov (live Airtable: slot 16, Vykintas). Caveat on the page: the evidence covers
   the week, not the day.
3. **Load panel recomputed** against the E&A calendar as it stands plus the held decisions. After the rebuild and the 7 Oct
   removals: Vishen 13 E&A + 3 AIF live sessions, Vykintas 12 + 22, Vykintas peaks at 4 in a week (1 such week). **No same-hour double
   bookings** for either: the Monday opening keeps Vishen clear of his E&A Speaking lesson on Tue 17 Nov (post-rotation),
   his other AIF dates (2 and 16 Mar) fall after E&A ends.

### The load panel: how it is computed

`build_aif.py` does not trust the snapshot's dates. It derives each E&A session's date from its slot (slot 1 = Tue 6 Oct;
odd slots Tuesday, even slots the Friday of the same week; 9am PT; no sessions on 22 and 29 Dec), which reproduces all 37
dated rows in live Airtable exactly (checked 5 Oct). Titles, types and speakers come from the snapshot, then `EA_OVERLAY`
applies what the snapshot has not caught up with: Marisha on slots 18 and 20 (already in Airtable), the John Lee rotation
(13→25, 14→26, 29→13, 30→14, 25→29, 26→30) and Regan on Membership (held). Every overlay row applies only while the
snapshot still shows the old state, so refreshing the snapshot makes it a no-op. `sync-curriculum.js` currently writes
`slot` as null (`lib/curriculum.js`), so a refreshed snapshot falls back to its own dates; restore slot resolution there
before the next refresh.

### Decisions, 7 Oct (Gareth)

- **Office hours and the alumni reunion removed** from the Mastery (Vishen's diary; what follows graduation is a separate
  conversation).
- **The Guild is not mentioned on the Mastery pages** for now: no nav link, no card, no "belongs in the Guild" wording.
  The Guild page and its route are untouched, as is the Guild panel on the hub; both are another project, to be rebuilt
  in once there is clarity.
- **Price follows the launch brief**: the hub lozenge reads $6,999, proposed, for Vishen to lock.
- **"Run on AI" stays as the promise line** (not the summit name).
- **The artefact is named: the Founder Operating System** (company brain, marketing and sales engines, delivery and
  operations agents, the founder's cockpit). Used on the front door, the curriculum, the boundary and the brief. Change
  it later if the team does; use it consistently until then.
- **Start date clarified**: the programme starts at Vishen's opening on Monday 16 November; the curriculum hero now says
  so. Get AI-Ready (5 and 12 Nov) sits before it, in the sales window.
- **Consistency sweep**: `data/boundary.json` AIF card rewritten to the current programme and re-rendered into the
  proposal and positioning pages; `scripts/build_boundary.py` re-pointed at `ai-founders-proposal.html` (it still
  targeted the retired E&A proposal and the old `/ai-founders` page, and would have failed); the August proposal
  carries a superseded banner; `CURRICULUM-BRIEF.md` and `data/authors.json` no longer describe Priestley as co-owner;
  the orphan `live.html` (an unserved old copy of the hub) deleted.
- **Time slot, set 7 Oct: 7am Pacific, 3pm London** (2pm London in the final week, 16 and 18 March). Janja set it for team
  capacity and schedule. `briefs/AIF-TIME-SLOT-EVIDENCE.md` holds the attendance pull from five Mastery bases: the hour
  does not move live turnout between 7am and 10am Pacific, so the change costs nothing; the earlier 9am preference was
  about the North American majority's comfort, not attendance. Build, pages, slot object and Week 16 flags updated.
- **Summit speaker record, 7 Oct** (summit, not Mastery): Confirmed Vishen, Noelle Russell, Vykintas, Jason Goldberg.
  Outreach done Sabrina Ramonov, Callan Faulkner, Liam Ottley. In consideration Nick Saraev, Nate Herk. Not approved
  Natalie Ellis. Can't make it Daniel Priestley, Shawn Kanungo. Roster statuses in `aif_modules.json` updated to match.
- **Thanksgiving, checked against the day (7 Oct)**: AI Mastery 2025 showed no dip the day before or after; the one
  session on Thanksgiving Day itself (Entrepreneurship Mastery) kept about 70 percent of its room and its recording was
  the month's most watched Thursday. The Thu 26 Nov lab stays, flagged on both pages; Wed 25 Nov is the alternative.
  WhatsApp summary in the brief.
- **Curriculum Outline (7 Oct)**: new tab `/ai-founders/outline` for the co-creation survey invite: module, lesson, lab and
  a one-line teacher-free brief per lesson (`brief` field in `aif_modules.json`), no dates, no times, no names. The build
  also writes `briefs/AIF-CURRICULUM-OUTLINE.md` for pasting into the email. Survey link is a placeholder until the form exists.
- **Co-creation pack (7 Oct)**: `/ai-founders/pack` and a published artefact for marketing: the outline, a 20-question survey
  (`scripts/aif/aif_survey.json`, with why-we-ask lines, design notes and the analysis plan) and the two emails
  (`scripts/aif/aif_emails.json`: Vishen's 12 Oct email, then Gareth's survey email). Dates in the pack's sequence strip
  (12 Oct, v2 by 26 Oct) are proposed. Survey tooling and the responses table wait on Vishen's alignment.
- **Summit agenda on the front door (14 Oct)**: `/ai-founders` now shows the three summit days from a snapshot of the
  Airtable Summit Agenda table (`scripts/aif/summit_agenda.json`, read 14 Oct; Airtable stays the source of truth). The
  agenda changed since 7 Oct: new Vishen sessions (Your Voice Made Executable, From Idea to Launch in a Day, Sell Without a
  Single Sales Call, The AI-Powered CEO), Joe Stolte and Sara Davison with Tyler Fisk added, Sabrina and Nick gone, Callan's
  session retitled, The Orchestrator's Week is now the Day 3 offer. Four data flags listed on the page. Jaideep's curriculum
  review artefact (14 Oct) is a static Claude page, not linked to Airtable or this repo; feedback given in chat, nothing actioned.
- **Still open**: the Guild page itself still says 18 weeks, five pillars and Priestley.

### Storyboarding call, 6 Oct (Vishen, Jaideep, Ramya, Marijana, Ishaan, Chee Ling, Wendy, Gareth)

- **Summit name is AI for Founders Summit.** Vishen rejected "Run on AI: The Founders Summit" outright. The data and
  front door now carry the confirmed name; "Run on AI" survives only as the programme's promise line.
- **Co-creation is the launch mechanic.** Vishen wants total openness: publish a rough curriculum covering both the summit
  and the Mastery, invite the community to a feedback survey (what is missing, where to go deeper, which teachers), then
  publish version two with their input. Modelled on the 2015 Silva "co-create with us" launch. Gareth: the front door
  and curriculum are that rough draft; a feedback form is the next build.
- **Survey template.** Vishen asked Gareth for a reusable audience-survey model that serves curriculum design as well as
  marketing: where they are, how they want to grow, what they want changed, biggest needs, and what they do not know
  they should know. Jaideep: a second, deeper quiz runs at summit registration, as E&A did.
- **Email, Monday 12 Oct.** Vishen asked Gareth to help Ramya write a community email: thank the Expert & Authority
  community (Mastery sold out), announce the AI for Founders Summit, say a survey is coming, and start positioning Gareth
  as the curriculum and content designer the community recognises (photo of Vishen, Gareth, Jaideep). Draft in the
  session notes of 6 Oct.
- **Leads.** The 36 quiz takers at $1M+ get a nurturing call, not a sales push (Vishen, with Tom). The Guild launches
  alongside.
- **Speakers.** Confirmed for the summit as of the call: Vishen, Vykintas, Noelle. Marijana aims for 14 Oct for the rest;
  social promotion starts 16 or 17 Oct; Vishen's eight UGC videos need a diary slot around his Austin travel.
- **Curriculum finalisation** is wanted this week (Jaideep).

### Still open against E&A

- The onboarding survey (`ONBOARDING-SURVEY.md`, F2) still says "Tuesday teach, Thursday build day" for E&A, which now
  runs Tuesday / Friday.
