---
name: mastery-lesson-titles
description: Write, rewrite, score or review the titles of every session in a Mindvalley Mastery, Certification or cohort programme (lessons, workshops and labs, bonus calls, pre-recorded sessions, kick-offs, graduations), benchmarked on real Mastery titles and how those sessions drew live audiences. Use whenever someone asks to name, rename, retitle, tighten or check lesson or session titles, says titles feel generic, too "AI", unclear or unexciting, or asks for titles "like Expert & Authority", even if they never mention ABCS. Works from an Airtable Lessons table, a curriculum page or doc, or a pasted list.
---

# Mastery lesson titles

A Mastery title does one job: a student scanning the week's calendar knows in two seconds what the session is about and what they will walk out with. The calendar, the app, the emails and the reminder all show it, usually without the description. If the title doesn't earn the click, the session runs to a smaller room.

Titles written during curriculum design are working names: they describe the build ("Funnel Clinic", "Your Offer Book, and Prices on the Page") in the team's own words. This skill turns them into titles a student would choose, using a pattern measured on past Masteries.

## Step 1: Ask for the materials

Send this, adapted to what the person has already shared, then wait:

> To title the sessions, please share what you can. Links, pasted text, files or screenshots all work.
> 1. **The session list**: current title, type (lesson, workshop or lab, bonus, graduation), teacher and date for each. An Airtable Lessons table link is ideal.
> 2. **What each session delivers**: the customer descriptions if they exist, otherwise the curriculum notes.
> 3. **Where titles show**: the learning platform, the calendar, the emails. Does the platform show the session type (lesson, lab) next to the title?
> 4. **Words the programme owns**: named concepts students learn early and use throughout (for example a "company brain"), and any series names to keep (for example "Get AI-Ready").
> 5. **What students said**, if you have it: quiz or survey answers in their own words.

With Airtable connected, read the table yourself. Never write to Airtable until the person has approved the titles (step 5).

## Step 2: Read before you write

For each session, read its description first. The title promises what the session delivers, nothing more. A title that over-promises costs more in trust than it gains in clicks.

Read `references/benchmarks.md` before the first draft: the real titles from past Masteries, the house benchmark (Expert & Authority), and what the attendance data says.

## Step 3: Write each title to the formula

### Lesson: `Topic: Promise`
- **Topic**: one to four plain words the student already recognises: Website, Offer and Pricing, Copywriting, Inbox, Funnels, Meta Ads, Bookkeeping, Sales Calls. It answers "what is this about?"
- **Promise**: the outcome in their words, three to eight words. It answers "why should I come?" ("Who Buys, What to Sell, What to Charge", "Close More, Chase Less").
- If the working title already has a strong promise, keep it and add the topic. Don't rewrite what works.

### Workshop or lab: `Verb + Your + Result`
- Start with what they will do: Build, Launch, Set Up, Write, Create, Publish, Score, Send.
- Name the thing they leave with, and make it theirs: "Launch Your Website and Test Your Lead Form".
- Leave "Lab" or "Workshop" out of the title where the platform already shows the session type. Where it doesn't, use the programme's one prefix consistently.

### Bonus, pre-recorded, kick-off, graduation
- Keep a series name the programme already uses ("Get AI-Ready 1"), then a colon and the promise.
- Graduation says Graduation, then the before and after: "Graduation and Demo Day: The Hours You Got Back".
- A bonus can reuse the students' own question, word for word, if a quiz or survey surfaced one ("What to Automate First").

## The rules, and why

From the benchmark (Entrepreneurship Mastery 2025, AI Mastery 2025 and 2026, Social Media Mastery, Expert & Authority 2026):

