# NicheVault Apple-Level Experience Spec

This document defines how NicheVault should evolve from a strong concept into an Apple-level, production-ready product surface.

It is intentionally concrete. The goal is not to make the site more decorated — it is to make it calmer, clearer, and more trustworthy.

## Product-level principle

A visitor should understand three things within a few seconds:

1. **What NicheVault is**
2. **Why this matters to them**
3. **What the next honest action is**

Every page should support that sequence.

---

## Apple-level standard for NicheVault

### 1. Clarity before cleverness
- One dominant headline per page.
- One clear primary CTA per page.
- Supporting copy should reduce doubt, not repeat hype.
- Avoid multiple equal-weight sections competing above the fold.

### 2. Deference to the product promise
- Layout, gradients, shadows, and decorative treatments should never compete with the main message.
- The offer and primary next step should carry the page, not visual effects.
- If a section does not help the user understand value or decide what to do next, demote or remove it.

### 3. Honest launch-state behavior
- A CTA must reflect reality.
- If the waitlist is not live, label it as preview/prelaunch.
- If payment is not live, do not use `Buy Now` language.
- Never imply fulfillment speed or checkout readiness unless verified.

### 4. Calm premium rhythm
- Use generous spacing between major sections.
- Keep line lengths comfortable.
- Group related content tightly and separate unrelated content clearly.
- Let important content breathe instead of compressing multiple messages into the same visual band.

### 5. Accessibility as baseline quality
- Clear focus states on all interactive elements.
- Readable contrast for hero text, form labels, helper copy, and error states.
- Keyboard-usable form flow.
- Interaction states should not depend on color alone.

---

## Immediate corrections based on current repo surface

Current visible signals from the code audit:
- `index.html` uses `Join Free` in both the nav and hero CTA.
- `report-landing-page.html` uses `Buy Now with PayPal` and currently includes placeholder merchant details.
- The waitlist flow currently supports a placeholder Formspree configuration with fallback behavior.

These should be brought into alignment with a calmer, more honest experience.

---

## Page-by-page target state

## `index.html`

### Above-the-fold goal
The home page should communicate:
- what NicheVault finds
- who it helps
- what the visitor gets first

### Hero structure
Use this order:
1. short eyebrow / positioning label
2. one strong headline
3. one supporting paragraph
4. one primary CTA
5. one secondary reassurance line

### Copy behavior
- Replace vague ambition with concrete value.
- Prefer language about discovering under-served markets, validated opportunity, and decision support.
- Avoid stacking multiple promises in the hero.

### CTA rule
If the waitlist is not fully live:
- primary CTA should shift from `Join Free` to `Join Prelaunch List` or `Get Early Access`
- supporting text should explain what happens next
- success state should confirm whether the visitor joined a real list or a preview flow

If the waitlist is fully live:
- `Join Free` is acceptable, but only if the form is genuinely connected and tested

### Layout rule
- above the fold should contain one dominant message and one dominant action
- do not place too many proof blocks, explanation blocks, and offer variants before the user understands the core value

---

## `report-landing-page.html`

### Above-the-fold goal
The report page should answer:
- what this report is
- who it is for
- why it is worth paying for
- whether it is actually purchasable right now

### CTA rule
If payment is not configured:
- replace `Buy Now with PayPal` with `Request Access`, `Join Waitlist`, or `Preview Report Availability`
- remove or rewrite any copy implying immediate fulfillment
- add a short note that this is a preview / prelaunch offer

If payment is configured and tested:
- `Buy Now with PayPal` can remain
- add a short trust line only if true and verified
- keep the trust line quiet and factual, not salesy

### Information hierarchy
The page should present information in this order:
1. report value and audience
2. what is included
3. proof / sample insight
4. price and fulfillment expectations
5. primary CTA

### Tone rule
- calm confidence over urgency theater
- specific over generic
- fewer promises, more proof

---

## Typography and spacing guidance

### Headings
- Use fewer headline sizes, not more.
- The main headline should do most of the work.
- Avoid decorative emphasis inside the headline unless it materially improves comprehension.

### Body copy
- Keep paragraphs short and scan-friendly.
- Supporting text should read like product guidance, not ad copy.
- Avoid dense blocks immediately adjacent to CTAs.

### Spacing
- consistent vertical rhythm is mandatory
- repeated section patterns should use repeated spacing values
- CTA clusters need breathing room from surrounding text

---

## Interaction and state guidance

### Forms
- show field labels clearly
- show inline validation clearly
- show success and failure states explicitly
- tell the user what happens after submission

### Purchase / request actions
- if live, say what delivery timing is expected
- if preview, say what follow-up path is expected
- never let a broken or placeholder path look like a valid live transaction

### Navigation
- keep the nav light
- only one nav item should feel like the primary action
- avoid giving the nav CTA equal visual weight to too many other actions

---

## Definition of Apple-level done for NicheVault

NicheVault can be considered meaningfully closer to Apple-level when:
- each page has one clear focal point
- launch state is honest at all times
- the main CTA reflects real backend/payment reality
- supporting copy is tighter and less noisy
- interaction states are explicit and trustworthy
- the site feels calmer, more legible, and less eager to oversell

---

## Recommended implementation order

1. **Honor reality in CTAs**
   - switch CTA labels based on real configuration state
2. **Tighten hero hierarchy**
   - one message, one action, one reassurance
3. **Improve form/purchase states**
   - explicit success/failure/prelaunch messaging
4. **Reduce copy noise**
   - shorter supporting text, stronger grouping
5. **Polish spacing and typography**
   - only after hierarchy and truthfulness are fixed
