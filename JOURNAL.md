# JOURNAL.md — NM Thera / SOKY Build Log

---

## Session — Tuesday, April 14, 2026
### What We Did

**1. Combined HTML File — Merged Home + PDP into Single Deliverable**
- Created `nmthera-combined.html` — merged sitemap superpage (Home) and PDP into one unified file
- Architecture: Home + Shop, with hover dropdown nav revealing three sub-pages (Hand SOKY Single / Pair / Travel System)
- Each SKU now lives on its own independent PDP, per Tiffany's recommendation
- Shop hover dropdown uses `::after` bridge pseudo-element for smooth cursor travel
- Fixed iframe embed URL typo (dot vs hyphen) for WordPress/Elementor deployment

**2. Tiffany Feedback — Accessibility & Design Pass**
- Removed progress bar from nav
- Trimmed nav to Home + Shop only
- Ran full accessibility contrast sweep — 24 CSS changes across 5 tasks (nav text, hero overlay, dark-mode nav, body sections, image captions)
- Updated "First Batch Launching May 1" → "Available Now — Limited First Drop"
- Added safety disclaimers, return policy, and full Policies page
- Generated Claude Code prompts for all changes + verification checklist
- Drafted Asana task description and comment for merged Home V2 + PDP V2 task with handoff instructions

**3. Product Insert — SKU 002 Science at a Glance Rework**
- Replaced old stats (iontophoresis %, adherence %, condition count) — too similar-looking and unsubstantiated
- New stats grounded in published science: skin permeability (3–5×), transdermal absorption (~10×), water conservation (2×+), soak time (15–20 min)
- Added waterdrop logo to match SKU 001 insert
- Removed footer top border

**4. Seymour Everett — Investor Call Briefing**
- Built comprehensive briefing for phone call with Seymour covering product status, web/GTM progress, team, Campaign 1 readiness, financial position, and runway concern
- Framed the equity ask: inviting Seymour to exercise his contractual right to invest additional capital at original terms before the pre-seed round opens at $3.2M cap
- Call completed

**5. Fernando — B2B Sales Role**
- Drafted and iterated text message bringing Fernando back in a sales capacity
- Role structure: commission-based B2B sales targeting podiatrists/clinicians via HubSpot CRM
- Benchmarks: 50–100 calls + 50–100 emails per day, WFH/browser-based, no travel required
- Key selling point: 15,000 contacts in CRM with zero competition — wide open opportunity
- Connected role to Foot SOKY pipeline specifically (podiatry accounts)
- Long-term path: Sales Director → potentially CSO, but leading with opportunity, not title
- Kenny backs him on closes; no equity lead, commission TBD

**6. TopSheng / Jack — Manufacturing Terms Secured**
- Reconnected with Jack about next Hand SOKY batch: 500 pieces (250 pairs), split across SKU 001 and SKU 002
- Was upfront about funding timeline; asked for flexible payment terms
- Jack initially offered 3-month terms
- Sean Tan advised pushing to 4–5 months for breathing room as the raise comes together
- Went back to Jack — he agreed to 5-month payment terms
- Next steps: send specs and packaging designs for both SKUs, schedule a call with Jack to finalize details
- Planted seed on Foot SOKY as next product development opportunity — Jack is interested
- Open question: clarify whether 5 months runs from order placement, delivery, or invoice date
- Sean's manufacturing experience was directly valuable in this negotiation

**7. Sean Tan — Advisor Momentum**
- Spoke with Sean; he's excited about the company's progress
- Pitch deck and business plan (built in earlier sessions) are landing well with him
- Sean provided direct tactical guidance on the TopSheng negotiation (push to 4–5 months, consider installment structure)
- Also suggested potentially offering TopSheng equity — parked for now but on Kenny's mind given commitment to sole-manufacturer relationship

**8. USPTO Trademark Update**
- Received official notice: design search codes assigned to stylized trademark application (SN: 99562473)
- Codes: raindrop/teardrop shapes + curved lines/bands — consistent with SOKY visual identity
- Routine and good news — application progressing normally
- No action required; codes have no legal significance
- Flagged: need trademark counsel lined up (James Yang no longer available) in case Office Action comes back

**9. Jenn Nguyen — Samsara Background Analysis**
- Analyzed what Jenn's Samsara experience brings to NM Thera
- IoT product design → SOKY sensor/data platform architecture
- Complex-to-simple workflow design → ritual UX and onboarding
- Design systems discipline → scaling BSG v3.0 to production
- Pre-to-post-IPO range (Samsara: startup → $25B+ market cap)
- Full-stack design execution: research → wireframe → prototype → production spec

**10. SBIR Grant Strategy**
- S. 3971 signed into law — SBIR/STTR reauthorized through 2031 after September 2025 lapse
- Phase I awards ~$250K–$275K non-dilutive (NIH NIBIB or NSF best fit)
- Timeline: 9–15 months prep-to-award; targeting September 2026 submission, funds ~mid-2027
- Decision: park until post-Campaign 1; begin grant writer search June/July
- This funds R&D layer (electrotherapy, sensors, clinical validation) for Series A — parallel track, not current lifeline

