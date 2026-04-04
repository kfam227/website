# JOURNAL.md — NM Thera / SOKY Build Log

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

### Key Decisions

- **Self-hosted video over YouTube embeds** — YouTube iframes fail to autoplay inside cross-origin iframes on mobile. Self-hosted `.mp4` with `playsinline` attribute is the reliable path.
- **GitHub Pages as CDN** — Serving compressed video (32 MB) directly from GitHub Pages rather than WordPress media library. Faster, no plugin dependencies, version-controlled.
- **OG image standardized** — All files point to `NM-THERA-LOGO-SITE-IMAGE.png` on nmthera.com as the shared social preview image.
- **Print layouts left as-is** — `soky-001-product-insert-v2.html` and `soky-002-kit-insert.html` are intentionally non-responsive (fixed 8.5x11in print layouts). No responsive fixes applied.

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
```

### Next Steps

- Verify all video sources load correctly on GitHub Pages (cache propagation can take a few minutes)
- Test pitch deck iframe embed on additional mobile devices and browsers
- Consider adding a lower-bitrate mobile variant of KV Blue for bandwidth-constrained connections
- Address remaining audit items: remove `console.log` calls from sitemap superpage, add skip-links, fix heading hierarchy gaps in draft files
- Review "Coming Soon" labels across product inserts — update any that have since launched
- Sync the Apply Media CSS drift (standalone `.css` vs embedded copies in scripts)
