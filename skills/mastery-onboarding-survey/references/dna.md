# Mastery Onboarding Survey DNA, condensed

Source: "Mastery Onboarding Survey DNA" (Process DNA, Google Drive file `1AQV6LlZlJYJ-Q_YEoeDLZpBlEBadDWOf`, June 2026). This file keeps its rules and adds the exact option lists taken from the live forms, so every survey uses the same values.

## Contents
1. Purpose and ownership
2. Platform, reuse and naming
3. Timing, distribution, approval, reporting
4. Core block (exact options)
5. The two recurring sections
6. Question design principles
7. Standardisation checklist

## 1. Purpose and ownership

Onboarding surveys go to students before a programme begins. They capture background, experience level, goals, motivations and challenges, so hosts and speakers can tailor sessions and the business can segment each cohort.

Operations (Janja) builds them today, for historical reasons. Ownership should move to Customer Experience or Learning Experience, who sit closest to how the answers are used.

## 2. Platform, reuse and naming

- Built and hosted in Airtable, in the Forms tab (or an interface form page). Every submission is a record. Responses are read in a view named "Onboarding survey answers".
- **Reuse over rebuild.** Most programmes are relaunches. Don't create a new form or a new answers tab. Separate cohorts with views filtered by submission date. Add new questions to the existing form; remove old ones from the form without deleting the field, which keeps history. Build a new form only for a programme that has never run, or a complete redesign.
- **Title:** "[Program name]: Getting to Know You", for example "Spiritual Mastery: Getting to Know You".
- **Description:** a short intro line under the title, welcoming the student and saying their answers help tailor the programme.
- **Background:** the programme's key art.

## 3. Timing, distribution, approval, reporting

- **Timing:** set up about two weeks before the summit, as part of building the onboarding journey. Sent during onboarding, before the programme begins.
- **Distribution:** the link sits at several points in the automated onboarding emails; the host and concierges share it in the community.
- **Approval:** Operations sends it via Slack to Customer Experience and Learning Experience to review, edit and approve before it goes live. Keep this checkpoint after any ownership change.
- **Reporting:** Customer Experience analyses the answers and compiles a report for the whole Academy team; Author Relations or Learning Experience sends it on to the programme's speakers.
- **Response rate:** historically low. The journey was revamped so the survey appears more often. Monitor the rate against past cohorts.

## 4. Core block (exact options)

Every survey opens with this block. Wording and options below are the canonical set; the notes say where live forms drift.

| Question | Field type | Required | Options |
|---|---|---|---|
| Name | Short text | Required | |
| Email Address | Email | Required | Primary identifier and join key |
| Phone Number | Short text or phone | **Optional** | Social Media 2026 has it required; that breaks the standard |
| Gender | Single select | Required | Female · Male · Non-binary · Prefer not to say. Most forms lack Non-binary; Social Media 2026 has it. Adding it keeps the old values intact |
| Age Group | Single select | Required | 18-24 · 25-34 · 35-44 · 45-54 · 55-64 · 65+. Speaking & Influence, Manifesting and the clones start at 25-34 and stop at 55+; 55-64 and 65+ collapse into 55+ for comparison with older cohorts |
| Location | Country link (linked record to the Countries table) | Required | Timezone and language context |
| What is your personal annual income? | Single select | **Optional** | Under $25,000 · $25,000 – $49,999 · $50,000 – $74,999 · $75,000 – $99,999 · $100,000 – $149,999 · $150,000 – $199,999 · $200,000+ · Prefer not to say |
| Have you ever enrolled in any other Mastery or Certification programs? | **Multi-select** | Required | No previous programs · AI Mastery · Speaking & Influence Mastery · Manifesting Mastery · Social Media Mastery · Investing Mastery · Coaching Career Mastery · Health & Body Mastery · Entrepreneurship Mastery · Spiritual Mastery · Expert & Authority Mastery · AI for Founders Mastery · Mindvalley Certified Life Coach · Mindvalley Certified Hypnotherapist · Mindvalley Certified Business Coach · Mindvalley Certified Holobody Coach · Mindvalley Certified Money Coach. No cohort years: year-suffixed lists go stale every launch. Add any programme launched since |

Income was introduced on Manifesting Mastery and is now standard on every programme. "What is your desired personal income?" (same brackets, optional) belongs on Manifesting Mastery only.

Entrepreneurship Mastery adds "Are you a Mindvalley Certified Coach?" (dropdown, required) to its core block.

## 5. The two recurring sections

After the core block, every programme asks the same four things in its own language: experience level, current skills or tools, goals or desired outcome, and motivation for joining.

**A. Goals and motivation**
- A motivation or focus question: why they joined, or what they most want to work on now. Usually single select; multi-select where several motivations co-exist (Manifesting, Spiritual, Entrepreneurship).
- A desired-outcome question: the transformation they want by the end. Usually open text, because it can't be pre-categorised.
- Often a focus-areas question: the specific areas or formats they care about. Usually multi-select.

**B. Experience and current skills**
- A self-rated level: Beginner / Intermediate / Advanced, sometimes Expert, or an equivalent scale. Single select.
- Tenure or frequency: how long, or how regularly. Single select.
- Current tools, platforms or modalities: tailored to the programme. Usually multi-select.
- A skills self-assessment: least confident in and/or most want to master. Multi-select. Speaking & Influence adds 1 to 10 confidence and comfort ratings.

## 6. Question design principles

- **Mandatory vs optional.** Goals, intentions, motivations and skills are mandatory: they are why the survey exists. Supplementary fields ("anything else") are optional. Phone and personal income are always optional.
- **Open vs closed.** Default to dropdowns and pre-set choices, because closed answers group immediately in AI-assisted analysis. Use open text only when a dropdown is truly impossible, and categorise those answers with extra care. Example: follower and reach numbers vary too much to bracket, so they are open text.
- **Edit in place.** When questions change between cohorts, edit them on the reused form. AI Mastery's 2026 form rewrote its 2025 usage and aim options from judgmental phrasing ("Focus only on the low-hanging fruits of AI") into clearer, benefit-led descriptions without rebuilding the form.

## 7. Standardisation checklist

Apply when next editing any form, in place, without deleting fields:
- Add "Annual personal income" (dropdown, optional) where missing.
- Keep "Desired personal income" on Manifesting only.
- Set Phone Number to optional.
- Make goals, intentions, motivation and skills mandatory; leave comment fields optional.
- Prefer dropdowns; reserve open text for what can't be pre-categorised.
- Confirm the prior-programmes field is present and configured the same way everywhere.
