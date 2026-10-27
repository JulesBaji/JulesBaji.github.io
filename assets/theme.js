/* Theme: dark by default, light on demand (remembered in localStorage). */
(function () {
  var root = document.documentElement;
  document.querySelectorAll('button.theme').forEach(function (b) {
    b.addEventListener('click', function () {
      var light = root.dataset.theme !== 'light';
      if (light) root.dataset.theme = 'light'; else delete root.dataset.theme;
      try { localStorage.setItem('theme', light ? 'light' : 'dark'); } catch (e) {}
      document.dispatchEvent(new Event('themechange'));
    });
  });
})();
