# Expert & Authority Mastery — Curriculum Proposal

A 17-week Mastery programme proposal turning Vishen Lakhiani's six-hour
*Become a World-Class Expert and Authority in Your Niche* accelerator into a
full cohort programme.

**Internal Mindvalley document.** Contains cohort ratings, faculty status,
pricing and commercial strategy. Keep this repository private.

## Running locally

```bash
npm install
npm start        # http://localhost:8080
```

No build step — `index.html` is self-contained with embedded CSS and JS.

## Routes

| Route | Serves |
|---|---|
| `/` | The proposal |
| `/proposal` | The proposal (alias) |
| `/healthz` | Health check |

## What's in the proposal

Eight tabs, in the order the argument runs:

1. **The Case** — SCQA, the four reasons, and the structural decision that authors teach while implementers run the build days
2. **The Evidence** — the programme is already sold from stage; the IP is open; author scores; format data and its failure modes; live base status; demand
3. **The Programme** — the organising idea, the weekly rhythm, the doctrine, the standards check, the honest risks
4. **Week by Week** — 17 weeks, four modules, the week-9 Masterclass Intensive
5. **Authors** — Curriculum Expert, seven named teachers, the implementation team, and the author × curriculum map
6. **Format & Contracts** — the curriculum-first rule, lesson counts per author, payment tiers, format spec
7. **The Artefact** — Your Ladder, Live: the six components students graduate owning
8. **Commercials & Next Steps** — ecosystem position, decisions made, decisions outstanding, sources

## Structure

- **Spine:** Vishen's SAS framework — Be Seen · Architecture · Show Up
- **Sequence:** build one rung → build the masterclass that sells it → turn on the traffic → extend the ladder
- **Cadence:** Teach (Tue) + Implementation Day (Thu), 16 paired weeks plus a 3-day intensive at week 9
- **Certification:** a live product ladder with three paid rungs — not videos watched

## Sources

- Full transcript of the Expert & Authority Accelerator (Mindvalley U, Tallinn)
- Author-proposal deck, Expert & Authority section
- Speaking & Influence Mastery 2025 vs 2026 comparison (Airtable rollup)
- AI for Founders Mastery proposal
- Expert & Authority Summit & Mastery Airtable base (read 18 August 2026)

## Deployment

Node.js buildpack, no Dockerfile. `npm start` binds to `process.env.PORT`.
