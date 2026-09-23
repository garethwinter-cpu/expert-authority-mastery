# Mastery Proposals

Mindvalley Mastery curriculum proposals — one repo, one data source, one
design system. **Internal**: contains cohort ratings, pricing and faculty
compensation structure. Keep this repository private.

## Routes

| Route | Page |
|---|---|
| `/` | Hub — all proposals |
| `/expert-authority` | Expert & Authority Mastery curriculum, rendered from Airtable on every request (`lib/curriculum.js`) |
| `/api/curriculum` | The same curriculum as JSON |
| `/covers/*` | Lesson cover images synced from Airtable |
| `/ai-founders` | AI for Founders Mastery (18 weeks, Vishen × Daniel Priestley) |
| `/positioning` | One Pathway, Two Masteries — the canonical boundary |
| `/health` | Health check (Google's frontend reserves `/healthz` on Cloud Run) |

## Running locally

```bash
npm install
npm start        # http://localhost:8080
```

## The anti-drift architecture

The reason this is one repo and not one per programme: shared figures kept
drifting between documents (Chris Do was 9.78 on one page and 9.83 on
another). So anything cited in more than one place lives in exactly one file:

| Source of truth | What it holds | Rendered where |
|---|---|---|
| `data/curriculum.json` | Snapshot of the Airtable Lessons table (base `appnHZYcirCg1VqUP`, view `2026 \| Lessons`). Served when `AIRTABLE_TOKEN` is not set or Airtable is unreachable | `/expert-authority`, `/api/curriculum` |
| `data/authors.json` | Every verified author rating, sample size, status, allocation | Both proposals cite it; verify against it before editing any figure |
| `data/boundary.json` | The E&A ↔ AI-for-Founders positioning: cards, router, comparison table, overlap rules | Injected into **both** proposal pages and generates `positioning.html` |
| `data/learnings.json` | The S&I / AIM format findings (retention, workshop gap, opener failures) | Cited by both proposals |
| `shared/wellness.css` | The design system — structure and type only; each page supplies its own accent tokens | Linked by every page |

### The curriculum reads Airtable

The Expert & Authority curriculum has one source of truth: the Airtable Lessons table.
With `AIRTABLE_TOKEN` set in the environment, `lib/curriculum.js` reads the table (and
the Speakers and Modules tables it links to) at launch and again whenever its ten-minute
cache expires, so an edit in Airtable appears on the page within ten minutes. Without a
token it serves `data/curriculum.json`. Refresh that snapshot and the cover images with:

```bash
AIRTABLE_TOKEN=pat... node scripts/sync-curriculum.js
```

The earlier drafts (v1 to v5 and the comparison) were retired on 23 September 2026;
their routes redirect to `/expert-authority`.

### Editing the boundary

Never hand-edit between `<!-- boundary:auto -->` markers — the build
overwrites it. Instead:

```bash
# 1. edit data/boundary.json
python3 scripts/build_boundary.py   # 2. re-renders both pages + positioning.html
# 3. commit — the diff shows the same change landing in all three outputs
```

The script is idempotent; each page renders the shared facts from its own
perspective (own card tinted and ordered first).

### Adding the next proposal

Follow `CURRICULUM-BRIEF.md` — the inputs table, the master prompt, the house
rules. New page links `shared/wellness.css`, defines its own accent tokens,
cites `data/authors.json`, and gets a route in `server.js`.

## Deployment

Node.js buildpack, no Dockerfile. `npm start` binds `process.env.PORT`;
`/health` responds 200. Deployed via Kessel from this
repo's `main`, same as the speaking-influence and ai-founder services.