**11. Flagship Store Brainstorm**
- Deep conceptual design session for brick-and-mortar NM Thera flagship
- Concept: "wellness mod shop" — cross between apothecary and nail salon
- Five zones: Apothecary Bar (walk-in soak bar + blend wall), Mod Bench (device customization workshop), Wellness Studio (group sessions + practitioner consults), Heritage Wall, storefront experience
- Customer journey mapped from walk-in → modification → community practice
- Generated five-panel concept art prompt for Nano Banana to illustrate
- Modalities: heat therapy, electrotherapy, hyperbaric gas therapy

### Key Decisions
- **5-month payment terms secured with TopSheng** — production can begin before funding closes (June–August). Sean Tan's guidance was instrumental.
- **Fernando enters as commission-based B2B sales rep** — no hourly, no equity lead. 15K-contact CRM is the pitch.
- **Three SKUs split into separate PDPs** — confirmed and built per Tiffany's recommendation.
- **SBIR parked until post-Campaign 1** — September 2026 submission target, grant writer search starts June/July.
- **TopSheng equity idea parked** — on Kenny's mind but not ready to play forward yet.

### Learnings
- **Sean Tan is delivering tangible value.** Direct tactical guidance on manufacturing negotiation resulted in better terms. The pitch deck and business plan are serving their intended purpose as shareable investor-facing assets.
- **Jack/TopSheng trust is real and mutual.** "I trust you and would love to support you" — this relationship is a strategic asset worth protecting. Sole-manufacturer commitment is the right posture.
- **Payment term specifics matter.** 5 months agreed in principle, but start date (order vs delivery vs invoice) and payment structure (lump sum vs installments) still need to be nailed down on the follow-up call.
- **SBIR is a 9–15 month play.** It funds the R&D layer that makes Series A compelling, but it can't rescue current operations.
- **Hover dropdowns need bridge elements.** Without a `::after` pseudo-element, the menu closes as cursor crosses empty space.
- **Merging tasks reduces coordination overhead.** Two Asana tasks → one task, one file, one handoff.

### Files Changed
- `HTML/nmthera-combined.html` — NEW: merged Home + Shop + 3 separate PDPs
- `HTML/soky-002-kit-insert.html` — Science at a Glance rework, waterdrop logo, footer border removed
- Claude Code prompts generated: accessibility contrast fix (24 changes), PDP feedback fixes, combined file verification checklist

### Next Steps
- **TopSheng:** Send specs and packaging designs for SKU 001 + SKU 002. Schedule call with Jack. Clarify payment term start date and installment structure. Consider having Sean on or briefed before the call.
- **Fernando:** Wait for his response. If he bites, walk him through HubSpot and the database. Have commission structure ready.
- **Seymour:** Follow up on equity conversation from today's call.
- **Tiffany:** Review live draft at nmthera.com/home2 — flag anything that still needs work.
- **Hameed:** After Tiffany sign-off, begin Elementor rebuild. Each page gets its own WordPress URL.
- **WooCommerce:** Connect all Add to Cart buttons (backend annotations already in code).
- **SBIR:** Park. Revisit June/July for grant writer search, target September submission.
- **Trademark:** Monitor for examining attorney's next step. Line up replacement trademark counsel.
- **Product insert:** Finalize SKU 002 insert with updated stats, prep for print run.
- **Chi + Kenichiro:** Share TopSheng manufacturing update (drafted and ready to send).

---

## Session — April 7, 2026

### What We Did

