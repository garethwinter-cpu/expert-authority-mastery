#!/usr/bin/env python3
"""Audit a Mindvalley Mastery onboarding form against the Mastery Onboarding Survey DNA.

Input: the JSON that Airtable's get_form_schema returns, saved to a file (a tool-result wrapper with the JSON
inside a text field also works). Output: a Markdown report of what passes, what to fix, and an estimated
completion time.

Usage:
  python audit_form.py form.json --programme "AI for Founders Mastery" [--promise-minutes 3]
"""
import argparse, json, re, sys

STANDARD_AGES = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
STANDARD_INCOME = ["Under $25,000", "$25,000 – $49,999", "$50,000 – $74,999", "$75,000 – $99,999",
                   "$100,000 – $149,999", "$150,000 – $199,999", "$200,000+", "Prefer not to say"]
GENERIC_SECTIONS = {"group 1", "group 2", "new group", "untitled", "section 1", ""}
# words that betray a form cloned from another programme; checked only against labels and non-history options
TOPIC_WORDS = {
    "speaking": ["speak", "speaking", "stage talk", "public speaker", "presentation"],
    "manifesting": ["manifest"],
    "spiritual": ["spiritual", "chakra", "reiki", "higher self"],
    "social media": ["follower", "social media", "reels", "tiktok"],
    "ai": ["ai tool", "ai experience", "artificial intelligence"],
}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
SECONDS = {"one_tap": 6, "short_text": 20, "long_text": 40}

def load(path):
    raw = open(path, encoding="utf-8").read()
    data = json.loads(raw)
    if isinstance(data, dict) and "sections" not in data:
        for v in data.values():           # tool-result wrappers: {"result": "<json>"} or similar
            if isinstance(v, str) and '"sections"' in v:
                return json.loads(v)
    if isinstance(data, list) and data and isinstance(data[0], dict) and "text" in data[0]:
        return json.loads(data[0]["text"])
    return data

def elements(form):
    for s in form.get("sections", []):
        for r in s.get("rows", []):
            for e in r.get("elements", []):
                yield s, e

def choices(e):
    return [c.get("name", "") for c in (e.get("options") or {}).get("choices", [])]

