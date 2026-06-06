# NicheVault

**Discover Markets Nobody Knows Exist.**

NicheVault identifies untapped market gaps with zero competition using unconventional data research — patent databases, regulatory filings, hobbyist communities, job posting anomalies, and creative synthesis.

We deliver actionable go-to-market blueprints for founders and small businesses who are tired of competing in crowded spaces.

## What's in this repo

| Directory | Contents |
|-----------|----------|
| Root (`/`) | Landing page (`index.html`), Niche Library (`niche-library.html`), Sample Report (`sample-report.html`) |
| `reports/` | Sample report preview |
| `assets/` | Logo SVG, email capture draft |
| `content/` | Lead magnet content (blog posts, social threads) |
| `niches/` | Raw research markdown for identified niches |
| `blueprints/` | Detailed GTM blueprints for each niche |
| `products/` | Sellable product pages (HTML) |
| `strategy/` | Overall go-to-market strategy |

## Revenue Model
- **Free Newsletter** — Monthly niche alert (1 brief), sample reports, blog access
- **Paid Research Reports** ($49–$199 per niche deep-dive)
- **Done-for-You Strategy Blueprints** ($499–$999 per custom report)
- **Subscription Tier** ($29/month for 4+ niche briefs and 2 full reports)

## Email Capture Setup

The waitlist form on `index.html` supports three modes:

### 1. Formspree (Recommended — Free)
- Create a free form at [https://formspree.io](https://formspree.io) (50 submissions/month)
- Replace `YOUR_FORM_ID` in the JavaScript at the bottom of `index.html`:
  ```js
  const FORMSPREE_ID = 'abc123def';
  ```
- The form will POST directly to Formspree automatically

### 2. localStorage Fallback (No setup)
- If Formspree isn't configured, signups are saved to the visitor's browser via localStorage
- A signup counter displays below the form
- A `mailto:` link opens for the first 3 signups to alert you manually

### 3. Swap to Beehiiv / ConvertKit later
- When you're ready, simply replace the form action or embed their signup snippet

## Built With
- Pure HTML/CSS/JS — no frameworks
- Dark theme, responsive design
- Self-contained, lightweight
