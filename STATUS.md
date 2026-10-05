# Status and held decisions

Internal working file. Not served by any route. Read this first in any new session.
House rules: no fees or compensation on any page or data file (run `python3 scripts/check-no-fees.py`
before every push); push to `main` (auto-deploys) and to `claude/expert-authority-mastery-proposal-3en6ld`;
bump `package.json` on every ship.

## Expert & Authority Mastery: held decisions (5 Oct 2026)

Proposed by Gareth to the team, Marta and Marijana. **Not yet applied to Airtable.** Apply only when
Gareth confirms the dates. Airtable is the source of truth: base `appnHZYcirCg1VqUP`, Lessons table.
Cadence rule: lessons on Tuesdays, workshops on Fridays, 9am PT. Vishen does not teach Fridays.

### 1. John Lee: three-way rotation

John cannot do his November dates. Pre-recording is not done for Mastery. He can do Tue 12 Jan
and Fri 15 Jan (Marta corrected the dates on 5 Oct: not 5 and 8 Jan).

Edits, all in the Slot column of the Lessons table:

| Row | Slot now | Change to | New date |
|---|---|---|---|
| Platforms, Reels & Algorithmic Growth (John Lee) | 13 (2026) | 25 (2026) | Tue 12 Jan |
| Workshop, Platforms (John Lee) | 14 (2026) | 26 (2026) | Fri 15 Jan |
| Speaking & Stages (Vishen) | 29 (2026) | 13 (2026) | Tue 17 Nov |
| Workshop, Speaking (Vykintas) | 30 (2026) | 14 (2026) | Fri 20 Nov |
| Membership, Continuity & Superfans | 25 (2026) | 29 (2026) | Tue 26 Jan |
| Workshop, Membership (Vykintas) | 26 (2026) | 30 (2026) | Fri 29 Jan |

Then set Module on both Speaking rows to Pillar 2, and check that slots 13, 14, 25, 26, 29 and 30
each hold exactly one lesson.

Still open: John's second lesson, Content Machine (Tue 10 Nov / Fri 13 Nov). Marta's message with
his further dates was cut off. If he has any Tuesday, swap that week the same way and Vykintas runs
the Friday. If not, Vishen teaches it and John teaches one lesson.

### 2. Regan Hillyer: her own lesson, Tue 26 Jan

Regan teaches **Membership, Continuity & Superfans: Build Revenue That Renews Itself** on her own
(not a fireside). Vishen's title and outline stay exactly as written; the description never names
Vishen, so the only Airtable change is the Speaker field. 90 minutes. Workshop stays with Vykintas
(Fri 29 Jan). The date assumes the John Lee rotation above; without it the lesson is Tue 12 Jan.

To apply: add Regan Hillyer to the Speakers (Lessons) table (name, Zoom email, photo), replace Vishen
with Regan on the Membership lesson, keep status Proposed until she confirms, and fill the slot and
session fields on her Speaker Engagements row (she is already Confirmed there for E&A Oct 2026).

Conditions: her team shares real examples of recurring revenue, community and retention; Vishen
signs off (he cut her standalone fireside on 17 Sep). Second choice if she has no recurring product:
Speaking & Stages. Funnel Design (Tue 8 Dec) only if 8 Dec is her sole available date.

### Other E&A state

- Marisha Lakhiani: Confirmed, Paid Advertising workshop Fri 4 Dec and Funnel Design workshop Fri 11 Dec.
- No Thanksgiving break (2025 data showed no drop). Christmas break 21 Dec to 3 Jan; graduation Tue 23 Feb.
- `data/curriculum.json` is the 23 Sep snapshot and is stale (it predates the no-Thanksgiving-break calendar and Marisha's two
  workshops); refresh with `scripts/sync-curriculum.js`. Note that script writes `slot` as null; see the AIF load-panel note below.
- `AIRTABLE_TOKEN` is not set on Cloud Run yet, so the live page serves the snapshot.

## AI for Founders Mastery: state after the 5 Oct session (second pass)

- Draft page `/ai-founders`, rendered from `data/ai-founders-curriculum.json` (mode draft, not aligned). Rebuild with
  `python3 scripts/aif/build_aif.py`. All copy lives in `scripts/aif/aif_modules.json` (eight modules, the calls, the
  teacher map); the E&A calendar for the load panel is in the script's `EA_OVERLAY` (see "The load panel" below).