1. **Full 2025 tax prep buildout** — Parsed 601 transactions from Wells Fargo year-end spending report (CSV). Classified every transaction as business, medical, or personal using regex-based rules against Kenny's tax category list.
2. **Chase Business Ink analysis** — Ingested Chase Ink ...9908 CSV (closed card). Found $2,385 in business purchases (Jan–Apr) and $5,046 in business credit card interest potentially deductible. Card was closed involuntarily by Chase mid-April — root cause of all commingling on personal accounts.
3. **Business account analysis** — Parsed INC (...3560) and LLC (...1356) Chase Business checking CSVs. Mapped all outflows: $8,165 to TopSheng, $8,500 to contractors, $86,399 to Kenny (salary/draw + mortgage allocation), $130,120 in investor deposits.
4. **IVF deduction identified** — $26,000 IVF procedure charged to wife's CC in 2025, refinanced via medical loan. Fully deductible on Schedule A in the year charged. Combined with Kaiser ($5,145), pharmacy ($604), and Blue Shield ($230), total medical is $31,749.
5. **Itemizing vs standard deduction analysis** — Medical alone (~$26.5K after 7.5% AGI floor) nearly matches the $29,200 standard deduction. Adding SALT and mortgage interest likely makes itemizing the better path.
6. **Contractor 1099 audit** — Identified four contractors needing late 1099-NECs: Hameed ($4,000), Tiffany ($1,500), Jenn ($1,500), Chi ($1,000). Charlie Kim under $600 threshold. Deadline was Jan 31 — penalty est. $240–600.
7. **Hameed payment channels mapped** — ITSMADEEZY Innovative Solutions (India entity) received payments via PayPal/ACH (Feb $1,500) and ICICI Bank wires (Jun $1,500, Nov $500, Dec $500). All four transactions reference same entity. Needs W-8BEN or W-8BEN-E.
8. **Kenichiro R&D reimbursement** — $2,000 via Zelle (2 x $1,000) for iontophoresis machines. Confirmed as 2026 payment — removed from 2025 totals. Equipment supports Model E1 development and R&D credit case.
9. **LLC partnership return flagged** — LLC is multi-member (Kenny + Kenichiro), requiring Form 1065 + K-1s. Ownership percentages are informal and need formalization before filing. Unclear whether 1065 was filed in prior years.
10. **Corp-E-Corp identified** — $430.63 payment (Apr 7, LLC) identified as likely Delaware C Corp annual franchise tax / registered agent fee.
11. **24 Hour Fitness flagged as personal** — $335.87 (Jan + Feb, LLC) was personal spending commingled accidentally. Excluded from business totals.
12. **Tax prep spreadsheet built** — Eight-tab Excel workbook: Cover Memo, WF Business Expenses, Chase Ink (closed), Business Accounts, Medical (Schedule A), 1099 Filing Summary, Grand Summary, Personal Summary. Iterated through six major versions as new data sources were added.
13. **Cover memo for Stewart (Robinson CPA)** — Clean single-pass briefing: entity structure, financial summary, contractor/1099 status, eight questions for Stewart, folder checklist with IRS form links.
14. **Spending pattern analysis** — Burn rate doubled Jun–Dec vs Jan–May. WF CC payments escalated from $579/mo to $5,325/mo. Two overdraft fees in one week (Jul). SaaS creep to ~$800–900/mo by Q4. Amazon black box ($4,823, spike Oct–Nov).
15. **Red flag / green flag audit** — Green: capital-efficient build ($32K ops on $130K capital), documented contractor SOWs, traceable expenses, legitimate IP and manufacturing spend. Red: commingling across five accounts, no 1099s filed, no W-2 payroll, informal LLC ownership, $40K personal CC debt.
16. **Fundraising strategy discussion** — Recommended $500K target on $3.2M SAFE. Three tiers analyzed (survival $150–250K, working $400–600K, growth $800K–1M). Lead with product/IP/margins in pitch, not macro thesis. Raise now — angels less sensitive to market volatility.
17. **W-9 and W-8BEN messages drafted** — Template for Tiffany/Jenn/Chi (W-9) and custom message for Hameed (W-8BEN individual with entity question flagged for Stewart).

### Key Decisions

- **File extensions before April 15** — Form 4868 (personal) + Form 7004 (C Corp + partnership). Return cannot be properly filed in 8 days given C Corp, LLC 1065, compensation characterization, and late 1099s.
- **All contractors treated as independent contractors** — Correct for current phase. SOW documentation exists for all team members.
- **Hameed files as individual (W-8BEN)** — His preference. Stewart may also need W-8BEN-E for ITSMADEEZY entity given Feb payment went through the company.
- **Kenichiro iontophoresis payment is 2026** — Removed from 2025 business totals. Will be 2026 R&D expense.
- **24 Hour Fitness excluded** — Personal expense commingled on LLC. Treated as personal draw.
- **Corp-E-Corp is DE corp maintenance** — Not flagged as unknown. Likely franchise tax or registered agent.
- **KP SF = Kenny's mortgage/home account** — ~$4K/mo housing allocation. Stewart to characterize along with direct salary payments.
- **Credit card statements (Discover, Amazon Store Card) not included** — Confirmed no business charges on those cards. Rolling personal balances only.
- **Chase Ink closure caused the commingling** — Not carelessness. Card was the primary business card; after involuntary closure, all subscriptions migrated to personal WF accounts.
- **Post-raise clean break** — Day one of pre-seed funding: new business CC, Gusto payroll, zero personal card usage for business.

### Files Changed

- None (tax prep session — spreadsheet output only, not added to repo)
- Output: `NMThera_2025_Tax_FINAL_v4.xlsx` (8-tab workbook for Stewart)

### Next Steps

- File Form 4868 + Form 7004 before April 15
- Send W-9 requests to Tiffany, Jenn, Chi
- Send W-8BEN request to Hameed
- Collect wife's W-2 + IVF invoice + CC line items + loan agreement
- Get iontophoresis machine receipts from Ken (for 2026 filing)
- Hand Stewart the folder: spreadsheet + 5 CSVs + 2 screenshots
- Stewart to advise on: LLC 1065 history, Kenny comp characterization, R&D credit eligibility, biz CC interest deductibility, Blue Shield placement
- Formalize LLC ownership percentages (Kenny + Kenichiro) before K-1s
- April 30 — Campaign 1 launch (unchanged)

---

## Session — April 3, 2026

