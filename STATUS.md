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
- `data/curriculum.json` is the 23 Sep snapshot and is stale; refresh with `scripts/sync-curriculum.js`.
- `AIRTABLE_TOKEN` is not set on Cloud Run yet, so the live page serves the snapshot.

## AI for Founders Mastery: state for the next session (5 Oct 2026)

- Draft page `/ai-founders`, rendered from `data/ai-founders-curriculum.json` (mode draft, not aligned).
  Rebuild with `python3 scripts/aif/build_aif.py`; week copy lives in `scripts/aif/aif_weeks_raw.json`,
  per-week speaker overrides in the script's `OVR` dict.
- The August proposal is at `/ai-founders-proposal` (deep links `#programme`, `#programme-w5`, `#authors`).
- Do not use the AIF Airtable base (`app7lhR1V9Fts0mNc`, empty) until Vishen has aligned. Seeding it
  later is a copy of the JSON, same schema as E&A.
- Team direction (26 Sep, Jaideep, Marijana, Marta): Vishen leads the summit and only the big Mastery
  sessions; Vykintas leads the curriculum and every lab; six speakers at about three classes each.
- Allocation: Vishen W1, W13, W18; Vykintas W2, W4, W9, W11 and co-closes W18; Noelle Russell W3, W10, W15;
  Maria Wendt W5, W6, W8; Callan Faulkner W7, W12, W14; Shawn Kanungo W16, W17.
- Open: Vishen alignment; Callan Faulkner may decline and has no headshot in `authors/`; Daniel Priestley
  being looked at for Social Media instead; Vykintas is a single point of failure across both programmes.
- Needs a decision in the next session:
  - The draft runs Tuesday lesson / **Thursday** lab. E&A now runs Tuesday / Friday. Decide whether AIF
    matches.
  - The draft says the Week 3 lab on Thanksgiving (26 Nov) should move. E&A decided against a
    Thanksgiving break on 2025 data; apply the same logic.
  - The Vishen/Vykintas load panel was computed against the stale 23 Sep E&A snapshot. Recompute it
    after the E&A Airtable changes above.
