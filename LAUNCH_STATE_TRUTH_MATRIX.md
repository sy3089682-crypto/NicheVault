# Launch-State Truth Matrix

This document turns the current launch-state trust work into a concrete, repeatable verification artifact for `NicheVault`.

It should be used together with:
- [PRODUCTION_READINESS.md](./PRODUCTION_READINESS.md)
- [APPLE_LEVEL_EXPERIENCE_SPEC.md](./APPLE_LEVEL_EXPERIENCE_SPEC.md)
- [Issue #3: Fail closed when launch config is placeholder-based on waitlist and report pages](https://github.com/sy3089682-crypto/NicheVault/issues/3)

The goal is simple: **the primary CTA, supporting trust copy, and success messaging must always match the real runtime state.**

## State model

### `prelaunch`
Use `prelaunch` when any core conversion path still depends on placeholder, manual, or demo configuration.

Examples:
- `FORMSPREE_ID === 'YOUR_FORM_ID'`
- signups still fall back to browser `localStorage`
- manual `mailto:` alert flow is still active
- PayPal business identity is still placeholder-based
- checkout flow is not fully wired and verified end to end

### `live`
Use `live` only when the real submission and payment paths are configured, tested, and ready for production traffic.

## Truth rules

1. Never show launch-ready CTA copy when the runtime path is still placeholder-based.
2. Never describe browser fallback or manual follow-up as if it were a production backend.
3. Never show checkout-only trust claims unless checkout is genuinely ready.
4. Prefer calm, explicit prelaunch framing over silent failure or overstated readiness.
5. Keep one clear primary action per page.

## Page-by-page matrix

### `index.html`

| Runtime state | Primary CTA copy | Supporting copy | Success / follow-up message |
| --- | --- | --- | --- |
| `prelaunch` | `Request Early Access` or `Join the Prelaunch Waitlist` | Explain that NicheVault is in prelaunch and early access requests may be handled manually while launch wiring is completed. | Be explicit about whether the request was saved locally, forwarded manually, or sent to a real service. |
| `live` | `Join Free` | Keep supporting copy focused on the user benefit, not the system internals. | Confirm that the request was submitted successfully to the live signup flow. |

### `report-landing-page.html`

| Runtime state | Primary CTA copy | Supporting copy | Trust claims |
| --- | --- | --- | --- |
| `prelaunch` | `Join the Report Waitlist` or `Request Release Access` | Explain the report is not yet available for live purchase and that the visitor will be notified when access opens. | Hide checkout-only claims such as secure payment, instant download, and refund guarantee. |
| `live` | `Get the Report` or `Get the Report for $49` | Focus on the report value and what the buyer receives. | Show payment and delivery trust copy only after checkout is fully configured and verified. |

## Copy blocks that should be gated behind `live`

Do **not** show these while placeholder configuration is active:
- `Join Free`
- `Buy Now with PayPal`
- `Get the Report for $49`
- `Secure PayPal checkout`
- `Instant download`
- refund / guarantee language tied to a checkout path that is not actually live

## Calm prelaunch indicators

When the product is in `prelaunch`, prefer understated language such as:
- `Prelaunch access`
- `Early access request`
- `Release waitlist`
- `We’ll notify you when this goes live`

Avoid loud warning styling. The goal is honesty with composure.

## Verification checklist

### Waitlist surface
- [ ] Placeholder Formspree config forces `prelaunch` copy.
- [ ] Real Formspree config restores `live` CTA copy.
- [ ] Success message explains the actual outcome.
- [ ] No fallback behavior is described as production-ready submission.

### Report surface
- [ ] Placeholder PayPal config forces `prelaunch` copy.
- [ ] Real checkout config restores purchase CTA copy.
- [ ] Checkout-only trust claims are hidden in `prelaunch`.
- [ ] The primary action remains visually clear on mobile and desktop.

## Definition of done for the next implementation wave

A future code change should not be considered complete until:
- both public pages read from the same launch-state rules
- placeholder config automatically flips the experience into a truthful prelaunch mode
- success and follow-up messaging reflect actual behavior
- visual hierarchy remains calm and premium in both states

If there is any doubt, default to `prelaunch`.
