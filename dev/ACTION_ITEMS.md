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

## 5. Feature parity — Card-machine games missing quiz, achievements, stats, settings

**Severity:** Medium | **Effort:** Large

The 7 classic games all have: quiz mode, achievements (5 badges), stats dashboard, and settings panel (dark mode, font size, sound, auto-speak). The 4 card-machine games have none of these.

| Feature | Classic (7 games) | Card-machine (4 games) | Woodcutter |
|---|---|---|---|
| Quiz mode | Yes | No | No |
| Achievements (5 badges) | Yes | No | No |
| Stats dashboard | Yes | No | No |
| Settings panel | Yes | No | No |
| Dark mode | Yes | No | No |
| Progress persistence (localStorage) | Yes | Partial (progress bar only) | No |

- [ ] Add features to `flashcards-game.html`
- [ ] Add features to `solar-system-game.html`
- [ ] Add features to `dinosaurs-game.html`
- [ ] Add features to `weather-game.html`

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
| 5 | Card games missing quiz/achievements/stats | Medium | Large | Open |
| 6 | ~~Duplicate CSS in index.html~~ | ~~Low~~ | ~~Tiny~~ | ✅ Done |
| 7 | ~~GAME_REFERENCE.md outdated~~ | ~~Low~~ | ~~Tiny~~ | ✅ Done |
| 8 | ~~Build info footer missing~~ | ~~Low~~ | ~~Tiny~~ | ✅ Done |
| 9 | ~~Meta descriptions missing~~ | ~~Low~~ | ~~Small~~ | ✅ Done |

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
