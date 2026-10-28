# What the live forms and recent surveys teach

Read when writing programme questions: what each live form does well, where it drifts from the DNA, and what the two most recent surveys added. Full question sets are in the annex of `dna.md`.

## Contents
- Speaking & Influence Mastery (live form)
- Spiritual Mastery (live form)
- Social Media Mastery 2026 (live form)
- Manifesting Mastery (live form)
- AI Mastery (DNA annex and live table)
- Entrepreneurship Mastery (DNA annex)
- Expert & Authority Mastery (spec, September 2026)
- AI for Founders Mastery (approved survey, October 2026)
- Drift seen across forms

## Speaking & Influence Mastery
- **Sections:** "Group 1" (core), "Speaking Experience", "Goals", "Skills".
- **Experience:** "Do you currently speak or present regularly in any context?" (Yes, regularly · Occasionally · Rarely · Never). "What speaking environments are you currently most familiar with (if any)?" (multi: corporate, keynote, on camera, webinars, coaching groups, don't speak publicly yet, other, none).
- **Baselines:** two 1 to 10 ratings, "how confident are you currently in your speaking abilities?" and "how comfortable are you currently when speaking?". This is the model for any programme with a measurable before-and-after.
- **Goals:** "Which of these best describes your focus right now?" (single, six "I want to…" options plus Other, with a conditional required "If you chose Other, please specify."). Then "What transformation do you want to walk away with by the end of this program?" (open, required).
- **Skills:** "Which of these elements do you feel LEAST confident in?" and "Which of these would you LOVE to master?" (both multi, required, "(check all that apply)" as helper text).
- **Drift:** age bands start at 25-34; emoji in the environment options; section title "Group 1". It has income (optional) and no programme-history field on the form.

## Spiritual Mastery
- **Best practice:** the only form with the programme-history question as a **multi-select without cohort years**, and an 18-24 age band.
- **Experience:** relationship with spirituality (five first-person stages, from "I'm completely new to spirituality" to "I consider myself advanced in spiritual growth"); daily practice (Yes, consistently · Yes, but inconsistently · Not yet, but I want to · No); tenure (six bands); modalities (multi with Other, followed by an optional conditional "Please specify.").
- **Goals & Intentions:** motivation (multi, eleven "I want to…" options plus Other) and challenges or blocks (multi, eleven options plus Others), each followed by an optional conditional "Please specify.".
- **Drift:** no desired-outcome open question and no income field; core section titled "New Group"; inconsistent "Other" and "Others".

## Social Media Mastery 2026
- **Best practice:** the fullest age bands (18-24 to 65+) and Non-binary in Gender; experience levels with descriptions, as in "Beginner (just starting or inconsistent)"; a conditional follow-up ("If yes, how are you monetizing?") shown only when it applies.
- **Experience:** level, tenure, platforms (multi), top-priority platform (single), follower counts and average reach (open text, because they can't be bracketed).
- **Goals & Challenges:** primary goal (single), content format to master (single), whether they earn from social (single), challenges (open), skills to learn (open).
- **Drift:** **phone number required** (the DNA says optional); no income; no programme history; four open-text questions, heavy for analysis.

## Manifesting Mastery
- **Best practice:** both income questions, annual and desired, optional, with identical brackets. Desired income belongs only here.
- **Experience:** level (Beginner · Intermediate · Advanced · Expert), tenure, daily practice, techniques (multi), biggest success (open), blocks (open).
- **Goals & Intentions:** motivation (single plus Other with a conditional), life areas (multi), goals for the programme (open), skills to learn (open).
- **Drift:** age options out of order and starting at 25-34; four required open-text questions.

## AI Mastery
- **Background:** position or role (Employee · Middle Manager · Executive · CEO / Founder), organisation size (Solopreneur · Startup up to 10 · Small 10–49 · Medium 50–249 · Large 250+), functional area, industry.
- **AI experience:** usage frequency ("I'm just getting started" to "I already build AI tools or systems"), self-rated expertise (Beginner · Intermediate · Advanced), areas already using AI (multi), tools used (multi: ChatGPT, Claude, Perplexity, Midjourney, DALL·E, ElevenLabs, Gemini, Microsoft Copilot, Other).
- **Goals:** "My aim during AI Mastery is to…" (single: save time, improve business or career, build simple tools and automations, build advanced systems and products, deeply understand AI) and "What do you hope to achieve after completing this program?" (open).
- **Lesson:** the 2026 rewrite of usage and aim options into benefit-led, non-judgmental wording, done in place.

## Entrepreneurship Mastery
- Certified-coach status in the core block; "Do you currently run a business?" (full-time, part-time, preparing, exploring); focus (multi); desired transformation (open); a thirteen-option LEAST confident list and an eleven-option LOVE to master list.
- **Drift:** focus, transformation and both skills lists are optional, against the DNA rule that goals and skills are mandatory.

## Expert & Authority Mastery (spec, 14 September 2026)
- Five questions copy the summit quiz word for word, so quiz and survey join per student.
- Every programme question names the week it feeds.
- An inventory question ("Which of these do you already have?") feeds the week that builds on it.
- Two 1 to 10 baselines tied to specific weeks and re-asked at graduation.
- Practical questions: live-call attendance forecast, consent to a student story, anything else.

## AI for Founders Mastery (approved survey, October 2026)
The full survey is `examples/aif-survey.json`. It is the standard to meet.
- **Found by audit:** the live form linked from every welcome email was still another programme's form with a new title, asking founders about public speaking. Check the questions of any form a programme inherits, not just its title.
- **Its first draft failed review.** It went straight to a build spec with field types and IDs, so nobody could see the survey a student would see. A clickable preview fixed that in one round.
- **What made the approved version better:**
  - "love to have" and "least confident" share one nine-item list in curriculum order, pick up to three on each
  - one decisive question ("Have you used Claude Code before?") replaces an eight-tool list
  - a website address collected as the before-and-after artefact
  - a closed reflection question ("If AI gave you back one day a week…")
  - summit attendance
  - four measures asked again at graduation
  - a thank-you screen with the next three dates
  - years in business cut, because stage and revenue already answered it
- 28 questions, about 3.6 minutes of required answers; the intro says four.

## Drift seen across forms
| Drift | Where | Fix |
|---|---|---|
| Form inherited from another programme still asks its questions | AI for Founders (a Speaking & Influence clone) | Replace the questions; keep the page so email links work |
| Phone required | Social Media 2026 | Make optional |
| Age bands start at 25-34 or stop at 55+ | Speaking, Manifesting, clones | Use the six bands in `dna.md` |
| Programme history single-select or with cohort years | Speaking clone, AI for Founders clone | Multi-select, no years |
| No income field | Spiritual, Social Media | Add, optional |
| Section titled "Group 1" or "New Group" | Speaking, Spiritual, Social Media, Manifesting | Name it "About you" |
| Emoji in option labels | Speaking | Plain text |
| Goals or skills optional | Entrepreneurship (annex) | Required |
| Many required open-text questions | Social Media, Manifesting | Convert to lists where categories exist |
