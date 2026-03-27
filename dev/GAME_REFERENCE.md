# Kids Learning Games — New Game Reference Guide

Use this file as the authoritative reference whenever a new game is added to the project.
Copy the patterns below and customise the theme-specific values.

---

## 1. File & Folder Conventions

| What | Pattern | Example |
|------|---------|---------|
| Game file | `games/<topic>-game.html` | `games/solar-system-game.html` |
| File name words | lowercase, hyphen-separated | `hindi-alphabets.html` |
| Data images | Iconify Noto SVG via CDN | `https://api.iconify.design/noto/<icon>.svg?width=96&height=96` |
| Fallback image | Inline SVG with relevant emoji | see §6 |

---

## 2. Existing Games Inventory

| File | Title | Nav Label | Theme Gradient | Card Class | Card Emoji |
|------|-------|-----------|----------------|------------|------------|
| `alphabet-game.html` | Alphabets Learning Game | Alphabets | `#667eea → #764ba2` | `alphabets` | 🔤 |
| `numbers-game.html` | Numbers Learning Game | Numbers | `#56ab2f → #a8e6cf → #88d8a3` | `numbers` | 🔢 |
| `colors-game.html` | Colors Learning Game | Colors | `#ff9a9e → #fecfef` | `colors` | 🌈 |
| `shapes-game.html` | Shapes Learning Game | Shapes | `#f093fb → #f5576c` | `shapes` | ⬛ |
| `animals-game.html` | Animals Learning Game | Animals | `#43cea2 → #185a9d` | `animals` | 🐾 |
| `hindi-alphabets.html` | Hindi Alphabets | Hindi | `#ff9933 → #138808` | `alphabets` | 🇮🇳 |
| `birds.html` | Birds | Birds | `#00c6ff → #0072ff` | `animals` | 🦜 |
| `flashcards-game.html` | Flash Cards | Flashcards | (multi) | *(inline style)* | 🃏 |

When adding a new game, pick a **unique gradient** not already used above.

---

## 3. Step-by-Step Checklist for a New Game

1. [ ] Create `games/<name>-game.html` using the HTML template in §4.
2. [ ] Add all topic items to the JS data object (§6).
3. [ ] Set `GAME_KEY` (used for `localStorage`) — must be unique, e.g. `solar_system`.
4. [ ] Add a nav link inside the `.navigation` bar of the new file **and** in every existing game file.
5. [ ] Add an `<a>` card to `index.html` `.games-grid` (§7).
6. [ ] Update `service-worker.js` — add the new HTML file to the `CACHE_ASSETS` array.
7. [ ] Update `manifest.json` `shortcuts` array if desired.

---

