/* Horizontal project list: arrow buttons, scrolled by one card. */
(function () {
  document.querySelectorAll('section').forEach(function (sec) {
    var sc = sec.querySelector('.scroller'); if (!sc) return;
    var prev = sec.querySelector('.sb.prev'), next = sec.querySelector('.sb.next');
    function stepPx() { var c = sc.querySelector('.proj'); return c ? c.getBoundingClientRect().width + 12 : 300; }
    function update() {
      if (prev) prev.disabled = sc.scrollLeft <= 2;
      var end = sc.scrollLeft + sc.clientWidth >= sc.scrollWidth - 2;
      if (next) next.disabled = end;
      sc.classList.toggle('not-start', sc.scrollLeft > 2);
      sc.classList.toggle('at-end', end);
    }
    if (prev) prev.addEventListener('click', function () { sc.scrollBy({ left: -stepPx(), behavior: 'smooth' }); });
    if (next) next.addEventListener('click', function () { sc.scrollBy({ left: stepPx(), behavior: 'smooth' }); });
    sc.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { sc.scrollBy({ left: stepPx(), behavior: 'smooth' }); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { sc.scrollBy({ left: -stepPx(), behavior: 'smooth' }); e.preventDefault(); }
    });
    sc.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });
})();
