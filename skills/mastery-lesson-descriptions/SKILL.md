---
name: mastery-lesson-descriptions
description: Write, rewrite or review the customer-facing description of every session in a Mindvalley Mastery, Certification or cohort programme (lessons, workshops and labs, bonus calls, pre-recorded sessions, kick-offs, graduations) in the house style students see in the learning platform. Use whenever someone asks to write, rewrite, clean up, standardise or check lesson descriptions, session blurbs, workshop summaries or Airtable "Description" fields, or says descriptions read like internal notes, even if they never say "house style". Works from an Airtable Lessons table, a curriculum page or doc, or pasted text.
---

# Mastery lesson descriptions

Every live call in a Mastery has a description. Students read it in the learning platform before the session starts, and the same text often feeds the calendar, the emails and the app. So it is customer copy, not a note for the team.

The most common failure is internal notes passed off as descriptions: who runs which AI agent, which week reuses what, how the programme differs from a sister programme. That text is useful to the team but tells a student nothing about why to show up. This skill turns any of it into the house style, consistently, across every programme.

## Step 1: Ask for the materials

Send this, adapted to what the person has already shared, then wait:

> To write the descriptions, please share what you can. Links, pasted text, files or screenshots all work.
> 1. **The session list**: title, type (lesson, workshop or lab, bonus, graduation) and date for each. An Airtable Lessons table link is ideal.
> 2. **What each session covers**: the current descriptions, internal notes, a curriculum page, or transcripts for past sessions.
> 3. **Who teaches each session**, and which of those teachers are confirmed.
> 4. **Which lesson each workshop or lab follows**, if it isn't obvious from the order.
> 5. **Two or three descriptions you already like**, if there are any. Otherwise I'll use the house examples.

With Airtable connected, read the table yourself: titles, type, teacher, the slot or date, and the current description. Never write to Airtable until the person has approved the drafts (step 4).

## Step 2: Write each description to the formula

Every description has exactly two parts: **one paragraph**, then **a heading and a short bullet list**.

### Lesson
- **Paragraph, 60 to 100 words.** Open with a one-line hook: a truth or tension the student recognises ("A website brings visitors. A funnel turns them into leads."). Then "This week [Teacher] shows you how to..." and two or three sentences on what they'll do and come away with. Handle the obvious objection in a sentence when there is one ("No website yet? Ten minutes of you talking is enough to start.").
- **Heading:** `You'll learn:`
- **3 to 5 bullets**, each starting "How to...", "Why...", "Which..." or a short noun phrase. Skills and ideas, not tasks.

### Workshop or lab
- **Paragraph, 50 to 90 words.** Open from the lesson: "[Teacher]'s lesson gave you X. In this session, [Teacher] has you [apply it to your own business]." Then the concrete steps in the order they happen in the room, ending on something done live ("Before the session ends, your link goes in the community thread.").
- **Heading:** `You'll leave with:`
- **2 or 3 bullets**, each a finished artefact or result in the student's hands ("Your website rewritten and live, with a before and after score").

### Bonus call, pre-recorded session, kick-off, graduation
- **Paragraph, 30 to 80 words**: why it exists for them, what happens, when or how to watch.
- **Heading:** `You'll leave with:`
- **2 or 3 bullets.**
- Graduation may use "we" ("This is where we close the program together.").

### Voice rules
- Second person, present or future tense: "you'll build", never "students will" or "the participant".
- Outcomes over mechanics. Mention a tool or an AI role only when it is what the student sees and uses.
- Short, plain sentences. No dashes for asides; use a comma, colon or full stop. No emoji. No hype words ("revolutionary", "game-changing").
- Spelling and terms match the programme's other customer copy (Mindvalley customer copy uses "program").
- No pricing or payment language of any kind; the checker flags it.
- Plain bullet syntax, `- ` at the start of each line, no full stops at the end.

### What to strip from internal notes
Cut anything a student doesn't need before the session:
- how the team designed the lesson or why it sits in this week
- comparisons with other programmes ("The line with Expert & Authority: ...")
- staff roles, guides, packs, checklists or IDs named as internal assets
- chains of references to other weeks ("the inbox team reads it in week 5, the funnel in weeks 7 and 8..."). One forward pointer is fine ("From next week, every AI team you build writes in that voice.").
- placeholders such as [TBD], [CALL NAME] or "topic to be confirmed"

### Naming teachers
- Name the teacher only when they are **confirmed**. If the teacher may still change, write around it ("This week you'll learn...", "The lesson showed you...") so nothing needs rewriting when the line-up is settled.
- Workshops name the lesson's teacher in the opening line when that teacher is confirmed: "Vishen's lesson gave you the framework."

## Step 3: Check every draft

Save the drafts as JSON, a list of `{"title", "type", "description"}`, and run:

```
python scripts/check_descriptions.py descriptions.json
```

It checks:
- the heading for the session type
- paragraph length and bullet count
- second person throughout
- workshops opening from the lesson
- internal wording, money words, dashes, emoji and placeholders

Fix every FAIL. Fix each WARN, or decide on purpose to keep it. If Python isn't available, apply the same checks by eye.

## Step 4: Show, approve, then write

1. Show the person three representative drafts first: a lesson, a workshop and a bonus or graduation. Agree the voice before doing the rest.
2. Then show all of them, as a list in chat or as a preview page.
3. Only after approval, write them to the description field (in Airtable, the lesson's Description field). Change no other field.
4. Read the records back to check every one saved.
5. Keep the old text somewhere: a copy in the repo, or the record's Internal Notes. It is still the team's working brief.

## Files

- `references/examples.md`: approved descriptions for each session type, and one full before and after. Read it before writing; match its rhythm.
- `scripts/check_descriptions.py`: the checker for step 3.