def find(form, *patterns):
    for s, e in elements(form):
        lab = e.get("label", "").lower()
        if any(re.search(p, lab) for p in patterns):
            return e
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("form")
    ap.add_argument("--programme", default="")
    ap.add_argument("--promise-minutes", type=float, default=None, help="the length the onboarding emails promise, if any")
    a = ap.parse_args()
    form = load(a.form)
    fix, ok = [], []
    prog = a.programme.strip()
    title = form.get("name", "")

    # title and description
    if not re.search(r":\s*Getting to Know You\s*$", title):
        fix.append(f'Title is "{title}". The DNA format is "[Programme name]: Getting to Know You".')
    elif prog and prog.lower().split(" 20")[0] not in title.lower():
        fix.append(f'Title "{title}" does not name {prog}.')
    else:
        ok.append(f'Title follows the DNA: "{title}".')
    desc = form.get("description") or ""
    if not desc:
        fix.append("No intro line under the title. Add one or two sentences saying the answers shape the sessions.")
    elif len(desc) > 320:
        fix.append(f"Intro line is {len(desc)} characters. Keep it to one or two sentences; state the promised length.")

    # core block
    core = {
        "Name": find(form, r"^name$", r"full name"),
        "Email": find(form, r"email"),
        "Phone": find(form, r"phone"),
        "Gender": find(form, r"gender"),
        "Age group": find(form, r"age"),
        "Location": find(form, r"location", r"country"),
        "Personal annual income": find(form, r"(annual|current).*income", r"income\?$", r"personal annual"),
        "Programme history": find(form, r"enrolled", r"other mastery", r"certification program"),
    }
    for k in ["Name", "Email", "Gender", "Age group", "Location"]:
        e = core[k]
        if not e: fix.append(f"Core block: no {k} question.")
        elif not e.get("isRequired"): fix.append(f"Core block: {k} should be required.")
    ph = core["Phone"]
    if ph and ph.get("isRequired"): fix.append("Phone Number is required. The DNA standardised it as optional.")
    inc = core["Personal annual income"]
    if not inc: fix.append("No personal annual income question. Add it (single select, optional, standard brackets).")
    else:
        if inc.get("isRequired"): fix.append("Personal annual income is required. The DNA says optional.")
        if choices(inc) and choices(inc) != STANDARD_INCOME:
            fix.append("Income brackets differ from the standard list in references/dna.md, which breaks cross-programme comparison.")
    age = core["Age group"]
    if age:
        got = choices(age); missing = [b for b in STANDARD_AGES if b not in got and not (b in ("55-64", "65+") and "55+" in got)]
        if missing: fix.append(f"Age Group is missing {', '.join(missing)}. Standard bands: {' · '.join(STANDARD_AGES)}.")
        order = [b for b in got if b in STANDARD_AGES or b == "55+"]
        if order != sorted(order, key=lambda b: (STANDARD_AGES + ["55+"]).index(b) if b != "55+" else 4.5):
            fix.append("Age Group options are out of order.")
    g = core["Gender"]
    if g and "Prefer not to say" not in choices(g): fix.append('Gender has no "Prefer not to say".')
    hist = core["Programme history"]
    if not hist: fix.append('No "Have you ever enrolled in any other Mastery or Certification programs?" question (required by the DNA).')
    else:
        if hist.get("fieldType") != "multipleSelects": fix.append("Programme history is single select. Make it multi-select: people have taken more than one.")
        yrs = [c for c in choices(hist) if re.search(r"20\d\d", c)]
        if yrs: fix.append(f"Programme history lists cohort years ({len(yrs)} options, e.g. \"{yrs[0]}\"). Year-suffixed lists go stale every launch; list programmes without years.")
        if not hist.get("isRequired"): fix.append("Programme history should be required.")
    desired = find(form, r"desired.*income")
    if desired and "manifest" not in prog.lower():
        fix.append("Desired personal income is asked. The DNA keeps it on Manifesting Mastery only.")

    # sections
    for s in form.get("sections", []):
        if (s.get("title") or "").strip().lower() in GENERIC_SECTIONS:
            fix.append(f'Section titled "{s.get("title")}". Give it a real title such as "About you".')

    # cloned-programme residue
    if prog:
        pl = prog.lower()
        for topic, words in TOPIC_WORDS.items():
            if topic in pl or (topic == "ai" and re.search(r"\bai\b", pl)): continue
            hits = []
            for s, e in elements(form):
                if e is hist: continue
                text = " ".join([e.get("label", ""), " ".join(choices(e)), s.get("title") or ""]).lower()
                if any(w in text for w in words): hits.append(e.get("label"))
            if hits:
                fix.insert(0, f'**Inherited from another programme ({topic}):** {len(hits)} question(s) still ask about {topic}, starting with "{hits[0]}". '
                              f'Students of {prog} see these now. Replace them with questions written for {prog}.')

    # options: emoji, Other without follow-up
    conditional_on = set()
    for s, e in elements(form):
        for f in (e.get("visibilityFilters") or {}).get("filterSet", []):
            conditional_on.add(f.get("fieldId"))
    for s, e in elements(form):
        cs = choices(e)
        if any(EMOJI.search(c) for c in cs):
            fix.append(f'Emoji in the options of "{e.get("label")}". Use plain text; emoji split answers in analysis.')
        if any(c.strip().lower().startswith("other") for c in cs) and e.get("fieldId") not in conditional_on:
            fix.append(f'"{e.get("label")}" offers Other with no conditional "Please specify" field.')

    # goals and skills required
    for s, e in elements(form):
        lab = e.get("label", "").lower()
        if re.search(r"goal|motivat|focus|transformation|confident|love to master|hope to achieve|aim", lab) and not e.get("visibilityFilters"):
            if not e.get("isRequired"): fix.append(f'"{e.get("label")}" is a goals or skills question and should be required.')

    # count and time
    one_tap = short = long_ = conditional = 0
    for s, e in elements(form):
        if e.get("visibilityFilters"): conditional += 1; continue
        t = e.get("fieldType", "")
        if t in ("multilineText", "richText"): long_ += 1
        elif t in ("singleLineText", "email", "phoneNumber", "number", "url"): short += 1
        else: one_tap += 1
    secs = one_tap * SECONDS["one_tap"] + short * SECONDS["short_text"] + long_ * SECONDS["long_text"]
    open_req = sum(1 for s, e in elements(form) if e.get("fieldType") in ("multilineText", "richText") and e.get("isRequired") and not e.get("visibilityFilters"))
    if open_req > 2: fix.append(f"{open_req} required long-text questions. The DNA prefers lists; keep open text for what can't be categorised.")
    if a.promise_minutes is not None and secs / 60 > a.promise_minutes + 0.5:
        fix.append(f"Estimated {secs/60:.1f} minutes against a promise of {a.promise_minutes:g}. Pre-fill name and email, or cut programme questions that feed the fewest weeks.")

    print(f"# Audit: {title or '(untitled form)'}\n")
    print(f"Source table: {form.get('sourceTableName', form.get('sourceTableId', '?'))} · form page {form.get('pageId', '?')}\n")
    print(f"**Count:** {one_tap} one-tap, {short} short typed, {long_} long typed, {conditional} conditional. "
          f"Estimated {secs/60:.1f} minutes before pre-fill.\n")
    print(f"## To fix ({len(fix)})")
    for f in fix: print(f"- {f}")
    if not fix: print("- Nothing. The form matches the DNA.")
    print(f"\n## Passing")
    for o in ok: print(f"- {o}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
