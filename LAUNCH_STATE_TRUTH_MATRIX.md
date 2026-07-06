# Launch-State Truth Matrix

This file defines the smallest shared truth contract for `NicheVault` public conversion surfaces.

The goal is simple: if a visitor-facing action is not genuinely live, the page must present a calm, premium **prelaunch** state instead of sounding launch-ready.

This keeps the product trustworthy while the real lead-capture and checkout paths are still being hardened.

## State model

Use only two public launch states:

- `prelaunch` — any placeholder, manual, local-only, demo, or ambiguous conversion path is still active
- `live` — the real conversion path is configured, verified, and ready for public traffic

If there is any doubt, resolve to `prelaunch`.

## Resolver rules

Treat the page as `prelaunch` when any of the following is true:

- `FORMSPREE_ID === 'YOUR_FORM_ID'`
- the main waitlist flow still depends on browser `localStorage` as the primary storage path
- the main waitlist flow still auto-opens `mailto:` for the visitor
- the PayPal business value is placeholder-based, including `YOUR_PAYPAL_EMAIL@example.com`
- a report purchase path behaves like a demo, manual-release, or placeholder checkout flow
- the implementation cannot clearly prove that the real endpoint or checkout flow is available

Treat the page as `live` only when the real endpoint or checkout path is configured and the primary action has been manually verified.

## Shared product rules

Across all conversion surfaces:

1. The primary CTA label must match the resolved launch state.
2. Dynamic follow-up copy must describe the real outcome, not the intended future outcome.
3. The page root should expose `data-launch-state="prelaunch"` or `data-launch-state="live"`.
4. Each page should have one polite status region: `aria-live="polite"`.
5. Email contact can exist as a secondary option, but the primary flow must not surprise visitors by opening their mail client.
6. Purchase-only trust language must never appear while checkout is still placeholder-based.
7. Prelaunch mode should still feel premium: calm, minimal, readable, and honest.

## Surface truth matrix

| Surface | `prelaunch` | `live` | Never allow |
| --- | --- | --- | --- |
| Landing nav CTA | `Join the Prelaunch Waitlist` | `Join Free` | Launch-ready CTA copy while placeholder config is active |
| Landing hero CTA | `Request Early Access →` | `Join Free →` | Live-sounding join CTA when the flow is local/manual only |
| Landing support copy | Short note explaining rolling prelaunch access or manual review | Short note explaining live waitlist enrollment | Hidden state or vague copy that implies a backend path exists when it does not |
| Landing submit behavior | On-page capture / follow-up message only, with no automatic mail-client side effect | Real configured submission flow | `window.open(mailto:...)` as the primary submit outcome |
| Landing success message | Truthful prelaunch wording such as `Thanks — your request was captured for prelaunch review.` | Live wording such as `You're on the list! We'll notify you at launch.` | Backend-confirmation language in prelaunch mode |
| Report primary CTA | `Request Release Access →` or `Join the Report Waitlist →` | `Get the Report for $49 →` | Placeholder checkout exposed as a purchase-ready primary action |
| Report support / trust copy | Calm prelaunch copy such as `Prelaunch release • early-access invites are rolling out in batches.` | `Secure PayPal checkout • 30-day guarantee • Instant download` | Checkout trust claims shown while checkout is not actually live |
| Report purchase behavior | Route to a truthful interest / release-access step instead of placeholder checkout | Route to a verified live checkout path | Submitting visitors into a placeholder PayPal merchant flow |
| DOM hooks | `data-launch-state="prelaunch"` + one `aria-live="polite"` status region | `data-launch-state="live"` + one `aria-live="polite"` status region | Scattered state-specific string checks with no single source of truth |

## Tone and hierarchy guardrails

### In `prelaunch`

- Keep the message short and composed.
- Prefer truthful invitation language over warning language.
- Preserve one obvious primary action.
- Explain the state in one sentence, not a large alert block.
- Never make the page feel broken just because it is not fully live yet.

### In `live`

- Restore direct action language only after the real path works.
- Keep trust copy specific and restrained.
- Avoid decorative marketing claims that are not backed by the actual flow.

## Manual release gate

A page should not move from `prelaunch` to `live` until all of the following are true:

- the real endpoint or checkout path is configured
- the primary CTA routes into the real flow
- the follow-up text matches the actual outcome
- the flow has been manually checked on desktop and mobile
- keyboard users still encounter one clear primary action and readable status text

## Why this matters

`NicheVault` can feel premium before launch, but it cannot feel trustworthy if its copy outruns its implementation.

This matrix keeps the product aligned with a calmer Apple-level standard: clarity first, honest state communication, accessible feedback, and restrained presentation before extra polish.
