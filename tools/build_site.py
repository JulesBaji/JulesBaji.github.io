#!/usr/bin/env python3
"""Génère les 4 pages du site (FR/EN, accueil et stage CEA) à partir d'un seul jeu de textes."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GH = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')
MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 5h20v14H2V5zm2 2v.5l8 5 8-5V7H4zm16 2.8-8 5-8-5V17h16V9.8z"/></svg>'
IN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3V9zm7 0h3.8v1.7h.1c.5-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9V21h-4V9z"/></svg>'
DOC = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6V2zm8 1.5V8h4.5L14 3.5zM8 12h10v1.6H8V12zm0 3.5h10v1.6H8v-1.6zm0 3.5h7v1.6H8V19z"/></svg>'

import hashlib as _h, glob as _g
V = {os.path.basename(f): _h.md5(open(f, 'rb').read()).hexdigest()[:8] for f in _g.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', '*'))}

L = {
 'fr': dict(
  lang='fr', other='en/', other_label='EN', other_title='English version', other_hreflang='en',
  home='', p='', cea_page='stage-cea.html', proj_page='projets.html',
  title='Jules Baji · Ingénieur en informatique graphique',
  desc="Jules Baji, ingénieur en informatique graphique : rendu 3D, calcul GPU et IA pour la 3D. Stage au CEA Saclay sur le Gaussian Splatting pour la réalité virtuelle.",
  nav=[('@cea','Stage CEA')],
  contact='Contact',
  role='Ingénieur R&amp;D · Graphics, géométrie &amp; 3D ML',
  pitch="Jeune diplômé en informatique graphique : je développe en C++ et CUDA des moteurs de rendu 3D et des outils de calcul.",
  meta='Paris · disponible immédiatement',
  cv='CV (PDF)', cv_file='cv/CV_Jules_Baji.pdf', email='E-mail',
  h_hl='À la une', h_exp='Expérience', h_skills='Compétences', h_proj='Projets de master', prev='Projets précédents', next='Projets suivants', theme_label='Changer de thème (sombre/clair)', h_form='Formation', h_contact='Contact',
  hl_main=('Stage de fin d\'études · CEA Saclay · 2025', 'Des reflets plus réalistes en réalité virtuelle',
           "Amélioration du Gaussian Splatting, une technique qui recrée une scène 3D à partir de photos.", 'Voir les résultats →',
           'Comparaison avant/après : méthode de référence à gauche, ma méthode à droite'),
  exp=[('CEA Saclay','Stage de fin d\'études · R&amp;D en rendu 3D','Des reflets plus réalistes en Gaussian Splatting pour la réalité virtuelle.','01–07/2025',['C++','CUDA','PyTorch'], True),
       ('Kreon Technologies','Stage · logiciel de CAO','Correction d\'algorithmes de géométrie dans un logiciel en production.','04–05/2023',['C++'], False)],
  more='En savoir plus',
  skills=[('Rendu 3D','OpenGL · GLSL · Ray tracing · 3D Gaussian Splatting · WebGL'),
          ('Calcul GPU et parallèle','CUDA · OpenMP · MPI'),
          ('Langages et outils','C++ · Python · PyTorch · NumPy · JavaScript · Linux · Git'),
          ('Langues','Français · Anglais C1')],
  proj_sub='Université de Limoges, 2023-2025',
  projects=[
   ("Synthèse d'image réaliste","Path tracer avec BRDF à microfacettes, géométrie SDF et CSG, accéléré par BVH.",['C++','OpenMP'],['Path-Tracer']),
   ("Parallélisme","Kernels CUDA pour une carte de hauteur ; recherche de sous-image MPI et OpenMP.",['CUDA','MPI','OpenMP'],['GPGPU','Parallelisme']),
   ("Moteur 3D temps réel","Maillages, textures, caméras, lumières, shaders et rendu différé.",['C++','OpenGL','GLSL'],['Moteur3D']),
   ("Détection de collisions 3D","Sweep and Prune, BVH et test triangle-triangle de Möller.",['WebGL','JavaScript'],['Modelisation-Collision-Detection']),
   ("Simulation de fluide","Fluide SPH incompressible avec turbulences, d'après un <a href=\"https://doi.org/10.1109/TVCG.2018.2832080\" target=\"_blank\" rel=\"noopener\">article de recherche</a>.",['Java'],['SPH-Fluid']),
   ("Impression 3D","Découpe en couches : Delaunay et rastérisation GPU.",['Java','OpenGL'],['Impression-3D-GPU']),
   ("Géométrie discrète","Suivi de contour, polygonisation et mesures de forme.",['C++'],['Geometrie-Discrete']),
   ("Vision par ordinateur","Génération de visages, super-résolution et détection de photos recapturées d'après un <a href=\"https://doi.org/10.1016/j.image.2022.116662\" target=\"_blank\" rel=\"noopener\">article de recherche</a>.",['Python','Keras'],['Detection-Recapture']),
  ],
  form=[('Master Informatique ISICG','Université de Limoges · informatique graphique','2023–2025'),
        ('Licence Informatique','Université de Limoges','2020–2023')],
  interests="Centres d'intérêt : trompette au conservatoire (2011-2019), trésorier de l'association étudiante du master, escalade.",
  contact_line="Référence : ingénieur-chercheur au CEA, mon encadrant de stage, contact sur demande.",
  report='Rapport de stage (PDF, 6 Mo)',
  footer='© 2026 Jules Baji · Paris',
  # page du stage
  cea_title='Stage au CEA : des reflets plus réalistes en réalité virtuelle',
  cea_desc="Stage de fin d'études de Jules Baji au CEA Saclay : amélioration des reflets en Gaussian Splatting pour la réalité virtuelle.",
  cea_back='← Retour à l\'accueil', cea_meta='Stage de fin d\'études · CEA Saclay · janvier à juillet 2025',
  boxes=[('Le problème',"Le Gaussian Splatting recrée une scène 3D à partir de photos et l'affiche en temps réel, mais il rend mal les reflets (surfaces brillantes, vitres, objets métalliques)."),
         ("Ce que j'ai fait","J'ai d'abord testé le lancer de rayons, qui simule le trajet de la lumière : fidèle, mais trop lent pour un casque de réalité virtuelle (60 images par seconde minimum). J'ai ensuite ajouté au rendu classique un modèle mathématique des reflets (Gaussiennes Sphériques)."),
         ('Le résultat',"Des reflets nettement plus réalistes, plus proches de la photo réelle sur les trois scènes testées, à la même vitesse que la méthode de base (environ 300 images par seconde).")],
  h_cmp='Comparer', cmp_note="Faites glisser le curseur : à gauche la méthode de référence (gsplat), à droite ma méthode. Le PSNR mesure la ressemblance avec la photo réelle (plus haut = plus proche).",
  h_vid="Vidéos : méthodes étudiées pendant l'état de l'art", scene_sac='scène SAC', and_='et',
  h_tech='Technologies', tech=['C++','CUDA','OpenMP','PyTorch','Gaussian Splatting','Ray Tracing','VR'],
  js=dict(ref='Référence (gsplat)', mine='Ma méthode', photo='Photo réelle', dec=',', gtTab='Face à la photo réelle', gtMeta='Photo réelle à droite',
          full='Pleine résolution :', view='Vue', compare='Comparer', r1='Résolution 1:1', r2='Résolution 1:2'),
 ),
 'en': dict(
  lang='en', other='../', other_label='FR', other_title='Version française', other_hreflang='fr',
  home='', p='../', cea_page='cea-internship.html', proj_page='projects.html',
  title='Jules Baji · Computer graphics engineer',
  desc="Jules Baji, computer graphics engineer: 3D rendering, GPU computing and AI for 3D. Internship at CEA Saclay on Gaussian Splatting for virtual reality.",
  nav=[('@cea','CEA internship')],
  contact='Contact',
  role='R&amp;D Engineer · Graphics, geometry &amp; 3D ML',
  pitch="Recent computer graphics graduate: I build 3D rendering engines and computing tools in C++ and CUDA.",
  meta='Paris · available immediately',
  cv='Resume (PDF)', cv_file='cv/Resume_Jules_Baji.pdf', email='Email',
  h_hl='Highlights', h_exp='Experience', h_skills='Skills', h_proj="Master's projects", prev='Previous projects', next='Next projects', theme_label='Switch theme (dark/light)', h_form='Education', h_contact='Contact',
  hl_main=("Master's thesis internship · CEA Saclay · 2025", 'More realistic reflections in virtual reality',
           "Improving Gaussian Splatting, a technique that recreates a 3D scene from photos.", 'See the results →',
           'Before/after comparison: reference method on the left, my method on the right'),
  exp=[('CEA Saclay',"Master's thesis internship · 3D rendering R&amp;D",'More realistic reflections in Gaussian Splatting for virtual reality.','01–07/2025',['C++','CUDA','PyTorch'], True),
       ('Kreon Technologies','Internship · CAD software','Fixes to geometry algorithms in production software.','04–05/2023',['C++'], False)],
  more='Learn more',
  skills=[('3D rendering','OpenGL · GLSL · Ray tracing · 3D Gaussian Splatting · WebGL'),
          ('GPU and parallel computing','CUDA · OpenMP · MPI'),
          ('Languages and tools','C++ · Python · PyTorch · NumPy · JavaScript · Linux · Git'),
          ('Spoken languages','French · English C1')],
  proj_sub='University of Limoges, 2023-2025',
  projects=[
   ("Realistic image synthesis","Path tracer with microfacet BRDFs, SDF geometry and CSG, accelerated by a BVH.",['C++','OpenMP'],['Path-Tracer']),
   ("Parallel computing","CUDA kernels for a heightmap; MPI and OpenMP sub-image search.",['CUDA','MPI','OpenMP'],['GPGPU','Parallelisme']),
   ("Real-time 3D engine","Meshes, textures, cameras, lights, shaders and deferred rendering.",['C++','OpenGL','GLSL'],['Moteur3D']),
   ("3D collision detection","Sweep and Prune, BVH and Möller's triangle-triangle test.",['WebGL','JavaScript'],['Modelisation-Collision-Detection']),
   ("Fluid simulation","Incompressible SPH fluid with turbulence, based on a <a href=\"https://doi.org/10.1109/TVCG.2018.2832080\" target=\"_blank\" rel=\"noopener\">research paper</a>.",['Java'],['SPH-Fluid']),
   ("3D printing","Layer slicing: Delaunay and GPU rasterization.",['Java','OpenGL'],['Impression-3D-GPU']),
   ("Discrete geometry","Contour tracking, polygonization and shape measures.",['C++'],['Geometrie-Discrete']),
   ("Computer vision","Face generation, image super-resolution and recaptured-photo detection based on a <a href=\"https://doi.org/10.1016/j.image.2022.116662\" target=\"_blank\" rel=\"noopener\">research paper</a>.",['Python','Keras'],['Detection-Recapture']),
  ],
  form=[('MSc Computer Science, ISICG','University of Limoges · computer graphics','2023–2025'),
        ('BSc Computer Science','University of Limoges','2020–2023')],
  interests="Interests: trumpet at the conservatory (2011-2019), treasurer of the master's student association, climbing.",
  contact_line="Reference: research engineer at CEA, my internship supervisor, contact on request.",
  report='Internship report (PDF, French, 6 MB)',
  footer='© 2026 Jules Baji · Paris',
  cea_title='CEA internship: more realistic reflections in virtual reality',
  cea_desc="Jules Baji's master's thesis internship at CEA Saclay: better reflections in Gaussian Splatting for virtual reality.",
  cea_back='← Back to home', cea_meta="Master's thesis internship · CEA Saclay · January to July 2025",
  boxes=[('The problem',"Gaussian Splatting recreates a 3D scene from photos and displays it in real time, but it renders reflections poorly (shiny surfaces, glass, metal objects)."),
         ('What I did',"I first tested ray tracing, which simulates the path of light: accurate, but too slow for a virtual reality headset (60 frames per second minimum). I then added a mathematical model of reflections (Spherical Gaussians) to the standard renderer."),
         ('The result',"Much more realistic reflections, closer to the real photo on all three test scenes, at the same speed as the base method (about 300 frames per second).")],
  h_cmp='Compare', cmp_note="Drag the slider: the reference method (gsplat) on the left, my method on the right. PSNR measures similarity to the real photo (higher is closer).",
  h_vid='Videos: methods studied during the state-of-the-art review', scene_sac='SAC scene', and_='and',
  h_tech='Technologies', tech=['C++','CUDA','OpenMP','PyTorch','Gaussian Splatting','Ray Tracing','VR'],
  js=dict(ref='Reference (gsplat)', mine='My method', photo='Real photo', dec='.', gtTab='Against the real photo', gtMeta='Real photo on the right',
          full='Full resolution:', view='View', compare='Compare', r1='Resolution 1:1', r2='Resolution 1:2'),
 ),
}

def head(t, title, desc, p):
    return f'''<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css?v={V["style.css"]}">
<script>try{{if(localStorage.getItem('theme')==='light')document.documentElement.dataset.theme='light'}}catch(e){{}}</script>
</head>
<body>
'''

THEME_BTN = ('<button class="theme" type="button" aria-label="{l}" title="{l}">'
  '<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 1.8v3M12 19.2v3M1.8 12h3M19.2 12h3M4.8 4.8l2.1 2.1M17.1 17.1l2.1 2.1M4.8 19.2l2.1-2.1M17.1 6.9l2.1-2.1"/></svg>'
  '<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 14.6A8.6 8.6 0 0 1 9.4 3.5 8.6 8.6 0 1 0 20.5 14.6z"/></svg></button>')

def nav(t, home_prefix, other_href, current=''):
    def href(h): return {'@cea': t['cea_page'], '@proj': (home_prefix or '') + '#projets'}.get(h, home_prefix + h)
    items = ''.join(f'<li><a href="{href(h)}"' + (' aria-current="page"' if h == current else '') + f'>{l}</a></li>' for h, l in t['nav'])
    return f'''<nav>
  <div class="wrap">
    <a class="brand" href="{home_prefix or './'}">Jules Baji</a>
    <div class="ctl-mobile">{THEME_BTN.format(l=t['theme_label'])}<a class="lang" href="{other_href}" hreflang="{t['other_hreflang']}" lang="{t['other_hreflang']}" title="{t['other_title']}">{t['other_label']}</a><a class="cta" href="{home_prefix}#contact">{t['contact']}</a></div>
    <ul>
      {items}
      <li class="ctl">{THEME_BTN.format(l=t['theme_label'])}</li>
      <li class="ctl"><a class="lang" href="{other_href}" hreflang="{t['other_hreflang']}" lang="{t['other_hreflang']}" title="{t['other_title']}">{t['other_label']}</a></li>
      <li class="ctl"><a class="cta" href="{home_prefix}#contact">{t['contact']}</a></li>
    </ul>
  </div>
</nav>
'''

def chips(xs): return '<div class="chips">' + ''.join(f'<span class="chip">{x}</span>' for x in xs) + '</div>'
def repo(r): return f'<a href="https://github.com/JulesBaji/{r}" target="_blank" rel="noopener" aria-label="GitHub {r}">{GH}<span>{r}</span></a>'

def links(t):
    p = t['p']
    return f'''<div class="links">
        <a class="btn primary" href="{p}{t['cv_file']}" download>{DOC}{t['cv']}</a>
        <a class="btn" href="mailto:julesbaji1@gmail.com">{MAIL}{t['email']}</a>
        <a class="btn" href="https://www.linkedin.com/in/julesbaji" target="_blank" rel="noopener">{IN}LinkedIn</a>
        <a class="btn" href="https://github.com/JulesBaji" target="_blank" rel="noopener">{GH}GitHub</a>
      </div>'''

LOGOS = {
    'CEA Saclay': '<img class="logo logo-cea" src="{p}images/logos/cea.svg" alt="Logo du CEA" width="48" height="48">',
    'Kreon Technologies': '<img class="logo logo-kreon" src="{p}images/logos/kreon.png" alt="Logo de Kreon" width="110" height="28">',
}
UNILIM = ('<img class="logo logo-unilim on-dark" src="{p}images/logos/unilim-sombre.png" alt="Logo de l\'Université de Limoges" width="110" height="36">'
          '<img class="logo logo-unilim on-light" src="{p}images/logos/unilim.png" alt="" width="110" height="36">')

# Animated card backgrounds: repo -> (file in images/web or (dark, light) pair, invert in light theme, object-position)
PROJ_BG = {'Modelisation-Collision-Detection': ('collisions', True, '70% 50%'),
           'SPH-Fluid': (('fluide-dk', 'fluide-lt'), False, '50% 80%'),
           'Moteur3D': ('moteur3d', False, '50% 40%'),
           'Detection-Recapture': ('recapture.jpg', False, '50% 50%'),
           'GPGPU': ('parallelisme', False, '70% 30%'),
           'Geometrie-Discrete': (('geometrie-dk', 'geometrie-lt'), False, '50% 50%'),
           'Impression-3D-GPU': ('impression3d.jpg', False, '60% 50%')}  # photo CC0, Wikimedia Commons (pxhere)

def _video(f, p, cls, pos):
    return (f'<video class="{cls}" autoplay muted loop playsinline preload="metadata" aria-hidden="true" '
            f'style="object-position:{pos}" poster="{p}images/web/{f}.jpg"><source src="{p}images/web/{f}.mp4" type="video/mp4"></video>')

def proj_bg(r, p):
    if r not in PROJ_BG: return ''
    f, inv, pos = PROJ_BG[r]
    if isinstance(f, str) and f.endswith('.jpg'):  # still image
        return f'<img class="bg" src="{p}images/web/{f}" alt="" aria-hidden="true" style="object-position:{pos}">'
    if isinstance(f, tuple):
        return _video(f[0], p, 'bg on-dark', pos) + _video(f[1], p, 'bg on-light', pos)
    return _video(f, p, 'bg inv' if inv else 'bg', pos)

def home(t):
    p = t['p']; cp = t['cea_page']
    m = t['hl_main']
    exp = ''.join(f'''
      <div class="entry"><div class="side"><span class="when">{d}</span>{LOGOS.get(o, '').format(p=p)}<span class="org">{o}</span></div><div class="main"><h3>{r}</h3><p>{w}</p>{chips(c)}{f'<a class="more" href="{cp}">{t["more"]} →</a>' if more else ''}</div></div>''' for o, r, w, d, c, more in t['exp'])
    def sk(v, last):
        return f'<span class="plain">{v}</span>' if last else chips([x.replace('Ray tracing', 'Ray Tracing') for x in v.split(' · ')])
    skills = ''.join(f'<div class="sk"><b>{k}</b>{sk(v, i == len(t["skills"]) - 1)}</div>' for i, (k, v) in enumerate(t['skills']))
    projs = ''.join(f'''
      <article class="card proj{' has-bg' if rs[0] in PROJ_BG else ''}">{proj_bg(rs[0], p)}<h3>{n}</h3><p>{d}</p>{chips(c)}<div class="repo">{''.join(repo(r) for r in rs)}</div></article>''' for n, d, c, rs in t['projects'])
    form = ''.join(f'''
      <div class="entry"><div class="side"><span class="when">{c}</span>{UNILIM.format(p=p)}</div><div class="main"><h3>{a}</h3><p>{b}</p></div></div>''' for a, b, c in t['form'])
    return head(t, t['title'], t['desc'], p) + nav(t, '', t['other']) + f'''
<header class="hero">
  <canvas id="cornell" aria-hidden="true"></canvas>
  <div class="wrap">
    <div>
      <h1>Jules Baji</h1>
      <p class="role">{t['role']}</p>
      <p class="pitch">{t['pitch']}</p>
      <p class="meta">{t['meta']}</p>
      {links(t)}
    </div>
  </div>
</header>

<main>
<section id="points-forts">
  <div class="wrap">
    <h2>{t['h_hl']}</h2>
    <div class="highlights">
      <a class="card hl-main" href="{cp}">
        <div class="ba" role="img" aria-label="{m[4]}"><img src="{p}images/web/teaser_ref.webp" alt="" width="1200" height="615"><img class="ba-mine" src="{p}images/web/teaser_mine.webp" alt="" width="1200" height="615"><span class="ba-line" aria-hidden="true"></span></div>
        <div class="body"><p class="kicker">{m[0]}</p><h3>{m[1]}</h3><p>{m[2]}</p><span class="more">{m[3]}</span></div>
      </a>
    </div>
  </div>
</section>

<section id="projets">
  <div class="wrap">
    <div class="h2row"><h2>{t['h_proj']}</h2><div class="scroll-btns"><button type="button" class="sb prev" aria-label="{t['prev']}">←</button><button type="button" class="sb next" aria-label="{t['next']}">→</button></div></div>
    <div class="scroller" tabindex="0" aria-label="{t['h_proj']}">{projs}
    </div>
  </div>
</section>

<section id="experience">
  <div class="wrap">
    <h2>{t['h_exp']}</h2>
    <div class="entries">{exp}
    </div>
  </div>
</section>

<section id="competences">
  <div class="wrap">
    <h2>{t['h_skills']}</h2>
    <div class="card skills">{skills}</div>
  </div>
</section>

<section id="formation">
  <div class="wrap">
    <h2>{t['h_form']}</h2>
    <div class="entries">{form}
    </div>
    <p class="small" style="margin:12px 0 0">{t['interests']}</p>
  </div>
</section>

<section id="contact" class="contact">
  <div class="wrap">
    <h2>{t['h_contact']}</h2>
    {links(t)}
    <p class="small" style="margin-top:14px">{t['contact_line']}</p>
  </div>
</section>
</main>

<footer>{t['footer']}</footer>
<script src="{p}assets/chips.js?v={V["chips.js"]}"></script>
<script src="{p}assets/theme.js?v={V["theme.js"]}"></script>
<script src="{p}assets/cornell.js?v={V["cornell.js"]}"></script>
<script src="{p}assets/scroller.js?v={V["scroller.js"]}"></script>
</body>
</html>
'''

def cea(t):
    p = t['p']; j = t['js']
    boxes = ''.join(f'<div class="card"><p class="kicker">{a}</p><p>{b}</p></div>' for a, b in t['boxes'])
    v = 'videos/web/'
    vids = [('comparaison_3dgs_rg', f"<b>3DGS {t['and_']} RayGauss</b> · {t['scene_sac']}"),
            ('3dgs_dr_sac', f"<b>3DGS-DR</b> · {t['scene_sac']}"), ('3d_grut_sac', f"<b>3D-GRUT</b> · {t['scene_sac']}"),
            ('3dgs_cbox', '<b>3DGS</b> · Cornell Box'), ('rg_cbox', '<b>RayGauss</b> · Cornell Box'), ('3dgs_dr_cbox', '<b>3DGS-DR</b> · Cornell Box')]
    vh = ''.join(f'<figure><video controls muted loop playsinline preload="none" poster="{p}{v}{n}.jpg" src="{p}{v}{n}.mp4"></video><figcaption>{c}</figcaption></figure>' for n, c in vids)
    jsconf = f'''<script>
window.CEA_TXT = {{ prefix: '{p}', ref: '{j['ref']}', mine: '{j['mine']}', photo: '{j['photo']}', dec: '{j['dec']}',
  gtTab: '{j['gtTab']}', gtMeta: '{j['gtMeta']}', full: '{j['full']}', view: '{j['view']}', compare: '{j['compare']}',
  meta1: function (a, b) {{ return '{j['r1']} · PSNR <b>' + a + '</b> → <b>' + b + '</b>'; }},
  meta2: function (a, b) {{ return '{j['r2']} · PSNR <b>' + a + '</b> → <b>' + b + '</b>'; }} }};
</script>'''
    other = ('../' + L['en']['cea_page']) if False else None
    other_href = 'en/cea-internship.html' if t['lang'] == 'fr' else '../stage-cea.html'
    home_prefix = './' if t['lang'] == 'fr' else './'
    return head(t, t['cea_title'] + ' · Jules Baji', t['cea_desc'], p) + nav(t, './', other_href, '@cea') + f'''
<main>
<div class="wrap page-head">
  <a class="back" href="./">{t['cea_back']}</a>
  <h1>{t['cea_title']}</h1>
  <p>{t['cea_meta']}</p>
  <div class="head-tools">{chips(t['tech'])}
    <a class="btn primary" href="{p}rapport/rapport_stage_cea_jules_baji.pdf" download>{DOC}{t['report']}</a>
  </div>
</div>

<section style="border-top:0">
  <div class="wrap">
    <div class="explain">{boxes}</div>
    <h2>{t['h_cmp']}</h2>
    <p class="note">{t['cmp_note']}</p>
    <div class="tabs" role="tablist" id="scene-tabs"></div>
    <div class="card viewer">
      <div class="top-line"><span class="meta" id="scene-meta"></span><div class="views" id="scene-views"></div></div>
      <div class="compare" id="cmp"></div>
      <div class="full" id="cmp-full"></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>{t['h_vid']}</h2>
    <div class="videos">{vh}</div>
  </div>
</section>

</main>

<footer>{t['footer']}</footer>
{jsconf}
<script src="{p}assets/chips.js?v={V["chips.js"]}"></script>
<script src="{p}assets/theme.js?v={V["theme.js"]}"></script>
<script src="{p}assets/cea.js?v={V["cea.js"]}"></script>
</body>
</html>
'''

def redirect(to):
    return f'<!DOCTYPE html><html><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{to}"><title>Jules Baji</title></head><body><a href="{to}">{to}</a></body></html>\n'

for k, t in L.items():
    base = ROOT if k == 'fr' else os.path.join(ROOT, 'en')
    os.makedirs(base, exist_ok=True)
    open(os.path.join(base, 'index.html'), 'w').write(home(t))
    open(os.path.join(base, t['cea_page']), 'w').write(cea(t))
    open(os.path.join(base, t['proj_page']), 'w').write(redirect('./#projets'))
print('ok')
