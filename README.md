# 🎮 Kids Learning Games - PWA Edition

A Progressive Web App featuring 12 educational games for children — Alphabets, Numbers, Colors, Shapes, Animals, Birds, Hindi, Flashcards, Solar System, Dinosaurs, Weather, and an interactive Story.

**🌐 Live:** https://aakash-jain-1.github.io/kids-learning-games/

## 📱 Features

- **Installable PWA** — Can be installed on mobile, tablet, and desktop
- **Offline Support** — Works without internet after first load; offline fallback page
- **Fluid Responsive Design** — Uses `clamp()`, `min()`, `dvh`, and `aspect-ratio` to scale naturally on any screen size or orientation
- **12 Educational Games** — Comprehensive learning platform across two game types
- **Quiz Mode** — 10-question quizzes with scoring for each game + story comprehension quiz
- **Settings Panel** — Dark mode, font size adjustment, sound toggle, auto-speak
- **Achievement System** — 55+ unlockable badges across all games
- **Statistics Dashboard** — Track progress, quizzes completed, accuracy, high scores
- **Sound Effects** — Audio feedback and text-to-speech pronunciation
- **Accessibility** — `prefers-reduced-motion` support, proper `lang` attributes, keyboard-dismissible modals
- **Social Sharing** — Open Graph and Twitter Card meta tags on all pages
- **Performance** — Canvas-based confetti, reused AudioContext, cached API calls, lazy-loaded images
- **Touch Optimizations** — Enhanced mobile experience with no double-tap zoom

## 🎯 Games Included

### Classic Two-Pane Games
1. **🔤 Alphabets** — Learn A-Z with words and images (26 letters)
2. **🔢 Numbers** — Count 1-10 with interactive objects
3. **🌈 Colors** — Discover 12 colors with shapes
4. **⬛ Shapes** — Explore 14 different shapes
5. **🐾 Animals** — Meet 37 animals A-Z with images and facts
6. **🦜 Birds** — Learn 15 bird species with facts
7. **🇮🇳 Hindi Alphabets** — Master 48 Hindi letters (vowels + consonants)

### Card-Machine Games
8. **🃏 Flash Cards** — Numbers, colors, shapes, fruits, and animals with category filtering
9. **🪐 Solar System** — Explore 11 planets and space objects with CSS art
10. **🦕 Dinosaurs** — Discover 20 dinosaur species with fun facts
11. **🌦️ Weather** — Learn 20 weather types and seasons

### Story Mode
12. **📖 Woodcutter Story** — Animated story with comprehension quiz

## 🔧 Technical Details

### File Structure

```
├── index.html              # Main menu / home page
├── manifest.json           # PWA manifest
├── service-worker.js       # Offline caching (auto-updates on version bump)
├── offline.html            # Offline fallback page
├── README.md
├── assets/
│   ├── icon-192.svg        # PWA icon (192x192)
│   └── icon-512.svg        # PWA icon (512x512)
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
│   └── common-cards.js     # Shared JS utilities for card-machine games
└── dev/
    ├── SETUP.html              # Dev/setup utilities
    ├── _gen_flashcards.py      # Flashcard data generation script
    ├── ACTION_ITEMS.md         # Known issues & fix tracker
    └── GAME_REFERENCE.md       # Template & conventions for adding games
```

### Technologies Used

- HTML5, CSS3, Vanilla JavaScript (no frameworks or build tools)
- Web Audio API (sound effects)
- Web Speech API (text-to-speech)
- Service Workers (offline caching, auto cache-bust on version bump)
- Web App Manifest (PWA install prompt)
- LocalStorage (progress, achievements, settings)
- Canvas API (confetti animations)
- Fluid CSS: `clamp()`, `min()`, `100dvh`, `aspect-ratio` for device-agnostic layout
- Open Graph / Twitter Card meta tags for social sharing

### Responsive Design Approach

All layout sizing uses fluid CSS values instead of device-specific `@media (max-height)` breakpoints:
- **Font sizes**: `clamp(min, vmin-value, max)` — naturally scales with the smaller viewport dimension
- **Image/card heights**: `min(fixed-max, viewport-fraction)` — caps at a max but shrinks proportionally
- **Cards**: `aspect-ratio` instead of fixed width + height — cards maintain proportions automatically
- **Overflow**: `overflow-y: auto` on all panes — content is never silently clipped

### Updating the App

1. Make changes to HTML/JS/CSS files
2. Increment the version in `service-worker.js` (e.g., `kids-learning-games-v15`)
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

PWA icons (`assets/icon-192.svg` and `assets/icon-512.svg`) are included in the repository. No generation step is needed.

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
