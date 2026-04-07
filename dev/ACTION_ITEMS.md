# Kids Learning Games — Action Items

> Last updated: 2026-04-07

---

## Issue Tracker

### Status Legend
- [ ] Open
- [x] Done

---

## 1. Home Page — Missing game cards

**Severity:** High | **Effort:** Small

`index.html` only links to 9 of the 12 games. Three games exist in `games/` but have no card on the home page — users can't discover them.

**Missing from home page:**
- `dinosaurs-game.html`
- `weather-game.html`
- `woodcutter-story.html`

**Fix:** Add `<a>` cards for each inside the `.games-grid` div, following the existing card pattern.

- [x] Add Dinosaurs card to `index.html`
- [x] Add Weather card to `index.html`
- [x] Add Woodcutter Story card to `index.html`

---

## 2. Cross-game navigation — Card-machine games have no navbar

**Severity:** High | **Effort:** Medium

The 4 "card-machine" games (`flashcards`, `solar-system`, `dinosaurs`, `weather`) only have Prev/Next card buttons and a "Home" back-link. There is no cross-game navigation bar — once inside, you can't jump to another game without going back to the home page.

`woodcutter-story.html` only links to Home and Alphabets.

**Fix:** Add a consistent `.navigation` bar (matching the classic games) to all 5 files.

- [x] Add navbar to `flashcards-game.html`
- [x] Add navbar to `solar-system-game.html`
- [x] Add navbar to `dinosaurs-game.html`
- [x] Add navbar to `weather-game.html`
- [x] Add full navbar to `woodcutter-story.html`

---

## 3. Navigation — Flashcards and Woodcutter not linked from any game

**Severity:** High | **Effort:** Small

No game's navigation bar includes links to Flashcards or Woodcutter Story. These two games are completely orphaned from the cross-game navigation mesh.

**Fix:** Add `<a href="flashcards-game.html" class="nav-btn">Flashcards</a>` and `<a href="woodcutter-story.html" class="nav-btn">Story</a>` to the `.navigation` div in all game files.

**Files to update:**
- [ ] `alphabet-game.html`
- [ ] `numbers-game.html`
- [ ] `colors-game.html`
- [ ] `shapes-game.html`
- [ ] `animals-game.html`
- [ ] `hindi-alphabets.html`
- [ ] `birds.html`
- [ ] `flashcards-game.html` (once it has a navbar)
- [ ] `solar-system-game.html` (once it has a navbar)
- [ ] `dinosaurs-game.html` (once it has a navbar)
- [ ] `weather-game.html` (once it has a navbar)
- [ ] `woodcutter-story.html` (once it has a full navbar)

---

## 4. Service Worker — `woodcutter-story.html` not cached

**Severity:** Medium | **Effort:** Tiny

`service-worker.js` lists all 11 other game files in `urlsToCache` but is missing `games/woodcutter-story.html`. The story won't work offline.

**Fix:** Add `'games/woodcutter-story.html'` to the `urlsToCache` array and bump the cache version.

- [ ] Add woodcutter to `service-worker.js`
- [ ] Bump `CACHE_NAME` version

---

## 5. Feature parity — Card-machine games missing quiz, achievements, stats, settings

**Severity:** Medium | **Effort:** Large

The 7 classic games all have: quiz mode, achievements (5 badges), stats dashboard, and settings panel (dark mode, font size, sound, auto-speak). The 4 card-machine games have none of these.

| Feature | Classic (7 games) | Card-machine (4 games) |
|---|---|---|
| Quiz mode | Yes | No |
| Achievements (5 badges) | Yes | No |
| Stats dashboard | Yes | No |
| Settings panel | Yes | No |
| Dark mode | Yes | No |
| Progress persistence (localStorage) | Yes | Partial (progress bar only) |

**Fix:** Add quiz, achievements, stats, and settings to each card-machine game. Can be done incrementally per game.

- [ ] Add features to `flashcards-game.html`
- [ ] Add features to `solar-system-game.html`
- [ ] Add features to `dinosaurs-game.html`
- [ ] Add features to `weather-game.html`

---

## 6. Home Page — Duplicate CSS rules

**Severity:** Low | **Effort:** Tiny

`index.html` lines 123-126 define `.game-card:nth-child(10)` and `:nth-child(11)` animation delays twice (duplicate rules).

- [x] Remove the duplicate CSS block

---

## 7. Dev docs — `GAME_REFERENCE.md` inventory table outdated

**Severity:** Low | **Effort:** Tiny

The "Existing Games Inventory" table in `dev/GAME_REFERENCE.md` only lists 8 games. Missing: `solar-system-game.html`, `dinosaurs-game.html`, `weather-game.html`, `woodcutter-story.html`.

- [ ] Update inventory table with all 12 games

---

## Priority Summary

| # | Issue | Severity | Effort | Items |
|---|---|---|---|---|
| 1 | Missing home page cards | High | Small | 3 cards |
| 2 | Card games missing navbar | High | Medium | 5 files |
| 3 | Flashcards + Story not in any navbar | High | Small | 12 files |
| 4 | Woodcutter not in service worker | Medium | Tiny | 1 file |
| 5 | Card games missing quiz/achievements/stats | Medium | Large | 4 files |
| 6 | ~~Duplicate CSS in index.html~~ | ~~Low~~ | ~~Tiny~~ | Done |
| 7 | GAME_REFERENCE.md outdated | Low | Tiny | 1 file |

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
