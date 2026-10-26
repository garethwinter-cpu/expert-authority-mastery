# AI for Founders Mastery: Getting to Know You

**Onboarding survey · build spec for the team · 26 October 2026**

Built to the Mastery Onboarding Survey DNA: the standard core block, then goals and motivation, then experience and current tools. Dropdowns by default, goals and skills required, phone and income optional. It follows the Expert & Authority spec of 14 September and the live AI Mastery form. Every programme question below exists because a week of the curriculum needs the answer, and six of them use the summit survey's exact options, so each student's summit and onboarding answers join on email.

---

## 1. Fix this first: the live form is still the Speaking & Influence survey

The welcome emails (E1 in every version) and the survey reminder (E3) link to the form at `airtable.com/app7lhR1V9Fts0mNc/pagDVtdJFyONjOwUL/form`. That form is titled "AI for Founders Mastery: Getting to Know You", but its questions are the Speaking & Influence clone:

- "Do you currently speak or present regularly in any context?"
- "What speaking environments are you currently most familiar with?"
- 1 to 10 speaking confidence and comfort
- "I want to become a paid public speaker" as a focus option
- "Telling compelling stories" and "Crafting unforgettable stage talks" as skills

Its programme-history list also stops at 2025 cohorts and is single-select. The summit runs 30 October to 1 November, so the first buyers will meet this form within days. Replace its questions with the ones below before the summit, and keep the same form page so the links already in the emails keep working.

---

## 2. Form set-up

| Item | Value |
|---|---|
| Form title | **AI for Founders Mastery: Getting to Know You** (already set) |
| Intro line | Three minutes, and it shapes the whole programme. Tell us about your business, where you're starting with AI, and what you want running by graduation, so Vishen, Ileana and the teachers can build every session around the founders actually in the room. |
| Background | AI for Founders Mastery key art |
| Where it lives | Base `app7lhR1V9Fts0mNc`, table **👯‍♀️ Student Onboarding Survey** (`tbl3pUVsIlo3tnbYW`), form page `pagDVtdJFyONjOwUL`. Reuse the table and the page. Add the new fields, then hide the Speaking & Influence fields on the form; do not delete them |
| Responses view | "Onboarding survey answers", filtered by submission date for the November 2026 cohort |
| Timing | Live before the summit opens on 30 October. Buyers get it one minute after purchase in E1 |
| Distribution | E1 welcome (all versions), E3 reminder, and Ileana and the concierges in Finerminds |
| Pre-fill | Pre-fill Name and Email from the email's merge tags with Airtable's `prefill_` parameters, so most students start at question 3. Test that the interface form accepts them; if it does not, leave the two fields for students to type |
| Approval | Operations sends the form via Slack to Customer Experience and Learning Experience for review and sign-off before it goes live |
| Reporting | Customer Experience compiles the cohort report for the Academy team. Author Relations or Learning Experience forwards it to Vishen, Vykintas, Ileana and each guest teacher before their week |

---

## 3. The questions

Required fields are marked **●**. Optional fields are marked ○. "Mirrors the summit" means the question and options are copied word for word from the **🧭 AI for Founders Summit Survey** table, so the answers join on email.

### Section A · About you (standard core block)

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| A1 | Name | Short text | ● | Existing field. Pre-filled from the email |
| A2 | Email Address | Email | ● | Existing field. Pre-filled. The join key to enrolment, the summit survey and the quiz |
| A3 | Phone Number | Short text | ○ | Existing field. Standard: optional |
| A4 | Gender | Single select | ● | Existing field and options |
| A5 | Age Group | Single select | ● | Existing field. **Add "18-24"**: the current list starts at 25-34 |
| A6 | Location | Country link | ● | Existing field. Timezone context for the live calls |
| A7 | What is your personal annual income? | Single select (brackets) | ○ | **New field.** The DNA's standard brackets. Personal income, not business revenue; B3 asks about the business |
| A8 | Have you ever enrolled in any other Mastery or Certification programs? (check all that apply) | Multi-select | ● | **New multi-select field**, replacing the old single-select on the form. Add the missing cohorts: AI Mastery 2025, AI Mastery 2026, Entrepreneurship Mastery 2025, Speaking & Influence Mastery 2026, Expert & Authority Mastery 2026, Spiritual Mastery, plus the existing list and "No previous programs". AI Mastery alumni need less of week 0; Expert & Authority students overlap with weeks 2, 3 and 7 |

### Section B · Your business