## 4. Full HTML File Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TOPIC Learning Game</title>
  <style>
    /* ── Reset & touch ──────────────────────────────── */
    * {
      -webkit-tap-highlight-color: transparent;
      -webkit-touch-callout: none;
      -webkit-user-select: none;
      user-select: none;
      touch-action: manipulation;
    }

    /* ── Body / theme ───────────────────────────────── */
    body {
      font-family: 'Comic Sans MS', cursive, Arial, sans-serif;
      background: linear-gradient(135deg, THEME_COLOR_1 0%, THEME_COLOR_2 100%);
      text-align: center;
      margin: 0;
      padding: 100px 0 0 0;
      min-height: 100vh;
      position: relative;
      overflow-x: hidden;
      transition: all 0.3s ease;
    }
    body.dark-mode { background: linear-gradient(135deg, #0a3d62 0%, #1e272e 100%); }
    body.font-small  { font-size: 14px; }
    body.font-medium { font-size: 16px; }
    body.font-large  { font-size: 18px; }

    /* ── Particle canvas ────────────────────────────── */
    #particleCanvas {
      position: fixed; top: 0; left: 0;
      width: 100%; height: 100%;
      pointer-events: none; z-index: 0; opacity: 0.6;
    }

    /* ── Toggle switch (dark-mode / sound / auto-speak) */
    .switch input:checked + span              { background-color: #4caf50; }
    .switch input:checked + span:before      { transform: translateX(26px); }
    .switch span:before {
      position: absolute; content: "";
      height: 26px; width: 26px; left: 4px; bottom: 4px;
      background-color: white; transition: 0.4s; border-radius: 50%;
    }

    /* ── Standard keyframe animations ──────────────── */
    @keyframes fadeIn     { from{opacity:0} to{opacity:1} }
    @keyframes fadeInUp   { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
    @keyframes fadeInDown { from{opacity:0;transform:translateY(-20px)} to{opacity:1;transform:translateY(0)} }
    @keyframes slideUp    { from{opacity:0;transform:translateY(50px) scale(0.9)} to{opacity:1;transform:translateY(0) scale(1)} }
    @keyframes pulse-glow {
      0%,100%{ box-shadow:0 0 20px rgba(255,215,0,.6),0 0 40px rgba(255,215,0,.4); }
      50%    { box-shadow:0 0 30px rgba(255,215,0,.8),0 0 60px rgba(255,215,0,.6); }
    }
    @keyframes sparkle {
      0%   { transform:translateY(0) rotate(0deg); }
      100% { transform:translateY(-100px) rotate(360deg); }
    }
    @keyframes bounce {
      0%,20%,50%,80%,100% { transform:translateY(0); }
      40% { transform:translateY(-10px); }
      60% { transform:translateY(-5px); }
    }
    @keyframes flip3d {
      0%  { transform:rotateY(0deg); }
      50% { transform:rotateY(90deg); }
      100%{ transform:rotateY(0deg); }
    }
    .ripple {
      position:absolute; border-radius:50%;
      background:rgba(255,255,255,.6); transform:scale(0);
      animation:ripple-animation .6s ease-out; pointer-events:none;
    }
    @keyframes ripple-animation { to{ transform:scale(4); opacity:0; } }

    /* ── Navigation bar ─────────────────────────────── */
    .navigation {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      background: rgba(0,0,0,.4); backdrop-filter: blur(10px);
      padding: 10px 15px;
      display: flex; justify-content: center; align-items: center;
      gap: 10px; flex-wrap: wrap;
    }
    .nav-btn {
      background: linear-gradient(135deg, THEME_COLOR_1 0%, THEME_COLOR_2 100%);
      border: none; border-radius: 8px; padding: 10px 20px;
      cursor: pointer; font-size: 1em; font-weight: 600; color: white;
      transition: all .3s ease; text-decoration: none;
      box-shadow: 0 2px 5px rgba(0,0,0,.2);
    }
    .nav-btn:hover { transform:translateY(-2px); box-shadow:0 4px 10px rgba(0,0,0,.3); }

    /* ── Control panel ──────────────────────────────── */
    .control-panel {
      display: flex; justify-content: center; align-items: center;
      gap: 15px; margin: 25px auto; padding: 15px;
      background: rgba(255,255,255,.15); backdrop-filter: blur(10px);
      border-radius: 20px; box-shadow: 0 8px 32px rgba(0,0,0,.15);
      border: 1px solid rgba(255,255,255,.3);
      max-width: 700px; position: relative; z-index: 10; flex-wrap: wrap;
    }
    .control-btn {
      background: linear-gradient(145deg, #ffffff, #f0f0f0);
      border: 3px solid THEME_COLOR_1; border-radius: 15px;
      padding: 12px 24px; font-size: 1.2em; font-weight: bold;
      color: THEME_COLOR_2; cursor: pointer; transition: all .3s ease;
      box-shadow: 0 4px 10px rgba(0,0,0,.2); min-width: 130px;
    }
    .control-btn:hover:not(:disabled) {
      background: linear-gradient(145deg, THEME_COLOR_1, THEME_COLOR_DARK);
      color: white; transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(0,0,0,.3);
    }
    .control-btn:active:not(:disabled) { transform:translateY(0); box-shadow:0 2px 5px rgba(0,0,0,.2); }
    .control-btn:disabled { opacity:.5; cursor:not-allowed; }
    .progress-counter {
      background:rgba(255,255,255,.9); border:2px solid THEME_COLOR_1;
      border-radius:12px; padding:10px 20px; font-size:1.3em;
      font-weight:bold; color:THEME_COLOR_2;
      box-shadow:0 4px 10px rgba(0,0,0,.15); min-width:150px;
    }

    /* ── Two-pane layout ────────────────────────────── */
    .main-container {
      display: flex; justify-content: center; align-items: flex-start;
      gap: 40px; margin: 40px auto; padding: 0 20px;
      max-width: 1100px; height: 80vh; position: relative; z-index: 1;
    }
    .left-pane {
      flex: 1; display: flex; flex-direction: column;
      align-items: center; justify-content: flex-start;
      background: rgba(255,255,255,.15); backdrop-filter: blur(10px);
      border-radius: 20px; padding: 20px;
      box-shadow: 0 8px 32px rgba(0,0,0,.15);
      border: 1px solid rgba(255,255,255,.3);
      max-height: 80vh; overflow-y: auto;
    }
    .right-pane {
      flex: 1; display: flex; flex-direction: column;
      align-items: center; justify-content: center; min-width: 350px;
      background: rgba(255,255,255,.2); backdrop-filter: blur(10px);
      border-radius: 20px; padding: 30px;
      box-shadow: 0 8px 32px rgba(0,0,0,.15);
      border: 1px solid rgba(255,255,255,.3);
      position: relative; overflow-y: auto;
    }

    /* ── Item grid buttons (left pane) ──────────────── */
    .items-grid {
      display: grid; grid-template-columns: repeat(4,1fr);
      gap: 15px; width: 100%; max-width: 500px; margin-top: 20px;
    }
    .item-btn {
      background: linear-gradient(145deg, #ffffff, #f0f0f0);
      border: 3px solid THEME_COLOR_1; border-radius: 15px;
      font-size: 1.3em; font-weight: bold; padding: 15px 8px;
      cursor: pointer; transition: all .3s ease; width: 100%;
      box-shadow: 0 6px 20px rgba(0,0,0,.2); color: THEME_COLOR_2;
      position: relative; overflow: hidden; min-height: 60px;
      display: flex; align-items: center; justify-content: center;
    }
    .item-btn.flipping { animation: flip3d .6s ease-in-out; }
    .item-btn:hover {
      background: linear-gradient(145deg, THEME_LIGHT, THEME_LIGHTER);
      transform: translateY(-5px) scale(1.05);
      box-shadow: 0 12px 30px rgba(0,0,0,.3); border-color: THEME_COLOR_DARK;
    }
    .item-btn:active { transform:translateY(0) scale(.95); }
    .item-btn.learned { background:linear-gradient(145deg,#c8e6c9,#a5d6a7); border-color:#2e7d32; }

    /* ── Right-pane display ─────────────────────────── */
    .item-name {
      font-size: clamp(1.8em, 4.5vmin, 3.5em); font-weight: bold;
      color: #fff; text-align: center; margin-bottom: 20px;
    }
    .item-image {
      width: 200px; height: 200px; border-radius: 20px;
      background: white; padding: 15px; object-fit: contain;
      box-shadow: 0 10px 30px rgba(0,0,0,.3);
      animation: fadeInScale .8s ease-out;
    }
    @keyframes fadeInScale {
      from { opacity:0; transform:scale(.5); }
      to   { opacity:1; transform:scale(1); }
    }
    .item-fact {
      font-size: 1.3em; color: rgba(255,255,255,.95);
      margin-top: 20px; line-height: 1.5; max-width: 350px; text-align: center;
    }

    /* ── H1 / title ─────────────────────────────────── */
    h1 {
      color: #fff; font-size: 3.5em; margin-top: 20px;
      text-shadow: 2px 2px 4px rgba(0,0,0,.3);
      position: relative; z-index: 1;
    }

    /* ── Confetti / celebration ──────────────────────── */
    .confetti {
      position: fixed; width: 10px; height: 10px;
      animation: confetti-fall 3s linear forwards; z-index: 9999;
    }
    @keyframes confetti-fall {
      0%   { transform:translateY(0) rotateZ(0deg); opacity:1; }
      100% { transform:translateY(100vh) rotateZ(720deg); opacity:0; }
    }

    /* ── Responsive ─────────────────────────────────── */
    @media (max-width: 768px) {
      .main-container { flex-direction: column !important; height: auto !important; gap: 20px !important; }
      .items-grid     { grid-template-columns: repeat(3,1fr) !important; }
      .right-pane     { min-width: unset !important; width: 100% !important; }
      .left-pane      { max-height: none !important; overflow-y: visible !important; }
    }
    @media (max-width: 600px) {
      body { padding-top: 52px !important; }
      .navigation { padding:6px 8px; flex-wrap:nowrap; overflow-x:auto; justify-content:flex-start; }
      .nav-btn    { padding:6px 10px; font-size:.76em; white-space:nowrap; flex-shrink:0; }
    }

    /* Performance: disable heavy background animations on all devices */
    body::before  { display: none; }
    #particleCanvas { display: none; }
    .right-pane::before { display: none; }
  </style>
</head>
<body>
  <canvas id="particleCanvas"></canvas>

  <!-- ── Navigation ──────────────────────────────────── -->
  <div class="navigation">
    <a href="../index.html"        class="nav-btn">Home</a>
    <a href="alphabet-game.html"   class="nav-btn">Alphabets</a>
    <a href="numbers-game.html"    class="nav-btn">Numbers</a>
    <a href="colors-game.html"     class="nav-btn">Colors</a>
    <a href="shapes-game.html"     class="nav-btn">Shapes</a>
    <a href="animals-game.html"    class="nav-btn">Animals</a>
    <a href="hindi-alphabets.html" class="nav-btn">Hindi</a>
    <a href="birds.html"           class="nav-btn">Birds</a>
    <!-- ADD NEW GAME LINK HERE, e.g.: -->
    <!-- <a href="solar-system-game.html" class="nav-btn">Solar System</a> -->
  </div>

  <h1>EMOJI Learn TOPIC EMOJI</h1>

  <!-- ── Control panel ───────────────────────────────── -->
  <div class="control-panel">
    <button id="randomBtn"   class="control-btn">🎲 Random</button>
    <button id="quizBtn"     class="control-btn" style="background:linear-gradient(145deg,#ff9800,#f57c00);border:3px solid #e65100;">🎯 Quiz</button>
    <button id="settingsBtn" class="control-btn" style="background:linear-gradient(145deg,#9c27b0,#7b1fa2);border:3px solid #6a1b9a;">⚙️ Settings</button>
    <button id="speakBtn"    class="control-btn" disabled>🔊 Speak</button>
    <button id="resetBtn"    class="control-btn">🔄 Reset</button>
    <button id="statsBtn"    style="background:linear-gradient(135deg,#2196f3,#1976d2);border:none;padding:12px 30px;border-radius:25px;font-size:1.2em;font-weight:bold;cursor:pointer;box-shadow:0 4px 15px rgba(33,150,243,.4);color:white;transition:all .3s;">📊 Stats</button>
    <div class="progress-counter" id="progressCounter" aria-live="polite">0 / TOTAL learned</div>
  </div>

  <!-- ── Quiz Modal ───────────────────────────────────── -->
  <div id="quizModal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.8);backdrop-filter:blur(10px);z-index:1000;justify-content:center;align-items:center;">
    <div style="background:linear-gradient(145deg,THEME_COLOR_1,THEME_COLOR_2);padding:30px;border-radius:25px;max-width:600px;width:90%;box-shadow:0 10px 50px rgba(0,0,0,.5);position:relative;">
      <button id="closeQuiz" style="position:absolute;top:15px;right:15px;background:rgba(255,255,255,.3);border:none;font-size:2em;cursor:pointer;border-radius:50%;width:45px;height:45px;line-height:45px;padding:0;color:white;">×</button>
      <h2 style="color:white;font-size:2.5em;margin-bottom:20px;">🎯 TOPIC Quiz</h2>
      <div style="margin:20px 0;">
        <img id="quizItemImage" src="" alt="" style="width:200px;height:200px;border-radius:20px;box-shadow:0 5px 20px rgba(0,0,0,.3);background:white;padding:20px;">
      </div>
      <p style="color:white;font-size:1.5em;margin:20px 0;">What is this?</p>
      <div id="quizOptions" style="display:grid;grid-template-columns:1fr 1fr;gap:15px;margin:20px 0;"></div>
      <p id="quizFeedback" style="font-size:1.3em;font-weight:bold;margin:15px 0;min-height:30px;"></p>
      <div id="quizScore" style="color:white;font-size:1.2em;margin:15px 0;font-weight:bold;"></div>
      <button id="nextQuizBtn" style="display:none;background:linear-gradient(145deg,THEME_COLOR_1,THEME_COLOR_2);border:3px solid white;padding:15px 40px;border-radius:25px;font-size:1.3em;font-weight:bold;color:white;cursor:pointer;margin-top:15px;">Next →</button>
    </div>
  </div>

  <!-- ── Stats Modal ──────────────────────────────────── -->
  <div id="statsModal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.8);backdrop-filter:blur(10px);z-index:1000;justify-content:center;align-items:center;overflow-y:auto;">
    <div style="background:linear-gradient(135deg,#2196f3,#1976d2);padding:30px;border-radius:20px;max-width:600px;width:90%;max-height:90vh;overflow-y:auto;margin:20px auto;">
      <h2 style="color:white;margin-bottom:20px;text-align:center;">📊 Your Statistics</h2>
      <div id="statsContent"></div>
      <h3 style="color:white;margin:30px 0 15px;text-align:center;">🏆 Achievements</h3>
      <div id="achievementsList" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px;margin-bottom:20px;"></div>
      <button id="closeStats" style="width:100%;padding:15px;background:white;color:#2196f3;border:none;border-radius:10px;font-size:18px;font-weight:bold;cursor:pointer;margin-top:20px;">Close</button>
    </div>
  </div>

  <!-- ── Settings Modal ──────────────────────────────── -->
  <div id="settingsModal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.8);backdrop-filter:blur(10px);z-index:1000;justify-content:center;align-items:center;">
    <div style="background:linear-gradient(135deg,THEME_COLOR_1,THEME_COLOR_2);border-radius:30px;padding:40px;max-width:500px;width:90%;box-shadow:0 20px 60px rgba(0,0,0,.5);position:relative;">
      <button id="closeSettings" style="position:absolute;top:15px;right:15px;background:rgba(255,255,255,.3);border:none;color:white;font-size:24px;width:40px;height:40px;border-radius:50%;cursor:pointer;">✕</button>
      <h2 style="color:white;margin-bottom:30px;text-align:center;">⚙️ Settings</h2>
      <div style="background:rgba(255,255,255,.1);padding:25px;border-radius:20px;">
        <!-- Dark mode -->
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:25px;padding-bottom:20px;border-bottom:2px solid rgba(255,255,255,.2);">
          <label style="color:white;font-size:1.2em;font-weight:bold;">🌙 Dark Mode</label>
          <label class="switch" style="position:relative;display:inline-block;width:60px;height:34px;">
            <input type="checkbox" id="darkModeToggle" style="opacity:0;width:0;height:0;">
            <span style="position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:#ccc;transition:.4s;border-radius:34px;"></span>
          </label>
        </div>
        <!-- Font size -->
        <div style="margin-bottom:25px;padding-bottom:20px;border-bottom:2px solid rgba(255,255,255,.2);">
          <label style="color:white;font-size:1.2em;font-weight:bold;display:block;margin-bottom:15px;">📏 Font Size</label>
          <div style="display:flex;gap:10px;justify-content:center;">
            <button class="fontSizeBtn" data-size="small"  style="background:rgba(255,255,255,.2);border:2px solid white;color:white;padding:10px 20px;border-radius:15px;cursor:pointer;font-size:.9em;">Small</button>
            <button class="fontSizeBtn active" data-size="medium" style="background:white;border:2px solid white;color:THEME_COLOR_1;padding:10px 20px;border-radius:15px;cursor:pointer;font-size:1em;font-weight:bold;">Medium</button>
            <button class="fontSizeBtn" data-size="large"  style="background:rgba(255,255,255,.2);border:2px solid white;color:white;padding:10px 20px;border-radius:15px;cursor:pointer;font-size:1.1em;">Large</button>
          </div>
        </div>
        <!-- Sound -->
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:25px;padding-bottom:20px;border-bottom:2px solid rgba(255,255,255,.2);">
          <label style="color:white;font-size:1.2em;font-weight:bold;">🔊 Sound Effects</label>
          <label class="switch" style="position:relative;display:inline-block;width:60px;height:34px;">
            <input type="checkbox" id="soundToggle" checked style="opacity:0;width:0;height:0;">
            <span style="position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:#4caf50;transition:.4s;border-radius:34px;"></span>
          </label>
        </div>
        <!-- Auto-speak -->
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <label style="color:white;font-size:1.2em;font-weight:bold;">🗣️ Auto-Speak</label>
          <label class="switch" style="position:relative;display:inline-block;width:60px;height:34px;">
            <input type="checkbox" id="autoSpeakToggle" style="opacity:0;width:0;height:0;">
            <span style="position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:#ccc;transition:.4s;border-radius:34px;"></span>
          </label>
        </div>
      </div>
      <button onclick="document.getElementById('settingsModal').style.display='none'" style="background:linear-gradient(145deg,#4caf50,#2e7d32);border:none;padding:15px 40px;border-radius:25px;font-size:1.2em;font-weight:bold;color:white;cursor:pointer;margin-top:25px;width:100%;">✓ Save Settings</button>
    </div>
  </div>

  <!-- ── Main two-pane layout ─────────────────────────── -->
  <div class="main-container">
    <div class="left-pane">
      <div class="items-grid" id="itemsGrid"></div>
    </div>
    <div class="right-pane">
      <div class="item-name"  id="itemName"></div>
      <div id="itemDisplayContainer" style="display:none;flex-direction:column;align-items:center;">
        <img class="item-image" id="itemImage" src="" alt="">
        <div class="item-fact" id="itemFact"></div>
      </div>
    </div>
  </div>

  <script>
    // ── 1. DATA ──────────────────────────────────────────
    // Replace with topic-specific items.
    // Each key = display name, value = { img, emoji, fact }
    const GAME_KEY = 'TOPIC_KEY'; // unique localStorage prefix
    const items = {
      'Item Name': {
        img:   'https://api.iconify.design/noto/ICON-NAME.svg?width=96&height=96',
        emoji: '🌍',
        fact:  'One interesting fact for kids!'
      },
      // … add all items …
    };
    const itemNames   = Object.keys(items);
    const TOTAL_ITEMS = itemNames.length;

    // ── 2. STATE ─────────────────────────────────────────
    let currentItem = '';
    let learnedItems = new Set(JSON.parse(localStorage.getItem(GAME_KEY + '_learned') || '[]'));
    let soundEnabled    = true;
    let autoSpeak       = false;

    // ── 3. DOM refs ──────────────────────────────────────
    const itemsGrid            = document.getElementById('itemsGrid');
    const itemName             = document.getElementById('itemName');
    const itemImage            = document.getElementById('itemImage');
    const itemDisplayContainer = document.getElementById('itemDisplayContainer');
    const itemFact             = document.getElementById('itemFact');
    const randomBtn            = document.getElementById('randomBtn');
    const speakBtn             = document.getElementById('speakBtn');
    const resetBtn             = document.getElementById('resetBtn');
    const progressCounter      = document.getElementById('progressCounter');

    // ── 4. TEXT-TO-SPEECH ────────────────────────────────
    function speak(text) {
      if (!soundEnabled) return;
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const utt = new SpeechSynthesisUtterance(text);
        utt.rate = 0.8; utt.pitch = 1.2; utt.volume = 1;
        window.speechSynthesis.speak(utt);
      }
    }

    // ── 5. DISPLAY ITEM ──────────────────────────────────
    function displayItem(name) {
      currentItem = name;
      const data  = items[name];

      itemName.textContent = name;
      itemName.style.animation = 'none';
      void itemName.offsetHeight;
      itemName.style.animation = 'bounce .6s ease-in-out';

      itemDisplayContainer.style.display = 'flex';

      itemImage.src = data.img;
      itemImage.alt = name;
      itemImage.style.animation = 'none';
      void itemImage.offsetHeight;
      itemImage.style.animation = 'fadeInScale .8s ease-out';
      itemImage.onerror = () => {
        itemImage.src = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96"><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-size="60">${data.emoji}</text></svg>`;
      };

      itemFact.textContent = data.fact;

      speakBtn.disabled = false;
      learnedItems.add(name);
      localStorage.setItem(GAME_KEY + '_learned', JSON.stringify([...learnedItems]));
      updateProgress();
      renderGrid();
      if (autoSpeak) speak(name);
    }

    // ── 6. PROGRESS COUNTER ──────────────────────────────
    function updateProgress() {
      progressCounter.textContent = learnedItems.size + ' / ' + TOTAL_ITEMS + ' learned';
    }

    // ── 7. RENDER GRID ───────────────────────────────────
    function renderGrid() {
      itemsGrid.innerHTML = '';
      itemNames.forEach(name => {
        const btn = document.createElement('button');
        btn.className = 'item-btn' + (learnedItems.has(name) ? ' learned' : '');
        btn.textContent = name;
        btn.setAttribute('aria-label', 'Learn about ' + name);
        btn.addEventListener('click', (e) => {
          createRipple(e);
          btn.classList.add('flipping');
          setTimeout(() => btn.classList.remove('flipping'), 600);
          displayItem(name);
        });
        itemsGrid.appendChild(btn);
      });
    }

    // ── 8. RIPPLE ────────────────────────────────────────
    function createRipple(e) {
      const btn  = e.currentTarget;
      const rect = btn.getBoundingClientRect();
      const rip  = document.createElement('span');
      const size = Math.max(rect.width, rect.height);
      rip.style.cssText = `width:${size}px;height:${size}px;left:${e.clientX-rect.left-size/2}px;top:${e.clientY-rect.top-size/2}px;`;
      rip.classList.add('ripple');
      btn.appendChild(rip);
      setTimeout(() => rip.remove(), 600);
    }

    // ── 9. RANDOM ────────────────────────────────────────
    randomBtn.addEventListener('click', () => {
      const idx = Math.floor(Math.random() * TOTAL_ITEMS);
      displayItem(itemNames[idx]);
    });

    // ── 10. SPEAK ────────────────────────────────────────
    speakBtn.addEventListener('click', () => { if (currentItem) speak(currentItem); });

    // ── 11. RESET ────────────────────────────────────────
    resetBtn.addEventListener('click', () => {
      if (confirm('Reset all progress for this game?')) {
        learnedItems.clear();
        localStorage.removeItem(GAME_KEY + '_learned');
        localStorage.removeItem(GAME_KEY + '_stats');
        localStorage.removeItem(GAME_KEY + '_achievements');
        currentItem = '';
        itemDisplayContainer.style.display = 'none';
        itemName.textContent = '';
        speakBtn.disabled = true;
        updateProgress();
        renderGrid();
      }
    });

    // ── 12. QUIZ ─────────────────────────────────────────
    const quizModal   = document.getElementById('quizModal');
    const closeQuiz   = document.getElementById('closeQuiz');
    const quizOptions = document.getElementById('quizOptions');
    const quizFeedback= document.getElementById('quizFeedback');
    const quizScore   = document.getElementById('quizScore');
    const nextQuizBtn = document.getElementById('nextQuizBtn');
    const quizImgEl   = document.getElementById('quizItemImage');
    const quizBtn     = document.getElementById('quizBtn');

    let quizState = { current: null, correct: 0, total: 0, totalQs: 10, idx: 0, answered: false };

    function startQuiz() {
      quizState = { current: null, correct: 0, total: 0, totalQs: Math.min(10, TOTAL_ITEMS), idx: 0, answered: false };
      quizModal.style.display = 'flex';
      loadQuizQuestion();
    }

    function loadQuizQuestion() {
      quizState.answered = false;
      quizFeedback.textContent = '';
      nextQuizBtn.style.display = 'none';
      quizScore.textContent = `Question ${quizState.idx + 1} / ${quizState.totalQs}  ·  Score: ${quizState.correct}`;

      const shuffled = [...itemNames].sort(() => Math.random() - .5);
      const answer   = shuffled[0];
      const choices  = shuffled.slice(0, 4).sort(() => Math.random() - .5);
      quizState.current = answer;

      quizImgEl.src = items[answer].img;
      quizImgEl.onerror = () => {
        quizImgEl.src = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96"><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-size="60">${items[answer].emoji}</text></svg>`;
      };

      quizOptions.innerHTML = '';
      choices.forEach(choice => {
        const opt = document.createElement('button');
        opt.textContent = choice;
        opt.style.cssText = 'padding:15px;font-size:1.2em;border-radius:15px;border:3px solid white;background:rgba(255,255,255,.2);color:white;cursor:pointer;transition:all .3s;font-weight:bold;';
        opt.addEventListener('click', () => checkAnswer(choice, opt));
        quizOptions.appendChild(opt);
      });
    }

    function checkAnswer(choice, btn) {
      if (quizState.answered) return;
      quizState.answered = true;
      quizState.total++;
      const correct = choice === quizState.current;
      if (correct) { quizState.correct++; quizFeedback.textContent = '✅ Correct!'; quizFeedback.style.color = '#4caf50'; }
      else         { quizFeedback.textContent = `❌ It's ${quizState.current}`; quizFeedback.style.color = '#f44336'; }
      btn.style.background = correct ? '#4caf50' : '#f44336';
      quizState.idx++;
      if (quizState.idx < quizState.totalQs) nextQuizBtn.style.display = 'inline-block';
      else showQuizResults();
    }

    function showQuizResults() {
      const pct = Math.round((quizState.correct / quizState.totalQs) * 100);
      quizOptions.innerHTML = '';
      quizImgEl.src = '';
      quizFeedback.textContent = '';
      quizScore.innerHTML = `<div style="font-size:2em;color:white;">🎉 Quiz Done!</div>
        <div style="font-size:1.5em;color:white;">Score: ${quizState.correct}/${quizState.totalQs} (${pct}%)</div>`;
      nextQuizBtn.style.display = 'none';
      const restartBtn = document.createElement('button');
      restartBtn.textContent = '🔄 Play Again';
      restartBtn.style.cssText = 'margin-top:15px;padding:12px 30px;font-size:1.2em;font-weight:bold;background:white;color:#333;border:none;border-radius:20px;cursor:pointer;';
      restartBtn.addEventListener('click', startQuiz);
      quizScore.appendChild(restartBtn);
    }

    quizBtn.addEventListener('click', startQuiz);
    closeQuiz.addEventListener('click', () => { quizModal.style.display = 'none'; });
    quizModal.addEventListener('click', (e) => { if (e.target === quizModal) quizModal.style.display = 'none'; });
    nextQuizBtn.addEventListener('click', loadQuizQuestion);

    // ── 13. SETTINGS ─────────────────────────────────────
    const settingsBtn   = document.getElementById('settingsBtn');
    const settingsModal = document.getElementById('settingsModal');
    const darkModeToggle= document.getElementById('darkModeToggle');
    const soundToggle   = document.getElementById('soundToggle');
    const autoSpeakTgl  = document.getElementById('autoSpeakToggle');

    settingsBtn.addEventListener('click', () => { settingsModal.style.display = 'flex'; });
    document.getElementById('closeSettings').addEventListener('click', () => { settingsModal.style.display = 'none'; });
    darkModeToggle.addEventListener('change', () => { document.body.classList.toggle('dark-mode', darkModeToggle.checked); });
    soundToggle.addEventListener('change', () => { soundEnabled = soundToggle.checked; });
    autoSpeakTgl.addEventListener('change', () => { autoSpeak = autoSpeakTgl.checked; });
    document.querySelectorAll('.fontSizeBtn').forEach(b => {
      b.addEventListener('click', () => {
        document.querySelectorAll('.fontSizeBtn').forEach(x => { x.style.background='rgba(255,255,255,.2)'; x.style.color='white'; x.style.fontWeight='normal'; });
        b.style.background='white'; b.style.color='THEME_COLOR_1'; b.style.fontWeight='bold';
        document.body.className = document.body.className.replace(/font-\w+/, '');
        document.body.classList.add('font-' + b.dataset.size);
      });
    });

    // ── 14. STATS & ACHIEVEMENTS ─────────────────────────
    const achievements = {
      first_item:  { name: '⭐ First Step',     desc: 'Learn your first item',  unlocked: false },
      halfway:     { name: '🌗 Halfway There',  desc: 'Learn half the items',   unlocked: false },
      all_learned: { name: '🏅 Expert!',        desc: 'Learn all items',        unlocked: false },
      perfect_quiz:{ name: '💯 Perfect Score',  desc: 'Get 100% in a quiz',     unlocked: false },
      quiz_master: { name: '🎓 Quiz Master',    desc: 'Complete 10 quizzes',    unlocked: false }
    };
    const savedAch = JSON.parse(localStorage.getItem(GAME_KEY + '_achievements') || '{}');
    Object.keys(savedAch).forEach(k => { if (achievements[k]) achievements[k].unlocked = savedAch[k]; });
    let stats = JSON.parse(localStorage.getItem(GAME_KEY + '_stats') || '{"totalQuizzes":0,"totalCorrect":0,"totalQuestions":0,"highScore":0}');

    function saveAchievements() {
      const out = {}; Object.keys(achievements).forEach(k => { out[k] = achievements[k].unlocked; });
      localStorage.setItem(GAME_KEY + '_achievements', JSON.stringify(out));
    }
    function saveStats() { localStorage.setItem(GAME_KEY + '_stats', JSON.stringify(stats)); }

    function showAchievementBadge(ach) {
      const el = document.createElement('div');
      el.style.cssText = 'position:fixed;top:20px;right:20px;background:linear-gradient(135deg,#ffd700,#ffed4e);color:#333;padding:20px 30px;border-radius:15px;box-shadow:0 10px 30px rgba(0,0,0,.3);z-index:10001;font-weight:bold;border:3px solid #ff8800;animation:slideIn .5s ease-out;';
      el.innerHTML = `<div style="font-size:1.5em;margin-bottom:5px;">${ach.name}</div><div style="font-size:.9em;opacity:.8;">${ach.desc}</div>`;
      document.body.appendChild(el);
      if (!document.getElementById('achAnimStyle')) {
        const s = document.createElement('style'); s.id='achAnimStyle';
        s.textContent = '@keyframes slideIn{from{transform:translateX(400px);opacity:0}to{transform:translateX(0);opacity:1}}';
        document.head.appendChild(s);
      }
      speak('Achievement unlocked: ' + ach.name);
      setTimeout(() => { el.style.transition='all .5s'; el.style.transform='translateX(400px)'; el.style.opacity='0'; setTimeout(() => el.remove(), 500); }, 3000);
    }

    function checkAchievements() {
      let changed = false;
      if (!achievements.first_item.unlocked  && learnedItems.size >= 1)              { achievements.first_item.unlocked = true;  showAchievementBadge(achievements.first_item);  changed = true; }
      if (!achievements.halfway.unlocked      && learnedItems.size >= TOTAL_ITEMS/2)  { achievements.halfway.unlocked = true;      showAchievementBadge(achievements.halfway);      changed = true; }
      if (!achievements.all_learned.unlocked  && learnedItems.size >= TOTAL_ITEMS)    { achievements.all_learned.unlocked = true;  showAchievementBadge(achievements.all_learned);  changed = true; }
      if (changed) saveAchievements();
    }

    // Stats modal
    const statsBtn2     = document.getElementById('statsBtn');
    const statsModal    = document.getElementById('statsModal');
    statsBtn2.addEventListener('click', () => {
      const s2 = JSON.parse(localStorage.getItem(GAME_KEY + '_stats') || '{"totalQuizzes":0,"totalCorrect":0,"totalQuestions":0,"highScore":0}');
      const acc = s2.totalQuestions > 0 ? ((s2.totalCorrect / s2.totalQuestions) * 100).toFixed(1) : 0;
      document.getElementById('statsContent').innerHTML = `
        <div style="display:grid;gap:15px;color:white;font-size:18px;">
          <div style="background:rgba(255,255,255,.1);padding:15px;border-radius:10px;"><div style="font-size:24px;margin-bottom:5px;">📝 ${s2.totalQuizzes}</div><div>Total Quizzes</div></div>
          <div style="background:rgba(255,255,255,.1);padding:15px;border-radius:10px;"><div style="font-size:24px;margin-bottom:5px;">❓ ${s2.totalQuestions}</div><div>Questions Answered</div></div>
          <div style="background:rgba(255,255,255,.1);padding:15px;border-radius:10px;"><div style="font-size:24px;margin-bottom:5px;">✅ ${acc}%</div><div>Overall Accuracy</div></div>
          <div style="background:rgba(255,255,255,.1);padding:15px;border-radius:10px;"><div style="font-size:24px;margin-bottom:5px;">🏆 ${s2.highScore}%</div><div>High Score</div></div>
        </div>`;
      const achList = document.getElementById('achievementsList');
      achList.innerHTML = '';
      Object.values(achievements).forEach(a => {
        const d = document.createElement('div');
        d.style.cssText = `background:${a.unlocked?'linear-gradient(135deg,#ffd700,#ffed4e)':'rgba(255,255,255,.1)'};padding:20px;border-radius:15px;text-align:center;opacity:${a.unlocked?1:.5};`;
        d.innerHTML = `<div style="font-size:48px;margin-bottom:10px;">${a.name.split(' ')[0]}</div><div style="font-weight:bold;font-size:16px;color:${a.unlocked?'#000':'#fff'};">${a.name.substring(a.name.indexOf(' ')+1)}</div><div style="font-size:14px;color:${a.unlocked?'#333':'#ccc'};">${a.desc}</div>${a.unlocked?'<div style="margin-top:10px;color:#000;font-weight:bold;">✓ UNLOCKED</div>':'<div style="margin-top:10px;color:#999;">🔒 Locked</div>'}`;
        achList.appendChild(d);
      });
      statsModal.style.display = 'flex';
    });
    document.getElementById('closeStats').addEventListener('click', () => { statsModal.style.display = 'none'; });
    statsModal.addEventListener('click', (e) => { if (e.target === statsModal) statsModal.style.display = 'none'; });

    // Hook quiz results into stats
    const _origShowQuizResults = showQuizResults;
    showQuizResults = function() {
      stats.totalQuizzes++; stats.totalCorrect += quizState.correct; stats.totalQuestions += quizState.totalQs;
      const pct = (quizState.correct / quizState.totalQs) * 100;
      if (pct > stats.highScore) stats.highScore = pct;
      if (pct === 100 && !achievements.perfect_quiz.unlocked) { achievements.perfect_quiz.unlocked = true; setTimeout(() => showAchievementBadge(achievements.perfect_quiz), 1000); saveAchievements(); }
      if (stats.totalQuizzes >= 10 && !achievements.quiz_master.unlocked) { achievements.quiz_master.unlocked = true; setTimeout(() => showAchievementBadge(achievements.quiz_master), 1500); saveAchievements(); }
      saveStats(); _origShowQuizResults();
    };

    // ── 15. INIT ─────────────────────────────────────────
    renderGrid();
    updateProgress();
    checkAchievements();
  </script>

  <!-- Service Worker registration -->
  <script>
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('../service-worker.js');
      let r = false;
      navigator.serviceWorker.addEventListener('controllerchange', () => { if (!r) { r = true; location.reload(); } });
    }
  </script>

  <div id="build-info" style="text-align:center;padding:10px 10px 20px;font-size:.7em;color:rgba(255,255,255,.35);"></div>
  <script>
    fetch('https://api.github.com/repos/aakash-jain-1/kids-learning-games/commits/main')
      .then(r => r.json())
      .then(d => { document.getElementById('build-info').textContent = 'Build: ' + d.sha.slice(0,7) + ' · ' + d.commit.committer.date.slice(0,10); })
      .catch(() => {});
  </script>
</body>
</html>
```

---

## 5. Placeholder Substitution Guide

| Placeholder | Replace with | Example |
|-------------|-------------|---------|
| `TOPIC` | Human-readable topic name | `Solar System` |
| `TOPIC_KEY` | lowercase_underscore key | `solar_system` |
| `EMOJI` | Relevant emoji | `🪐` |
| `TOTAL` | Total item count | `9` |
| `THEME_COLOR_1` | Primary gradient start hex | `#1a1a2e` |
| `THEME_COLOR_2` | Primary gradient end hex | `#e94560` |
| `THEME_COLOR_DARK` | Darker shade for hover | `#c72f47` |
| `THEME_LIGHT` | Light tint for item hover | `#fce4ec` |
| `THEME_LIGHTER` | Lighter tint | `#f8bbd0` |
| `ICON-NAME` | Iconify Noto icon slug | `ringed-planet` |

---

## 6. Image / Icon Sources

**Primary — Iconify Noto (preferred, no API key needed):**
```
https://api.iconify.design/noto/<icon-slug>.svg?width=96&height=96
```
Browse icons at: https://icon-sets.iconify.design/noto/

**Fallback (inline SVG with emoji):**
```js
itemImage.onerror = () => {
  itemImage.src = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96"><text x="50%" y="50%" text-anchor="middle" dy=".3em" font-size="60">EMOJI</text></svg>`;
};
```

---

## 7. Adding the Card to index.html

Add inside the `.games-grid` div in `index.html`:

```html
<a href="games/TOPIC-game.html" class="game-card CARD_CLASS" style="border-top:5px solid THEME_COLOR_1;">
  <div class="game-icon">EMOJI</div>
  <h2>TOPIC</h2>
  <p>Short one-line description for kids!</p>
</a>
```

**Existing `game-card` classes & their border colours:**

| Class | Border colour |
|-------|--------------|
| `alphabets` | `#667eea` |
| `numbers`   | `#56ab2f` |
| `colors`    | `#ff6b9d` |
| `shapes`    | `#f093fb` |
| `animals`   | `#43cea2` |

Use an inline `style="border-top:5px solid …"` for any new unique colour (see flashcards card for precedent).

Also update the animation-delay counter:
```css
.game-card:nth-child(N) { animation-delay: 0.Ns; }
```

---

## 8. service-worker.js — Add to Cache

Open `service-worker.js` and add the new file to the `CACHE_ASSETS` (or equivalent) array:

```js
'games/TOPIC-game.html',
```

---

## 9. localStorage Key Naming

All keys for a game must share a single prefix `GAME_KEY` to avoid collisions:

| Purpose | Key |
|---------|-----|
| Learned items | `GAME_KEY_learned` |
| Quiz stats | `GAME_KEY_stats` |
| Achievements | `GAME_KEY_achievements` |

---

## 10. Navigation — Update ALL Existing Games

When a new game is added, insert one `<a>` tag in the `.navigation` div of **every** existing game file:

```html
<a href="TOPIC-game.html" class="nav-btn">LABEL</a>
```

Files to update:
- `games/alphabet-game.html`
- `games/numbers-game.html`
- `games/colors-game.html`
- `games/shapes-game.html`
- `games/animals-game.html`
- `games/hindi-alphabets.html`
- `games/birds.html`
- `games/flashcards-game.html`
