# SOKY Business Plan — Media Integration Package
## NM Thera · March 2026

---

## What This Package Contains

| File | Purpose |
|------|---------|
| `apply_media.py` | **Automated script** — run against your original HTML to produce the enhanced version |
| `media-css-additions.css` | Standalone CSS — all new styles for video, images, media pairs |
| `media-patches.html` | **Visual reference** — every insertion with exact HTML and context markers |

---

## Quick Start (Automated)

```bash
# 1. Place your original business-plan.html in the same directory
# 2. Run:
python3 apply_media.py business-plan.html business-plan-enhanced.html

# 3. Open business-plan-enhanced.html in your browser to verify
# 4. Upload to your server
```

The script makes 18 targeted find-and-replace operations. It does NOT modify any existing content — it only adds media elements at strategic insertion points.

---

## Manual Application

If you prefer to apply changes by hand, open `media-patches.html` and follow each numbered edit. Every edit includes:

1. **FIND** — the exact text string to search for in your HTML
2. **INSERT BEFORE/AFTER or REPLACE** — what to do
3. **The exact HTML** — copy and paste

### Application Order

1. Add CSS from `media-css-additions.css` before `</style>`
2. **Topbar**: Replace the CSS `.drop` div with the logo `<img>` tag
3. **Cover**: Add video background + mute button before `.cover-caustic`
4. **Cover top**: Replace empty brand span with logo image
5. **S1–S14**: Insert media elements at each marked location
6. **JavaScript**: Add mute toggle functions before `</script>`

---

## Media Asset Map

### Videos (3)
| Asset | Section | Treatment |
|-------|---------|-----------|
| 26Mar2026-KV-BLUE.mp4 | Cover | Full-bleed background video, muted/autoplay/loop, 35% opacity with gradient overlay |
| 0227.mp4 (Travel Kit Anim) | S5 Launch | Hero video section before proof points |
| pool-water-video-cl-edit.mp4 | S3 Product | Visual break before Engineering Core |

### Patent/Technical Drawings (4)
| Asset | Section | Treatment |
|-------|---------|-----------|
| Patent Fig 1 (HandSOKY) | S7 IP | Full-width patent figure above IP table |
| Fig HandSOKY Model F | S3 Product | Side-by-side with annotated diagram |
| Fig FootSOKY Model F | S6 Roadmap | Side-by-side with KneeSOKY |
| Fig KneeSOKY Model F | S6 Roadmap | Side-by-side with FootSOKY |

### Product Photography (5)
| Asset | Section | Treatment |
|-------|---------|-----------|
| SKU001-Launch-Assets-3 (water) | S1 Overview | Hero image after lede |
| SKU001-Launch-Assets-4 (plant) | S12 Markets | Visual break before market analysis |
| SKU001-Launch-Assets-2 (annotated) | S3 Product | Side-by-side with Model F drawing |
| SKU001-Launch-Assets-6 (flat) | S5 Launch | Side-by-side with Travel Kit static |
| Travel Kit static | S5 Launch | Side-by-side with flat shot |

### Lifestyle / In-Use Photography (7)
| Asset | Section | Treatment |
|-------|---------|-----------|
| IRL Key Visual (IMG_0152) | S2 Founding | Full-width after quote band |
| IMG_9940 (fist balled) | S3 Product | Short break before Platform Expansion |
| IMG_1196 (spa tiles) | S4 Modes | Medium break before Volume Advantage |
| IMG_9929 (fingers splayed) | S9 Partners | Short break visual |
| IMG_1194 (spa tiles #2) | S10 Supply | Short break before regulatory |
| IMG_9594 + IMG_9601 (book) | S11 Clinical | Side-by-side pair before dispensing |
| IMG_9921 + IMG_0289 (hands) | S8 Team | Side-by-side pair before Advisors |

### Closing (1)
| Asset | Section | Treatment |
|-------|---------|-----------|
| IMG_0283 (side profile) | S14 Valuation | Short break before analyst quote |

### Logo Assets (2)
| Asset | Location | Treatment |
|-------|----------|-----------|
| NM Thera Main Logo | Cover top area | 28px height, 60% opacity |
| NM Thera Water Drop | Topbar brandline | 22px icon replacing CSS drop shape |

---

## CSS Classes Reference

| Class | Usage |
|-------|-------|
| `.media-break` | Full-width image container with rounded corners and shadow |
| `.media-break.tall` | Max 480px height |
| `.media-break.medium` | Max 360px height |
| `.media-break.short` | Max 260px height |
| `.media-break-caption` | Overlay caption at bottom of media-break |
| `.inline-media` | Bordered image container within content |
| `.inline-media.patent` | White background, padded, for technical drawings |
| `.inline-media-caption` | Below-image caption bar |
| `.media-pair` | Two-column grid for side-by-side images |
| `.video-section` | Video container with dark background |
| `.video-section-caption` | Overlay caption for video sections |
| `.video-mute` | Circular mute toggle button for inline videos |
| `.cover-video-wrap` | Full-bleed cover video container |
| `.cover-mute-btn` | Cover-specific mute button |
| `.topbar-logo` | Logo image in the topbar |

All classes are fully responsive across the existing breakpoints (1200px, 900px, 700px, 480px, 380px) and hidden in print.

---

## Notes

- All videos are `muted` and `autoplay` by default with `loop` and `playsinline` attributes
- Each video has a mute/unmute toggle button
- The cover video uses a `poster` attribute (SKU001-Launch-Assets-3.jpg) as a fallback
- All images use `loading="lazy"` for performance
- All media elements include the `reveal` class for the existing scroll-triggered fade-in animation
- No existing content, styles, or scripts are modified — only additions
