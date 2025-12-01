document.addEventListener('DOMContentLoaded', () => {
      const productsContainer = document.querySelector('.store-products');
      const paginatorContainer = document.getElementById('store-paginator');
      const applyFiltersBtn = document.getElementById('apply-filters');

      function getChecked(name) {
        return Array.from(document.querySelectorAll(`input[name="${name}"]:checked`))
                    .map(cb => cb.value);
      }

      function fetchProducts(page = 1) {
        const params = new URLSearchParams();
        getChecked('marca').forEach(marca => params.append('marca', marca));
        getChecked('categoria').forEach(categoria => params.append('categoria', categoria));
        const precioMin = document.getElementById('precio-min').value;
        const precioMax = document.getElementById('precio-max').value;
        if (precioMin) params.append('precio_min', precioMin);
        if (precioMax) params.append('precio_max', precioMax);
        params.append('page', page);

        const url = `${window.location.pathname}?${params}`;

        fetch(url, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
          .then(response => response.json())
          .then(data => {
            productsContainer.innerHTML = data.products_html;
            if (paginatorContainer) {
              paginatorContainer.innerHTML = data.paginator_html;
            }
            attachPaginationEvents();
          });
      }

      function attachPaginationEvents() {
        document.querySelectorAll('.store-pagination a').forEach(link => {
          link.addEventListener('click', e => {
            e.preventDefault();
            const page = new URL(link.href).searchParams.get('page') || 1;
            fetchProducts(page);
          });
        });
      }

      document.querySelectorAll('input[name="categoria"]').forEach(cb =>
        cb.addEventListener('change', () => fetchProducts())
      );
      document.querySelectorAll('input[name="marca"]').forEach(cb =>
        cb.addEventListener('change', () => fetchProducts())
      );
      if (applyFiltersBtn) {
        applyFiltersBtn.addEventListener('click', e => {
          e.preventDefault();
          fetchProducts();
        });
      }

      attachPaginationEvents();
    });