### What We Did

1. **Dev environment setup** — Installed VS Code on both desktop and laptop. Initialized Git on desktop, connected both machines to `kfam227/website` on GitHub. Resolved merge conflicts from parallel initial commits.
2. **GitHub Pages enabled** — Turned on Pages for the repo to serve live HTML previews at `kfam227.github.io/website/`.
3. **WordPress iframe embed** — Set up full-screen iframe on `nmthera.com/pd_s26` to serve the pitch deck from GitHub Pages. Configured `z-index: 99999`, zero margin/padding, 100vw/100vh to eliminate WordPress chrome.
4. **Mobile zoom fix** — Applied `initial-scale=0.85, user-scalable=no` to the horizontal pitch deck for mobile viewport control (`c6317dd`).
5. **Full repo audit** — Ran a complete technical audit across all 23 files. Identified missing meta tags, accessibility gaps, placeholder content, and tooling issues.
6. **Audit fixes applied** — Added OG and Twitter Card meta tags to all 16 HTML files. Added `<meta name="description">` to 11 files missing them. Replaced 3 "TBD" entries in pricing tables with "Available upon request" (`7dfaaa9`).
7. **KV Blue video compression** — Compressed the hero video from 268 MB to 32 MB using HandBrake. Uploaded to `Videos/` folder on the repo for GitHub Pages hosting (`f30ae44`).
8. **Mobile autoplay fix** — YouTube iframe embeds do not autoplay on mobile inside WordPress iframes. Tested YouTube iframe first (`32e73c1`), then switched to self-hosted `<video>` with `autoplay muted loop playsinline` (`2c20cc1`). Applied same swap to business plan and pitch deck (`e6ef55f`).
9. **Mobile autoplay confirmed** — Self-hosted `<video playsinline>` autoplays successfully through the WordPress iframe on `nmthera.com/pd_s26` on iOS Safari and Android Chrome.
10. **Team roster updated — pitch deck** — Updated S10 (Team slide) in `HTML/soky-pitch-deck-h.html` with full accurate roster: 6 core team members (Kenny, Kenichiro, Chi, Hameed, Tiffany, Jenn), 4 advisors (Dr. Heller, Dr. Salem Lebada, Sean Tan, Jennifer Nguyen), 2 investors (Seymour Everett, Sosimo Roman). Profiles sourced from uploaded LinkedIn PDFs.
11. **Team roster updated — business plan** — Updated team section in `HTML/business-plan-enhanced.html` with full long-form profiles for all 12 team members, advisors, and investors. Three distinct groups with visual separation.
12. **iframe fix — business plan** — Added `<meta http-equiv="Content-Security-Policy" content="frame-ancestors *">` to `business-plan-enhanced.html` to resolve X-Frame-Options block preventing WordPress iframe embed.
13. **WordPress iframe — bp_s26** — Set up full-screen iframe on `nmthera.com/bp_s26` serving business plan from GitHub Pages. Same `position:fixed; z-index:99999` pattern as pitch deck.
14. **WordPress iframe — home2** — Set up full-screen iframe on `nmthera.com/home2` serving sitemap superpage from GitHub Pages.
15. **KV Blue video — sitemap superpage** — Swapped WordPress-hosted KV Blue URL to self-hosted GitHub Pages video in `HTML/nmthera-sitemap-superpage.html`. Confirmed mobile autoplay working.
16. **Git workflow established across two machines** — Desktop (NMT_Claude_WorkshopG) and laptop (Claude Local Laptop Folder) both connected to `kfam227/website`. Documented pull-before-work, push-when-done rhythm. Confirmed Claude Code can git pull and push on command.
17. **Repo organized** — Moved `soky-pitch-deck-h.html` from root into `HTML/` folder. Updated all WordPress iframe URLs accordingly. Deleted unused file from root.
18. **SOKY Rx margin fix** — Changed "High" to "Available upon request" in pitch deck unit economics table (S6). Updated `og:url` meta tag to correct `HTML/` subfolder path.
19. **Team update one-pager built** — Created `HTML/nmthera-team-update-q2.html` — BSG v3.0 styled internal team update with: dark cover hero with 3 live links, Asana board progress bar (49%/528 tasks), 5-node launch timeline, traction stats, 4 swim lanes (Yellow/Red/Blue/Green teams), 3 horizons (Now/Near/Beyond), honest context callout, manifesto quote.
20. **Team update rebuilt as multi-tab** — Rebuilt `HTML/nmthera-team-update-q2.html` into 4-tab page matching sitemap superpage architecture: Tab 1 Overview, Tab 2 Roadmap (Gantt-style campaign timeline), Tab 3 Build Log (from JOURNAL.md), Tab 4 Links & Assets.
21. **WordPress iframe — team-update slug** — Set up iframe on `nmthera.com/team-update` pointing to GitHub Pages team update. Diagnosed mobile rendering issue — provided div wrapper fix using `100dvh`.
22. **Q2 team message drafted** — Wrote internal team update message referencing Feb 12 launch, 250K Reddit views, 2 sales, honest leadership accountability note, Q2 bandwidth ask, and investor pitch deck share request.
23. **JOURNAL.md initialized and backfilled** — Created JOURNAL.md with all sessions from March 13 through April 3. Reversed to newest-first order.

