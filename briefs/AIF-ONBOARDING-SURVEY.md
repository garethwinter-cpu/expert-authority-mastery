# AI for Founders Mastery: Getting to Know You

**Onboarding survey · build spec for the team · 26 October 2026**

Built to the Mastery Onboarding Survey DNA: the standard core block, then experience, goals, skills and practical questions. Dropdowns by default, goals and skills required, phone and income optional. It follows the Expert & Authority spec of 14 September and the live AI Mastery form. Every programme question below serves a week of the curriculum. Seven questions copy the post-registration summit survey word for word, so each student's summit and onboarding answers join on email.

## Fix this first

The welcome emails (E1 in every version) and the survey reminder (E3) link to form page `pagDVtdJFyONjOwUL`. It is titled "AI for Founders Mastery: Getting to Know You", but an audit against the DNA on 26 October found it is still the Speaking & Influence form:

- **Seven questions ask about public speaking.** Examples: "Do you currently speak or present regularly in any context?", a 1 to 10 speaking confidence rating, "I want to become a paid public speaker", "Crafting unforgettable stage talks". A founder who buys at the summit sees these within a minute of paying.
- **Programme history** is single-select and lists cohort years that stop at 2025.
- **Age Group** has no 18-24 band.
- **No personal annual income** question.
- **Emoji** in the speaking-environment options.
- **"Other" with no follow-up** on the speaking-environment question.
- **The core section is titled "Group 1"**, and the intro line runs to 362 characters.

The summit runs 30 October to 1 November. Replace the questions on the same form page before then, so the links already in the emails keep working.

## Form set-up

| Item | Value |
|---|---|
| Form title | **AI for Founders Mastery: Getting to Know You** (already set) |
| Intro line | Three minutes, and it shapes the whole programme. Tell us about your business and where you're starting with AI, so Vishen, Ileana and the teachers can build every session around the founders in the room. |
| Background | AI for Founders Mastery key art |
| Where it lives | Base `app7lhR1V9Fts0mNc`, table **👯‍♀️ Student Onboarding Survey** (`tbl3pUVsIlo3tnbYW`), form page `pagDVtdJFyONjOwUL`. Reuse the table and the page. Add the new fields and hide the Speaking & Influence fields on the form; do not delete them |
| Responses view | "Onboarding survey answers", filtered by submission date for the November 2026 cohort |
| Timing | Live before the summit opens on 30 October. Buyers get it one minute after purchase in E1 |
| Distribution | E1 welcome (every version), E3 reminder, and Ileana and the concierges in Finerminds |
| Pre-fill | Name and Email from the email's merge tags, with Airtable's `prefill_` parameters. Test that the interface form accepts them; if not, leave the two fields for students to type |
| Approval | Operations sends it via Slack to Customer Experience and Learning Experience for sign-off before it goes live |
| Reporting | Customer Experience compiles the cohort report. Author Relations or Learning Experience forwards it to Vishen, Vykintas, Ileana and each guest teacher before their week |

## The questions

Required fields are marked **●**. Optional fields are marked ○. "Mirrors the summit" means the question and options are copied word for word from the **🧭 AI for Founders Summit Survey** table.

### Section A · About you (standard core block)

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| A1 | Name | Short text | ● | Existing field. Pre-filled |
| A2 | Email Address | Email | ● | Existing field. Pre-filled. The join key to enrolment, the summit survey and the quiz |
| A3 | Phone Number | Short text | ○ | Existing field. Optional, as the DNA standardises |
| A4 | Gender | Single select | ● | Female · Male · Non-binary · Prefer not to say. Add Non-binary to the existing field |
| A5 | Age Group | Single select | ● | 18-24 · 25-34 · 35-44 · 45-54 · 55-64 · 65+. Add 18-24, 55-64 and 65+; old "55+" answers still compare by combining the last two |
| A6 | Location | Country link | ● | Existing field |
| A7 | What is your personal annual income? | Single select | ○ | **New field.** Under $25,000 · $25,000 – $49,999 · $50,000 – $74,999 · $75,000 – $99,999 · $100,000 – $149,999 · $150,000 – $199,999 · $200,000+ · Prefer not to say. Personal income; B3 asks about the business |
| A8 | Have you ever enrolled in any other Mastery or Certification programs? | Multi-select | ● | **New multi-select field**, replacing the single-select one on the form. No previous programs · AI Mastery · Entrepreneurship Mastery · Expert & Authority Mastery · Speaking & Influence Mastery · Social Media Mastery · Manifesting Mastery · Spiritual Mastery · Investing Mastery · Coaching Career Mastery · Health & Body Mastery · Mindvalley Certified Life Coach · Mindvalley Certified Hypnotherapist · Mindvalley Certified Business Coach · Mindvalley Certified Holobody Coach · Mindvalley Certified Money Coach. AI Mastery alumni need less of week 0; Expert & Authority students overlap with weeks 2, 3 and 7 |

