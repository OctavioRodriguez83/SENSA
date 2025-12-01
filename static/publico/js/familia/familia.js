document.addEventListener('DOMContentLoaded', () => {
  const checkboxes = document.querySelectorAll('input[name="familia"]');
  const detalles = document.querySelectorAll('.familia-detalle');

  function mostrarDetalle() {
    let familiaId = null;
    checkboxes.forEach(cb => {
      if (cb.checked) familiaId = cb.value;
    });
    detalles.forEach(det => {
      if (det.getAttribute('data-familia-id') === familiaId) {
        det.style.display = '';
      } else {
        det.style.display = 'none';
      }
    });
  }

  checkboxes.forEach(cb => {
    cb.addEventListener('change', () => {
      // Solo permite un checkbox activo a la vez
      checkboxes.forEach(c => c.checked = false);
      cb.checked = true;
      mostrarDetalle();
    });
  });

  mostrarDetalle(); // Inicializa al cargar

  // --- Descripción colapsable en móviles ---
  function setupDescripcionColapsable() {
    const maxLength = 200; // caracteres a mostrar en móvil
    document.querySelectorAll('.familia-descripcion').forEach(desc => {
      const span = desc.querySelector('.descripcion-corta');
      const fullText = span.textContent.trim();
      const verMasBtn = desc.querySelector('.ver-mas-btn');
      const verMenosBtn = desc.querySelector('.ver-menos-btn');

      function colapsar() {
        if (window.innerWidth <= 600 && fullText.length > maxLength) {
          span.textContent = fullText.slice(0, maxLength) + '...';
          verMasBtn.style.display = 'inline-block';
          verMenosBtn.style.display = 'none';
        } else {
          span.textContent = fullText;
          verMasBtn.style.display = 'none';
          verMenosBtn.style.display = 'none';
        }
      }

      function expandir() {
        span.textContent = fullText;
        verMasBtn.style.display = 'none';
        verMenosBtn.style.display = 'inline-block';
      }

      verMasBtn.onclick = expandir;
      verMenosBtn.onclick = colapsar;

      // Inicializa
      colapsar();
      // Recolapsa si cambia el tamaño de pantalla
      window.addEventListener('resize', colapsar);
    });
  }

  setupDescripcionColapsable();
});

