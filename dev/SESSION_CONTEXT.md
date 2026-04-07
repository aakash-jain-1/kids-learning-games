# Kids Learning Games — Session Context

> Reference file for new chat sessions. Summarises all work done across previous sessions
> so that a new AI assistant can pick up where things left off.
>
> Last updated: 2026-04-07

---

## 1. Project Overview

**Repo:** `kids-learning-games` (GitHub Pages PWA)
**Live URL:** https://aakash-jain-1.github.io/kids-learning-games/
**Stack:** HTML5 + CSS3 + Vanilla JS — zero frameworks, zero build tools
**Total commits:** 28 (as of 2026-04-07)
**Service Worker cache version:** v19

A Progressive Web App with **12 educational games** for children, organised into three architectures:

| Architecture | Games | Key traits |
|---|---|---|
| Classic Two-Pane | Alphabets, Numbers, Colors, Shapes, Animals, Birds, Hindi | Left pane = item list/grid, right pane = detail card; quiz, achievements, stats, settings |
| Card Machine | Flashcards, Solar System, Dinosaurs, Weather | Swipeable card deck; quiz, achievements, stats, settings |
| Story Mode | Woodcutter Story | Animated narrative with comprehension quiz |

---

## 2. File Structure

```
├── index.html              # Home page / game launcher
├── manifest.json           # PWA manifest
├── service-worker.js       # Offline cache + network-first strategy (v19)
├── offline.html            # Offline fallback page
├── assets/
│   ├── icon-192.svg        # PWA icon 192×192
│   └── icon-512.svg        # PWA icon 512×512
├── games/
│   ├── alphabet-game.html
│   ├── numbers-game.html
│   ├── colors-game.html
│   ├── shapes-game.html
│   ├── animals-game.html
│   ├── birds.html
│   ├── hindi-alphabets.html
│   ├── flashcards-game.html
│   ├── solar-system-game.html
│   ├── dinosaurs-game.html
│   ├── weather-game.html
│   ├── woodcutter-story.html
│   ├── common-cards.css    # Shared styles for card-machine games
│   └── common-cards.js     # Shared JS utilities (reference file, not yet linked)
└── dev/
    ├── SETUP.html           # Dev setup guide
    ├── ACTION_ITEMS.md      # Issue tracker (all 11 issues resolved)
    ├── GAME_REFERENCE.md    # Template & conventions for adding new games
    ├── SESSION_CONTEXT.md   # This file
    ├── _gen_solar_css_planets.py
    └── _gen_games_v2.py
```

---

## 3. Work Completed (Chronological)

### Phase 1 — Environment Setup
- Configured dual Git identities (Amdocs GitLab + personal GitHub)
- Set up SSH keys, proxy config (`corkscrew`), `~/.ssh/config` host aliases

### Phase 2 — Bug Fixes & Missing Features (Issues 1–9)
All tracked in `dev/ACTION_ITEMS.md`.

| # | Issue | What was done |
|---|---|---|
| 1 | Missing home page cards | Added Dinosaurs, Weather, Woodcutter cards to `index.html` |
| 2 | Card-machine games had no navbar | Added full navigation bar to all 5 newer games |
| 3 | Flashcards & Story not linked from any game | Updated navbars in all 12 games |
| 4 | Woodcutter not in SW cache | Added to `urlsToCache`, bumped cache, added SW registration |
| 5 | Card-machine games missing quiz/achievements/stats/settings | Implemented full feature parity (quiz, 5 badges, stats, settings with dark mode/font/sound/auto-speak) in 4 card-machine games |
| 6 | Duplicate CSS in index.html | Removed duplicate block |
| 7 | GAME_REFERENCE.md outdated | Updated inventory table with all 12 games |
| 8 | Build info footer missing from newer games | Added GitHub API build-info to 4 games |
| 9 | No meta descriptions on game pages | Added `<meta name="description">` to all 12 games |

### Phase 3 — Deep Enhancement Audit (Issue 10 — 22 findings)
Comprehensive audit across bugs, UX, performance, accessibility, SEO, and architecture.

