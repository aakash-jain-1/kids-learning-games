const CACHE_NAME = 'kids-learning-games-v22';
const urlsToCache = [
  './',
  'index.html',
  'offline.html',
  'games/alphabet-game.html',
  'games/numbers-game.html',
  'games/colors-game.html',
  'games/shapes-game.html',
  'games/animals-game.html',
  'games/birds.html',
  'games/hindi-alphabets.html',
  'games/flashcards-game.html',
  'games/solar-system-game.html',
  'games/dinosaurs-game.html',
  'games/weather-game.html',
  'games/woodcutter-story.html',
  'games/common-cards.css',
  'games/common-cards.js',
  'manifest.json',
  'assets/icon-192.svg',
  'assets/icon-512.svg'
];

// Install — pre-cache shell assets, skip waiting to activate immediately
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
  );
  self.skipWaiting();
});

// Activate — purge old caches and take control of all clients
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n)))
    )
  );
  self.clients.claim();
});

// Fetch — network-first for navigations, stale-while-revalidate for assets
self.addEventListener('fetch', (event) => {
  const { request } = event;

  if (request.method !== 'GET') return;

  if (request.mode === 'navigate') {
    // HTML pages: try network first, fall back to cache, then offline page
    event.respondWith(
      fetch(request)
        .then((response) => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
          return response;
        })
        .catch(() => caches.match(request).then((r) => r || caches.match('offline.html')))
    );
    return;
  }

  // Sub-resources (CSS, JS, images, SVG): serve cache, revalidate in background
  event.respondWith(
    caches.open(CACHE_NAME).then((cache) =>
      cache.match(request).then((cached) => {
        const networkFetch = fetch(request).then((response) => {
          if (response && response.status === 200) {
            cache.put(request, response.clone());
          }
          return response;
        });
        return cached || networkFetch;
      })
    )
  );
});
