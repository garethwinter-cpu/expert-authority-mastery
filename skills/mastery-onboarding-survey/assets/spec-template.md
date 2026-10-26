# [Programme name]: Getting to Know You

**Onboarding survey · build spec for the team · [date]**

[One paragraph: built to the Mastery Onboarding Survey DNA; what it follows; that every programme question serves a week; which questions mirror the summit quiz or survey.]

## Fix this first
[Only if the audit found something affecting students now, such as a live form with the wrong questions, a broken link or a required phone. Say what students currently see, why it matters, and the fix. Leave the section out if nothing is urgent.]

## Form set-up

| Item | Value |
|---|---|
| Form title | **[Programme name]: Getting to Know You** |
| Intro line | [One or two sentences: the promised length, and that answers shape the sessions. Name the host if known] |
| Background | [Programme] key art |
| Where it lives | Base `[app id]`, table **[table name]** (`[tbl id]`), form page `[pag id]`. Reuse or new, and what to hide |
| Responses view | "Onboarding survey answers", filtered by submission date for the [month year] cohort |
| Timing | [When it must be live, relative to the summit and the first welcome email] |
| Distribution | [Which emails link it; host and concierges in the community] |
| Pre-fill | [Name and Email from the email's merge tags, if the form accepts it] |
| Approval | Operations sends it via Slack to Customer Experience and Learning Experience for sign-off before it goes live |
| Reporting | Customer Experience compiles the cohort report; Author Relations or Learning Experience forwards it to [host, teachers] before their week |

## The questions

Required fields are marked **●**. Optional fields are marked ○.

### Section A · About you (standard core block)

| # | Question | Field type | Req | Options and notes |
|---|---|---|---|---|
| A1 | Name | Short text | ● | |
| ... | | | | |

### Section B · [Topic] experience
### Section C · Goals
### Section D · Skills and baselines
### Section E · Practical

[Same five-column table in each section. In the notes column say where options come from ("Mirrors the summit") and which week or decision the answer feeds.]

**Count:** [total questions; how many a student sees after pre-fill and conditionals; how many are one tap or typed; the estimated time against the promise.]

## Why these questions and not others
- **Every programme question maps to a week.** [Which sections feed which weeks.]
- **[N] questions mirror the summit word for word.** [Which ones, and the join it allows.]
- **Open text is used [N] times.** [Where, and why a list couldn't work.]
- **What is deliberately not asked.** [Each omission with its reason.]

## What the answers change before kickoff

| Answer | Action |
|---|---|
| [question and answer] | [who does what, and when] |

## Build checklist for Operations
- [ ] Add the new fields to `[table]`; hide, do not delete, inherited fields this survey does not use
- [ ] Copy option lists exactly from [source table] for the mirrored questions
- [ ] Set conditional fields ("Other → Please specify", follow-ups)
- [ ] Phone and income optional; goals, motivation and skills required; supplementary fields optional
- [ ] Title, intro line and key-art background
- [ ] Create the "Onboarding survey answers" view for this cohort
- [ ] Send on Slack to Customer Experience and Learning Experience for approval, before [date]
- [ ] Embed the approved link in the onboarding emails; hand it to the host and concierges
- [ ] Track the response rate against [previous cohort] and report it with the analysis
