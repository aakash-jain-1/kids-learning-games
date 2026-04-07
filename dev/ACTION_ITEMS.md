# Kids Learning Games — Action Items

> Last updated: 2026-04-07

---

## Issue Tracker

### Status Legend
- [ ] Open
- [x] Done

---

## 1. ~~Home Page — Missing game cards~~ ✅

**Severity:** High | **Effort:** Small | **Status:** Done

- [x] Add Dinosaurs card to `index.html`
- [x] Add Weather card to `index.html`
- [x] Add Woodcutter Story card to `index.html`

---

## 2. ~~Cross-game navigation — Card-machine games have no navbar~~ ✅

**Severity:** High | **Effort:** Medium | **Status:** Done

- [x] Add navbar to `flashcards-game.html`
- [x] Add navbar to `solar-system-game.html`
- [x] Add navbar to `dinosaurs-game.html`
- [x] Add navbar to `weather-game.html`
- [x] Add full navbar to `woodcutter-story.html`

---

## 3. ~~Navigation — Flashcards and Woodcutter not linked from any game~~ ✅

**Severity:** High | **Effort:** Small | **Status:** Done

- [x] `alphabet-game.html`
- [x] `numbers-game.html`
- [x] `colors-game.html`
- [x] `shapes-game.html`
- [x] `animals-game.html`
- [x] `hindi-alphabets.html`
- [x] `birds.html`
- [x] `flashcards-game.html` (added with navbar in #2)
- [x] `solar-system-game.html` (added with navbar in #2)
- [x] `dinosaurs-game.html` (added with navbar in #2)
- [x] `weather-game.html` (added with navbar in #2)
- [x] `woodcutter-story.html` (added with navbar in #2)

---

## 4. ~~Service Worker — `woodcutter-story.html` not cached + no SW registration~~ ✅

**Severity:** Medium | **Effort:** Tiny | **Status:** Done

- [x] Add `'games/woodcutter-story.html'` to `urlsToCache` in `service-worker.js`
- [x] Bump `CACHE_NAME` version (v11 → v12)
- [x] Add SW registration script to `woodcutter-story.html`

---

## 5. ~~Feature parity — Card-machine games missing quiz, achievements, stats, settings~~ ✅

**Severity:** Medium | **Effort:** Large | **Status:** Done

The 7 classic games all have: quiz mode, achievements (5 badges), stats dashboard, and settings panel (dark mode, font size, sound, auto-speak). The 4 card-machine games now have all of these too.

| Feature | Classic (7 games) | Card-machine (4 games) | Woodcutter |
|---|---|---|---|
| Quiz mode | Yes | Yes | Yes (comprehension) |
| Achievements (5 badges) | Yes | Yes | No |
| Stats dashboard | Yes | Yes | No |
| Settings panel | Yes | Yes | No |
| Dark mode | Yes | Yes | No |
| Progress persistence (localStorage) | Yes | Yes | No |

- [x] Add features to `flashcards-game.html`
- [x] Add features to `solar-system-game.html`
- [x] Add features to `dinosaurs-game.html`
- [x] Add features to `weather-game.html`

---

## 6. ~~Home Page — Duplicate CSS rules~~ ✅

**Status:** Done

- [x] Remove the duplicate CSS block

---

## 7. ~~Dev docs — `GAME_REFERENCE.md` inventory table outdated~~ ✅

**Severity:** Low | **Effort:** Tiny | **Status:** Done

- [x] Update inventory table with all 12 games

---

## 8. ~~Build info footer missing from newer games~~ ✅

**Severity:** Low | **Effort:** Tiny | **Status:** Done

- [x] `solar-system-game.html`
- [x] `dinosaurs-game.html`
- [x] `weather-game.html`
- [x] `woodcutter-story.html`

---

## 9. ~~No `<meta name="description">` on game pages~~ ✅

**Severity:** Low | **Effort:** Small | **Status:** Done

- [x] Add `<meta name="description">` to all 12 game files

---

## Priority Summary

| # | Issue | Severity | Effort | Status |
|---|---|---|---|---|
| 1 | ~~Missing home page cards~~ | ~~High~~ | ~~Small~~ | ✅ Done |
| 2 | ~~Card games missing navbar~~ | ~~High~~ | ~~Medium~~ | ✅ Done |
| 3 | ~~Flashcards + Story not in any navbar~~ | ~~High~~ | ~~Small~~ | ✅ Done |
| 4 | ~~Woodcutter not in SW cache + no SW reg~~ | ~~Medium~~ | ~~Tiny~~ | ✅ Done |
| 5 | ~~Card games missing quiz/achievements/stats~~ | ~~Medium~~ | ~~Large~~ | ✅ Done |
| 6 | ~~Duplicate CSS in index.html~~ | ~~Low~~ | ~~Tiny~~ | ✅ Done |
| 7 | ~~GAME_REFERENCE.md outdated~~ | ~~Low~~ | ~~Tiny~~ | ✅ Done |
| 8 | ~~Build info footer missing~~ | ~~Low~~ | ~~Tiny~~ | ✅ Done |
| 9 | ~~Meta descriptions missing~~ | ~~Low~~ | ~~Small~~ | ✅ Done |
| 10 | ~~Enhancement Audit (22 findings)~~ | ~~Mixed~~ | ~~Large~~ | ✅ Done (22/22, all resolved) |
| 11 | ~~Polish Audit (15 findings)~~ | ~~Mixed~~ | ~~Medium~~ | ✅ Done (13/15, M5 N/A, L2 already done) |

---

## 10. ~~Enhancement Audit — 22 findings across bugs, UX, perf, accessibility, SEO, architecture~~ ✅

**Severity:** Mixed (2 Critical, 5 High, 8 Medium, 7 Low) | **Status:** Done

| ID | Finding | Severity | Status |
|---|---|---|---|
| C1 | PWA icons missing | Critical | ✅ Created assets/icon-192.svg + assets/icon-512.svg |
| C2 | Quiz crash if <4 cards | Critical | ✅ Bounded wrongs loop |
| H1 | No Escape key / click-outside for modals | High | ✅ Added to 4 card-machine games |
| H2 | Auto-speak fires on page load | High | ✅ _pageReady guard |
| H3 | Dark mode incomplete (card-machine) | High | ✅ Added top-card, card-name, done-card, fact-box, bottom-bar |
| H4 | No prefers-reduced-motion | High | ✅ Added to all 13 pages |
| H5 | lang attribute wrong on hindi | High | ✅ Already lang="hi" |
| M2 | Outdated descriptions | Medium | ✅ Updated index.html + manifest.json |
| M3 | No OG / Twitter meta tags | Medium | ✅ Added to all 13 pages |
| M4 | GitHub API call every page load | Medium | ✅ localStorage cache w/ 1hr TTL |
| M5 | No loading="lazy" on images | Medium | ✅ Added to weather + flashcards |
| M6 | Code duplication | Medium | ✅ Created common-cards.css + common-cards.js |
| M7 | Woodcutter has no quiz | Medium | ✅ Added 6-question comprehension quiz |
| M8 | Tablet grid single-column too early | Medium | ✅ 2-column at 768px, 1-column at 480px |
| L1 | Navbar style inconsistency | Low | ✅ Unified to white/gradient style |
| L2 | No favicon | Low | ✅ SVG favicon added |
| L3 | push.bat leftover | Low | ✅ Deleted |
| L4 | CSS class reuse on home cards | Low | ✅ Unique classes for all 12 cards |
| L5 | No offline fallback | Low | ✅ Created offline.html + SW fallback |
| L6 | Confetti = 100 DOM divs | Low | ✅ Canvas-based (80 particles, 1 element) |
| L7 | AudioContext per answer | Low | ✅ Singleton _getAudioCtx() |
| M1 | SW cache-first staleness | Medium | ✅ Network-first for HTML, stale-while-revalidate for assets (v19) |

---

## Resolved Issues (from previous audit)

The following mobile rendering issues were identified earlier and have been **fixed**:

- [x] `alphabet-game.html` — Two-pane layout stacks on mobile
- [x] `animals-game.html` — Two-pane layout stacks on mobile
- [x] `numbers-game.html` — Two-pane layout stacks on mobile
- [x] `hindi-alphabets.html` — Two-pane layout stacks on mobile
- [x] `colors-game.html` — Nav overflow + padding fixed
- [x] `shapes-game.html` — Nav overflow + padding fixed
- [x] `birds.html` — Already had the fix (reference implementation)
- [x] All classic games — Navbar compact on small screens

---

## 11. Polish Audit — 15 findings across consistency, accessibility, UX, SEO

**Severity:** Mixed (4 High, 6 Medium, 5 Low) | **Status:** Done

| ID | Finding | Severity | Status |
|---|---|---|---|
| H1 | Navbar labels inconsistent (emojis in classic, plain in card-machine) | High | ✅ Removed emojis from 7 classic game navbars |
| H2 | No theme-color meta on any game page | High | ✅ Added to all 12 games |
| H3 | Home page has no dark mode | High | ✅ Added prefers-color-scheme:dark styles |
| H4 | Incomplete Twitter Card tags (no description/image on games) | High | ✅ Added twitter:description, twitter:image, og:url to all 13 pages |
| M1 | No manifest.json shortcuts for quick game access | Medium | ✅ Added 4 shortcuts |
| M2 | No 404.html for GitHub Pages | Medium | ✅ Created 404.html |
| M3 | No :focus-visible styles (keyboard accessibility) | Medium | ✅ Added to all pages + common-cards.css |
| M4 | No ARIA roles on modals (role="dialog", aria-modal) | Medium | ✅ Added to all 12 modal overlays |
| M5 | Event listeners on modals not cleaned up on close | Medium | N/A — global listener checks visibility, doesn't stack |
| M6 | Redundant Home back-link in card-machine games (navbar already has Home) | Medium | ✅ Removed back-link + dead CSS from 4 games |
| L1 | console.log left in index.html | Low | ✅ Removed 4 console.log calls |
| L2 | Home page animation delays only cover 8 of 12 cards | Low | N/A — already had all 12 |
| L3 | Build-info div outside .container on index.html | Low | ✅ Moved inside .container |
| L4 | SVG icons use fixed sizes in manifest (should be "any" for SVG) | Low | ✅ Simplified to 2 entries with sizes="any" |
| L5 | Woodcutter story has no progress persistence | Low | ✅ Added localStorage for quiz attempts, best score, last played |

---

## 12. New Game Ideas (for 3-year-olds)

| # | Game | Architecture | Status |
|---|---|---|---|
| 1 | Body Parts | Classic Two-Pane | ✅ Done |
| 2 | Emotions / Feelings | Card Machine | Planned |
| 3 | Opposites | Card Machine | Planned |
| 4 | Musical Instruments | Card Machine | Planned |
| 5 | Daily Routines | Story Mode | Planned |
| 6 | Rhyming Words | Card Machine | Planned |
