(function (global) {
  'use strict';

  function normalize(value) {
    return typeof value === 'string' ? value.trim() : '';
  }

  function isPlaceholder(value, placeholder) {
    const normalizedValue = normalize(value);
    const normalizedPlaceholder = normalize(placeholder);

    return !normalizedValue || normalizedValue === normalizedPlaceholder;
  }

  function resolveWaitlistState(options) {
    const settings = options || {};
    const formspreeId = settings.formspreeId;
    const usesLocalCapture = Boolean(settings.usesLocalCapture);
    const opensMailto = Boolean(settings.opensMailto);

    const isLive = !isPlaceholder(formspreeId, 'YOUR_FORM_ID') && !usesLocalCapture && !opensMailto;

    return isLive ? 'live' : 'prelaunch';
  }

  function resolveReportState(options) {
    const settings = options || {};
    const paypalBusiness = settings.paypalBusiness;
    const supportsInstantDownload = Boolean(settings.supportsInstantDownload);
    const hasVerifiedCheckout = Boolean(settings.hasVerifiedCheckout);

    const isLive =
      !isPlaceholder(paypalBusiness, 'YOUR_PAYPAL_EMAIL@example.com') &&
      supportsInstantDownload &&
      hasVerifiedCheckout;

    return isLive ? 'live' : 'prelaunch';
  }

  function resolvePageState(options) {
    const settings = options || {};

    if (settings.page === 'report') {
      return resolveReportState(settings);
    }

    return resolveWaitlistState(settings);
  }

  var LANDING_COPY = Object.freeze({
    prelaunch: Object.freeze({
      navCta: 'Join the Prelaunch Waitlist',
      heroCta: 'Request Early Access →',
      support:
        'Prelaunch access is rolling out in batches. Request access and we will follow up with the next release window.',
      success: 'Thanks — your request was captured for prelaunch review.',
      error: 'We could not capture your prelaunch request. Please try again shortly.'
    }),
    live: Object.freeze({
      navCta: 'Join Free',
      heroCta: 'Join Free →',
      support: 'Join the live waitlist and get notified when new niches drop.',
      success: "You're on the list! We'll notify you at launch.",
      error: 'We could not submit your request right now. Please try again shortly.'
    })
  });

  var REPORT_COPY = Object.freeze({
    prelaunch: Object.freeze({
      primaryCta: 'Request Release Access →',
      support: 'Prelaunch release • early-access invites are rolling out in batches.',
      status: 'Thanks — your request was captured for report release follow-up.'
    }),
    live: Object.freeze({
      primaryCta: 'Get the Report for $49 →',
      support: 'Secure PayPal checkout • 30-day guarantee • Instant download',
      status: 'Secure payment via PayPal. You will receive the PDF immediately after payment.'
    })
  });

  function getLandingCopy(state) {
    return LANDING_COPY[state] || LANDING_COPY.prelaunch;
  }

  function getReportCopy(state) {
    return REPORT_COPY[state] || REPORT_COPY.prelaunch;
  }

  var api = Object.freeze({
    isPlaceholder: isPlaceholder,
    resolveWaitlistState: resolveWaitlistState,
    resolveReportState: resolveReportState,
    resolvePageState: resolvePageState,
    LANDING_COPY: LANDING_COPY,
    REPORT_COPY: REPORT_COPY,
    getLandingCopy: getLandingCopy,
    getReportCopy: getReportCopy
  });

  global.NicheVaultLaunchState = api;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
  }
})(typeof window !== 'undefined' ? window : globalThis);
