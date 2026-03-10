# 🎮 Kids Learning Games - PWA Edition

A Progressive Web App featuring 8 educational games for children to learn Alphabets, Numbers, Colors, Shapes, Animals, Birds, Hindi Alphabets, and a Story mode.

**🌐 Live:** https://aakash-jain-1.github.io/kids-learning-games/

## 📱 Features

- **Installable PWA** — Can be installed on mobile, tablet, and desktop
- **Offline Support** — Works without internet after first load
- **Fluid Responsive Design** — Uses `clamp()`, `min()`, `dvh`, and `aspect-ratio` to scale naturally on any screen size or orientation — no per-device breakpoints
- **8 Educational Games** — Comprehensive learning platform
- **Quiz Mode** — 10-question quizzes with scoring for each game
- **Settings Panel** — Dark mode, font size adjustment, sound toggle, auto-speak
- **Achievement System** — 35+ unlockable badges across all games
- **Statistics Dashboard** — Track progress, quizzes completed, accuracy, high scores
- **Sound Effects** — Audio feedback and text-to-speech pronunciation
- **Touch Optimizations** — Enhanced mobile experience with no double-tap zoom
- **Flash Cards** — Dedicated flash card machine game with category filtering
- **Story Mode** — The Woodcutter story with interactive animations

## 🎯 Games Included

1. **🔤 Alphabets** — Learn A-Z with words and images (26 letters)
2. **🔢 Numbers** — Count 1-10 with interactive objects
3. **🌈 Colors** — Discover 12 colors with shapes
4. **⬛ Shapes** — Explore 14 different shapes
5. **🐾 Animals** — Meet 37 animals A-Z with images and facts
6. **🦜 Birds** — Learn 15 bird species with facts
7. **🔤 Hindi Alphabets** — Master 48 Hindi letters (vowels + consonants)
8. **🃏 Flash Cards** — Review animals, colors, numbers, and more in card format
9. **📖 Woodcutter Story** — Read-along story mode

## 🔧 Technical Details

### File Structure

```
├── index.html              # Main menu / home page
├── manifest.json           # PWA manifest
├── service-worker.js       # Offline caching (auto-updates on version bump)
├── README.md
├── games/
│   ├── alphabet-game.html
│   ├── numbers-game.html
│   ├── colors-game.html
│   ├── shapes-game.html
│   ├── animals-game.html
│   ├── birds.html
│   ├── hindi-alphabets.html
│   ├── flashcards-game.html
│   └── woodcutter-story.html
└── dev/
    ├── SETUP.html          # Dev/setup utilities
    └── ACTION_ITEMS.md
```

### Technologies Used

- HTML5, CSS3, Vanilla JavaScript (no frameworks or build tools)
- Web Audio API (sound effects)
- Web Speech API (text-to-speech)
- Service Workers (offline caching, auto cache-bust on version bump)
- Web App Manifest (PWA install prompt)
- LocalStorage (progress, achievements, settings)
- Canvas API (confetti)
- Fluid CSS: `clamp()`, `min()`, `100dvh`, `aspect-ratio` for device-agnostic layout

### Responsive Design Approach

All layout sizing uses fluid CSS values instead of device-specific `@media (max-height)` breakpoints:
- **Font sizes**: `clamp(min, vmin-value, max)` — naturally scales with the smaller viewport dimension
- **Image/card heights**: `min(fixed-max, viewport-fraction)` — caps at a max but shrinks proportionally
- **Cards**: `aspect-ratio` instead of fixed width + height — cards maintain proportions automatically
- **Overflow**: `overflow-y: auto` on all panes — content is never silently clipped

### Updating the App

1. Make changes to HTML/JS/CSS files
2. Increment the version in `service-worker.js` (e.g., `kids-learning-games-v10`)
3. Commit and push — active users auto-reload when the new SW activates

## 📲 Installing the PWA

### Android (Chrome/Edge)
1. Open the live URL in Chrome
2. Tap **"📲 Install App"** or menu → "Add to Home screen"

### iOS (Safari)
1. Open the live URL in Safari
2. Tap Share → **"Add to Home Screen"**

### Desktop (Chrome/Edge)
1. Click the install icon in the address bar or the **"📲 Install App"** button

## 🖼️ App Icons

To generate PWA icons:
1. Open `dev/SETUP.html` in your browser
2. Download `icon-192.png` and `icon-512.png`
3. Place both files in the root folder (same level as `index.html`)

## 🧪 Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome / Edge (v90+) | ✅ Full PWA |
| Firefox (v88+) | ✅ Full features |
| Safari (v14+) | ✅ Add to Home Screen |
| Mobile Chrome (Android) | ✅ Full PWA |
| Mobile Safari (iOS) | ✅ Full features |

## ⚡ Performance

- Loads instantly after first visit (service worker cache)
- No external dependencies — all assets self-contained
- Background animations removed for smooth performance on low-end devices
- Lazy image loading via FluentUI Emoji CDN

## 📄 License

Free to use for educational purposes.

---

Created with ❤️ for kids to learn and have fun!