*Sets the example business for every demo, the solo and team rooms in the labs, and the "no website yet" path in week 1.*

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| B1 | Which of these sounds most like you today? | Single select | ● | I have a job and I'm exploring a business · I'm planning a business, not started yet · I'm a solo founder, it's mostly me · I run a small team (2–10 people) · I run a bigger team (11+ people)<br>*Mirrors the summit. Decides the solo or team room in every lab* |
| B2 | How long have you been running your business? | Single select | ● | Not running one yet · Less than a year · 1–3 years · 3–10 years · More than 10 years<br>*Mirrors the summit* |
| B3 | In the last 12 months, roughly what did your business earn? | Single select | ● | Nothing yet · Under $50K · $50K–$100K · $100K–$250K · $250K–$500K · $500K–$1M · $1M–$3M · $3M–$10M · $10M–$20M · $20M+ · I'd rather not say<br>*Mirrors the summit. "I'd rather not say" keeps it required without forcing an answer* |
| B4 | In one sentence: what do you sell, and to whom? | Short text | ● | Example: "Leadership coaching for first-time managers in tech." The one question no dropdown can answer. It gives Vykintas the businesses to demo with in week 1 and week 2, and lets Ileana form pods by market |

### Section C · Goals and motivation

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| C1 | Which part of your business would you most like off your plate first? | Single select | ● | Marketing and content · Sales and follow-up · Client work and delivery · Operations and admin · Team and hiring · Finance and reporting · Product and what to build next<br>*Mirrors the summit's first pick. Tells each teacher how much of the room came for their week* |
| C2 | What would you love to have running by graduation? (check all that apply) | Multi-select | ● | A website that beats my competitors · Clear offers and prices · Copy that turns visitors into buyers · My inbox sorted every morning · One company brain my AI team reads from · A funnel collecting leads while I sleep · Being recommended by ChatGPT and Google · A month of content scheduled · Meta ads running without an agency · My bookkeeping off my desk · Every lead answered the same day · Proposals and follow-ups written for me · One dashboard and a Monday briefing · A week where I only decide<br>*One option per lesson, in curriculum order. The DNA's "love to master" question, written as outputs because every lesson ends with something live* |
| C3 | What is the biggest thing that has stopped you automating more so far? | Single select | ● | I don't know where to start · I've tried tools but didn't get real results · I don't have the time to set it up · I'm worried about data and safety · My team isn't on board yet · I'm not sure it's worth the cost · Something else<br>*Mirrors the summit. A high "data and safety" share lengthens the privacy segments, starting with week 5* |
| C4 | By graduation on 30 March, what would make you say this was worth it? | Long text | ● | The DNA's desired-outcome question, open because it can't be pre-categorised. Read at graduation against what each student built |

### Section D · Where you're starting

*Sizes week 0, the go-live clinic and the setup guides. The stack is Claude Code, GitHub and Cloudflare, so the computer and the existing tools matter before the first lesson.*

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| D1 | Where are you with AI in your business today? | Single select | ● | I haven't really started · I use it for writing and ideas · I use it regularly for specific tasks · I have some automations running · It's built into how my business runs<br>*Mirrors the summit. The DNA's self-rated level* |
| D2 | Which AI tools do you use today? (check all that apply) | Multi-select | ● | ChatGPT · Claude · Claude Code · Gemini · Microsoft Copilot · Perplexity · Image or video tools (Midjourney and others) · None yet<br>*The AI Mastery list with Claude Code added. Everyone who doesn't tick Claude Code needs week 0* |
| D3 | Which computer will you build on? | Single select | ● | Mac · Windows · Chromebook · Only a tablet or phone · Not sure<br>*Claude Code needs a Mac or Windows computer. Chromebook, tablet and "Not sure" answers go to the concierges before week 0, not on the day of the go-live clinic* |
| D4 | Which of these does your business already have? (check all that apply) | Multi-select | ● | A website · My own domain name · An email list · An email tool (Kit, Mailchimp or similar) · A lead magnet or free download · A CRM or sales pipeline · Bookkeeping software · A Meta (Facebook and Instagram) ad account · People who work with me · None of these yet<br>*The lesson inventory: week 1 (website and domain), weeks 6 to 8 (email tool and lead magnet), week 12 (Meta account), week 13 (bookkeeping), week 14 (CRM), week 17 (people to own systems)* |
| D5 | Where does your website live today? | Single select | ● | WordPress · Squarespace · Wix · Shopify · Webflow · Something else<br>*Shown only when D4 includes "A website". Picks the adapter guide and the move-or-subdomain path in week 1* |