### Section B · Your business

*Sets the solo and team rooms in every lab, the demo businesses, and the "no website yet" path in week 1.*

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| B1 | Which of these sounds most like you today? | Single select | ● | I have a job and I'm exploring a business · I'm planning a business, not started yet · I'm a solo founder, it's mostly me · I run a small team (2–10 people) · I run a bigger team (11+ people)<br>*Mirrors the summit. Decides the solo or team room in every lab* |
| B2 | How long have you been running your business? | Single select | ● | Not running one yet · Less than a year · 1–3 years · 3–10 years · More than 10 years<br>*Mirrors the summit* |
| B3 | In the last 12 months, roughly what did your business earn? | Single select | ● | Nothing yet · Under $50K · $50K–$100K · $100K–$250K · $250K–$500K · $500K–$1M · $1M–$3M · $3M–$10M · $10M–$20M · $20M+ · I'd rather not say<br>*Mirrors the summit* |
| B4 | In one sentence: what do you sell, and to whom? | Short text | ● | Example: "Leadership coaching for first-time managers in tech." No list can answer it. Gives Vykintas real businesses to demo with in weeks 1 and 2, and lets Ileana form pods by market |

### Section C · Where you're starting

*Sizes week 0, the 12 November go-live clinic and the setup guides. The stack is Claude Code, GitHub and Cloudflare.*

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| C1 | Where are you with AI in your business today? | Single select | ● | I haven't really started · I use it for writing and ideas · I use it regularly for specific tasks · I have some automations running · It's built into how my business runs<br>*Mirrors the summit. The DNA's self-rated level* |
| C2 | Which AI tools do you use today? | Multi-select | ● | ChatGPT · Claude · Claude Code · Gemini · Microsoft Copilot · Perplexity · Image or video tools · None yet<br>*The AI Mastery list with Claude Code added. Anyone without Claude Code needs week 0* |
| C3 | Which computer will you build on? | Single select | ● | Mac · Windows · Chromebook · Only a tablet or phone · Not sure<br>*Claude Code needs a Mac or Windows computer* |
| C4 | Which of these does your business already have? | Multi-select | ● | A website · My own domain name · An email list · An email tool (Kit, Mailchimp or similar) · A lead magnet or free download · A CRM or sales pipeline · Bookkeeping software · A Meta (Facebook and Instagram) ad account · People who work with me · None of these yet<br>*Feeds week 1 (website, domain), weeks 7 and 8 (email tool, lead magnet), week 12 (Meta account), week 13 (bookkeeping), week 14 (CRM) and week 17 (people to own systems)* |
| C5 | Where does your website live today? | Single select | ● | WordPress · Squarespace · Wix · Shopify · Webflow · Something else<br>*Shown only when C4 includes "A website". Picks the move-or-subdomain path in week 1* |

### Section D · Goals

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| D1 | Which part of your business would you most like off your plate first? | Single select | ● | Marketing and content · Sales and follow-up · Client work and delivery · Operations and admin · Team and hiring · Finance and reporting · Product and what to build next<br>*Mirrors the summit's first pick. The DNA's motivation question* |
| D2 | What is the biggest thing that has stopped you automating more so far? | Single select | ● | I don't know where to start · I've tried tools but didn't get real results · I don't have the time to set it up · I'm worried about data and safety · My team isn't on board yet · I'm not sure it's worth the cost · Something else<br>*Mirrors the summit* |
| D2a | Please specify. | Short text | ○ | Shown only when D2 is "Something else" |
| D3 | By graduation on 30 March, what would make you say this was worth it? | Long text | ● | The DNA's desired-outcome question. Read at graduation against what each student built |

### Section E · Skills and baselines

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| E1 | Which of these do you feel LEAST confident in? | Multi-select | ● | Knowing what to automate first · Writing copy that sells · Building a website or funnel · Getting found online · Making content consistently · Running paid ads · Following up and closing sales · Keeping the books and the numbers · Giving AI access to my data safely · Handing work to my team or to AI<br>*One option per part of the programme, so each teacher sees what the room fears before their week* |
| E2 | What would you LOVE to have running by graduation? | Multi-select | ● | A website that beats my competitors · Clear offers and prices · Copy that turns visitors into buyers · One company brain my AI team reads from · My inbox sorted every morning · A professional brand without an agency · A funnel collecting leads while I sleep · Being recommended by ChatGPT and Google · A month of content, and weekly content that brings customers · Meta ads running without an agency · My bookkeeping off my desk · Every lead answered the same day · Proposals and follow-ups written for me · One dashboard and a Monday briefing · A week where I only decide<br>*One option per lesson, in curriculum order, written as outcomes* |
| E3 | In a normal week, how many hours does your business need you personally to keep running? | Single select | ● | Under 20 · 20 to 40 · 40 to 60 · More than 60 · I honestly do not know<br>*Baseline for the programme's one measure. The week 0 hours log refines it; graduation counts it again* |
| E4 | On a scale of 1 to 10, how comfortable are you giving AI access to your business email and files? | Rating 1 to 10 | ● | Baseline for week 5, the first week AI reads private email, and for the privacy segment in every lab. Re-asked at graduation |