| ID | Finding | Resolution |
|---|---|---|
| C1 | PWA icons missing | Created `assets/icon-192.svg` + `assets/icon-512.svg` |
| C2 | Quiz crash if <4 cards in deck | Bounded `wrongs` loop safely |
| H1 | No Escape / click-outside for modals | Added `keydown` + overlay click listeners (4 card-machine games) |
| H2 | Auto-speak fires on page load | Added `_pageReady` guard; speak only after user navigates |
| H3 | Dark mode incomplete (card-machine) | Added styles for `.top-card`, `.card-name-big`, `.done-card`, `.fact-box`, `.bottom-bar` |
| H4 | No `prefers-reduced-motion` | Added media query block to all 13 HTML pages |
| H5 | Hindi lang attribute | Already correct (`lang="hi"`) |
| M1 | SW cache-first staleness | ✅ Switched to network-first for HTML, stale-while-revalidate for assets (v19) |
| M2 | Outdated descriptions | Updated `index.html` + `manifest.json` |
| M3 | No Open Graph / Twitter meta tags | Added to all 13 pages with absolute `og:image` URLs |
| M4 | GitHub API fetched every page load | Direct fetch on each load (no cache — avoids stale SHA after deploy) |
| M5 | No `loading="lazy"` on images | Added to weather + flashcards (others use CSS art) |
| M6 | Code duplication across card-machine games | Extracted `common-cards.css` + `common-cards.js` |
| M7 | Woodcutter has no quiz | Added 6-question comprehension quiz |
| M8 | Tablet grid → single column too early | 2-col at ≤768px, 1-col at ≤480px |
| L1 | Navbar style inconsistency | Unified to white/gradient style across all games |
| L2 | No favicon | SVG favicon on all pages |
| L3 | `push.bat` leftover | Deleted |
| L4 | CSS class reuse on home cards | Unique classes for all 12 game cards |
| L5 | No offline fallback | Created `offline.html` + SW `.catch()` fallback |
| L6 | Confetti = 100 DOM divs | Canvas-based (80 particles, 1 element) |
| L7 | `new AudioContext()` per answer | Singleton `_getAudioCtx()` |

### Phase 4 — Secondary Audit & Cleanup
After Phase 3, a second pass found and fixed:

- Removed dead confetti CSS (`.cf`, `@keyframes cfFall`) from 4 card-machine games
- Fixed stale `.png` icon references in `README.md` and `dev/SETUP.html` → `.svg`
- Updated stale cache version example in `README.md` (v10 → v15)
- Added `<link rel="icon">` favicon to all 12 game pages
- Fixed `woodcutter-story.html` navbar overlap (`padding-top: 48px`)
- Changed `og:image` to absolute URLs in all 13 HTML files
- Removed stale `generate-icons.html` reference from `.gitignore`
- Updated `GAME_REFERENCE.md` CSS classes and `urlsToCache` reference
- Moved icons from root to `assets/` directory; updated all references

### Phase 5 — Polish Audit (Issue 11 — 15 findings)
A third pass focused on consistency, accessibility, SEO completeness, and UX polish:

- **H1**: Unified navbar labels — removed emojis from classic game nav links to match card-machine plain text style
- **H2**: Added `<meta name="theme-color">` to all 12 game pages (per-game colors)
- **H3**: Added OS-level dark mode to `index.html` via `@media(prefers-color-scheme:dark)`
- **H4**: Completed Twitter Card tags (`twitter:description`, `twitter:image`) and added `og:url` to all 13 pages
- **M1**: Added 4 PWA shortcuts to `manifest.json` (Alphabets, Numbers, Animals, Flash Cards)
- **M2**: Created `404.html` for GitHub Pages with matching app style
- **M3**: Added `:focus-visible` styles (gold outline) to all pages + `common-cards.css`
- **M4**: Added `role="dialog"` and `aria-modal="true"` to all 12 modal overlays (4 games × 3 modals)
- **M6**: Removed redundant `.back-link` Home button from 4 card-machine games (navbar already has Home)
- **L1**: Removed 4 `console.log` calls from `index.html`
- **L3**: Moved `#build-info` div inside `.container` on `index.html`
- **L4**: Simplified manifest icons to 2 entries with `sizes="any"` (SVG is scalable)
- **L5**: Added `localStorage` persistence for woodcutter story quiz (attempts, best score, last played)
- Bumped service worker cache to v16

