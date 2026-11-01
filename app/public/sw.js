// Service worker do MenteMat: cache do essencial da aplicação (shell) para uso offline.
// Os dados (aulas guardadas, fila de tentativas) ficam no armazenamento local da app, não aqui.
const CACHE = 'mentemat-shell-v1';
const SHELL = ['/', '/index.html', '/icon.svg', '/manifest.webmanifest'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.hostname.endsWith('supabase.co')) return; // nunca guardar dados da API em cache

  // Navegação: rede primeiro, shell em cache se estiver offline
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).catch(() => caches.match('/index.html')));
    return;
  }
  // Ficheiros estáticos: cache primeiro, atualiza em segundo plano
  e.respondWith(
    caches.match(req).then((hit) => {
      const net = fetch(req).then((res) => {
        if (res.ok && (url.origin === location.origin || url.hostname.includes('fonts') || url.hostname.includes('gstatic'))) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => hit);
      return hit || net;
    }),
  );
});
