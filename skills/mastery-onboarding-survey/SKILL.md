---
name: mastery-onboarding-survey
description: Design, rebuild or audit the "Getting to Know You" onboarding survey for any Mindvalley Mastery, Certification or cohort programme, whatever the subject (AI, business, speaking, social media, manifesting, spiritual, health, money, relationships, or a programme that has never run). Carries the full Mastery Onboarding Survey DNA, every live programme's question set, and a clickable student preview. Use whenever someone asks to build, write, draft, update, refresh, clean up, check or review an onboarding survey, intake form, welcome survey, pre-programme questionnaire or Getting to Know You form, or shares an Airtable form for one, even if they never say "DNA". Also use when a programme's welcome emails link to a survey that needs checking before launch.
---

# Mastery onboarding survey

Every Mastery sends one onboarding survey before the programme starts. Hosts and teachers use the answers to pitch each session at the room. The business uses them to understand who bought, and graduation uses them as the "before".

This skill is self-contained. The company standard (the Mastery Onboarding Survey DNA) and every live programme's questions are inside it, in `references/`. The only things it needs from the person asking are the programme-specific materials in step 1.

## How the work runs

1. **Ask for the materials.** One message, then wait.
2. **Audit the existing form**, if there is one, and flag anything urgent straight away.
3. **Design the questions** with the action test.
4. **Show the survey as a student sees it**, as a clickable preview, and refine it together.
5. **After sign-off, write the build spec** for whoever builds the form.

Step 4 always comes before step 5. People judge a survey by reading it as a student would. A build spec full of field types and IDs hides the survey inside the paperwork, and reviewers can't tell whether it is any good.

## Step 1: Ask for the materials

Programme questions written without the curriculum come out generic, and nobody uses the answers. Before writing anything, send this request, adapted to what the person has already given you:

> To build a survey that fits this programme, please share what you can of the following. Links, pasted text, files, screenshots or exports all work.
>
> 1. **The curriculum**, week by week. A curriculum page, doc, HTML file or slide.
> 2. **Key dates**: programme start, live-call days and times, any setup or welcome sessions, graduation, and the host's name.
> 3. **The summit quiz or post-registration survey**, if there is one. I'll copy its wording so each student's two sets of answers can be compared.
> 4. **The current onboarding form**, if the programme has run before or a form already exists. An Airtable form link, or a screenshot of each section.
> 5. **The onboarding emails**, or just the line that links to the survey. I need the length they promise ("3 minutes").
>
> Nice to have: last cohort's survey answers, and anything the teachers have asked to know about students.

Then use what comes back:
- **Airtable connected:**
  - read a form with `get_form_schema`
  - read option lists with `get_table_schema`
  - never guess an option list you are meant to copy
- **Google Drive or another connector:** read shared docs with it.
- **Nothing connected:** work from pasted text, files and screenshots.
- **Something missing:** carry on. Build the core block and the standard sections from `references/dna.md`. Mark any programme question that depends on the missing material as pending, and say what it is waiting for.

## Step 2: Audit the existing form

If an existing form was shared as Airtable schema JSON, save it to a file and run:

```
python scripts/audit_form.py form.json --programme "[Programme name]" --promise-minutes 3
```

If you only have screenshots or pasted questions, check the same things by eye against the "Drift seen across forms" table in `references/live-forms.md`. Typical drift:
- a clone still asking another programme's questions
- a required phone number
- missing age bands
- single-select programme history, or history with cohort years
- "Other" with no follow-up box
- "Group 1" as a section title
- emoji in options

Report urgent findings in chat the moment you find them, in two or three lines. A welcome email that links to the wrong questions matters more than anything else you will produce. Keep audit findings out of the student preview.

## Step 3: Design the questions

### The action test

Each question must lead to something someone does. For every question, write down **who** acts on the answer, **what** they do, and **when**. Answers get used at three moments:

1. **Before week 1: getting each student ready.** Setup gaps, missing equipment, who needs a concierge message or a nudge to a welcome session.
2. **During the programme: what each teacher gets.** The room's level, what it wants and what it fears, real examples to teach with, how to group people.
3. **At graduation: before and after.** The numbers and artefacts measured again at the end, which become the programme's proof.

If you can't name who, what and when, cut the question. "Interesting to know" is not an action. The answer to the test becomes the question's `why`, and the checker fails any programme question without one.

### Structure

1. **About you**: the DNA core block, exactly as in `references/dna.md`. Phone and personal income optional. Programme history multi-select, required, without cohort years.
2. **Your [business / practice / work]**: stage and size, plus the one open "what do you do, and for whom" sentence.
3. **Where you're starting**: level, setup, what they already have.
4. **Your goals**: what they want first, what has blocked them, what they would love to have, and one open outcome question.
5. **Your starting point**: least confident, and the measures you will ask again at graduation.
6. **Practical**: summit attendance, live calls, story consent, anything else.

Give every section a real title and a one-line subtitle telling the student why it is there. Borrow wording from the matching programme in the `dna.md` annex: students already understand it.

### Patterns that work

