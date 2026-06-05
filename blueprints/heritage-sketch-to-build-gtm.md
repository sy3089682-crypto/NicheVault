# GTM Blueprint: Heritage Sketch-to-Build AI

## 1. Step-by-Step 90-Day Launch Plan

### Phase 1: Model Training & Core Dev (Days 1-30)
- **Data Collection:** Gather 5,000+ public domain images of heritage furniture (Queen Anne, Shaker, MCM) and their associated joinery details.
- **AI Model Development:** Fine-tune a vision model (e.g., using Stable Diffusion ControlNet or Segment Anything Model) to recognize furniture structures and map them to CAD-ready components.
- **Joinery Engine:** Build the logic that calculates mortise/tenon/dovetail sizes based on wood species and dimensions, using standard woodworking engineering formulas.

### Phase 2: Alpha Testing & Community Feedback (Days 31-60)
- **Alpha Launch:** Invite 50 hobbyist woodworkers from r/woodworking to test the "Photo-to-Plan" conversion for free.
- **Refinement:** Improve the "exploded view" visualization and the accuracy of the Bill of Materials (BOM).
- **Early Content:** Create 5 "Speed Build" videos showing the tool converting a museum photo into a finished project.

### Phase 3: Public Beta & Influencer Launch (Days 61-90)
- **Public Beta:** Open the platform with a "Pay-per-Plan" model.
- **Influencer Campaign:** Partner with 10 mid-tier woodworking YouTubers for "Scan-to-Build" challenges.
- **The "Antique Hunter" App:** Launch a basic mobile wrapper for "scanning" items in the wild.

---

## 2. Customer Acquisition Strategy

### Channels & Tactics
- **YouTube Influencers:** The primary channel. Provide the tool to makers who already build heritage pieces (e.g., Ishitani Furniture, Rex Krueger, Bourbon Moth Woodworking).
- **Social Media (Pinterest/Instagram):** High-quality renders of transformed antiques to capture aspirational DIYers.
- **SEO/Content Marketing:** Target keywords like "Free Shaker chair plans," "How to build MCM dresser," and "Photo to woodworking plan." Leverage forums like `Woodworking Talk` and `Sawmill Creek`.
- **Antique Store Partnerships:** QR codes in local antique shops: "Love this? Build it yourself."

### Estimated Costs
- **Compute/GPU for Training:** $3,000
- **Development (Contractor):** $5,000 (initial engine)
- **Influencer Marketing:** $2,000 (product-only or small stipends)
- **Social Media Ads:** $500/mo

---

## 3. MVP Scope
- **Web-Based Conversion Tool:** Upload a single JPG/PNG → Receive a 3D preview.
- **Downloadable Plan Package:** Includes a PDF cutting list, 2D drawings with dimensions, and a basic assembly guide.
- **Joinery Recommendation:** Suggestions for the best joint type based on the detected style.
- **Basic Library:** 50 pre-validated "Heritage" designs to explore.

---

## 4. Pricing & Monetization Recommendations
- **Pay-per-Plan:** $14.99 per high-res plan download.
- **Monthly Subscription (The Master Maker):** $19/month for unlimited conversions and advanced joinery customization.
- **Affiliate Revenue:** Partner with wood suppliers (e.g., Rockler, Woodcraft) for "Buy the materials for this plan" buttons.

---

## 5. Key Risks & Mitigations
- **Structural Integrity:** AI might suggest a joint that looks correct but fails in real life.
    - *Mitigation:* Include a clear "Hobbyist Use Only" disclaimer and use conservative, standardized joinery formulas.
- **Complexity of Furniture:** AI fails on highly ornate or unique pieces.
    - *Mitigation:* Start with specific, well-defined styles (Shaker, MCM) and expand as the model improves.

---

## 6. Resource Requirements
- **AI/ML Engineer:** (Vision/CAD specialization).
- **Master Woodworker:** For joinery logic validation and content creation.
- **UX/UI Designer:** To ensure the CAD interface isn't "scary" for hobbyists.
- **GPU Hosting:** (e.g., AWS, Lambda Labs).
