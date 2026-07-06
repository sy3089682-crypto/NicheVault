# NicheVault Launch-State Manual Verification

This playbook defines the **minimum trustworthy verification pass** for the two public conversion surfaces in `NicheVault`:

- `index.html`
- `report-landing-page.html`

It exists because the repo currently presents public-facing HTML surfaces without a visible automated browser test harness on the public audit surface. Until a stronger automated check exists, this manual pass is the baseline release gate for launch-state truthfulness.

Use this together with:

- `PRODUCTION_READINESS.md`
- `APPLE_LEVEL_EXPERIENCE_SPEC.md`
- `LAUNCH_STATE_TRUTH_MATRIX.md`
- issue `#3` — fail closed when launch config is placeholder-based on waitlist and report pages

---

## Release rule

Do **not** call either page production-ready until every required scenario below passes.

If a scenario fails or is ambiguous, the release decision is `prelaunch`, not `live`.

---

## What this pass protects

This verification pass is specifically designed to prevent the most trust-damaging launch mistakes:

- live-sounding CTA copy shown while placeholder config is still active
- local/demo/manual fallback behavior presented as if it were a live backend path
- placeholder checkout shown as the primary action
- purchase-only trust claims shown while payment is not truly configured
- inaccessible or unclear success/error states after submission attempts

---

## Required environments to simulate

Run the checks below in both of these modes:

### Mode A — `prelaunch`
Use placeholder or intentionally non-live configuration.

Examples:
- `FORMSPREE_ID === 'YOUR_FORM_ID'`
- PayPal business identity still placeholder-based
- any flow that still depends on local capture, demo wiring, or manual follow-up

### Mode B — `live`
Use real configured values for the relevant flow.

Only test this mode when the destination really exists and the next step is functional.

---

## Device and access modes

Each required scenario should be checked in these contexts:

- desktop viewport
- mobile viewport
- keyboard-only navigation

If dynamic status messages are present, verify that they are exposed through a polite `aria-live` region or an equivalently accessible status pattern.

---

## Scenario matrix

## 1) Landing page (`index.html`) in `prelaunch`

### Goal
Make sure the page feels calm and premium while clearly behaving like a prelaunch surface.

### Verify
- the nav CTA does **not** imply general availability if the form path is still placeholder-based
- the hero CTA does **not** imply immediate access when the system is still prelaunch
- one short support line explains the prelaunch nature of the flow without adding noisy warning UI
- if the user submits successfully through a non-live/manual path, the success message says exactly what happened
- if the submit fails, the error message is plain-language and does not imply capture succeeded
- keyboard users can still reach one obvious primary action without confusion

### Fail the scenario if
- `Join Free` remains the dominant CTA while placeholder config is active
- the page hides the fact that follow-up may be manual
- the success state sounds like a live backend confirmation when it was only locally stored or manually routed

---

## 2) Landing page (`index.html`) in `live`

### Goal
Make sure live wording appears only when the waitlist/signup path is truly configured.

### Verify
- general-availability CTA wording appears only in real live mode
- submit success reflects a real successful endpoint call
- submit failure remains understandable and does not trap the user
- the support copy stays concise and does not over-promise access beyond the real system behavior

### Fail the scenario if
- a real endpoint is configured but the messaging still reflects outdated prelaunch wording
- the UI implies instant access when the user is actually only joining a queue

---

## 3) Report page (`report-landing-page.html`) in `prelaunch`

### Goal
Ensure the page invites interest honestly without pretending checkout is live.

### Verify
- the primary CTA communicates release interest / early access / waitlist intent instead of immediate purchase
- purchase-only trust copy is absent when checkout is not truly configured
- placeholder checkout is not presented as the dominant action
- supporting text explains the truthful next step in one restrained line
- mobile layout still preserves one clear next action and calm hierarchy

### Fail the scenario if
- the page still uses live purchase framing such as `Get the Report for $49` while placeholder checkout is active
- checkout trust claims remain visible without a real verified payment path
- the primary action still opens or submits placeholder commerce flow

---

## 4) Report page (`report-landing-page.html`) in `live`

### Goal
Ensure purchase messaging appears only when backed by a real path.

### Verify
- purchase CTA wording returns only in live mode
- checkout trust copy is displayed only when it matches the real configured experience
- the purchase path is functional and aligned with the claims around delivery and follow-up
- the page still feels restrained and focused, with one clear primary action

### Fail the scenario if
- the checkout is technically wired but the trust copy overstates what the user receives or when they receive it
- the page mixes live purchase language with prelaunch fallback messaging

---

## 5) Cross-page consistency check

### Goal
Ensure both surfaces obey the same launch-state contract.

### Verify
- both pages fail closed to `prelaunch` when configuration is ambiguous
- both pages use calm, truthful, non-alarmist prelaunch copy
- both pages reserve live-sounding copy for actual live mode only
- both pages keep one obvious primary action instead of multiple competing focal points
- dynamic success/failure feedback remains accessible and readable on both surfaces

### Fail the scenario if
- one page is honest about prelaunch state while the other still sounds fully live
- the same configuration condition produces inconsistent messaging across pages

---

## Lightweight run sheet

Use this table during each verification pass.

| Surface | Mode | Desktop | Mobile | Keyboard only | Status messaging truthful | Result |
| --- | --- | --- | --- | --- | --- | --- |
| `index.html` | `prelaunch` | ☐ | ☐ | ☐ | ☐ | pass / fail |
| `index.html` | `live` | ☐ | ☐ | ☐ | ☐ | pass / fail |
| `report-landing-page.html` | `prelaunch` | ☐ | ☐ | ☐ | ☐ | pass / fail |
| `report-landing-page.html` | `live` | ☐ | ☐ | ☐ | ☐ | pass / fail |

---

## Evidence to capture while verifying

For each failed or questionable scenario, note:

- exact mode (`prelaunch` or `live`)
- page name
- visible CTA text
- visible support copy
- what actually happened after click/submit
- whether the result was truthful, ambiguous, or misleading
- whether the issue was visual hierarchy, copy, configuration detection, or accessibility

Short screenshots or screen recordings are helpful, but the written note must still explain the trust mismatch clearly.

---

## Definition of done for the next code wave

The next implementation wave is only complete when:

1. placeholder configuration automatically forces truthful `prelaunch` messaging on both pages
2. live configuration restores live wording only where it is truly supported
3. placeholder checkout is not the primary action in `prelaunch`
4. success and failure messages describe the real outcome clearly
5. mobile, desktop, and keyboard-only checks all pass
6. the pages still feel calm, premium, and intentionally designed

If there is uncertainty, ship the calmer `prelaunch` state and keep trust intact.
