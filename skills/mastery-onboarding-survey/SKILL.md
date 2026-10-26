---
name: mastery-onboarding-survey
description: Design, rebuild or audit the "Getting to Know You" onboarding survey for any Mindvalley Mastery programme, whatever the subject (AI, business, speaking, social media, manifesting, spiritual, health, money, relationships or a programme that has never run). Built on the Mastery Onboarding Survey DNA and the live Airtable forms. Use whenever someone asks to build, write, draft, update, refresh, clean up, check or review an onboarding survey, intake form, welcome survey, pre-programme questionnaire or Getting to Know You form for a Mastery, Certification or cohort programme, or pastes an Airtable form link for one, even if they never say "DNA". Also use when a Mastery's welcome emails link to a survey that needs checking before launch.
---

# Mastery onboarding survey

Every Mastery sends one onboarding survey before the programme starts. Hosts and teachers use it to pitch each session at the room, and the business uses it to understand who bought. The company standard is the **Mastery Onboarding Survey DNA** (Google Drive file `1AQV6LlZlJYJ-Q_YEoeDLZpBlEBadDWOf`). This skill turns the DNA, the live forms and the lessons from building them into one repeatable process for any subject.

The job is usually one of three things. Work out which before starting:

1. **Build** a survey for a programme (new or relaunched).
2. **Audit** a live form, often because a welcome email already links to it.
3. **Update** a reused form for a new cohort.

All three end in the same deliverable: a build spec Operations can follow, in the format in `assets/spec-template.md`.

## Step 1: Gather the inputs before writing a question