### Section F · Practical

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| F1 | Can you join the live calls? (Tuesday lesson, Thursday lab, 7am Los Angeles, 3pm London) | Single select | ● | Both, most weeks · Tuesdays only · Thursdays only · Mostly recordings<br>*The labs only work live; low Thursday numbers mean more lab twins and recaps* |
| F2 | Would you be open to sharing your results as a student story during or after the programme? | Single select | ○ | Yes · Maybe, ask me later · No<br>*Consent on the way in, for Demo Day and case studies* |
| F3 | Anything else you'd like Vishen, Ileana and the team to know? | Long text | ○ | Standard supplementary field |

**Count:** 28 questions, two of them conditional (C5, D2a). With Name and Email pre-filled, a student answers 21 one-tap questions and two typed ones (B4 and D3): about three minutes, which keeps the emails' promise. The optional phone number and comment add about a minute for those who give them. E2 is the longest list; keep its options in curriculum order so it scans quickly.

## Why these questions and not others

- **Every programme question maps to a week.** Section B sets the lab rooms and demo businesses. Section C sizes week 0 and the guides. E1 and E2 tell each teacher what the room fears and wants from their week. E3 and E4 are the two before-and-after numbers graduation reports.
- **Seven questions mirror the summit word for word:** B1, B2, B3, C1, D1, D2 and its write-in. Identical options let Customer Experience compare buyers with registrants and join each student's two surveys without a translation table.
- **Open text is used three times:** what they sell (B4), what would make it worth it (D3), and the optional comment (F3). Everything else is closed, so the cohort report can be built the day the form closes.
- **What is deliberately not asked.** Which teachers they want, because teachers are still being mapped. Desired income, which the DNA keeps on Manifesting Mastery only. Follower counts, because the programme builds content without needing a face or an audience.

## What the answers change before kickoff

| Answer | Action |
|---|---|
| C3 is Chromebook, tablet or "Not sure" | Concierge message before week 0: the computer they need and how to borrow one |
| C2 has no Claude Code | Nudge to the week 0 sequence and the 12 November go-live clinic |
| C4 has no website | Week 1 starts from the onboarding template and a voice note; Vykintas demos with one of these businesses |
| C4 has no Meta ad account | The Meta setup guide goes out in early February, a week before week 12 |
| D2 or E1 shows a large share worried about data | The week 5 privacy segment runs long, and Noelle's brief says so |
| E1 shows a cluster | That week's teacher gets the number and the students' own words before their lesson |
| F1 is mostly recordings or Tuesdays only | Lab twins and weekly lab recaps get priority |
| B1 splits solo and team | Sets the size of the solo and team rooms in every lab |

## Build checklist for Operations

- [ ] In table `tbl3pUVsIlo3tnbYW`, add the new fields: A7, A8 (multi-select), B1 to B4, C1 to C5, D1, D2, D2a, E1 to E4, F1 to F3. Reuse the existing "Goals" long-text field for D3
- [ ] Add Non-binary to Gender, and 18-24, 55-64 and 65+ to Age Group
- [ ] Copy the options for B1, B2, B3, C1, D1 and D2 exactly from the **🧭 AI for Founders Summit Survey** table
- [ ] On form page `pagDVtdJFyONjOwUL`, hide the Speaking Experience section, the Speaking focus question, the "If you chose Other" field and both Speaking skills questions (do not delete the fields), then lay out sections A to F with these titles
- [ ] Set C5 to show only when C4 includes "A website", and D2a only when D2 is "Something else"
- [ ] Replace the intro line with the one in the set-up table
- [ ] Phone, income, D2a, F2 and F3 optional; everything else required
- [ ] Test the Name and Email pre-fill from the E1 link; if it works, add the `prefill_` parameters to every survey button in E1 and E3
- [ ] Create the "Onboarding survey answers" view for the November 2026 cohort
- [ ] Send on Slack to Customer Experience and Learning Experience for approval, before 30 October
- [ ] Track the response rate against AI Mastery 2026 and Expert & Authority 2026, and report it with the cohort analysis
