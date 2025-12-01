"""
URL configuration for ABV_ELECTRIC_SUPPLY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from abv_web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
# --------------------------------------url de administración-------------------------------------------------
    # URLs para autenticación y acceso al dashboard
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # URLs para gestión de marcas
    path('marcas/', views.marcas, name='marcas'),
    path('marcas/eliminar/<int:marca_id>/', views.eliminar_marca, name='eliminar_marca'),
    path('marcas/editar/<int:marca_id>/', views.editar_marca, name='editar_marca'),
    path('marcas/restaurar/<int:marca_id>/', views.restaurar_marca, name='restaurar_marca'),

    # URLs para gestión de categorías
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/eliminar/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/restaurar/<int:categoria_id>/', views.restaurar_categoria, name='restaurar_categoria'),

    # ------------------ NUEVAS URLs para gestión de familias ------------------
    path('familias/', views.familias, name='familias'),
    path('familias/eliminar/<int:familia_id>/', views.eliminar_familia, name='eliminar_familia'),
    path('familias/editar/<int:familia_id>/', views.editar_familia, name='editar_familia'),
    path('familias/restaurar/<int:familia_id>/', views.restaurar_familia, name='restaurar_familia'),

    # ------------------ NUEVAS URLs para gestión de imágenes secundarias ------------------
    path('imagenes_secundarias/', views.imagenes_secundarias, name='imagenes_secundarias'),
    path('imagenes_secundarias/eliminar/<int:imagen_id>/', views.eliminar_imagen_secundaria, name='eliminar_imagen_secundaria'),
    path('imagenes_secundarias/editar/<int:imagen_id>/', views.editar_imagen_secundaria, name='editar_imagen_secundaria'),
    
    # URLs para gestión de carrouselBanner
    path('carrouselBanner/', views.carrouselBanner, name='carrouselBanner'),
    path('carrouselBanner/eliminar/<int:carrouselBanner_id>/', views.eliminar_carrouselBanner, name='eliminar_carrouselBanner'),
    path('carrouselBanner/editar/<int:carrouselBanner_id>/', views.editar_carrouselBanner, name='editar_carrouselBanner'),

    # URLs para gestión de usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # URLs para gestión de tiendas
    path('tiendas/', views.tiendas, name='tiendas'),
    path('tiendas/editar/<int:tienda_id>/', views.editar_tienda, name='editar_tienda'),
    path('tiendas/eliminar/<int:tienda_id>/', views.eliminar_tienda, name='eliminar_tienda'),

    # URLS para CRUD de Productos
    path('productos/', views.productos, name='productos'),
    path('producto/ver/<int:producto_id>/', views.ver_producto, name='ver_producto'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('ajax/get_categorias_por_marca/', views.get_categorias_por_marca, name='get_categorias_por_marca'),
    path('ajax/get_familias_por_categoria/', views.get_familias_por_categoria, name='get_familias_por_categoria'),

    # URLs para Productos Destacados
    path('productos/destacados/', views.productos_destacados, name='productos_destacados'),
    path('productos_destacados/agregar/', views.agregar_destacado, name='agregar_destacado'),
    path('productos_destacados/eliminar/<int:destacado_id>/', views.eliminar_destacado, name='eliminar_destacado'),

    # URLs para CRUD de Servicios
    path('servicios/', views.servicios, name='servicios'),
    path('servicios/editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('servicios/eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),

    # URLs para CRUD de Proyectos
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyectos/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    
    # URLs para Proyectos Destacados
    path('proyectos_destacados/', views.proyectos_destacados, name='proyectos_destacados'),
    path('proyectos_destacados/agregar/', views.agregar_proyecto_destacado, name='agregar_proyecto_destacado'),
    path('proyectos_destacados/eliminar/<int:destacado_id>/', views.eliminar_proyecto_destacado, name='eliminar_proyecto_destacado'),

    # URLs para CRUD de Inventario
    path('agregar_inventario/<int:producto_id>/', views.agregar_inventario, name='agregar_inventario'),
    path('modificar_stock/<int:inventario_id>/', views.modificar_stock, name='modificar_stock'),

    # URLs para plantillas
    path('plantillas/', views.plantillas, name='plantillas'),
    path('plantillas/download/<str:template_slug>/', views.download_template, name='download_template'),

    # URLs para cargas masivas
    path('imports/', views.dashboard_carga, name='dashboard_carga'),
    path('imports/<str:model_slug>/', views.import_excel, name='import_excel'),
    path('upload-images/', views.upload_images, name='upload_images'),

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------url de publico--------------------------------------------------------
    path('', views.home, name='home'),
    path('about_us', views.about, name='about'),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('services/', views.services, name ='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
    path('products/marca/<str:Nmarca>/', views.categorias_marca, name='products2'),
    path('products/categoria/<str:Ncate>/', views.familias_categoria, name='products3'),
    path('products/categoria/familia/<str:Nfamilia>/', views.familia, name='products4'),
    path('product/<str:sku>/', views.product, name='product'),
    path('store/', views.store, name='store'),
    #path('products/', views.store, name='products'),
    #path('store/', views.products, name='store'),
    path('search/', views.search_products, name='navbar_search'),
    path('tableros/', views.tableros_diag, name='tableros'),
    path('cotizacion/', views.cotizacion, name='cotizacion'), 

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)