- **Mirror the summit.** Where the summit quiz or survey already asks something, copy the question and options word for word, so buyers can be compared with registrants.
- **Pair "love to have" with "least confident", using the same list.** One option per module, in curriculum order, "pick up to three" on both. Each teacher gets two numbers for their week: how many want it and how many fear it. The "love" answers also show which outcomes to lead with when selling the next cohort. Write "love" options as outcomes ("A funnel that collects leads while I sleep") and "least confident" options as skills ("Building a brand and a funnel").
- **Replace a long list with the one question that decides something.** If only one tool decides who needs setup help, ask about that tool, not all eight.
- **Collect one before-and-after artefact**: a website address, a sample post, a talk recording. A saved copy shown beside the graduation version is the strongest proof a programme has.
- **Use one to three measures you'll ask again at graduation.** 1 to 10 ratings on what the programme promises to change, plus one hard number such as hours a week or offers sold. Tell students in the section subtitle that you'll ask again.
- **Ask one reflection question.** It makes the survey feel like the programme's first step rather than admin. Keep it closed so it can be counted. Example: "If AI gave you back one day a week, what would you do with it?" The host can open the programme with the room's answers.
- **Ask whether they attended the summit**, so week 1 builds on it instead of repeating it.
- **End on a thank-you screen with the next dates**, so students finish knowing what happens next.

### Writing for students

- Write plainly, in the second person: "Which computer will you use for the programme?", not "Device type".
- No capitals for emphasis ("LEAST"), no emoji, no field jargon.
- Keep options short and parallel. Put a pick limit as a sub-line: "Pick up to three."
- Every "Other" or "Something else" gets a follow-up box that only appears when chosen.
- Keep required long answers to one. Each open answer costs completion and analysis time.
- Never ask desired income outside Manifesting. Never ask which teachers they want while the faculty is undecided.

### Respect the promised length

The checker times the survey at:

| Question type | Seconds |
|---|---|
| One tap, or a 1 to 10 rating | 6 |
| Dropdown | 8 |
| Ticking a list (people read every option) | 12 |
| Short typed answer | 25 |
| Long typed answer | 45 |
| Pre-filled name and email | 0 |

If the required answers run over the promise, cut the questions with the weakest action, or tell the person the emails need a new number. Never quietly break the promise.

## Step 4: Show it, and refine it together

Write the survey as JSON in the shape of `examples/aif-survey.json`: programme, intro, promised minutes, thank-you steps, and sections of questions, each with a `why`. Then run:

```
python scripts/build_preview.py survey.json --out preview.html
```

It checks the rules above and renders the survey as students will see it. Fix every FAIL; fix each WARN or raise it with the person.

Show `preview.html` where they can click through it. Publish it as an artifact if you can; otherwise share the HTML file. The page:
- has clickable answers, working follow-ups and pick limits
- ends on a thank-you screen
- has a switch, off by default, that shows each question's `why`, so the team can see the reasoning without cluttering the student view

If you can't run Python, apply the same checks by hand and write the preview yourself from `assets/preview-template.html`. Replace `__SURVEY_JSON__` with the JSON and `__PAGE_TITLE__` with "[Programme] Onboarding Survey".

In chat, keep the summary short:
- the sections and the count
- the time against the promise
- what you cut and why
- the one or two decisions only they can make

Iterate by editing the JSON, rebuilding and re-sharing at the same place. When they ask to compare with another programme's survey, give a short side-by-side table in chat, then say what to borrow.

## Step 5: After sign-off, the build spec

Only once the person approves the preview, write the spec for whoever builds the form, from the same JSON, using `assets/spec-template.md`. Keep it short:
- set-up
- the question table
- which options to copy from the summit table
- what the answers change before kickoff
- the build checklist

If they want it as a Google Doc and Drive is connected, create it from HTML and read it back to check the tables. Point to the preview at the top so readers can see the survey as students will.

## The process around the form (from the DNA)

Put these in the spec; launches slip here.

- **Reuse over rebuild.** Add fields to the existing table and hide old ones on the form. Never delete a field, because that deletes history. Separate cohorts with a view filtered by submission date, named "Onboarding survey answers".
- **Title and look.** "[Programme name]: Getting to Know You", a one- or two-sentence intro, and the programme's key art as background.
- **Timing.** Set up about two weeks before the summit. Live before the first buyer gets the welcome email.
- **Distribution.** Linked from several onboarding emails, and shared by the host and concierges in the community.
- **Approval.** Operations sends it on Slack to Customer Experience and Learning Experience for sign-off before it goes live.
- **Reporting.** Customer Experience compiles the cohort report. Each teacher gets their week's numbers before their week.
- **Response rate.** Historically low. Track it against the previous cohort.

## Editing a live form

Only build or edit a live form when the person explicitly asks. Live forms are linked from emails already sent, and some bases are on hold until a programme is signed off. When asked:
- read the schema first
- add fields rather than delete them
- copy mirrored options from their source tables
- hide inherited fields
- read the form back and audit it again

Otherwise, say plainly that the live form is unchanged.

## What's in this skill

| File | What it's for |
|---|---|
| `references/dna.md` | The full DNA: rules, process, the exact core block, and every programme's question set in the annex. Read for every survey |
| `references/live-forms.md` | What each live form does well, where it drifts, and what the most recent surveys added |
| `examples/aif-survey.json` | A complete approved survey (AI for Founders Mastery). Copy its shape, and treat its `why` lines as the bar to meet |
| `scripts/build_preview.py` | Rule check, timing, and the student preview |
| `scripts/audit_form.py` | Checks an existing Airtable form, from its schema JSON, against the DNA |
| `assets/preview-template.html` | The preview page `build_preview.py` fills |
| `assets/spec-template.md` | The build spec, for after sign-off |