### Key Decisions

- **Self-hosted video over YouTube embeds** — YouTube iframes fail to autoplay inside cross-origin iframes on mobile. Self-hosted `.mp4` with `playsinline` attribute is the reliable path.
- **GitHub Pages as CDN** — Serving compressed video (32 MB) directly from GitHub Pages rather than WordPress media library. Faster, no plugin dependencies, version-controlled.
- **OG image standardized** — All files point to `NM-THERA-LOGO-SITE-IMAGE.png` on nmthera.com as the shared social preview image.
- **Print layouts left as-is** — `soky-001-product-insert-v2.html` and `soky-002-kit-insert.html` are intentionally non-responsive (fixed 8.5x11in print layouts). No responsive fixes applied.
- **WordPress iframe pattern locked** — Every major HTML file now follows the same pattern: GitHub Pages URL → `position:fixed; z-index:99999` iframe → WordPress Elementor HTML widget. No more copy-pasting code into WordPress.
- **Team update as living document** — `nmthera-team-update-q2.html` is designed to be periodically updated via Claude Code + git push. WordPress page never needs to be touched again.
- **Full team roster sourced from LinkedIn PDFs** — All 12 profiles (6 team, 4 advisors, 2 investors) verified against uploaded LinkedIn profile PDFs before being written into pitch deck and business plan.
- **Honest framing in team comms** — Team update explicitly acknowledges leadership follow-through gaps, not just team bandwidth. Sets tone for Q2 accountability on both sides.

### Files Changed

```
e6ef55f  swap KV Blue to self-hosted video — business plan and pitch deck
         HTML/business-plan-enhanced.html
         HTML/soky-pitch-deck-h.html

2c20cc1  test self-hosted video embed — community feed mobile fix
         HTML/community-feed-3-card (1).html

f30ae44  add compressed KV Blue hero video
         Videos/26Mar2026 Kv Blue.mp4

32e73c1  test YouTube iframe embed — community feed
         HTML/community-feed-3-card (1).html

7dfaaa9  audit fixes — OG tags, meta descriptions, TBD pricing
         HTML/business-plan-enhanced.html
         HTML/community-feed-3-card (1).html
         HTML/nmthera-sitemap-superpage.html
         HTML/soky-001-product-insert-v2.html
         HTML/soky-002-kit-insert.html
         HTML/soky-homepage.html
         HTML/soky-pdp-v2.html
         HTML/soky-pitch-deck (1).html
         HTML/soky-pitch-deck-h.html
         HTML/Drafts/NMThera_BusinessPlan_2026_v4.html
         HTML/Drafts/NMThera_BusinessPlan_2026_v6.html
         HTML/Drafts/NMThera_Valuation_Analysis_2026.html
         HTML/Drafts/SOKY_Clinical_v1.2.html
         HTML/Drafts/SOKY_Investor_v1.3.html
         HTML/Drafts/SOKY_LandingVideo_v1.0.html
         HTML/Drafts/SOKY_Manifesto_v2.0.html

3da8fc5  moved pitch deck to HTML folder
         HTML/soky-pitch-deck-h.html

f27f60f  initial commit — desktop workshop files
         27 files (full repo)

ec1d9f5  rebuild team update — multi-tab with roadmap, build log, and links
         HTML/nmthera-team-update-q2.html

25dbc70  added team update html file
         HTML/nmthera-team-update-q2.html

989a597  update team slide — full roster with accurate profiles
         HTML/soky-pitch-deck-h.html

4b9b7f6  update team section — full roster with accurate profiles — business plan
         HTML/business-plan-enhanced.html

85946bd  add frame-ancestors CSP — business plan iframe fix
         HTML/business-plan-enhanced.html

53555c6  final fixes — SOKY Rx margin and OG url — pitch deck
         HTML/soky-pitch-deck-h.html

4b42eae  swap KV Blue to self-hosted video — sitemap superpage
         HTML/nmthera-sitemap-superpage.html
```

### Next Steps

- Pull latest on laptop before next session (`git pull`)
- Connect WooCommerce Add-to-Cart to front-end store pages
- Build email capture flow on nmthera.com
- Each team member confirms Q2 bandwidth this week
- Broadcast push target: April 14-21
- April 30 — Campaign 1 sell-through milestone

---

## Session — March 23, 2026

### What We Did

1. **Luminescent fluid formulation research** — Explored bioluminescence aesthetic for SOKY glove (dinoflagellate flash response to mechanical force).
2. **Formulation document produced** — NMT-FL-001 v0.1 "Luminal Ritual Fluid." Peroxyoxalate chemiluminescent base with phosphorescent pigment system.
3. **Procurement-ready spec** — Full ingredient list, concentrations, mixing protocol, and safety notes.

