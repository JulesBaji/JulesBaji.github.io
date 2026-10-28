// Comparaisons avant/après du stage CEA. Textes fournis par la page dans window.CEA_TXT.
(function () {
  var T = window.CEA_TXT, P = T.prefix;
  function pair(a, b, la, lb, fa, fb) { return { a: P + 'images/web/' + a + '.webp', b: P + 'images/web/' + b + '.webp', la: la, lb: lb, fa: P + 'images/' + fa, fb: P + 'images/' + fb }; }
  function gs(scene, n) { var s = n > 1 ? n : ''; return pair(scene + '_gsplat' + s, scene + '_sg' + s, T.ref, T.mine, scene + '_gsplat' + s + '.png', scene + '_sg' + s + '.png'); }
  var SCENES = [
    { name: 'Bonsaï', meta: T.meta1('30' + T.dec + '68', '31' + T.dec + '52'), views: [gs('bonsai', 2), gs('bonsai', 1)] },
    { name: 'Bicycle', meta: T.meta2('25' + T.dec + '82', '26' + T.dec + '25'), views: [gs('bicycle', 1), gs('bicycle', 2), gs('bicycle', 3), gs('bicycle', 4)] },
    { name: 'Garden', meta: T.meta2('26' + T.dec + '86', '27' + T.dec + '34'), views: [gs('garden', 1), gs('garden', 2), gs('garden', 3)] },
    { name: T.gtTab, meta: T.gtMeta, views: [
      Object.assign(pair('bonsai_sg', 'gt_bonsai', T.mine, T.photo, 'bonsai_sg.png', 'gt_bonsai.JPG'), { tag: 'Bonsaï' }),
      Object.assign(pair('garden_sg', 'gt_garden', T.mine, T.photo, 'garden_sg.png', 'gt_garden.JPG'), { tag: 'Garden' }) ] }
  ];
  var tabs = document.getElementById('scene-tabs'), meta = document.getElementById('scene-meta'),
      views = document.getElementById('scene-views'), cmp = document.getElementById('cmp'), full = document.getElementById('cmp-full');
  function showView(v) {
    cmp.innerHTML =
      '<img alt="' + v.la + '" src="' + v.a + '">' +
      '<div class="top"><img alt="' + v.lb + '" src="' + v.b + '"></div>' +
      '<div class="bar"></div><div class="knob">⇆</div>' +
      '<span class="lbl l">' + v.la + '</span><span class="lbl r">' + v.lb + '</span>' +
      '<input type="range" min="0" max="100" value="50" aria-label="' + T.compare + ' ' + v.la + ' / ' + v.lb + '">';
    var top = cmp.querySelector('.top'), bar = cmp.querySelector('.bar'), knob = cmp.querySelector('.knob');
    cmp.querySelector('input').addEventListener('input', function (e) {
      var x = e.target.value;
      top.style.clipPath = 'inset(0 0 0 ' + x + '%)'; bar.style.left = x + '%'; knob.style.left = x + '%';
    });
    if (full) full.innerHTML = T.full + ' <a href="' + v.fa + '">' + v.la.toLowerCase() + '</a> · <a href="' + v.fb + '">' + v.lb.toLowerCase() + '</a>';
  }
  function showScene(i) {
    var sc = SCENES[i];
    tabs.querySelectorAll('.tab').forEach(function (t, j) { t.setAttribute('aria-selected', j === i ? 'true' : 'false'); });
    if (meta) meta.innerHTML = sc.meta; views.innerHTML = '';
    if (sc.views.length > 1) sc.views.forEach(function (v, j) {
      var b = document.createElement('button');
      b.textContent = v.tag || (T.view + ' ' + (j + 1));
      b.setAttribute('aria-pressed', j === 0 ? 'true' : 'false');
      b.onclick = function () { views.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); }); b.setAttribute('aria-pressed', 'true'); showView(v); };
      views.appendChild(b);
    });
    showView(sc.views[0]);
  }
  SCENES.forEach(function (sc, i) {
    var t = document.createElement('button');
    t.className = 'tab'; t.setAttribute('role', 'tab'); t.textContent = sc.name;
    t.onclick = function () { showScene(i); };
    tabs.appendChild(t);
  });
  showScene(0);
})();
