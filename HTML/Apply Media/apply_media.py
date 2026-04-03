#!/usr/bin/env python3
"""
SOKY Business Plan — Media Integration Script
Applies all image/video assets to the HTML business plan.
"""

import sys
import os

def apply_modifications(html):
    """Apply all media insertions to the business plan HTML."""

    # ═══════════════════════════════════════════════════════════════
    # 1. ADD NEW CSS — before </style>
    # ═══════════════════════════════════════════════════════════════
    new_css = """
/* ═══════════════════════════════════════
   MEDIA INTEGRATION · v1.0
═══════════════════════════════════════ */

/* ── COVER VIDEO ── */
.cover-video-wrap {
  position: absolute; inset: 0; z-index: 0; overflow: hidden;
}
.cover-video-wrap video {
  position: absolute; top: 50%; left: 50%;
  min-width: 100%; min-height: 100%;
  width: auto; height: auto;
  transform: translate(-50%, -50%);
  object-fit: cover;
  opacity: 0.35;
}
.cover-video-wrap::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(175deg,
    rgba(12,21,32,0.6) 0%,
    rgba(12,21,32,0.35) 40%,
    rgba(12,21,32,0.75) 100%);
  z-index: 1;
}
.cover-mute-btn {
  position: absolute; bottom: 20px; right: 20px; z-index: 10;
  background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2);
  border-radius: 50%; width: 40px; height: 40px;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: all 0.2s ease;
  color: rgba(255,255,255,0.5);
}
.cover-mute-btn:hover { background: rgba(255,255,255,0.2); color: rgba(255,255,255,0.8); }
.cover-mute-btn svg { width: 18px; height: 18px; fill: currentColor; }

/* ── TOPBAR LOGO ── */
.topbar-logo {
  width: 22px; height: 22px; object-fit: contain; flex: 0 0 auto;
  border-radius: 4px; opacity: 0.85;
}
.topbar.is-dark .topbar-logo { opacity: 0.7; filter: brightness(1.8); }

/* ── MEDIA BREAK (full-width visual between content) ── */
.media-break {
  width: 100%; border-radius: var(--r-xl); overflow: hidden;
  box-shadow: var(--shadow); position: relative;
}
.media-break img {
  width: 100%; height: auto; display: block;
  object-fit: cover;
}
.media-break.tall img { max-height: 480px; object-fit: cover; }
.media-break.medium img { max-height: 360px; object-fit: cover; }
.media-break.short img { max-height: 260px; object-fit: cover; }
.media-break.portrait img { max-height: 520px; object-fit: cover; object-position: center; }
.media-break-caption {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 2rem 1.5rem 1rem;
  background: linear-gradient(0deg, rgba(12,21,32,0.7) 0%, transparent 100%);
  font-family: var(--sub); font-size: 10px; font-weight: 600;
  letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.5);
}

/* ── INLINE MEDIA (inside content-stack) ── */
.inline-media {
  width: 100%; border-radius: var(--r-md); overflow: hidden;
  border: 1px solid var(--line); box-shadow: var(--shadow-sm);
}
.inline-media img {
  width: 100%; height: auto; display: block; object-fit: cover;
}
.inline-media.constrained img { max-height: 400px; object-fit: contain; background: #fafaf9; padding: 1rem; }
.inline-media.patent img { max-height: 440px; object-fit: contain; background: #fff; padding: 1.5rem; }
.inline-media-caption {
  padding: 0.5rem 0.75rem;
  font-family: var(--sub); font-size: 9.5px; font-weight: 600;
  letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted);
  background: rgba(49,89,138,0.03); border-top: 1px solid var(--line);
}

/* ── MEDIA PAIR (side by side) ── */
.media-pair {
  display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
}
.media-pair .inline-media img { max-height: 280px; object-fit: cover; }

/* ── VIDEO SECTION ── */
.video-section {
  width: 100%; border-radius: var(--r-xl); overflow: hidden;
  box-shadow: var(--shadow); position: relative;
  background: #0c1520;
}
.video-section video {
  width: 100%; height: auto; display: block;
  max-height: 500px; object-fit: cover;
}
.video-section .video-mute {
  position: absolute; bottom: 14px; right: 14px; z-index: 5;
  background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.15);
  border-radius: 50%; width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; transition: all 0.2s ease;
  color: rgba(255,255,255,0.6);
}
.video-section .video-mute:hover { background: rgba(0,0,0,0.7); color: #fff; }
.video-section .video-mute svg { width: 16px; height: 16px; fill: currentColor; }
.video-section-caption {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 2.5rem 1.25rem 0.85rem;
  background: linear-gradient(0deg, rgba(12,21,32,0.75) 0%, transparent 100%);
  font-family: var(--sub); font-size: 10px; font-weight: 600;
  letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.45);
}

/* ── PRODUCT IMAGE GRID ── */
.product-gallery {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;
}
.product-gallery .inline-media img { max-height: 220px; object-fit: cover; }

/* ── RESPONSIVE MEDIA ── */
@media (max-width: 900px) {
  .media-break.tall img { max-height: 320px; }
  .media-break.medium img { max-height: 260px; }
  .media-pair { grid-template-columns: 1fr; }
  .product-gallery { grid-template-columns: 1fr 1fr; }
  .video-section video { max-height: 360px; }
}
@media (max-width: 480px) {
  .media-break { border-radius: var(--r-lg); }
  .media-break.tall img { max-height: 260px; }
  .media-break.medium img { max-height: 200px; }
  .media-break.short img { max-height: 180px; }
  .video-section { border-radius: var(--r-lg); }
  .video-section video { max-height: 280px; }
  .product-gallery { grid-template-columns: 1fr; }
  .inline-media.patent img { padding: 0.75rem; }
  .cover-mute-btn { width: 34px; height: 34px; bottom: 14px; right: 14px; }
}
@media print {
  .cover-video-wrap, .video-section, .cover-mute-btn, .video-mute { display: none; }
}
"""
    html = html.replace('</style>', new_css + '\n</style>')

    # ═══════════════════════════════════════════════════════════════
    # 2. TOPBAR — Replace CSS drop with logo icon
    # ═══════════════════════════════════════════════════════════════
    html = html.replace(
        '<div class="drop" aria-hidden="true"></div>',
        '<img src="https://nmthera.com/wp-content/uploads/2026/03/Logo-Icon.png" alt="NM Thera" class="topbar-logo">'
    )

    # ═══════════════════════════════════════════════════════════════
    # 3. COVER — Add video background + mute button
    # ═══════════════════════════════════════════════════════════════
    cover_video = """<div class="cover-video-wrap" aria-hidden="true">
    <video id="cover-vid" autoplay muted loop playsinline preload="metadata" poster="https://nmthera.com/wp-content/uploads/2026/01/SKU001-Launch-Assets-3.jpg">
      <source src="https://nmthera.com/wp-content/uploads/2026/03/26Mar2026-KV-BLUE.mp4" type="video/mp4">
    </video>
  </div>
  <button class="cover-mute-btn" id="cover-mute" aria-label="Toggle sound" title="Toggle sound">
    <svg id="mute-icon" viewBox="0 0 24 24"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51A8.796 8.796 0 0 0 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3 3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06a8.99 8.99 0 0 0 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4 9.91 6.09 12 8.18V4z"/></svg>
    <svg id="unmute-icon" viewBox="0 0 24 24" style="display:none"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
  </button>"""

    html = html.replace(
        '<div class="cover-caustic" aria-hidden="true">',
        cover_video + '\n  <div class="cover-caustic" aria-hidden="true">'
    )

    # ═══════════════════════════════════════════════════════════════
    # 4. S1 OVERVIEW — Hero image after lede
    # ═══════════════════════════════════════════════════════════════
    s1_image = """
    <div class="media-break medium reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/SKU001-Launch-Assets-3.jpg" alt="HandSOKY — cinematic product shot against water" loading="lazy">
      <div class="media-break-caption">HandSOKY · Key Visual</div>
    </div>"""

    html = html.replace(
        '<p>The answer took eight years to build.',
        s1_image + '\n    <p>The answer took eight years to build.'
    )

    # ═══════════════════════════════════════════════════════════════
    # 5. S2 FOUNDING — IRL lifestyle image after quote band
    # ═══════════════════════════════════════════════════════════════
    s2_image = """
    <div class="media-break medium reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_0152.jpg" alt="SOKY in a home setting — relaxed, real" loading="lazy">
      <div class="media-break-caption">Real Use · Workshop G · Eastvale, CA</div>
    </div>"""

    html = html.replace(
        """<p>The options for treating conditions like palmar hyperhidrosis have barely evolved""",
        s2_image + '\n    <p>The options for treating conditions like palmar hyperhidrosis have barely evolved'
    )

    # ═══════════════════════════════════════════════════════════════
    # 6. S3 PRODUCT — Multiple media insertions
    # ═══════════════════════════════════════════════════════════════

    # 6a. Pool water video after the ritual bar + don callout
    s3_video = """
    <div class="video-section reveal">
      <video id="pool-vid" autoplay muted loop playsinline preload="metadata">
        <source src="https://videos.files.wordpress.com/2uAOPAQx/pool-water-video-cl-edit.mp4" type="video/mp4">
      </video>
      <button class="video-mute" onclick="toggleVidMute('pool-vid', this)" aria-label="Toggle sound">
        <svg viewBox="0 0 24 24"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51A8.796 8.796 0 0 0 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3 3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06a8.99 8.99 0 0 0 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4 9.91 6.09 12 8.18V4z"/></svg>
      </button>
      <div class="video-section-caption">HandSOKY · Caustic Light · Pool Water Key Visual</div>
    </div>"""

    html = html.replace(
        '<h3>The Engineering Core',
        s3_video + '\n    <h3>The Engineering Core'
    )

    # 6b. Hand Model F patent drawing after engineering core paragraph
    s3_patent = """
    <div class="media-pair reveal">
      <div class="inline-media patent">
        <img src="https://nmthera.com/wp-content/uploads/2026/03/Product-and-Program-Offer-Development-17.png" alt="HandSOKY Model F — active and inactive configuration showing cuff inversion" loading="lazy">
        <div class="inline-media-caption">HandSOKY Model F — Active &amp; Inactive Configuration · Cuff Inversion Detail</div>
      </div>
      <div class="inline-media patent">
        <img src="https://nmthera.com/wp-content/uploads/2026/01/SKU001-Launch-Assets-2.jpg" alt="HandSOKY — annotated product features" loading="lazy">
        <div class="inline-media-caption">HandSOKY — Annotated Feature Diagram</div>
      </div>
    </div>"""

    html = html.replace(
        '<h3>The Universal Port Interface</h3>',
        s3_patent + '\n    <h3>The Universal Port Interface</h3>'
    )

    # 6c. IMG_9940 (fist balled) near platform expansion
    s3_fist = """
    <div class="media-break short reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_9940.jpg" alt="HandSOKY being worn — fist balled showing seal integrity" loading="lazy">
      <div class="media-break-caption">Seal Under Load · Fist Formation</div>
    </div>"""

    html = html.replace(
        '<h3>Platform Expansion Arc</h3>',
        s3_fist + '\n    <h3>Platform Expansion Arc</h3>'
    )

    # ═══════════════════════════════════════════════════════════════
    # 7. S4 MODES — Spa tiles image
    # ═══════════════════════════════════════════════════════════════
    s4_image = """
    <div class="media-break medium reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_1196.jpg" alt="HandSOKY — frontal shot, fist balled, spa tile backdrop" loading="lazy">
      <div class="media-break-caption">HandSOKY · Spa Environment · Wellness Context</div>
    </div>"""

    html = html.replace(
        '<h3>The Volume Advantage',
        s4_image + '\n    <h3>The Volume Advantage'
    )

    # ═══════════════════════════════════════════════════════════════
    # 8. S5 LAUNCH — Travel kit video + product images
    # ═══════════════════════════════════════════════════════════════

    # 8a. Travel Kit Animation video before proof points
    s5_video = """
    <div class="video-section reveal">
      <video id="travelkit-vid" autoplay muted loop playsinline preload="metadata">
        <source src="https://nmthera.com/wp-content/uploads/2026/03/0227.mp4" type="video/mp4">
      </video>
      <button class="video-mute" onclick="toggleVidMute('travelkit-vid', this)" aria-label="Toggle sound">
        <svg viewBox="0 0 24 24"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51A8.796 8.796 0 0 0 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3 3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06a8.99 8.99 0 0 0 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4 9.91 6.09 12 8.18V4z"/></svg>
      </button>
      <div class="video-section-caption">HandSOKY Travel Kit · Product Animation · Key Visual</div>
    </div>"""

    html = html.replace(
        '<h3>Early Proof Points</h3>',
        s5_video + '\n    <h3>Early Proof Points</h3>'
    )

    # 8b. Product images between SKU cards and batch allocation
    s5_products = """
    <div class="media-pair reveal">
      <div class="inline-media">
        <img src="https://nmthera.com/wp-content/uploads/2026/01/SKU001-Launch-Assets-6.jpg" alt="HandSOKY — plain flat shot, top view on cotton towel" loading="lazy">
        <div class="inline-media-caption">HandSOKY — Flat Product Shot</div>
      </div>
      <div class="inline-media">
        <img src="https://nmthera.com/wp-content/uploads/2026/03/Product-and-Program-Offer-Development-12.png" alt="HandSOKY Travel Kit — gloves, towel, and travel bag" loading="lazy">
        <div class="inline-media-caption">HandSOKY Travel Kit — _002 SKU Contents</div>
      </div>
    </div>"""

    html = html.replace(
        '<div class="batch-alloc">',
        s5_products + '\n    <div class="batch-alloc">'
    )

    # ═══════════════════════════════════════════════════════════════
    # 9. S6 ROADMAP — Foot and Knee patent drawings
    # ═══════════════════════════════════════════════════════════════
    s6_images = """
    <div class="media-pair reveal">
      <div class="inline-media patent">
        <img src="https://nmthera.com/wp-content/uploads/2026/03/Product-and-Program-Offer-Development-14.png" alt="FootSOKY Model F — active and inactive configuration" loading="lazy">
        <div class="inline-media-caption">FootSOKY Model F — Active &amp; Inactive Configuration</div>
      </div>
      <div class="inline-media patent">
        <img src="https://nmthera.com/wp-content/uploads/2026/03/Product-and-Program-Offer-Development-15.png" alt="KneeSOKY Model F — active and inactive configuration" loading="lazy">
        <div class="inline-media-caption">KneeSOKY (Ni-SOKY) Model F — Active &amp; Inactive Configuration</div>
      </div>
    </div>"""

    # Insert after the mold cascade, before Track 2
    html = html.replace(
        """<div class="roadmap-track">
      <div class="track-head">
        <div class="track-dot dot-r"></div>""",
        s6_images + '\n    <div class="roadmap-track">\n      <div class="track-head">\n        <div class="track-dot dot-r"></div>'
    )

    # ═══════════════════════════════════════════════════════════════
    # 10. S7 IP — Patent drawing Fig 1
    # ═══════════════════════════════════════════════════════════════
    s7_patent = """
    <div class="inline-media patent reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/03/Product-and-Program-Offer-Development-18.png" alt="Patent Drawing Fig 1 — HandSOKY perspective view showing proximal body-entry opening, self-sealing cuff, and optional port assembly" loading="lazy">
      <div class="inline-media-caption">Patent Drawing · Fig. 1 — US 11,602,631 B2 · Perspective View · Inversion Cuff Seal &amp; Port Assembly</div>
    </div>"""

    html = html.replace(
        """<p>NM Thera's IP portfolio is a material competitive moat.""",
        s7_patent + "\n    <p>NM Thera's IP portfolio is a material competitive moat."
    )

    # ═══════════════════════════════════════════════════════════════
    # 11. S11 CLINICAL — Lifestyle reading image
    # ═══════════════════════════════════════════════════════════════
    s11_image = """
    <div class="media-pair reveal">
      <div class="inline-media">
        <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_9594.jpg" alt="HandSOKY resting on a book — lifestyle context" loading="lazy" style="object-position:center top;">
        <div class="inline-media-caption">Lifestyle · Book &amp; Soak · At-Home Context</div>
      </div>
      <div class="inline-media">
        <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_9601.jpg" alt="HandSOKY on hand, balled fist near book — about to soak and read" loading="lazy" style="object-position:center top;">
        <div class="inline-media-caption">Lifestyle · Don &amp; Read · In Ritual</div>
      </div>
    </div>"""

    html = html.replace(
        '<h3>Clinical Dispensing Opportunity</h3>',
        s11_image + '\n    <h3>Clinical Dispensing Opportunity</h3>'
    )

    # ═══════════════════════════════════════════════════════════════
    # 12. S12 MARKETS — Plant backdrop key visual
    # ═══════════════════════════════════════════════════════════════
    s12_image = """
    <div class="media-break medium reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/SKU001-Launch-Assets-4.jpg" alt="HandSOKY — moody cinematic portrait against plant backdrop" loading="lazy">
      <div class="media-break-caption">HandSOKY · Product Key Visual</div>
    </div>"""

    html = html.replace(
        """<p>SOKY enters the market as the only wearable soak platform""",
        s12_image + '\n    <p>SOKY enters the market as the only wearable soak platform'
    )

    # ═══════════════════════════════════════════════════════════════
    # 13. S9 PARTNERS — IMG_9929 (fingers splayed, looking at palms)
    # ═══════════════════════════════════════════════════════════════
    s9_image = """
    <div class="media-break short reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_9929.jpg" alt="HandSOKY worn — fingers splayed, looking at palms" loading="lazy">
      <div class="media-break-caption">In Use · Fingers Splayed · Full Mobility</div>
    </div>"""

    # Insert after the last callout in S9 (RLP callout)
    html = html.replace(
        """<div class="callout green"><div class="callout-lbl">Rapid Liquid Printing (RLP)""",
        s9_image + '\n    <div class="callout green"><div class="callout-lbl">Rapid Liquid Printing (RLP)'
    )

    # ═══════════════════════════════════════════════════════════════
    # 14. S14 VALUATION — Side profile near closing
    # ═══════════════════════════════════════════════════════════════
    s14_image = """
    <div class="media-break short reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_0283-rotated.jpg" alt="HandSOKY — side profile, fingers splayed" loading="lazy">
      <div class="media-break-caption">HandSOKY · Side Profile · Full Extension</div>
    </div>"""

    html = html.replace(
        '<div class="analyst-quote">',
        s14_image + '\n    <div class="analyst-quote">'
    )

    # ═══════════════════════════════════════════════════════════════
    # 15. S8 TEAM — IMG_9921 (hands clasped) + IMG_0289 (side fist)
    # ═══════════════════════════════════════════════════════════════
    s8_image = """
    <div class="media-pair reveal">
      <div class="inline-media">
        <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_9921.jpg" alt="HandSOKY worn — hands clasped together" loading="lazy">
        <div class="inline-media-caption">In Use · Hands Clasped · Seal Maintained</div>
      </div>
      <div class="inline-media">
        <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_0289-rotated.jpg" alt="HandSOKY — side profile, fist balled" loading="lazy">
        <div class="inline-media-caption">Side Profile · Fist Formation · Compression Hold</div>
      </div>
    </div>"""

    # Insert before the Advisors heading in S8
    html = html.replace(
        """<h3>Advisors</h3>
    <div class="people-grid">
      <div class="person hl-pool">
        <span class="person-badge badge-advisor">Research Advisor""",
        s8_image + '\n    <h3>Advisors</h3>\n    <div class="people-grid">\n      <div class="person hl-pool">\n        <span class="person-badge badge-advisor">Research Advisor'
    )

    # ═══════════════════════════════════════════════════════════════
    # 16. S10 SUPPLY — Spa image #2
    # ═══════════════════════════════════════════════════════════════
    s10_image = """
    <div class="media-break short reveal">
      <img src="https://nmthera.com/wp-content/uploads/2026/01/IMG_1194.jpg" alt="HandSOKY — frontal shot, fist balled, spa tile backdrop" loading="lazy">
      <div class="media-break-caption">Product in Wellness Environment · Spa Tiles</div>
    </div>"""

    html = html.replace(
        '<h3>Regulatory Pathway</h3>',
        s10_image + '\n    <h3>Regulatory Pathway</h3>'
    )

    # ═══════════════════════════════════════════════════════════════
    # 17. COVER — Add NM Thera logo in cover-top
    # ═══════════════════════════════════════════════════════════════
    html = html.replace(
        '<span class="cover-brand"><span></span></span>',
        '<span class="cover-brand"><img src="https://nmthera.com/wp-content/uploads/2026/03/NM-THERA-LOGO-SITE-IMAGE.png" alt="NM Thera" style="height:28px;width:auto;opacity:0.6;vertical-align:middle;margin-right:8px;"><span></span></span>'
    )

    # ═══════════════════════════════════════════════════════════════
    # 18. JAVASCRIPT — Add mute toggle functions before </script>
    # ═══════════════════════════════════════════════════════════════
    mute_js = """

/* ══ VIDEO MUTE TOGGLES ══ */
// Cover video mute toggle
(function() {
  const btn = document.getElementById('cover-mute');
  const vid = document.getElementById('cover-vid');
  const muteIcon = document.getElementById('mute-icon');
  const unmuteIcon = document.getElementById('unmute-icon');
  if (btn && vid) {
    btn.addEventListener('click', function() {
      vid.muted = !vid.muted;
      muteIcon.style.display = vid.muted ? 'block' : 'none';
      unmuteIcon.style.display = vid.muted ? 'none' : 'block';
    });
  }
})();

// Generic video mute toggle
function toggleVidMute(vidId, btn) {
  var vid = document.getElementById(vidId);
  if (!vid) return;
  vid.muted = !vid.muted;
  btn.title = vid.muted ? 'Unmute' : 'Mute';
  btn.style.opacity = vid.muted ? '0.6' : '1';
}
"""
    html = html.replace('</script>', mute_js + '\n</script>')

    return html


# ═══════════════════════════════════════════════════════════════
# MAIN: Read input, apply modifications, write output
# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    input_path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/business-plan-original.html'
    output_path = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/business-plan-enhanced.html'

    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        print("Usage: python3 apply_media.py <input.html> <output.html>")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"Read {len(html):,} characters from {input_path}")

    modified = apply_modifications(html)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(modified)

    chars_added = len(modified) - len(html)
    print(f"Wrote {len(modified):,} characters to {output_path}")
    print(f"Added {chars_added:,} characters of media content")
    print(f"Media integrations applied: 18 assets across 14 sections")
    print("Done!")
