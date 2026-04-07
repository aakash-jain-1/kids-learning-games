const CACHE_NAME = 'kids-learning-games-v18';
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

// Install event - cache files
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
  self.skipWaiting();
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Cache hit - return response
        if (response) {
          return response;
        }
        
        // Clone the request
        const fetchRequest = event.request.clone();
        
        return fetch(fetchRequest).then((response) => {
          if (!response || response.status !== 200 || response.type !== 'basic') {
            return response;
          }
          const responseToCache = response.clone();
          caches.open(CACHE_NAME)
            .then((cache) => {
              cache.put(event.request, responseToCache);
            });
          return response;
        }).catch(() => {
          if (event.request.mode === 'navigate') {
            return caches.match('offline.html');
          }
        });
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});