### Section E · Two baselines we measure again at graduation

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| E1 | In a normal week, how many hours does your business need you personally to keep running? | Single select | ● | Under 20 · 20 to 40 · 40 to 60 · More than 60 · I honestly do not know<br>*The before number for the programme's one measure. The week 0 hours log refines it; graduation counts it again. Same options as the community survey* |
| E2 | On a scale of 1 to 10, how comfortable are you giving AI access to your business email and files? | Rating 1 to 10 | ● | Baseline for week 5, the first week AI reads private email, and for the privacy segment in every lab. Re-asked at graduation |

### Section F · Practical

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| F1 | Can you join the live calls? (Tuesday lesson, Thursday lab, 7am Los Angeles, 3pm London) | Single select | ● | Both, most weeks · Tuesdays only · Thursdays only · Mostly recordings<br>*The labs only work live. Low Thursday numbers mean more pre-recorded lab twins and a lab-recap post every week* |
| F2 | Would you be open to sharing your results as a student story during or after the programme? | Single select | ○ | Yes · Maybe, ask me later · No<br>*Consent on the way in, for Demo Day and case studies* |
| F3 | Anything else you'd like Vishen, Ileana and the team to know? | Long text | ○ | Standard supplementary field |

**Count:** 26 questions. With Name and Email pre-filled, a student sees at most 24: twenty one-tap answers, two short typed answers (B4 and C4), and an optional phone number and comment. D5 shows only to students with a website. That is about three minutes, which keeps the emails' promise.

---

## 4. Why these questions and not others

**Every programme question maps to a week.** B1 to B4 set the lab rooms and the demo businesses. C2 is the curriculum as a checklist, one option per lesson. D1 to D5 size week 0 and the setup guides. E1 and E2 are the two before-and-after numbers graduation reports: the hours the business needs the founder, and comfort with AI handling private data.

**Six questions mirror the summit survey word for word:** B1, B2, B3, C1, C3 and D1. The summit survey already holds these answers for most registrants. Identical options mean we can compare buyers with registrants, and Customer Experience can join a student's two surveys without a translation table.

**Open text is used three times:** what you sell (B4), what would make it worth it (C4), and the optional supplementary field (F3). Everything else is closed, so the cohort report can be built the day the form closes.

**Three things are deliberately not asked.**
- *A long "least confident in" list.* C2 already names what each student wants, and a second fourteen-option list would break the three-minute promise.
- *Which teachers they want.* Teachers are being mapped now, and the survey must not promise names.
- *Desired income.* That field belongs to Manifesting Mastery only, under the DNA.

---

## 5. What the answers change before kickoff

| Answer | Action |
|---|---|
| D3 is Chromebook, tablet or "Not sure" | Concierge message before week 0: what computer they need and how to borrow one |
| D2 has no Claude Code | Nudge to the week 0 sequence and the 12 November go-live clinic |
| D4 has no website | Week 1 starts from the onboarding template and a voice note; Vykintas uses one of these businesses as a demo |
| D4 has no Meta ad account | The Meta setup guide goes out in early February, a week before week 12 |
| C3 is "worried about data and safety" for a large share | The week 5 privacy segment runs long, and Noelle's brief says so |
| F1 is mostly recordings or Tuesdays only | Lab twins and weekly lab recaps get priority |
| B1 splits solo and team | Sets the size of the solo and team rooms in every lab |

---

## 6. Build checklist for Operations

- [ ] In table `tbl3pUVsIlo3tnbYW`, add the new fields: personal annual income (A7), programmes multi-select (A8), B1 to B4, C1 to C3, D1 to D5, E1, E2, F1, F2, F3. Reuse the existing "Goals" long-text field for C4
- [ ] Copy the options for B1, B2, B3, C1, C3 and D1 exactly from the **🧭 AI for Founders Summit Survey** table, so the values match for joining
- [ ] Add "18-24" to Age Group
- [ ] On form page `pagDVtdJFyONjOwUL`, remove the Speaking Experience section, the Speaking focus question and both Speaking skills questions from the form (hide, do not delete the fields), then lay out sections A to F
- [ ] Set D5 to show only when D4 includes "A website"
- [ ] Replace the intro line with the one in section 2
- [ ] Phone, personal income, F2 and F3 optional; everything else required
- [ ] Test the Name and Email pre-fill from the E1 link; if it works, add the `prefill_` parameters to every survey button in E1 and E3
- [ ] Create the "Onboarding survey answers" view filtered to the November 2026 cohort
- [ ] Send the form link on Slack to Customer Experience and Learning Experience for approval, before 30 October
- [ ] Track the response rate against AI Mastery 2026 and Expert & Authority 2026, and report it with the cohort analysis
