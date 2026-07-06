# Launch-State Implementation Sketch

This document turns the trust requirement from [issue #3](https://github.com/sy3089682-crypto/NicheVault/issues/3) into a small, implementation-ready runtime plan.

The goal is not a redesign. The goal is to make the existing pages behave honestly, calmly, and accessibly when conversion config is still placeholder-based.

## Why this file exists

`NicheVault` already has the right direction captured in:

- `PRODUCTION_READINESS.md`
- `APPLE_LEVEL_EXPERIENCE_SPEC.md`
- `LAUNCH_STATE_TRUTH_MATRIX.md`
- `LAUNCH_STATE_MANUAL_VERIFICATION.md`

The remaining gap is execution clarity inside the HTML pages.

This sketch defines the smallest shared runtime contract that should be implemented before any extra polish work.

## Apple-level rule for this wave

When configuration is not truly live, the UI must fail closed into a premium `prelaunch` state.

That means:

- calm, explicit prelaunch wording
- no live-sounding checkout or backend promises
- one clear primary action
- no surprise `mailto:` side effects
- accessible status feedback that describes the real outcome

## Shared runtime contract

Use one shared resolver on both pages.

```js
function isPlaceholder(value, placeholder) {
  return !value || value.trim() === '' || value === placeholder;
}

function resolveLaunchState(options) {
  const {
    formspreeId,
    paypalBusiness,
    usesLocalCapture,
    opensMailto,
    supportsInstantDownload
  } = options;

  const waitlistIsLive = !isPlaceholder(formspreeId, 'YOUR_FORM_ID') && !usesLocalCapture && !opensMailto;
  const checkoutIsLive = !isPlaceholder(paypalBusiness, 'YOUR_PAYPAL_EMAIL@example.com') && supportsInstantDownload;

  if (waitlistIsLive && checkoutIsLive) {
    return 'live';
  }

  return 'prelaunch';
}
```

If the pages need different readiness inputs, that is fine.

The non-negotiable rule is:

- any placeholder or ambiguous state resolves to `prelaunch`

## DOM contract

Each page should expose the resolved state through the DOM.

### Required hooks

- page root: `data-launch-state="prelaunch"` or `data-launch-state="live"`
- one status region per page: `role="status" aria-live="polite"`
- one primary CTA element whose label is updated from a single state map
- one support-copy element whose text is updated from the same state map

Example shape:

```html
<body data-launch-state="prelaunch">
  <!-- page content -->
  <p id="launch-support-copy">Prelaunch release • early-access invites are rolling out in batches.</p>
  <p id="launch-status" role="status" aria-live="polite"></p>
</body>
```

## State copy maps

Keep copy decisions centralized instead of scattering string checks.

```js
const LANDING_COPY = {
  prelaunch: {
    navCta: 'Join the Prelaunch Waitlist',
    heroCta: 'Request Early Access →',
    support: 'Prelaunch access is rolling out in batches. Request access and we will follow up with the next release window.',
    success: 'Thanks — your request was captured for prelaunch review.'
  },
  live: {
    navCta: 'Join Free',
    heroCta: 'Join Free →',
    support: 'Join the live waitlist and get notified when new niches drop.',
    success: "You're on the list! We'll notify you at launch."
  }
};

const REPORT_COPY = {
  prelaunch: {
    primaryCta: 'Request Release Access →',
    support: 'Prelaunch release • early-access invites are rolling out in batches.',
    status: 'Thanks — your request was captured for report release follow-up.'
  },
  live: {
    primaryCta: 'Get the Report for $49 →',
    support: 'Secure PayPal checkout • 30-day guarantee • Instant download',
    status: 'Secure payment via PayPal. You will receive the PDF immediately after payment.'
  }
};
```

## `index.html` integration sketch

### Current trust problem

The landing page still combines placeholder Formspree configuration with live-sounding CTA and success language, plus a `mailto:` side effect.

### Minimum implementation steps

1. Resolve waitlist state from the current Formspree configuration and fallback behavior.
2. Set `document.body.dataset.launchState`.
3. Update:
   - nav CTA label
   - hero CTA label
   - one short support-copy element near the waitlist action
4. Remove automatic `window.open(mailto:...)` from the primary submission path.
5. After submit, write outcome text into the polite status region.
6. If email contact is still useful, expose it as a normal secondary link or note.

### Pseudocode

```js
const landingState = !FORMSPREE_CONFIGURED || USES_LOCAL_CAPTURE || OPENS_MAILTO ? 'prelaunch' : 'live';
document.body.dataset.launchState = landingState;

navCta.textContent = LANDING_COPY[landingState].navCta;
heroCta.textContent = LANDING_COPY[landingState].heroCta;
supportCopy.textContent = LANDING_COPY[landingState].support;

statusRegion.textContent = '';

async function handleWaitlistSubmit(event) {
  event.preventDefault();

  if (landingState === 'prelaunch') {
    captureRequestLocallyWithoutMailClientSideEffect();
    statusRegion.textContent = LANDING_COPY.prelaunch.success;
    return;
  }

  await submitToLiveEndpoint();
  statusRegion.textContent = LANDING_COPY.live.success;
}
```

## `report-landing-page.html` integration sketch

### Current trust problem

The report page still shows purchase framing while the PayPal business value remains placeholder-based.

### Minimum implementation steps

1. Resolve checkout state from the PayPal business identity and real delivery readiness.
2. Set `document.body.dataset.launchState`.
3. In `prelaunch`:
   - change the primary CTA label
   - replace checkout-only trust copy
   - do not route the visitor through placeholder checkout as the main action
4. Use one polite status or follow-up element for release-access messaging.
5. Only restore PayPal purchase framing when checkout is genuinely live.

### Pseudocode

```js
const paypalBusiness = getPaypalBusinessValue();
const reportState = isPlaceholder(paypalBusiness, 'YOUR_PAYPAL_EMAIL@example.com') ? 'prelaunch' : 'live';
document.body.dataset.launchState = reportState;

reportPrimaryCta.textContent = REPORT_COPY[reportState].primaryCta;
reportSupportCopy.textContent = REPORT_COPY[reportState].support;
reportStatus.textContent = '';

if (reportState === 'prelaunch') {
  hideOrDisablePlaceholderCheckoutForm();
  wirePrimaryActionToReleaseInterestFlow();
} else {
  showLiveCheckoutForm();
}
```

## Accessibility requirements

Do not treat this as copy-only work.

The implementation should also:

- keep one obvious keyboard-reachable primary action per page
- ensure status updates are announced politely
- avoid relying on color alone to convey state
- keep support text short enough to scan on mobile
- avoid warning-banner styling that would make the page feel noisy or defensive

## Definition of done for the coding wave

The implementation is ready when all of the following are true:

- placeholder config automatically resolves to `prelaunch`
- `index.html` no longer auto-opens the visitor's mail client in the main flow
- live-sounding success language is not used in `prelaunch`
- `report-landing-page.html` no longer exposes placeholder checkout as the main action
- both pages expose `data-launch-state`
- both pages include one polite status region
- copy and behavior match `LAUNCH_STATE_TRUTH_MATRIX.md`
- the scenarios in `LAUNCH_STATE_MANUAL_VERIFICATION.md` pass

## Recommended coding order

1. Add the shared helper and state maps.
2. Wire `index.html` to the shared copy/state contract.
3. Remove automatic `mailto:` from the landing flow.
4. Wire `report-landing-page.html` to the same contract.
5. Run manual verification on mobile and keyboard-only paths.

## What not to do in this wave

- do not redesign the full page layout
- do not add more gradients, shadows, or motion
- do not keep live purchase claims visible in `prelaunch`
- do not introduce multiple competing primary actions
- do not let fallback behavior remain hidden behind launch-ready wording