- Routes now live under one namespace: `/ai-founders` (curriculum), `/ai-founders/proposal` (the August proposal, deep
  links `#programme`, `#programme-w5`, `#authors` intact), `/ai-founders/guild`, `/api/ai-founders`. The old flat routes
  301 to these. Same repo, same Cloud Run service: the anti-drift architecture (shared authors, boundary, learnings,
  design system) is the reason not to split. A separate hostname later is a Kessel domain mapping, not a code change.
  The old `garethwinter-cpu/ai-founder-mastery` repo (last pushed 20 Aug) should be archived with a pointer here; it could
  not be opened this session.
- Do not seed the AIF Airtable base (`app7lhR1V9Fts0mNc`) until Vishen has aligned. Reading it is fine: the quiz, summit
  agenda and speaker tables were read on 5 Oct. Seeding later is a copy of the JSON, same schema as E&A.
- Sources absorbed 5 Oct: Jaideep's launch brief (claude.ai artifact, ten tabs), Vykintas's curriculum proposal
  (Google Doc `1PY6N7uNqGRWk7Rh540IDIqNFrDyKDhXCxntHrOEvlvg`), the AI for Founders quiz (812 rows, 669 written answers),
  the AIF Summit Agenda (36 rows, already tagged M1 to M8) and Speaker Engagements.

### The curriculum as rebuilt 5 Oct

Vykintas's eight modules, two weeks each, lesson Tuesday and lab Thursday at 9am PT (Gareth, 5 Oct: two sessions a week,
same as E&A). Opening Monday 16 November with Vishen (the brief's start date). Weeks run Tue 17 Nov to Thu 18 Mar, break
21 Dec to 3 Jan. Get AI-Ready calls Thu 5 Nov and Thu 12 Nov in the sales window. Office hours Fri 4 Dec, 15 Jan, 26 Feb,
12 Mar. Alumni Thu 29 Apr. 40 live sessions, 59 hours.

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
- Daniel Priestley: the brief says he cannot be on both E&A and AIF, Airtable says Can't make it. He is out of this draft
  and out of the proposal's co-owner framing; `/ai-founders/proposal` still carries the August "Vishen × Daniel
  Priestley" header and should be revised once Vishen aligns.

### Decided 5 Oct (the three items held over from the last session)

1. **Cadence stays Tuesday lesson / Thursday lab.** AIF does not match E&A's Tuesday / Friday. Vykintas leads every AIF lab
   and, after the John Lee rotation, holds eight E&A Friday workshops at 9am PT inside the AIF run (20 and 27 Nov, 18 Dec,
   8 and 29 Jan, 5, 12 and 19 Feb). A Friday lab would double-book him on each.
2. **The Thanksgiving lab stays, Thu 26 Nov** (now Week 2). Same logic as E&A: 2025 data showed no attendance drop over
   Thanksgiving week, so E&A kept Fri 27 Nov (live Airtable: slot 16, Vykintas). Caveat on the page: the evidence covers
   the week, not the day.
3. **Load panel recomputed** against the E&A calendar as it stands plus the held decisions. After the rebuild: Vishen 13
   E&A + 6 AIF live sessions, Vykintas 12 + 27, Vykintas peaks at 4 in a week (2 such weeks). **No same-hour double
   bookings** for either: the Monday opening keeps Vishen clear of his E&A Speaking lesson on Tue 17 Nov (post-rotation),
   his other AIF dates (2 and 16 Mar) fall after E&A ends, and office hours avoid Vykintas's E&A Fridays.

### The load panel: how it is computed

`build_aif.py` does not trust the snapshot's dates. It derives each E&A session's date from its slot (slot 1 = Tue 6 Oct;
odd slots Tuesday, even slots the Friday of the same week; 9am PT; no sessions on 22 and 29 Dec), which reproduces all 37
dated rows in live Airtable exactly (checked 5 Oct). Titles, types and speakers come from the snapshot, then `EA_OVERLAY`
applies what the snapshot has not caught up with: Marisha on slots 18 and 20 (already in Airtable), the John Lee rotation
(13→25, 14→26, 29→13, 30→14, 25→29, 26→30) and Regan on Membership (held). Every overlay row applies only while the
snapshot still shows the old state, so refreshing the snapshot makes it a no-op. `sync-curriculum.js` currently writes
`slot` as null (`lib/curriculum.js`), so a refreshed snapshot falls back to its own dates; restore slot resolution there
before the next refresh.

### Still open against E&A

- **Vishen on Fridays.** E&A's rule is that Vishen does not teach Fridays; AIF office hours 1 (Fri 4 Dec) and 4 (Fri 12
  Mar) have him on. Confirm whether the rule is a diary constraint or an E&A convention.
- The onboarding survey (`ONBOARDING-SURVEY.md`, F2) still says "Tuesday teach, Thursday build day" for E&A, which now
  runs Tuesday / Friday.
