# NicheVault Analytics Setup

## Current Solution: Lightweight Privacy-Friendly Tracker

We've implemented a zero-dependency analytics system in `analytics.js` that:
- Tracks page views, CTA clicks, and form submissions
- Stores data in localStorage (no cookies, no external requests)
- Is fully privacy-compliant (no IP tracking, no fingerprinting, no personal data)
- Requires no third-party accounts or paid services

### How to view data

Open browser DevTools console on any NicheVault page and run:

```javascript
// Get summary
NicheVaultAnalytics.getSummary()

// Export all events as JSONL
NicheVaultAnalytics.exportCSV()

// Track a custom event
NicheVaultAnalytics.track('purchase', { product: 'pet-bereavement-report', amount: 49 })
```

### Data structure

Events are stored as JSON objects with these fields:
- `t` — ISO timestamp
- `type` — pageview | click | form_submit | custom
- `page` — page pathname (for pageviews)
- `text` — button/link text (for clicks)
- `href` — link URL (for clicks)
- `form_id` — form identifier (for form submissions)
- `name` — custom event name
- `url` — current page URL
- `ref` — referrer

## Migration Path: Plausible (Recommended)

When ready to upgrade, Plausible is the best privacy-friendly analytics option:

### Option A: Plausible Cloud (Paid, $9/month)
1. Sign up at https://plausible.io
2. Add your domain
3. Copy the provided script tag
4. Replace `<script src="analytics.js" defer></script>` in all HTML files

### Option B: Plausible Self-Hosted (Free, requires server)
1. Deploy Plausible via Docker: https://github.com/plausible/analytics
2. Add your site
3. Copy the provided script tag
4. Replace `<script src="analytics.js" defer></script>` in all HTML files

## Alternative: Cloudflare Web Analytics (Free)

1. Sign up for a free Cloudflare account
2. Add your site (no DNS change required for analytics-only)
3. Go to Analytics → Web Analytics
4. Copy the provided JavaScript snippet
5. Replace `<script src="analytics.js" defer></script>` in all HTML files

Pros: Free, privacy-friendly, no cookie banner needed, real-time.
Cons: Less detailed event tracking than Plausible.

## Alternative: Google Analytics 4 (Free)

1. Create a GA4 property at https://analytics.google.com
2. Copy the GA4 measurement ID (G-XXXXXXXXXX)
3. Add the standard gtag.js snippet to all pages

Pros: Free, extensive features, integrates with Google Ads.
Cons: Requires cookie consent in EU, heavy script, privacy concerns.

## Pages with analytics installed

- `index.html`
- `niche-library.html`
- `sample-report.html`
- `report-landing-page.html`
- `thank-you.html`

## KPIs we track

| KPI | How we measure it |
|-----|-------------------|
| Newsletter signups | `form_submit` events on waitlist form |
| Report page visits | `pageview` on `/report-landing-page.html` |
| Report sales | Custom `purchase` event (track via PayPal IPN or button click) |
| Conversion rate | Report page visits ÷ Report purchases |
| Content engagement | CTA click events on niche cards |
| Traffic sources | `ref` field on pageview events |
