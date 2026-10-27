// Couleur des compétences par catégorie
(function () {
  var CAT = {
    'C++':'lang','Python':'lang','GLSL':'lang','JavaScript':'lang','Java':'lang','C':'lang',
    'CUDA':'gpu','OpenMP':'gpu','MPI':'gpu',
    '3D Gaussian Splatting':'gfx','Gaussian Splatting':'gfx','OpenGL':'gfx','WebGL':'gfx','Ray Tracing':'gfx','VR':'gfx',
    'PyTorch':'ml','NumPy':'ml','Keras':'ml',
    'Linux':'tool','Git':'tool'
  };
  document.querySelectorAll('.chip').forEach(function (c) { c.classList.add(CAT[c.textContent.trim()] || 'tool'); });
})();
