// Fond de l'en-tête : Cornell box rendue en path tracing progressif (WebGL2).
// Un échantillon par pixel et par image, accumulé jusqu'à MAX_SPP puis arrêt (plus aucun calcul GPU).
(function () {
  var canvas = document.getElementById('cornell');
  if (!canvas) return;
  var gl = canvas.getContext('webgl2', { antialias: false, alpha: false, preserveDrawingBuffer: false });
  if (!gl) { canvas.remove(); return; }
  var floatOK = !!gl.getExtension('EXT_color_buffer_float');
  var MAX_SPP = 600;

  var VS = '#version 300 es\nin vec2 p; out vec2 uv; void main(){ uv = p*0.5+0.5; gl_Position = vec4(p,0.,1.); }';

  var TRACE = `#version 300 es
precision highp float;
in vec2 uv; out vec4 o;
uniform sampler2D prevTex; uniform float frame; uniform vec2 res; uniform float shift; uniform vec3 bg;
const float PI = 3.14159265;
uint seed;
uint hash(uint x){ x ^= x >> 16; x *= 0x7feb352du; x ^= x >> 15; x *= 0x846ca68bu; x ^= x >> 16; return x; }
float rnd(){ seed = hash(seed); return float(seed) / 4294967296.0; }

// Matériaux : 0 blanc, 1 rouge, 2 vert, 3 lumière, 4 miroir, 5 verre, 6 bleu mat
const vec3 SPH_C[3] = vec3[3](vec3(-0.42, 0.42, -0.38), vec3(0.48, 0.34, 0.22), vec3(0.05, 0.16, 0.62));
const float SPH_R[3] = float[3](0.42, 0.34, 0.16);
const int SPH_M[3] = int[3](4, 5, 6);
const vec3 LMIN = vec3(-0.32, 1.995, -0.32), LMAX = vec3(0.32, 1.995, 0.32);
const vec3 LE = vec3(17.0, 15.0, 12.0);

float sph(vec3 ro, vec3 rd, vec3 c, float r){
  vec3 oc = ro - c; float b = dot(oc, rd); float h = b*b - dot(oc,oc) + r*r;
  if (h < 0.) return -1.; h = sqrt(h);
  float t = -b - h; if (t > 1e-3) return t; t = -b + h; return t > 1e-3 ? t : -1.;
}

// Intersection la plus proche ; renvoie t, normale n, matériau m
float scene(vec3 ro, vec3 rd, out vec3 n, out int m){
  float tb = 1e9; m = -1;
  // murs de la boîte : x=-1 (rouge), x=1 (vert), y=0, y=2, z=-1 (fond) ; face avant ouverte
  for (int i = 0; i < 5; i++){
    vec3 N; float d; int mat;
    if (i==0){ N=vec3(1,0,0); d=-1.; mat=1; } else if (i==1){ N=vec3(-1,0,0); d=1.; mat=2; }
    else if (i==2){ N=vec3(0,1,0); d=0.; mat=0; } else if (i==3){ N=vec3(0,-1,0); d=2.; mat=0; }
    else { N=vec3(0,0,1); d=-1.; mat=0; }
    int ax = i<2 ? 0 : (i<4 ? 1 : 2);
    float den = rd[ax]; if (abs(den) < 1e-6) continue;
    float t = (d - ro[ax]) / den; if (t < 1e-3 || t >= tb) continue;
    vec3 p = ro + t*rd;
    if (p.x < -1.001 || p.x > 1.001 || p.y < -0.001 || p.y > 2.001 || p.z < -1.001 || p.z > 1.0) continue;
    tb = t; n = N; m = mat;
    if (i==3 && p.x > LMIN.x && p.x < LMAX.x && p.z > LMIN.z && p.z < LMAX.z) m = 3;
  }
  for (int i = 0; i < 3; i++){
    float t = sph(ro, rd, SPH_C[i], SPH_R[i]);
    if (t > 0. && t < tb){ tb = t; n = normalize(ro + t*rd - SPH_C[i]); m = SPH_M[i]; }
  }
  return m < 0 ? -1. : tb;
}

vec3 albedo(int m){
  if (m==1) return vec3(0.63, 0.065, 0.05);
  if (m==2) return vec3(0.14, 0.45, 0.091);
  if (m==6) return vec3(0.10, 0.22, 0.55);
  return vec3(0.73);
}

vec3 cosDir(vec3 n){
  float a = rnd()*2.*PI, r = sqrt(rnd());
  vec3 t = normalize(abs(n.x) > .5 ? cross(n, vec3(0,1,0)) : cross(n, vec3(1,0,0)));
  vec3 b = cross(n, t);
  return normalize(t*r*cos(a) + b*r*sin(a) + n*sqrt(1.-r*r));
}

void main(){
  seed = hash(uint(gl_FragCoord.x) * 1973u + uint(gl_FragCoord.y) * 9277u + uint(frame) * 26699u);
  vec2 px = (gl_FragCoord.xy + vec2(rnd(), rnd())) / res;
  vec2 q = (px - vec2(0.5 + shift, 0.5)) * vec2(res.x / res.y, 1.);
  vec3 ro = vec3(0., 1., 3.55);
  vec3 rd = normalize(vec3(q * 0.78, -1.));
  vec3 L = vec3(0.), T = vec3(1.); bool spec = true;
  for (int b = 0; b < 6; b++){
    vec3 n; int m; float t = scene(ro, rd, n, m);
    if (t < 0.){ if (b == 0) L += bg; break; }
    vec3 p = ro + t*rd;
    if (dot(n, rd) > 0. && m != 5) n = -n;
    if (m == 3){ if (spec) L += T * LE; break; }
    if (m == 4){ ro = p + n*1e-3; rd = reflect(rd, n); T *= vec3(0.92); spec = true; continue; }
    if (m == 5){
      bool inside = dot(rd, n) > 0.; vec3 nn = inside ? -n : n; float eta = inside ? 1.5 : 1./1.5;
      float c = -dot(rd, nn); float r0 = 0.04; float F = r0 + (1.-r0)*pow(1.-c, 5.);
      vec3 rf = refract(rd, nn, eta);
      if (dot(rf, rf) < 1e-6 || rnd() < F){ rd = reflect(rd, nn); ro = p + nn*1e-3; }
      else { rd = rf; ro = p - nn*1e-3; }
      spec = true; continue;
    }
    vec3 A = albedo(m);
    // lumière directe (échantillonnage de la source)
    vec3 lp = vec3(mix(LMIN.x, LMAX.x, rnd()), LMIN.y, mix(LMIN.z, LMAX.z, rnd()));
    vec3 ld = lp - p; float dist2 = dot(ld, ld); ld /= sqrt(dist2);
    float cosS = dot(n, ld), cosL = ld.y;
    if (cosS > 0. && cosL > 0.){
      vec3 sn; int sm; float st = scene(p + n*1e-3, ld, sn, sm);
      if (sm == 3){
        float area = (LMAX.x-LMIN.x)*(LMAX.z-LMIN.z);
        L += T * LE * A / PI * cosS * cosL * area / dist2;
      }
    }
    T *= A; ro = p + n*1e-3; rd = cosDir(n); spec = false;
  }
  L = min(L, vec3(6.));
  vec3 prev = texture(prevTex, uv).rgb;
  o = vec4(mix(prev, L, 1. / (frame + 1.)), 1.);
}`;

  var SHOW = `#version 300 es
precision highp float;
in vec2 uv; out vec4 o; uniform sampler2D tex;
void main(){
  vec3 c = texture(tex, uv).rgb;
  c = c * (2.51*c + 0.03) / (c * (2.43*c + 0.59) + 0.14); // ACES approché
  o = vec4(pow(clamp(c, 0., 1.), vec3(1./2.2)), 1.);
}`;

  function prog(fs) {
    var p = gl.createProgram();
    [[gl.VERTEX_SHADER, VS], [gl.FRAGMENT_SHADER, fs]].forEach(function (s) {
      var sh = gl.createShader(s[0]); gl.shaderSource(sh, s[1]); gl.compileShader(sh);
      if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(sh));
      gl.attachShader(p, sh);
    });
    gl.bindAttribLocation(p, 0, 'p'); gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
    return p;
  }
  var trace, show;
  try { trace = prog(TRACE); show = prog(SHOW); } catch (e) { console.warn(e); canvas.remove(); return; }

  var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
  gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);

  var W = 0, H = 0, tex = [], fbo = [], frame = 0, cur = 0, raf = 0, visible = true;
  function target(w, h) {
    var t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t);
    if (floatOK) gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA32F, w, h, 0, gl.RGBA, gl.FLOAT, null);
    else gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    var f = gl.createFramebuffer(); gl.bindFramebuffer(gl.FRAMEBUFFER, f);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0);
    gl.clearColor(0, 0, 0, 1); gl.clear(gl.COLOR_BUFFER_BIT);
    return [t, f];
  }
  function bgColor() {
    var c = getComputedStyle(document.documentElement).getPropertyValue('--bg').trim() || '#0f1216';
    var m = c.match(/^#?([0-9a-f]{6})$/i); if (!m) return [0.06, 0.07, 0.085];
    var n = parseInt(m[1], 16);
    return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255].map(function (v) { return Math.pow(v, 2.2); });
  }
  function resize() {
    var r = canvas.getBoundingClientRect();
    var scale = Math.min(window.devicePixelRatio || 1, 1.5) * 0.75;
    var w = Math.max(64, Math.round(r.width * scale)), h = Math.max(64, Math.round(r.height * scale));
    var px = w * h, cap = 900000; if (px > cap) { var k = Math.sqrt(cap / px); w = Math.round(w * k); h = Math.round(h * k); }
    if (w === W && h === H) return;
    W = w; H = h; canvas.width = w; canvas.height = h;
    tex.forEach(function (t) { gl.deleteTexture(t); }); fbo.forEach(function (f) { gl.deleteFramebuffer(f); });
    var a = target(w, h), b = target(w, h); tex = [a[0], b[0]]; fbo = [a[1], b[1]];
    frame = 0; start();
  }
  var BG = bgColor();
  function step() {
    raf = 0;
    if (!visible || frame >= MAX_SPP) return;
    var wide = W / H > 1.6;
    var shift = wide ? 0.25 : 0.0;
    gl.viewport(0, 0, W, H);
    gl.useProgram(trace);
    gl.bindFramebuffer(gl.FRAMEBUFFER, fbo[1 - cur]);
    gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, tex[cur]);
    gl.uniform1i(gl.getUniformLocation(trace, 'prevTex'), 0);
    gl.uniform1f(gl.getUniformLocation(trace, 'frame'), frame);
    gl.uniform2f(gl.getUniformLocation(trace, 'res'), W, H);
    gl.uniform1f(gl.getUniformLocation(trace, 'shift'), shift);
    gl.uniform3f(gl.getUniformLocation(trace, 'bg'), BG[0], BG[1], BG[2]);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    cur = 1 - cur; frame++;
    gl.useProgram(show);
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    gl.bindTexture(gl.TEXTURE_2D, tex[cur]);
    gl.uniform1i(gl.getUniformLocation(show, 'tex'), 0);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    if (frame === 1) canvas.classList.add('on');
    start();
  }
  function start() { if (!raf && visible && frame < MAX_SPP) raf = requestAnimationFrame(step); }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (e) { visible = e[0].isIntersecting; start(); }).observe(canvas);
  }
  document.addEventListener('visibilitychange', function () { visible = !document.hidden; start(); });
  window.addEventListener('resize', function () { clearTimeout(resize.t); resize.t = setTimeout(resize, 200); });
  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: light)');
    var on = function () { BG = bgColor(); frame = 0; start(); };
    if (mq.addEventListener) mq.addEventListener('change', on);
  }
  resize();
})();