A survey written without the curriculum produces generic questions nobody uses. Collect these first, using whatever tools are connected (Airtable, Google Drive, the programme's repo or curriculum page):

| Input | Why it matters | Where it usually is |
|---|---|---|
| Programme name, cohort dates, host name | The title, the intro line and the live-call question | The onboarding email doc, the curriculum page |
| The curriculum, week by week | Every programme question must serve a week | Curriculum page, Airtable Lessons or Schedule table |
| The summit quiz and the post-registration summit survey | Copying their exact options lets each student's answers join on email | The programme's Airtable base, tables named Quiz or Summit Survey |
| The onboarding email journey | It states the survey's promised length and where the link points | Google Doc named "[Programme] Onboarding" |
| The existing onboarding form and table | The DNA says reuse, and the live form may be a stale clone | Airtable table "Student Onboarding Survey", form page in the Forms or Interface tab |
| Last cohort's survey answers, if any | Shows which questions produced usable data | The "Onboarding survey answers" view |

With Airtable connected, read the live form with `get_form_schema` and the source questions with `get_table_schema`. Never guess option lists: copy them from the source table.

If the curriculum isn't written yet, say so and build only the core block plus the standard experience and goals sections. Mark the programme-specific questions as pending.

## Step 2: Audit what exists

Run the audit even when building something new, because most programmes are relaunches and their table already exists. Save the `get_form_schema` result to a file and run:

```
python <skill>/scripts/audit_form.py form.json --programme "AI for Founders Mastery" --promise-minutes 3
```

It checks the form against the DNA and against the drift seen on the live forms. That drift includes a clone that still asks another programme's questions, a required phone number, missing age bands, a single-select programme history, "Other" with no follow-up, and generic section titles. Read `references/live-forms.md` for what each live form gets right and wrong. Put the findings at the top of the spec when they affect students now: a welcome email linking to the wrong questions is the most urgent thing in the document.

## Step 3: Build the questions

### The structure

Every survey has these sections in this order. The first three come from the DNA; the last two come from the specs that worked best.

1. **About you**: the standard core block, unchanged in wording.
2. **[Topic] experience** or **Where you're starting**: self-rated level, tenure or frequency, current tools, platforms or practices.
3. **Goals**: the motivation or focus question, a focus-areas question, and the open desired-outcome question.
4. **Skills** or **Baselines**: what they feel least confident in and what they'd love to master, plus any 1 to 10 ratings you will ask again at graduation.
5. **Practical**: whether they can join live, consent to share their story, and anything else they want the team to know.

Give every section a real title. "Group 1" and "New Group" are Airtable defaults, not titles.

### The core block

Copy it exactly from `references/dna.md`, section "Core block". The income brackets, age bands and programme list must match across programmes, or cross-programme analysis breaks. Two rules are easy to get wrong:

- **Phone number and personal income are always optional.** The DNA standardised this to cut friction.
- **"Have you ever enrolled in any other Mastery or Certification programs?" is multi-select and required.** List programmes without cohort years, plus "No previous programs". Add any programme launched since the list was last updated.

### The programme questions

Write them from the curriculum, not from imagination. For each candidate question, name the week or decision it feeds. If you can't name one, drop the question.

- **Mirror the summit.** Where the summit quiz or survey already asks something (stage, business size, revenue, level, biggest block), copy its question and options word for word. Identical options let Customer Experience compare buyers with registrants and join two answers per student without a translation table.
- **Experience level** uses the programme's own words, as in "I'm completely new to spirituality" or "Beginner (just starting or inconsistent)". It is single select and required.
- **Tools, platforms or practices** is multi-select and required, with an "Other" option followed by a conditional "Please specify" field.
- **Motivation or focus** is single select by default. Use multi-select when several motivations truly co-exist, as in Spiritual and Manifesting.
- **Least confident in** and **Love to master** are multi-select and required. Give one option per pillar, week or graduating outcome, so each teacher sees what the room needs from their week. Write "love to master" options as outcomes the student will have, not topic names.
- **Baselines** are 1 to 10 ratings on the one or two things the programme promises to move, such as speaking confidence or comfort letting AI read private email. Note in the spec that they are re-asked at graduation; that before-and-after is what the programme can report.
- **The desired-outcome question** is open text and required: "What transformation do you want to walk away with by the end of this program?", or a version tied to graduation.

### Rules from the DNA, with the reasons

- **Dropdowns by default.** Closed answers can be grouped the day the form closes. Use open text only where no list can work, such as follower counts across platforms, a one-sentence description of their business, or the desired outcome. Each open question costs analysis time and completion rate.
- **Goals, motivations and skills are required; supplementary fields are optional.** The required fields are why the survey exists. The rest only add friction.
- **Never ask desired income** unless the programme is Manifesting. The gap between current and desired income only means something there.
- **Don't ask which teachers they want** while the faculty is undecided. The survey must not promise names.
- **No emoji in options.** Several live forms use them; they split identical answers during analysis and break joins.

### Respect the promised length

Onboarding emails promise a length, often "three minutes". Count before you finish:

- about 6 seconds per one-tap question
- about 20 seconds per short typed answer
- about 40 seconds per long typed answer

Pre-filling name and email from the email's merge tags saves the slowest part of the core block. If the count runs over the promise, cut programme questions that feed the fewest weeks. Don't quietly break the promise; state the count in the spec.

## Step 4: Write the spec

Use the template in `assets/spec-template.md`. It has seven parts:

1. Anything to fix first
2. Form set-up
3. The questions, section by section, in tables
4. The count
5. Why these questions and not others
6. What the answers change before kickoff
7. The build checklist for Operations

The "what the answers change" table is what turns a survey into a tool: for each answer, the action someone takes before week 1.

Write in plain British English, one idea per sentence, with no em dashes in headings. Number the questions by section (A1, B2), so teams can refer to them in Slack.

If the user wants the spec as a Google Doc, create it with Drive `create_file` from HTML, then read it back to check the tables came through.

## Step 5: The process around the form

Put these in the spec's set-up table and checklist. They come straight from the DNA and are where launches slip.

- **Reuse over rebuild.** For a relaunch, add new fields to the existing table, hide old ones on the form, and never delete a field, because that deletes history. Separate cohorts with a view filtered by submission date, named "Onboarding survey answers".
- **Title and look.** The title is "[Programme name]: Getting to Know You". Add a one- or two-sentence intro saying the answers shape the sessions, and use the programme's key art as the background.
- **Timing.** The survey is set up about two weeks before the summit and is live before the first buyer receives the welcome email.
- **Distribution.** Link it from several points in the onboarding emails, and have the host and concierges share it in the community.
- **Approval.** Operations sends it on Slack to Customer Experience and Learning Experience for review and sign-off before it goes live.
- **Reporting.** Customer Experience analyses the answers and compiles a cohort report for the Academy team. Author Relations or Learning Experience forwards it to every teacher before their week.
- **Response rate.** It has historically been low. Track it against the previous cohort and report it with the analysis.

## Building in Airtable

Only build or edit the live form when the user explicitly asks you to. Live forms are linked from emails already sent, and some bases are frozen until a programme is aligned with Vishen. When asked:

- read the schema first
- add fields; don't delete them
- copy option lists from their source tables
- hide inherited fields on the form rather than removing them
- read the form back with `get_form_schema` and run the audit again

Otherwise, deliver the spec and say plainly that the live form is unchanged.

## Reference files

- `references/dna.md`: the DNA condensed, with the exact core block options. Read for every survey.
- `references/live-forms.md`: the question sets of AI Mastery, Social Media, Manifesting, Entrepreneurship, Speaking & Influence and Spiritual, plus the Expert & Authority and AI for Founders specs, with what each gets right and wrong. Read when writing programme questions, to borrow wording that works.
- `assets/spec-template.md`: the output format.
- `scripts/audit_form.py`: checks an Airtable form schema against the DNA.
