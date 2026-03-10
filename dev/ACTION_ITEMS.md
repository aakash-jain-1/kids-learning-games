# Mobile Rendering — Action Items

## Root Cause Summary
All games except `flashcards-game.html` use a **two-column desktop layout**
(`.main-container` with `display:flex`, `height:80vh`, `gap:40px`) that never
stacks to a single column on mobile. The top navbar also wraps into multiple rows
and overlaps content. Flashcards works because it was rebuilt with a mobile-first
flex layout from scratch.

---

## Action Items

### 1. `alphabet-game.html` — Two-pane layout does not stack on mobile
**Problem:** `.main-container` is `display:flex` with `height:80vh` and `gap:40px`.
No `@media` rule changes it to `flex-direction:column` on small screens.
Left pane (alphabet grid — repeat(6,1fr)) and right pane overflow side-by-side.  
**Fix:**
- Add `@media (max-width:768px)` rule: `.main-container { flex-direction:column; height:auto; gap:20px; }`
- Change `.alphabet-grid` from `repeat(6,1fr)` → `repeat(4,1fr)` on mobile
- Change `.alphabet-btn` font-size from `2.5em` → `1.6em` on mobile
- Reduce `.alphabet-btn` padding from `25px 0` → `14px 0` on mobile
- Reduce body `padding-top` from `100px` to `70px` on mobile so navbar doesn't overlap

---

### 2. `animals-game.html` — Two-pane layout does not stack on mobile
**Problem:** Same as above. `.main-container` uses `height:80vh` with two side-by-side panes.
Animals grid is `repeat(4,1fr)` — too wide for phone.  
**Fix:**
- Add `@media (max-width:768px)` rule: `.main-container { flex-direction:column; height:auto; gap:20px; }`
- Change `.animals-grid` from `repeat(4,1fr)` → `repeat(3,1fr)` on mobile
- Reduce body `padding-top` to `70px` on mobile

---

### 3. `numbers-game.html` — Two-pane layout does not stack on mobile
**Problem:** Same two-pane layout issue. Number display and objects grid overflow.  
**Fix:**
- Add `@media (max-width:768px)` rule: `.main-container { flex-direction:column; height:auto; gap:20px; }`
- Reduce body `padding-top` to `70px` on mobile

---

### 4. `hindi-alphabets.html` — Two-pane layout does not stack on mobile
**Problem:** Same two-pane layout issue. Hindi characters are small and the grid overflows.  
**Fix:**
- Add `@media (max-width:768px)` rule: `.main-container { flex-direction:column; height:auto; gap:20px; }`
- Change `.letter-grid` to `repeat(auto-fit, minmax(65px, 1fr))` on mobile
- Reduce body `padding-top` to `70px` on mobile

---

### 5. `colors-game.html` — Nav overflows, body has `padding-top:100px`
**Problem:** Navigation bar wraps to 2 rows at ~380px width, covering content.
Body `padding-top:100px` is hard-coded and not reduced on mobile.  
**Fix:**
- Reduce body `padding-top` to `70px` on screens ≤ 768px
- Add nav `.nav-btn` `font-size:0.85em; padding:8px 12px` on mobile to keep single row

---

### 6. `shapes-game.html` — Same nav + padding issue as colors
**Problem:** Same as #5 above.  
**Fix:**
- Reduce body `padding-top` to `70px` on screens ≤ 768px
- Shrink nav buttons on mobile

---

### 7. `birds.html` — Already has the two-pane column-stack fix ✅
**Status:** Has `@media (max-width:768px) { .main-container { flex-direction:column; height:auto; } }`
This is the pattern to replicate in items 1–4 above.

---

### 8. All games — Navbar too tall on small screens
**Problem:** The fixed navbar uses `padding:15px 20px` and `gap:10px`.
On phones ≤ 400px it wraps to 2–3 rows, taking 80–100px of height and
overlapping the game content underneath.  
**Fix (all files):**
```css
@media (max-width: 600px) {
  .navigation { padding: 8px 10px; gap: 6px; }
  .nav-btn { padding: 7px 10px; font-size: 0.78em; }
  body { padding-top: 72px; }
}
```

---

## Priority Order
| # | File | Severity | Fix Effort |
|---|------|----------|-----------|
| 1 | `alphabet-game.html` | High | Small |
| 2 | `animals-game.html` | High | Small |
| 3 | `numbers-game.html` | High | Small |
| 4 | `hindi-alphabets.html` | High | Small |
| 5 | All games — navbar | Medium | Small |
| 6 | `colors-game.html` | Medium | Small |
| 7 | `shapes-game.html` | Medium | Small |

---

## Reference: What flashcards does right
- Uses `height:100vh; overflow:hidden` with a flex `.layout` that is already a column stack on mobile
- Left pane and right pane are `width:50%` each with their own scroll — handled via `@media` with `flex-direction:column`
- No fixed pixel `padding-top` on body — navbar is part of the flow, not `position:fixed`
