from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Marca(models.Model):
	marca_name = models.CharField(max_length=100)
	marca_url_img = models.ImageField(upload_to="Imagenes_Marca", null=True)
	status = models.BooleanField(default=True)
	marca_descripcion = models.CharField(max_length=300)

	def __str__(self):
		return self.marca_name

class Categoria(models.Model):
	categoria_name = models.CharField(max_length=100)
	categoria_descripcion = models.CharField(max_length=300)
	categoria_url_img = models.ImageField(upload_to="Imagenes_Categoria", null=True)
	statusCategoria = models.BooleanField(default=True)
	categoria_prioridad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	# --- CAMBIO IMPORTANTE: ForeignKey para relación Uno-a-Muchos ---
	# Cada Categoria tendrá UNA Marca. Una Marca puede tener MUCHAS Categorias.
	marca = models.ForeignKey(
		Marca,
		on_delete=models.CASCADE, # Si se elimina una Marca, se eliminan sus Categorias asociadas
		null=True, # Permite que una Categoría no tenga una Marca asignada (opcional)
		blank=True, # Permite que el campo sea opcional en formularios
		related_name='categorias_asociadas' # Nombre inverso para acceder desde Marca a sus Categorias
	)

	def __str__(self):
		if self.marca:
			return f"{self.categoria_name} - {self.marca.marca_name}"
		return self.categoria_name

class Familia(models.Model):
	familia_name = models.CharField(max_length=100)
	familia_descripcion = models.CharField(max_length=2000)
	familia_url_img = models.ImageField(upload_to="Imagenes_Familia", null=True)
	statusFamilia = models.BooleanField(default=True)
	# --- CAMBIO IMPORTANTE: ForeignKey para relación Uno-a-Muchos ---
	# Cada Categoria tendrá UNA Marca. Una Marca puede tener MUCHAS Categorias.
	categoria = models.ForeignKey(
		Categoria,
		on_delete=models.CASCADE, # Si se elimina una Marca, se eliminan sus Categorias asociadas
		null=True, # Permite que una Categoría no tenga una Marca asignada (opcional)
		blank=True, # Permite que el campo sea opcional en formularios
		related_name='familias_asociadas' # Nombre inverso para acceder desde Marca a sus Categorias
	)

	def __str__(self):
		return self.familia_name

class ImagenSecundariaProducto(models.Model):
	familia = models.ForeignKey(Familia, on_delete=models.CASCADE,default=1)
	imagen_secundaria = models.ImageField(upload_to="Imagenes_Producto_Secundarias", null=True)

class Producto(models.Model):
    producto_extendido = models.CharField(max_length=30, null=True)
    producto_sku = models.CharField(max_length=30, null=True)
    producto_skunetsuite = models.CharField(max_length=300, default='')
    producto_ean = models.CharField(max_length=30 , null=True)
    producto_nombre = models.CharField(max_length=100, null=True)
    producto_descripcion = models.TextField(max_length=300, null=True, blank=True)
    producto_modelo = models.CharField(max_length=30, null=True, blank=True)
    producto_precio_base = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    producto_precio_amazon = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    producto_precio_mercadolibre = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    producto_precio_ebay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    producto_url_img = models.ImageField(upload_to="Imagenes_Producto", null=True)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.producto_nombre)


class Inventario(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	fecha_modificacion = models.DateTimeField(null=True, blank=True)
	stock = models.IntegerField(default=0)

	def clean(self):
		from django.core.exceptions import ValidationError
		if self.stock < 0:
			raise ValidationError("El stock no puede ser menor a 0.")

#------------------------------------------Publico-------------------------------------------------------
class Servicio(models.Model):
	servicio_nombre = models.CharField(max_length=50)
	servicio_descripcion = models.TextField(max_length=500)
	servicio_imagen = models.ImageField(upload_to="Imagenes_Servicio", null=True)

class Proyecto(models.Model):
	proyecto_nombre = models.CharField(max_length=50)
	proyecto_descripcion_corta = models.TextField(max_length=500)
	proyecto_descripcion_larga = models. TextField(max_length=2000)
	proyecto_imagen = models.ImageField(upload_to="Imagenes_Proyecto", null=True)
	proyecto_imagen_banner = models.ImageField(upload_to="Imagenes_Proyecto", null=True)

class ProyectoDestacado(models.Model):
	proyecto = models.OneToOneField(
		Proyecto,
		on_delete=models.CASCADE,
		related_name='featured_entry'
	)

	def __str__(self):
		return str(self.proyecto)

class ProductoDestacado(models.Model):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name='featured_entry'
    )

    def __str__(self):
        return str(self.producto)

class CarrouselBanner(models.Model):
	carrouselBanner_name = models.CharField(max_length=30)
	carrouselBanner_descripcion = models.CharField(max_length=300)
	carrouselBanner_url_img = models.ImageField(upload_to="Imagenes_CarrouselBanner", null=True)
	statusBanner = models.BooleanField(default=True)

class Usuario(User):
	"""Proxy model para el modelo User de Django, funciona como una extensión del modelo User"""
	class Meta:
		proxy = True
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

class Tienda(models.Model):
    tienda_enlace = models.URLField()
    tienda_nombre = models.CharField(max_length=30)
    tienda_descripcion = models.TextField(max_length=300)
    tienda_imagen = models.ImageField(upload_to='Imagenes_Tienda/')
