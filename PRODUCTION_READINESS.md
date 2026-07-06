# NicheVault Production Readiness Guide

This document defines the minimum bar for calling NicheVault production-ready.

The current repo already communicates strong product intent through its landing pages and sample report surfaces. That makes trust critical: if a page looks launch-ready, the primary actions on that page need to work, fail clearly, or be labeled honestly.

## Core standard

A production-ready NicheVault experience should meet five conditions:

1. **Honest conversion behavior** — no primary CTA should depend on placeholder credentials or silent fallback behavior that looks live.
2. **Clear launch state** — a visitor should be able to tell whether they are joining a real waitlist, buying a real report, or viewing a demo surface.
3. **Accessible interaction** — forms and CTAs must be keyboard-usable, legible, and clear in success/failure states.
4. **Reproducible verification** — a maintainer should have a short checklist that proves the conversion flow works before launch.
5. **Calm premium UX** — hierarchy, spacing, and copy should make the primary action obvious without visual noise.

## Current trust risks surfaced in audit

The public repo currently exposes two trust-sensitive areas:

- `index.html` contains a Formspree placeholder (`YOUR_FORM_ID`) with a local fallback path.
- `report-landing-page.html` contains a PayPal button placeholder (`YOUR_PAYPAL_EMAIL@example.com`).

These are acceptable for local development or demos, but they should not appear production-ready unless they are fully configured.

## Fail-closed launch rule

If production credentials are not configured, the UI should **not pretend to be live**.

Use one of these states explicitly:

### State A — Live
Use when Formspree and payment configuration are real and tested.

Requirements:
- waitlist submissions reach the real inbox / CRM
- the PayPal CTA resolves to a real checkout path
- success and failure states are visible and understandable

### State B — Demo / Prelaunch
Use when credentials are not configured.

Requirements:
- label the page clearly as preview, demo, or prelaunch
- replace transactional language like `Buy Now` with honest language like `Request early access` or `Join waitlist`
- avoid silently routing users into local-only storage as if they successfully joined a live list

## Launch checklist

Before calling NicheVault production-ready, verify all of the following.

### Conversion wiring
- [ ] `index.html` uses a real waitlist destination instead of placeholder credentials
- [ ] `report-landing-page.html` uses a real payment destination instead of placeholder merchant details
- [ ] success states confirm what happened next
- [ ] failure states explain what the visitor should do next

### UX clarity
- [ ] the main CTA is obvious above the fold
- [ ] no page has multiple competing primary actions
- [ ] copy makes the offer, audience, and next step clear in a few seconds
- [ ] preview/demo content is clearly labeled when not fully live

### Accessibility
- [ ] forms are keyboard navigable
- [ ] focus states are visible
- [ ] text contrast is readable
- [ ] error messages are understandable without relying on color alone
- [ ] motion, if any, does not interfere with comprehension

### Trust and QA
- [ ] a maintainer manually submits the waitlist flow in a staging or live-safe environment
- [ ] a maintainer manually verifies the payment CTA route
- [ ] mobile CTA behavior is tested
- [ ] broken-link sweep is completed across landing, library, and report pages
- [ ] README reflects the real launch state rather than the aspirational one

## Apple-level interpretation for NicheVault

For this product, Apple-level production readiness does **not** mean adding more visual treatment.

It means:
- a visitor instantly understands the offer
- the interface defers to the main action instead of distracting from it
- any preview or prelaunch state is honest
- interaction outcomes are clear and trustworthy
- the site feels calm, intentional, and predictable

## Recommended implementation order

1. Replace placeholder conversion credentials with real values **or** relabel the relevant surfaces as preview/prelaunch.
2. Add explicit inline success and failure messaging for the waitlist flow.
3. Add a clear pre-launch check for the payment CTA.
4. Review the landing pages for any copy or layout that over-promises beyond the current live behavior.
5. Only after the trust layer is solid, continue with visual polish.
