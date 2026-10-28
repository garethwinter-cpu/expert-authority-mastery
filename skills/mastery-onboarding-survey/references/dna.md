# Mastery Onboarding Survey DNA, condensed

Everything from Mindvalley's "Mastery Onboarding Survey DNA" (Process DNA, June 2026) that a survey needs: the rules, the process, the exact core block and every programme's question set. You don't need the original document. Where the live forms add detail the DNA lacks (exact age bands, Non-binary, programmes launched since), it is folded in here.

## Contents
1. Purpose and ownership
2. Platform, reuse and naming
3. Timing, distribution, approval, reporting
4. Core block (exact options)
5. The two recurring sections
6. Question design principles
7. Standardisation checklist
8. Annex: every programme's questions

## 1. Purpose and ownership

Onboarding surveys go to students before a programme begins. They capture background, experience level, goals, motivations and challenges, so hosts and speakers can tailor sessions and the business can segment each cohort.

Operations builds them today, for historical reasons rather than by design. Ownership should move to Customer Experience or Learning Experience, who sit closest to how the answers are used.

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
8. Annex: every programme's questions

Apply when next editing any form, in place, without deleting fields:
- Add "Annual personal income" (dropdown, optional) where missing.
- Keep "Desired personal income" on Manifesting only.
- Set Phone Number to optional.
- Make goals, intentions, motivation and skills mandatory; leave comment fields optional.
- Prefer dropdowns; reserve open text for what can't be pre-categorised.
- Confirm the prior-programmes field is present and configured the same way everywhere.

## 8. Annex: every programme's questions

Each programme opens with the core block, then adds these. Use them to borrow wording and option lists that students already understand. "Req" means required on the live form, which is not always what the DNA wants: see the drift notes in `live-forms.md`.

### AI Mastery
Focus: role, organisation, current AI use, tools and ambition, so content is pitched from "save time" users to people who already build AI systems.

| Question | Type | Req | Options |
|---|---|---|---|
| What best describes your current position or role? | Single | Yes | Employee · Middle Manager · Executive · CEO / Founder |
| What is the size of your organization? | Single | Yes | Solopreneur · Startup (up to 10) · Small (10–49) · Medium (50–249) · Large (250+) |
| What is your primary functional area or department? | Dropdown | Yes | Function list |
| Which industry are you currently working in? | Dropdown | Yes | Industry list |
| How frequently do you currently use AI in your personal or professional life? | Single | Yes | I'm just getting started · I use AI occasionally · I use AI regularly for work · I build prompts, workflows, or automations · I already build AI tools or systems |
| How would you rate your AI expertise prior to AI Mastery? | Single | Yes | Beginner · Intermediate · Advanced |
| In which areas are you already using AI (if any)? | Multi | Yes | Business Automation · Graphic & Video · Writing · Research · Data Analysis · Marketing · Personal Productivity · Coaching/Tutoring · Mental Health & Wellbeing |
| Which AI tools have you used before? | Multi | Yes | ChatGPT · Claude · Perplexity · Midjourney · DALL·E · ElevenLabs · Gemini · Microsoft Copilot · Other |
| My aim during AI Mastery is to… | Single | Yes | Save time in daily work · Improve business/career · Build simple AI tools & automations · Build advanced AI systems & products · Deeply understand how AI works |
| What do you hope to achieve after completing this program? | Open | Yes | |

The 2025 form judged people ("Never used AI actively before", "Focus only on the low-hanging fruits of AI"). The 2026 form rewrote these as plain, benefit-led options, in place on the same form. Write options a student is happy to pick.

### Social Media Mastery
Focus: platforms, audience size and reach, the platform to grow, whether they earn from it, formats and skills.

| Question | Type | Req | Options |
|---|---|---|---|
| How would you describe your experience with social media content creation? | Single | Yes | Beginner · Intermediate · Advanced |
| How long have you been creating content for your brand/business/professional purposes? | Single | Yes | I'm just starting · 6–12 months · 1–2 years · 2+ years |
| Which social media platforms are you currently active on? | Multi | Yes | Instagram · TikTok · YouTube · LinkedIn · Facebook · Other |
| Which platform is your top priority right now? | Single | Yes | Instagram · TikTok · YouTube · LinkedIn · Facebook · Not sure yet |
| Please share your current follower count for each platform. | Open | Yes | e.g. "Instagram ~3k, TikTok ~500". Too varied to bracket |
| What is your average post reach or view count on these platforms? | Open | Yes | e.g. "Instagram Reels ~3k views" |
| What is your primary goal for joining Social Media Mastery? | Single | Yes | Grow audience · Build brand authority · Sell products/services · Generate leads · Become full-time creator · Explore · Other |
| Which content formats are you most interested in mastering? | Single | Yes | Short-form video · Long-form video · Written content · Storytelling/brand · Educational · Sales & conversion |
| Are you currently making money from social media? | Single | Yes | No, not yet · Yes, occasionally · Yes, side income · Yes, main income |
| What challenges have you faced in growing your social media presence? | Open | Yes | |
| What specific skills or topics are you most excited to learn or improve? | Open | Yes | |

### Manifesting Mastery
Focus: experience, daily practice, techniques, blocks and successes, life areas. The only programme with desired income.

