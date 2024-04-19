// static/js/service-worker.js
self.addEventListener('push', event => {
    const data = event.data.json();
  
    const options = {
      body: data.body,
      icon: '/path/to/icon.png',
      vibrate: [100, 50, 100],
    };
  
    event.waitUntil(
      self.registration.showNotification(data.title, options)
    );
  });
  