### Phase 6 — Service Worker & Build-Info Overhaul
- **Removed `localStorage` caching** for build-info commit SHA — was causing stale footer after deploys
- **Switched service worker from cache-first to network-first** for HTML pages (navigations always hit network; cache is offline fallback only)
- **Sub-resources (CSS/JS/images)** use stale-while-revalidate (serve cached, update in background)
- Removed `SW_UPDATED` messaging (no longer needed without localStorage cache)
- Bumped service worker cache to v19

---

## 4. Architecture & Design Decisions

### Game architectures
- **Classic Two-Pane**: Left sidebar with item list/grid, right pane with detail card. All 7 share the same structural pattern but each has unique theming and data.
- **Card Machine**: Swipeable card deck with top-card/bottom-bar layout. Shared styles in `common-cards.css`. Each game has its own inline JS data and rendering logic.
- **Story Mode**: Linear narrative with scene progression, animated illustrations, and a comprehension quiz at the end.

### Shared code (`common-cards.css` / `common-cards.js`)
- `common-cards.css` is **linked** from all 4 card-machine games and contains shared modal, quiz, achievement, stats, and settings styles.
- `common-cards.js` is a **reference file only** — it contains extracted utility functions (`_getAudioCtx`, `lsGet`, `lsSet`, `checkAchievementsBase`, `showAchToast`, `playCorrectSound`, `launchConfettiCanvas`, `initModalDismiss`, `initBuildInfo`, `applySettingsBase`) but is **not yet `<script src>`-linked** from any game. The inline JS in each game uses differently-named versions of these functions, so linking both would add dead code without breaking anything. A future refactor could replace inline code with imports from this file.

### Service Worker strategy
- **HTML pages (navigations): network-first** — always fetches from network; falls back to cache if offline, then `offline.html`.
- **Sub-resources (CSS/JS/images): stale-while-revalidate** — serves cached version instantly, fetches fresh copy in background.
- Cache version bump (`CACHE_NAME`) triggers old cache deletion on activate.
- `skipWaiting()` + `clients.claim()` ensure new SW takes effect immediately.

### Build info footer
- All pages fetch the latest commit from GitHub API (`/repos/.../commits/main`) on every page load.
- No localStorage caching — ensures the footer always shows the actual latest deployed commit.

### Data & images
- Classic games: Iconify Noto SVG CDN (`api.iconify.design/noto/...`)
- Card-machine games: Mix of CSS art (solar system, dinosaurs) and CDN images (weather, flashcards)
- Fallback: Inline SVG with emoji for broken images

---

## 5. Remaining / Deferred Items

| Item | Priority | Notes |
|---|---|---|
| `common-cards.js` full integration | Low | Replace inline JS in card-machine games with `<script src="common-cards.js">` + thin per-game config. Requires renaming functions to match or updating call sites. |
| Woodcutter: achievements/stats/settings | Low | Story mode has a comprehension quiz but no badge/stats/settings system |
| Automated testing | Low | No test suite exists; consider Playwright for PWA testing |

---

## 6. Key Files to Know

| File | Purpose |
|---|---|
| `service-worker.js` | Network-first for HTML, stale-while-revalidate for assets; bump `CACHE_NAME` after changes |
| `manifest.json` | PWA metadata, icons, shortcuts |
| `index.html` | Home page with game grid; has its own build-info, OG tags, PWA registration |
| `games/common-cards.css` | Shared styles for card-machine modals, quizzes, achievements, settings |
| `dev/ACTION_ITEMS.md` | Full issue tracker with 10 resolved issues |
| `dev/GAME_REFERENCE.md` | Step-by-step guide + full HTML template for adding new games |

---

## 7. Git Configuration Notes

The workspace parent (`Github_AJ/`) uses a **local** `.gitconfig` for the personal GitHub account:
- `user.name` / `user.email` are set per-repo (not global)
- SSH key: `~/.ssh/id_ed25519_github`
- SSH config host alias: `github.com-personal` or similar
- Proxy: `corkscrew` via `ProxyCommand` when behind corporate network

The Amdocs GitLab account uses the **global** git config with HTTP/HTTPS proxy settings.

---

## 8. Useful Commands

```bash
# Serve locally (Python)
cd kids-learning-games && python3 -m http.server 8000

# Check what's cached in SW
# Open DevTools → Application → Cache Storage → kids-learning-games-v19

# Bump cache after changes
# Edit CACHE_NAME in service-worker.js (e.g., v19 → v20)
```