| Question | Type | Req | Options |
|---|---|---|---|
| What is your annual personal income? | Dropdown | No | Core-block brackets |
| What is your desired personal income? | Dropdown | No | Same brackets. Manifesting only |
| How would you describe your experience with manifestation? | Single | Yes | Beginner · Intermediate · Advanced · Expert |
| How long have you been practicing manifestation techniques? | Single | Yes | <6 months · 6 months–1 year · 1–3 years · 3+ years |
| Do you currently have a daily manifestation practice? | Single | Yes | Yes · I'm working on building one · No |
| Which manifestation techniques have you used before? | Multi | Yes | Visualization · Affirmations · Meditation · Journaling · Energy Work · Quantum Leaping · Other |
| What has been your biggest success with manifestation so far? | Open | Yes | |
| What challenges or blocks have you faced in your manifestation journey? | Open | Yes | |
| What motivated you to join the Manifesting Mastery program? | Single | Yes | Learn basics · Deepen advanced techniques · Overcome blocks · Manifest specific goals · Other |
| Are there specific areas of your life you'd like to focus on manifesting? | Multi | Yes | Wealth/Abundance · Career/Business · Relationships · Health/Wellness · Personal Growth · Spiritual Connection · Other |
| What specific goals or outcomes are you hoping to manifest during this program? | Open | Yes | |
| Are there any specific skills or topics you're eager to learn or improve? | Open | Yes | |

### Entrepreneurship Mastery
Focus: whether they run a business, certified-coach status, current focus, and the fullest skills self-assessment.

| Question | Type | Req | Options |
|---|---|---|---|
| Are you a Mindvalley Certified Coach? | Dropdown | Yes | Added to the core block |
| Do you currently run a business? | Single | Yes | Yes, full-time · Yes, part-time / side hustle · No, preparing to start · No, here to explore |
| Which of these best describes your focus right now? | Multi | No | Overcome self-sabotage · Find/validate idea · Create offers & revenue · Grow audience/reach · Scale systems & team · Build wealth & legacy · Other |
| What transformation do you want to walk away with by the end of this program? | Open | No | |
| Which of these elements do you feel least confident in? | Multi | No | Founder mindset · Finding/validating idea · Offers · Copy/marketing · Sales & pitching · Funnels · Scaling revenue · Finances · Hiring/leading · Systems · Networking · AI & automation · Time/energy/focus |
| Which of these would you love to master? | Multi | No | $10M vision · Product-market fit · Scalable revenue · Influence & sales · Marketing campaigns · Personal/company brand · Systems/delegation/AI · Negotiation · Multiple income streams · Wealth & legacy · Leading with confidence |

### Speaking & Influence Mastery
Focus: speaking contexts, two 1 to 10 baselines, focus, skills. The model for any programme with a measurable before-and-after.

| Question | Type | Req | Options |
|---|---|---|---|
| Do you currently speak or present regularly in any context? | Dropdown | Yes | Yes, regularly · Occasionally · Rarely · Never |
| What speaking environments are you currently most familiar with (if any)? | Multi | Yes | Corporate · Public/keynote · On camera · Webinars/workshops · Coaching/facilitating · Don't speak publicly yet · Other · None |
| On a scale of 1–10, how confident are you currently in your speaking abilities? | 1–10 | Yes | |
| On a scale of 1–10, how comfortable are you currently when speaking? | 1–10 | Yes | |
| Which of these best describes your focus right now? | Single | Yes | Get over fear · Become paid speaker · Speak in job/career · Attract followers/clients · Influence through content · Feel powerful & clear · Other |
| What transformation do you want to walk away with by the end of this program? | Open | Yes | |
| Which of these elements do you feel least confident in? | Multi | Yes | Structuring a talk · Storytelling · Nerves · Clarity & energy · Speaking spontaneously · Voice & body · Influence/conversion · On camera · Q&A / tough audiences |
| Which of these would you love to master? | Multi | Yes | Unforgettable stage talks · Viral content · No notes/slides · Hold attention · Persuade in business · Webinars/virtual events · Sell from stage/video · Authority on command |

### Spiritual Mastery
Focus: relationship with spirituality, practice, tenure, modalities, motivations, blocks.

| Question | Type | Req | Options |
|---|---|---|---|
| How would you describe your current relationship with spirituality? | Single | Yes | New to spirituality · Curious & exploring · Regular practice · Deep path for years · Advanced in spiritual growth |
| Do you currently have a daily spiritual practice? | Single | Yes | Yes, consistently · Yes, but inconsistently · Not yet, but I want to · No |
| For how long have you been exploring spiritual or energetic practices? | Single | Yes | <6 months · 6 months–1 year · 1–3 · 3–5 · 5–10 · 10+ years |
| Which spiritual or energetic modalities have you practiced or experienced so far? | Multi | Yes | Meditation · Breathwork · Journaling · Visualization · Energy Work/Reiki · Chakra/Meridian · Automatic Writing · Intuition Training · Shamanic · Manifestation · Nature rituals · Prayer/devotion · Other |
| What motivated you to join Spiritual Mastery? | Multi | Yes | Deepen connection · Strengthen intuition · Heal/release pain · Peace & alignment · Consistent practice · Understand energy · Connect with Higher Self · Purpose clarity · Improve relationships · Transformation · Other |
| What challenges, blocks, or patterns do you face on your spiritual journey? | Multi | Yes | Calming the mind · Trusting intuition · Emotional heaviness · Feeling disconnected · Inconsistency · Self-doubt · Letting go/forgiving · Feeling stuck · Overwhelm · Staying present · Other |