### Key Decisions

- **Long-term target is true mechanoluminescent microencapsulates** — Current formulation uses chemical chemiluminescence as a bridge. True mechanoluminescent capsules (force-activated light) are the goal once cosmetic-grade versions become commercially available.

### Files Changed

- None (formulation document produced in Claude Chat — not yet added to repo)

### Next Steps

- Source peroxyoxalate and phosphorescent pigment samples for bench testing
- Evaluate shelf life and skin-contact safety profile
- Draft formulation into HTML spec sheet for repo

---

## Session — March 20, 2026 — Session 7

### What We Did

1. **Investor valuation analysis HTML** — Produced comprehensive report with nine Chart.js interactive visualizations.
2. **Blended valuation** — Base case $3.2M (asset reconstruction 35%, comparable transactions 35%, risk-adjusted DCF 30%). Bear $1.5M, Bull $6.5M.
3. **Exit modeling** — Year 10 exit $240M–$361M (~113× return at base case).
4. **Key value event identified** — Patent issuance March 2023 as the single largest value inflection in company history.

### Key Decisions

- **Three-method blended valuation** — No single method is reliable for pre-revenue hardware startups. Blended approach with explicit weighting provides the most defensible number.

### Files Changed

- `HTML/Drafts/NMThera_Valuation_Analysis_2026.html`

### Next Steps

- Sensitivity analysis on DCF discount rate assumptions
- Add comparable transaction data sources as footnotes
- Link valuation report from investor journey page

---

## Session — March 20, 2026 — Session 6

### What We Did

1. **Claude Code Windows setup resolved** — Fixed Git Bash path issue via user environment variable (`CLAUDE_CODE_GIT_BASH_PATH`).
2. **Working pattern established** — Claude Chat for strategy and prompt drafting, Claude Code for file execution in the Workshop G directory.
3. **Terminal clarification** — Documented difference between Command Prompt and MINGW64/Git Bash terminals on Windows.

### Key Decisions

- **Git Bash is the required terminal for Claude Code on Windows** — Command Prompt lacks the Unix utilities Claude Code depends on.

### Files Changed

- None (environment setup — no repo files changed)

### Next Steps

- Test Claude Code file read/write/commit workflow
- Initialize repo from Claude Code terminal

---

## Session — March 20, 2026 — Session 5

### What We Did

1. **Investor outreach asset stack designed** — Mapped the full investor journey from first touch to ask.
2. **Single-page investor journey HTML** — Built 10-panel scrolling page: problem stats, ritual flow, SVG engineering diagram (inversion cuff), TAM/SAM/SOM charts, traction proof, IP timeline, platform roadmap, team/equity, revenue projections, ask with valuation milestone grid.

### Key Decisions

- **Sequence matters** — The investor journey follows a strict funnel: hero video → email gate → dashboard → full plan → ask. Each asset serves one stage.

### Files Changed

- `HTML/Drafts/SOKY_Investor_v1.3.html`

### Next Steps

- Build email gate component
- Connect investor page to pitch deck flow
- Test scroll performance on mobile

---

## Session — March 20, 2026 — Session 4

### What We Did

1. **Investor business plan HTML** — Built comprehensive plan (v3 → v4) incorporating BSG v1.2 design tokens.
2. **Six-mode enhancement system** — Documented the full SOKY product mode architecture.
3. **Precision frontier section** — Added topical peptide soaks as the next-generation product thesis.
4. **IP section corrected** — All four items: issued utility patent, pending platform patent, NM Thera trademark, SOKY logo trademark.
5. **Markdown export** — Produced parallel markdown version for audio review workflow.

### Key Decisions

- **Premium editorial presentation over standard business doc formatting** — The business plan is a design artifact, not a Word doc. Full BSG visual system applies.

### Files Changed

- `HTML/Drafts/NMThera_BusinessPlan_2026_v4.html`

### Next Steps

- Audio review pass using markdown export
- Iterate to v5/v6 with financial charts
- Add media elements (product photography, video sections)

---

## Session — March 20, 2026 — Session 3

### What We Did

1. **Skill file corrections** — Fixed five locations in v1.2 where the skill file overstated NM Thera's legal and governance structure.
2. **Corporate structure clarified** — NM Thera is a private venture: Delaware C Corp parent, California LLC subsidiary. Commons/foundation structure is future aspiration only — not current reality.
3. **Section 18 added** — Asana Operating System section with full campaign roadmap, team swim lanes, and COB personnel records.

### Key Decisions

- **Never describe NM Thera as steward-owned or foundation-governed** — These are aspirational structures. Current entity is a standard C Corp/LLC.

### Files Changed

- `.claude/skills/SOKY_NM_Thera_Foundational_Reference_System_v12_20Mar2026.skill`

### Next Steps

- Verify all downstream documents reflect corrected corporate structure
- Cross-check manifesto and investor docs for governance language

---

## Session — March 20, 2026 — Session 2

### What We Did

