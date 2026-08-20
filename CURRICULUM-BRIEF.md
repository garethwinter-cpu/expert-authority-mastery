# How to prompt a Mastery curriculum proposal

Reusable brief for producing a proposal page to the standard of the Expert &
Authority one. Paste the relevant section into Claude Code, in the repo that
holds the proposals.

---

## 0. Where to run it

**Run it in Claude Code, in the repo.** Not in a chat surface without repo
access. The reason is mechanical, not preference: a proposal of this kind needs
git history, the Airtable MCP server for live speaker and rating data, Google
Drive for the author-proposal deck, and a served route so the page has a URL to
share. A surface without those produces prose that then has to be re-typed into
a page by hand, which is where errors enter.

Use a chat surface for the thinking that precedes it — arguing about positioning,
naming, whether a teacher fits. Then bring the conclusion here to be built.

---

## 1. The inputs are the whole game

The Expert & Authority page is only as good as what it was fed. Do not start a
new proposal without these five. A prompt with none of them produces something
that reads plausible and cites nothing.

| Input | Why it matters | Where it lives |
|---|---|---|
| **Full transcript** of the source accelerator, summit or existing cohort | Every framework, quote, benchmark and audience show-of-hands comes from here. This is what makes the page specific rather than generic | Transcript library / upload directly |
| **Author-proposal deck**, the section for that programme | Ratings, sample sizes, status tiers, the Curriculum Expert definition, lesson-count bands, payment model, the curriculum-first rule | Google Drive — read it with the Drive MCP tools, don't retype |
| **Cohort ratings and attendance** for comparable programmes | Format evidence: what cadence holds a room, what openers fail, where workshops under-perform lessons | The programme's Airtable base |
| **Intake / onboarding surveys** | Who actually buys, versus who we imagine buys | Airtable, per programme |
| **The live speaker table** for that programme's base | Real statuses. Names sitting at "in consideration" with no lesson count are the thing the proposal has to resolve | Airtable |

**Check the base before writing.** For Expert & Authority, the Lessons, Modules,
Schedule and Agenda tables were all empty scaffolding — eleven authors in
consideration, not one with a lesson count. That finding became a section of the
proposal. Assume the same until proven otherwise.

---

## 2. The master prompt

> Build a curriculum proposal page for **[PROGRAMME NAME]**.
>
> **Inputs** — read all of these before writing anything:
> - Transcript: [path or upload]
> - Author-proposal deck: [Drive link], the [PROGRAMME] section
> - Airtable base: [name] — read the speaker table, the lessons/modules tables,
>   the ratings rollups and the onboarding survey. Report what is actually
>   populated versus empty.
> - Comparable format data: [which other Mastery bases to cite]
>
> **The argument.** Structure it top-down, Minto style. Open with SCQA:
> situation, complication, question, answer. Then a key line of four reasons,
> each of which must be backed by a figure from our own bases in the evidence
> section. If a claim has no number behind it, say so in the document rather
> than dressing it up.
>
> **What the student owns on graduation day** is the spine of the whole
> proposal. Name the graduating artefact, list its components, tie each one to
> the week it gets built, and set certification against shipped assets — never
> against attendance or videos watched. Flex the bar by student stage if the
> intake is mixed, but do not soften it.
>
> **Faculty.** Use the deck's tiers exactly: Curriculum Expert (owns the
> architecture, teaches the majority, royalty) / core author (4–8 lessons, flat
> fee or hybrid) / guest specialist (1–3 lessons, flat fee). Give every named
> teacher their real score with the sample size. Apply the 9.3 bar. Where
> someone doesn't clear it or has no cohort data, keep the lane and flag the
> teacher — lanes are non-negotiable, occupants are not.
>
> **Satisfy the curriculum-first rule before anything else.** No contract goes
> out until lesson count, session title and recording format exist for every
> author. The proposal must contain all three, in a table.
>
> **Format.** Take the cadence from what our data rewards and design against
> what it punishes. Name the failure modes you are designing around, with their
> scores.
>
> **Be honest in the document, not just to me.** Include a risks section with
> mitigations, and an appendix stating plainly what rests on assertion rather
> than our own data. A proposal that hides its weak points gets found out in the
> room.
>
> **Build it** as a self-contained HTML page in this repo, using the shared
> design system. Add the route, commit, and tell me what you could not verify.

---

## 3. Programme-specific deltas

### AI for Founders Mastery
- Co-owned: Vishen Lakhiani + Daniel Priestley. Priestley holds protected anchor
  days; the AI Summit talk is the strategic spine.
- The organising unit is the **five pillars** — marketing, sales, operations,
  people, finance — each rebuilt as a running AI system.
- Artefact: the **Founder Operating System**. Systems in production.
- It fixes **capacity**. Do not let it teach demand creation or personal brand —
  that is Expert & Authority's half.
- **Correct the author scores against the deck.** The current page carries Chris
  Do at 9.78 and John Lee at 9.54; the deck says 9.83 and 9.56.

### Expert & Authority Mastery
- Vishen is Curriculum Expert. Guest authors: Paul McKenna, Chris Do, Alessio
  Pieroni, Lisa Nichols, Natalie Ellis, Kwame Christian, John Lee.
- Lab co-led by Alessio Pieroni (funnels, offers, money) and Akash Rupalia
  (content, camera, production). Sabrina Stocker and Safwaan Mohammed are the
  named alternates.
- Spine is Vishen's **SAS** — Be Seen, Architecture, Show Up.
- Artefact: **Your Ladder, Live** — three paid rungs and first revenue.
- It fixes **demand**. Do not let it drift into ops or automation.
- Open: Chris Do carries two teach weeks and is not yet on the Expert &
  Authority speaker record.

---

## 4. House rules

1. **One number, one source.** Every figure cited in more than one proposal
   comes from a shared data file, not from whichever document was open at the
   time. This is how Chris Do ended up with two different ratings.
2. **Cite the sample size** next to any rating under ~50 ratings. A 9.56 on 34
   ratings and a 9.55 on 12 sessions are not the same claim.
3. **Never invent a figure**, including a plausible-looking one. If a number is
   needed and absent, write "no cohort rating" and put it in the decisions list.
4. **Design system comes from CLAUDE.md**, not from taste: Google Sans, brand
   purple `#7A12D4`, pill buttons at 128px, 16px card radius, the three
   shadows only, no emoji in product chrome.
5. **Flag, don't smooth.** Anything unverified goes in the document where the
   reader will see it, not only in the chat.
6. **Keep the boundary section current.** Any new Mastery in the Exponential
   Entrepreneur pathway needs its line against the neighbouring ones, or the two
   pages will contradict each other in market.

---

## 5. The differentiation, for reuse

The test that separates the two current programmes, usable verbatim in sales
copy and on both pages:

> **"Do you have something to sell that's drowning you — or something to say
> that nobody's paying for yet?"**

Drowning in delivery → **AI for Founders** — fixes capacity, graduates a machine.
Real expertise, no audience → **Expert & Authority** — fixes demand, graduates a
name. If they can't answer, they are Expert & Authority: you cannot systematise
demand that does not exist yet.

Sequence usually runs Expert & Authority first, then AI for Founders. Build the
name, then the machine to serve it. That matches the intake — 68% female, 78%
aged 45+, service businesses built on expertise, 91% of Social Media Mastery
students not yet earning from their audience.