1. **Name the business outcome, not the tool.** Titles with "AI" in them drew about half the live audience of their neighbours; "... with AI" was the weakest pattern of all. In an AI programme everyone knows AI is involved. Keep "AI" only when AI itself is the subject ("Search: Get Recommended by ChatGPT and Google").
2. **Topic first, then the promise.** Topic-and-promise titles drew about 1.4 times the sessions around them; titles without the split, under 1. Most of the Expert & Authority titles follow it; the few that don't ("Your Signature Method") are the ones a student can't place at a glance.
3. **No words the student hasn't learned yet.** The team's build vocabulary ("offer book", "answer hub", "owner pages", "clinic") means nothing before the session. A programme's own named concept may lead a title only if the promise explains it: "Company Brain: Never Explain Your Business Twice".
4. **No teacher names.** The platform shows the teacher, and line-ups change; a title with a name in it has to be rewritten when they do.
5. **No generic labels or bare part numbers.** "Community Session", "Introduction to...", "Part #2". Give each part its own promise.
6. **Concrete beats clever.** A number or a timeframe that is true ("Your 3 Closest Competitors", "in One Sitting"), a contradiction that is true ("Posts That Bring Customers, Not Just Likes"). No hype words.
7. **Short.** Under 58 characters reads in one glance; over 72 is too long to scan in a calendar.
8. **House style.** Title case, a colon between topic and promise, no dashes, no exclamation marks, no emoji, no capitals for emphasis, no money words.

### Score the strong candidates (ABCS, adapted)

For each lesson title, score 0 to 2 on each, 8 in total. Aim for 5 or more; never trade clarity for points.

| | What scores 2 |
|---|---|
| **A**utomation | The result comes from a system, not effort: "Wake Up to Sorted Email", "Run Your Company From One Screen" |
| **B**enefit | A business outcome the founder wants this quarter: leads, buyers, hours back, "Without a Design Agency" |
| **C**uriosity | A true contradiction or open loop: "Close More, Chase Less", "Never Explain Your Business Twice" |
| **S**pecifics | A true number, timeframe or concrete noun: "3 Closest Competitors", "Every Morning", "Invoices and Receipts" |

Then the clarity test, pass or fail: cover the description. Can a stranger say what the session teaches? If not, fix the topic before anything else.

### Read the list as a whole
- Read the titles top to bottom, as a student sees the calendar. It should read as the story of a business being built.
- Vary the verbs and openings; three labs in a row starting "Build Your" blur together.
- A lesson and its lab should be recognisably a pair without repeating each other: "Inbox: Wake Up to Sorted Email and Drafted Replies", then "Switch On Your Inbox Assistant and Pick What to Automate".

## Step 4: Check every draft

Save the drafts as JSON, a list of `{"title", "type", "teachers"}` (add `"old_title"` to keep the before), and run:

```
python scripts/check_titles.py titles.json --allow "company brain"
```

`--allow` takes the programme's own named concepts so they aren't flagged as jargon. The checker fails:
- a lesson without "Topic: Promise"
- jargon, teacher names, generic labels and "... with AI"
- dashes, emoji, money words and over-length titles

It warns on "AI" in a title, hype words, labs that don't start with a verb or say "your", topics over four words, and runs of titles that start the same way. Fix every FAIL. Fix each WARN, or keep it on purpose and say why.

If Python isn't available, apply the same checks by eye.

## Step 5: Show, approve, then write

1. Show three representative drafts first, a lesson, a lab and a bonus or graduation, as before and after. Agree the pattern before doing the rest.
2. Then show all of them as a before and after table, with any WARN you kept and why.
3. Only after approval, write them to the title field (in Airtable, the Lessons table's title field). Change no other field.
4. Read the records back to check every one saved.
5. Keep the old title: in the record's Internal Notes, or a copy in the repo. Search the descriptions, emails and pages for the old titles and update any that quote them.

## Files

- `references/benchmarks.md`: real titles from past Masteries with live attendance and ratings, the Expert & Authority set, and what the numbers say. Read before the first draft.
- `references/examples.md`: the AI for Founders Mastery rewrite, all 38 titles before and after, with the reasoning.
- `scripts/check_titles.py`: the checker for step 4.