1. **Asana Master Coordinator audit** — Full review of the NM Thera Asana board (project ID: `1208481693455010`).
2. **Campaign roadmap mapped** — Six-campaign sequential drop schedule April–December 2026.
3. **Task hygiene** — Identified 15 unassigned Campaign 1 subtasks. Found missing website, CRM, and email list tasks.
4. **Date corrections** — Updated Campaign 1 due date to April 30. Completed February payroll tasks and rolled forward recurring dates.

### Key Decisions

- **Asana is the company operating system** — Claude must actively maintain it, not just read from it. Task creation, assignment, and date management are ongoing responsibilities.

### Files Changed

- None (Asana operations — no repo files changed)

### Next Steps

- Assign all 15 unassigned Campaign 1 subtasks
- Create missing website/CRM/email list tasks
- Build Asana section into skill file

---

## Session — March 20, 2026 — Session 1

### What We Did

1. **Development tool comparison** — Evaluated GitHub, VS Code, Claude Code, and Claude Chat for task suitability. Mapped each tool to appropriate use cases.
2. **Task-to-tool routing** — Established which tool handles which class of work.

### Key Decisions

- **Primary rhythm: Claude Chat for strategy/copy/artifacts, Claude Code for file-system work** — Claude Code becomes primary as codebase complexity grows. Chat remains the strategy and drafting environment.

### Files Changed

- None (planning session)

### Next Steps

- Set up Claude Code on desktop with Workshop G directory
- Test file read/write workflow in Claude Code

---

## Session — March 19, 2026 — Session 3

### What We Did

1. **Code architecture reference tables** — Generated detailed structural documentation for all three core HTML documents: Investor Overview v1.3, Manifesto v1.9.1, Clinical Partner Program.
2. **Cross-document analysis** — Produced report identifying inconsistencies, errors, and consolidation opportunities across the three files.
3. **Errors identified** — Duplicate product label, incorrect patent status in manifesto, spaced wordmark rendering error.

### Key Decisions

- None (audit session — findings fed into subsequent fix sessions)

### Files Changed

- None (analysis output only — no edits applied this session)

### Next Steps

- Fix duplicate product label across affected files
- Correct patent status language in manifesto
- Resolve spaced wordmark rendering issue

---

## Session — March 19, 2026 — Session 2

### What We Did

