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

## AI for Founders Mastery: state after the 5 Oct session

- Draft page `/ai-founders`, rendered from `data/ai-founders-curriculum.json` (mode draft, not aligned).
  Rebuild with `python3 scripts/aif/build_aif.py`; week copy lives in `scripts/aif/aif_weeks_raw.json`,
  per-week speaker overrides in the script's `OVR` dict, the E&A calendar it computes diary load against in
  `EA_OVERLAY` (see "The load panel" below).
- The August proposal is at `/ai-founders-proposal` (deep links `#programme`, `#programme-w5`, `#authors`).
- Do not use the AIF Airtable base (`app7lhR1V9Fts0mNc`, empty) until Vishen has aligned. Seeding it
  later is a copy of the JSON, same schema as E&A.
- Team direction (26 Sep, Jaideep, Marijana, Marta): Vishen leads the summit and only the big Mastery
  sessions; Vykintas leads the curriculum and every lab; six speakers at about three classes each.
- Allocation: Vishen W1, W13, W18; Vykintas W2, W4, W9, W11 and co-closes W18; Noelle Russell W3, W10, W15;
  Maria Wendt W5, W6, W8; Callan Faulkner W7, W12, W14; Shawn Kanungo W16, W17.
- Open: Vishen alignment; Callan Faulkner may decline and has no headshot in `authors/`; Daniel Priestley
  being looked at for Social Media instead; Vykintas is a single point of failure across both programmes.

### Decided 5 Oct (the three items held over from the last session)

1. **Cadence stays Tuesday lesson / Thursday lab.** AIF does not match E&A's Tuesday / Friday. Vykintas leads
   every AIF lab and, after the John Lee rotation, holds eight E&A Friday workshops at 9am PT inside the AIF
   run (20 and 27 Nov, 18 Dec, 8 and 29 Jan, 5, 12 and 19 Feb). A Friday lab would double-book him on each.
   Thursday also keeps two clear days between a lesson and the lab that builds it. The one place the two
   programmes meet on the same weekday is Tuesday, which is where the clash below comes from.
2. **The Week 3 lab stays on Thanksgiving, Thu 26 Nov.** Same logic as E&A: 2025 data showed no attendance
   drop over Thanksgiving week, so E&A kept Fri 27 Nov (confirmed in live Airtable: slot 16, Vykintas). The lab
   is Vykintas-led and recorded; the Week 3 lesson (Noelle) is the Tuesday before. Caveat, stated on the page:
   the 2025 evidence covers the week, not Thanksgiving Day itself. The live number on the day is the test for
   the next cohort.
3. **Load panel recomputed** against the E&A calendar as it stands today plus the held decisions above. The
   23 Sep snapshot was wrong in two ways: it still skipped Fri 27 Nov (so every lesson from December landed on
   a Friday) and it had Vykintas on the 4 and 11 Dec workshops that Marisha now holds. New figures: Vishen 13
   E&A + 7 AIF live sessions (was 14 + 7; Regan takes Membership), Vykintas 12 + 30 (was 14 + 30), peak 3 in a
   week, 3 such weeks. The panel now also lists same-hour double bookings, which the old one did not check.

### The load panel: how it is computed

`build_aif.py` no longer trusts the snapshot's dates. It derives each E&A session's date from its slot
(slot 1 = Tue 6 Oct; odd slots Tuesday, even slots the Friday of the same week; 9am PT; no sessions on 22
and 29 Dec), which reproduces all 37 dated rows in live Airtable exactly (checked 5 Oct). Titles, types and
speakers come from the snapshot, then `EA_OVERLAY` applies what the snapshot has not caught up with: Marisha
on slots 18 and 20 (already in Airtable), the John Lee rotation (13→25, 14→26, 29→13, 30→14, 25→29, 26→30)
and Regan on Membership (held). Every overlay row applies only while the snapshot still shows the old state,
so refreshing the snapshot makes it a no-op rather than a double move. `sync-curriculum.js` currently writes
`slot` as null (`lib/curriculum.js`), so a refreshed snapshot falls back to its own dates; restore slot
resolution there before the next refresh or the overlay cannot key on slots.

### Also changed 5 Oct

- Office hours 3 moved from Fri 12 Feb to **Fri 26 Feb** (Vykintas runs E&A's Partnerships workshop at 9am PT
  on 12 Feb) and office hours 4 from 12 Mar to **Fri 19 Mar**, the Friday before graduation week.
- Session times now use the real Pacific zone. W18 (23 and 25 Mar), office hours 4 and the alumni call fall
  after US clocks change on 14 Mar 2027 and were an hour late (10am PT) before.

### New: needs a decision

- **Tue 16 Feb, 9am PT, Vishen is double-booked.** E&A slot 35 (Legacy, Vishen) and AIF W13 (The 4-Day Founder
  Week, Vishen) are the same hour. The only Vishen-free E&A Tuesdays inside the AIF run, after the held
  decisions, are 10 Nov (John Lee, status Checking), 24 Nov (Priestley), 12 and 26 Jan (Regan), 19 Jan (Ajit);
  from 2 Mar E&A is over. Options: (a) swap Vishen's W13 with Noelle's W15 (Tue 2 Mar), which keeps Vishen's
  three sessions but moves his anchor out of Phase 3; (b) run AIF W13 later the same day, breaking the 9am rule
  once; (c) E&A moves Legacy. Not changed on the page; flagged in the load panel.
- **Tue 10 Nov is a conditional clash.** AIF W1 (Vishen) is the same hour as E&A Content Machine (John Lee,
  Checking). If John has no Tuesday and Vishen covers it (STATUS, E&A item 1), Vishen is double-booked on
  AIF's opening day.
- **Vishen on Fridays.** E&A's rule is that Vishen does not teach Fridays; AIF office hours 1 (Fri 4 Dec) and 4
  (Fri 19 Mar) have him on. Confirm whether the rule is a diary constraint or an E&A convention.