1. **Clinical Partner Program page** — Refined from v1.3 to v1.4. Added all real product photography replacing SVG placeholders.
2. **SVG stroke icon system** — Ported from manifesto: 38×38 rounded square containers with consistent stroke weight.
3. **Manifesto v2.0 final output** — Produced clean final version with all icon and photography updates.
4. **Clinical tier badge fix** — Corrected badge color to pool (#006D77) for brand consistency.

### Key Decisions

- **Stroke-only icon system, no emoji** — All icons across all documents must use the SVG stroke system. Zero emoji anywhere.

### Files Changed

- `HTML/Drafts/SOKY_Clinical_v1.2.html`
- `HTML/Drafts/SOKY_Manifesto_v2.0.html`

### Next Steps

- Cross-check icon consistency across all documents
- Verify all product photos load from nmthera.com CDN

---

## Session — March 19, 2026 — Session 1

### What We Did

1. **HTML architecture fundamentals** — Discussed how HTML compares to compiled languages like C++, CSS variable systems, download button implementation, and 3D model viewer feasibility (Three.js/Babylon.js).
2. **Code navigation mental model** — Established approach for navigating large HTML files to make targeted edits without breaking surrounding structure.

### Key Decisions

- **HTML5 is the correct standard** — XHTML is legacy and not applicable to this project. All documents use `<!DOCTYPE html>`.

### Files Changed

- None (educational session — no code output)

### Next Steps

- Apply HTML navigation patterns to upcoming document edits
- Evaluate Three.js for potential 3D glove viewer on PDP

---

## Session — March 18, 2026 — Session 2

### What We Did

1. **Video landing page block** — Built HTML landing page featuring portrait video (9:16 aspect ratio) with reactive blurred canvas background.
2. **Canvas mirror system** — Canvas draws video edge pixels in real time, creating a blurred ambient light effect behind the video frame.
3. **Three design iterations** — Achieved full BSG design system parity: navy/pool/sunlight/paper palette, Montserrat 800, frosted glass panels, water ripple effect.

### Key Decisions

- **Canvas draws video cover-filled at 116% viewport** — CSS `filter` handles blur and saturation to avoid CORS taint issues with cross-origin video sources.

### Files Changed

- `HTML/Drafts/SOKY_LandingVideo_v1.0.html`

### Next Steps

- Test canvas performance on mobile devices (GPU compositing budget)
- Add mute toggle and CTA overlay
- Evaluate portrait vs landscape video for different viewport sizes

---

## Session — March 18, 2026 — Session 1

### What We Did

1. **SOKY Manifesto refinement** — Iterated from v0.6 to v1.3. Standardized the ritual sequence, expanded audiences grid from four to six cards, added ninth charter principle on conservation.
2. **Commons governance card rewrite** — Strengthened the open-platform governance language.
3. **Closing section rework** — Tightened the manifesto's closing statement.

### Key Decisions

- **Manifesto serves all six audiences simultaneously** — consumers, partners, collaborators, developers, practitioners, and investors. Single document, no audience-specific forks.

### Files Changed

- `HTML/Drafts/SOKY_Manifesto_v2.0.html` (predecessor versions)

### Next Steps

- Port manifesto to final v2.0 HTML with full BSG design system
- Add real product photography replacing placeholder content

---

## Session — March 17, 2026

### What We Did

1. **Built foundational SOKY/NM Thera skill file** — Created the persistent reference system (v1.0 → v1.2) using the Claude skill-creator framework.
2. **Encoded full company knowledge base** — Company identity, product architecture (5 SKUs), engineering mechanics, IP portfolio, competitor landscape, pricing strategy, brand voice rules, audience segmentation, and patent drawing visual reference library.

### Key Decisions

- **Skill file established as the single source of truth** for all future Claude sessions — eliminates re-briefing overhead and ensures consistency across Chat and Code contexts.

### Files Changed

- `.claude/skills/SOKY_NM_Thera_Foundational_Reference_System_v12_20Mar2026.skill` (initial creation, later renamed)

### Next Steps

- Test skill file persistence across new Claude sessions
- Add Asana operating system section
- Encode campaign roadmap and team structure

---

## Session — March 13, 2026

### What We Did

1. **Silicone glove recycling and circular economy research** — Explored end-of-life design strategies for SOKY gloves. Covered HCR vs LSR material properties, overmolding strategies, at-home patching techniques, and closed-loop manufacturing partnerships (Dow, Momentive, Wacker).
2. **Repurposing pathways** — Mapped options for glove second-life use and material recovery.

### Key Decisions

- **LSR overmolded onto TPU skeleton** selected as the most promising end-of-life design concept — enables material separation at recycling and extends usable life through structural reinforcement.

### Files Changed

- None (research session — no code output)

### Next Steps

- Investigate Dow/Momentive take-back programs for post-consumer LSR
- Model cost impact of TPU skeleton on BOM
- Draft circular economy section for business plan

---

## April 10, 2026 — Website Development Pipeline & PDP/Homepage Redesign

### What happened today
- Synced with Hameed on website architecture, SEO strategy, and global tax compliance
- Synced with Tiffany on UX review workflow, product offer structure, and launch scope
- Established a repeatable website development pipeline with defined roles:
  - **Kenny / Jen** → design generation (Claude AI, iterated to ~90% complete)
  - **Chi** → content & branding approval
  - **Tiffany** → UX, formatting, layout review
  - **Hameed** → Elementor build + backend connections
  - **Full team** → QA before launch
- Killed the Research Access offer ($45 + 8-week program). Replaced with single glove at $45 (SKU 000)
- Confirmed three-offer PDP structure: SKU 000 ($45 single glove), SKU 001 ($85 pair), SKU 002 ($120 Travel System)
- Scoped launch to US market only — international handled via "contact us" form
- Created Asana tasks (Home V2, PDP V2) with full handoff prompts, reference links, and implementation instructions
- Built pipeline diagram in FigJam for team reference

### Three implementation methods (Hameed)
1. **Method 1:** HTML native connectors — front-end to back-end directly in code
2. **Method 2:** Elementor overlay — Elementor mediates between front-end and back-end
3. **Method 3:** Full Elementor rebuild (~1.5 days) — best for SEO, editing, long-term maintenance

### Key decisions
- Method 3 is the default for all customer-facing pages (unique URLs for SEO indexing)
- Pipeline sequencing: Chi approves content BEFORE Tiffany reviews formatting (content must be locked first)
- WP Mail Logging plugin may be sufficient short-term — delays HubSpot integration
- Stripe setup deferred until after US launch

### Learnings & improvements for next time
1. **Lock content with Chi before generating the design** — saves a full iteration cycle
2. **Include Tiffany earlier in SKU/offer strategy** — UX concerns should surface before design is built, not after
3. **Don't make customers work** — the Research Access model added friction. Sell the product simply. Use a money-back guarantee to reduce risk instead of gating behind a program
4. **SEO requires unique URLs** — tabbed single-page HTML is invisible to Google. Every public page needs its own slug
5. **AI-generated designs need a human pass** — Method 3 exists partly to humanize the output
6. **Ship for one market first** — US-only launch keeps timeline tight. Handle international interest with a form
7. **Standardize the handoff artifact** — every page ships with: live draft link, GitHub source link, attached HTML file
8. **Document implementation methods permanently** — avoid re-explaining tradeoffs every time a new page comes up

### References
- Homepage draft: nmthera.com/home2
- PDP draft: nmthera.com/hand-soky
- GitHub (homepage): https://github.com/kfam227/website/blob/main/HTML/nmthera-sitemap-superpage.html
- GitHub (PDP): https://github.com/kfam227/website/blob/main/HTML/soky-pdp-v2.html
- Asana tasks: Home V2, PDP V2
