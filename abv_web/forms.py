from django import forms
from django.forms import ModelForm
from .models import (
    Marca,
    Categoria,
    Familia,
    ImagenSecundariaProducto,
    Producto,
    Inventario,
    CarrouselBanner,
    Usuario,
    Tienda,
    Servicio,
    Proyecto
)

# --------------------------------------------- CRUD MARCAS ----------------------------------------------------------#
class MarcaForm(forms.ModelForm):
    marca_name = forms.CharField(
        label="Nombre de la Marca",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=30
    )
    marca_url_img = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )
    marca_descripcion = forms.CharField(
        label="Descripción de la marca",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        max_length=2000
    )

    class Meta:
        model = Marca
        fields = ['marca_name', 'marca_url_img', 'marca_descripcion']


# ------------------------------------------ CRUD CATEGORIAS ---------------------------------------------------------#
class CategoriaForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all().order_by('marca_name'),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Marca Asociada",
        required=False
    )
    categoria_name = forms.CharField(
        label="Nombre de la Categoría",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=30
    )
    categoria_url_img = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )
    categoria_descripcion = forms.CharField(
        label="Descripción de la categoría",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        max_length=2000
    )
    statusCategoria = forms.BooleanField(
        label='Activa',
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = Categoria
        fields = ['categoria_name', 'categoria_url_img', 'categoria_descripcion', 'statusCategoria', 'marca']


# ------------------------------------------ CRUD FAMILIAS ---------------------------------------------------------#
class FamiliaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all().order_by('categoria_name'),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Categoría Asociada",
        required=False
    )
    familia_name = forms.CharField(
        label="Nombre de la Familia",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=30
    )
    familia_descripcion = forms.CharField(
        label="Descripción de la familia",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        max_length=2000
    )
    familia_url_img = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )
    statusFamilia = forms.BooleanField(
        label='Activa',
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = Familia
        fields = ['familia_name', 'familia_descripcion', 'familia_url_img', 'statusFamilia', 'categoria']


# ---------------------------------- CRUD IMAGENES SECUNDARIAS ---------------------------------- #
class ImagenSecundariaProductoForm(forms.ModelForm):
    familia = forms.ModelChoiceField(
        queryset=Familia.objects.all().order_by('familia_name'),
        label="Familia Asociada",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    imagen_secundaria = forms.ImageField(
        label="Imagen Secundaria",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )
    
    class Meta:
        model = ImagenSecundariaProducto
        fields = ['familia', 'imagen_secundaria']


# --------------------------------------------- CRUD PRODUCTOS --------------------------------------------------------#
class ProductoForm(forms.ModelForm):
    # Añadido ModelChoiceField para Familia
    familia = forms.ModelChoiceField(
        queryset=Familia.objects.all(),
        label='Familia',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        label='Marca',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        label='Categoría',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Producto
        fields = [
            'producto_extendido', 'producto_sku', 'producto_skunetsuite', 'producto_ean',
            'producto_nombre', 'producto_descripcion', 'producto_modelo',
            'producto_precio_base', 'producto_precio_amazon', 'producto_precio_mercadolibre',
            'producto_precio_ebay', 'producto_url_img', 'familia', 'marca', 'categoria'
        ]
        widgets = {
            'producto_extendido': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_skunetsuite': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_ean': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'producto_modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_precio_base': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto_precio_amazon': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto_precio_mercadolibre': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto_precio_ebay': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto_url_img': forms.FileInput(attrs={'class': 'form-control'}),
        }


# ------------------------------------------ CRUD INVENTARIO --------------------------------------------------------#
class InventarioForm(forms.ModelForm):
    # Asegura que se pueda seleccionar un producto
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all().order_by('producto_nombre'),
        label="Producto",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    stock = forms.IntegerField(
        label="Stock",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Inventario
        fields = ['producto', 'stock']


# ------------------------------------------ CRUD SERVICIOS ----------------------------------------------------------#
class ServicioForm(forms.ModelForm):
    servicio_nombre = forms.CharField(
        label="Titulo del Servicio",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=50
    )
    servicio_descripcion = forms.CharField(
        label="Descripción del Servicio",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        max_length=2000
    )
    servicio_imagen = forms.ImageField(
        label="Imagen descriptiva",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )

    class Meta:
        model = Servicio
        fields = ['servicio_nombre', 'servicio_descripcion', 'servicio_imagen']


# ------------------------------------------ CRUD PROYECTOS ----------------------------------------------------------#
class ProyectoForm(forms.ModelForm):
    proyecto_nombre = forms.CharField(
        label="Título del Proyecto",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=50
    )
    proyecto_descripcion_corta = forms.CharField(
        label="Descripción Corta",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        max_length=500
    )
    proyecto_descripcion_larga = forms.CharField(
        label="Descripción Larga",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 6}),
        max_length=2000
    )
    proyecto_imagen = forms.ImageField(
        label="Imagen del Proyecto",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )

    class Meta:
        model = Proyecto
        fields = [
            "proyecto_nombre",
            "proyecto_descripcion_corta",
            "proyecto_descripcion_larga",
            "proyecto_imagen"
        ]


# ------------------------------------------ CRUD CARROUSELBANNER -----------------------------------------------------#
class CarrouselBannerForm(forms.ModelForm):
    carrouselBanner_name = forms.CharField(
        label="Nombre del Banner",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=30
    )
    carrouselBanner_url_img = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )
    carrouselBanner_descripcion = forms.CharField(
        label="Descripción del Banner",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        max_length=2000
    )

    class Meta:
        model = CarrouselBanner
        fields = ['carrouselBanner_name', 'carrouselBanner_url_img', 'carrouselBanner_descripcion']


# ------------------------------------------ CRUD USUARIOS -----------------------------------------------------------#
class UsuarioForm(forms.ModelForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text='La contraseña debe tener al menos 8 caracteres.'
    )
    is_active = forms.BooleanField(
        label='Activo',
        required=False,
        widget=forms.CheckboxInput()
    )
    is_superuser = forms.BooleanField(
        label='Super Usuario',
        required=False,
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'is_active', 'is_superuser']

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if password and len(password) < 8:
            raise forms.ValidationError(
                'Para mantener la seguridad, la contraseña debe tener al menos 8 caracteres. Ingrese una contraseña válida o repita la existente para mantenerla sin cambios.'
            )
        return password


# ------------------------------------------ CRUD TIENDA ------------------------------------------------------------#
class TiendaForm(forms.ModelForm):
    tienda_enlace = forms.URLField(
        label='Enlace de la tienda',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ejemplo: https://FuseTech.com'
        }),
        help_text='Asegúrate de incluir http:// o https:// al inicio del enlace.'
    )
    tienda_nombre = forms.CharField(
        label='Nombre de la tienda',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ejemplo: FuseTech Componentes'
        }),
        max_length=30
    )
    tienda_descripcion = forms.CharField(
        label='Descripción de la tienda',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ejemplo: Expertos en fusibles, transformadores y circuitos para todo tipo de proyectos eléctricos.'
        }),
        max_length=300
    )
    tienda_imagen = forms.ImageField(
        label='Imagen de la tienda',
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'placeholder': 'Selecciona una imagen representativa de la tienda'
        }),
        help_text='Formato permitido: JPG, PNG. Tamaño máximo: 5MB.'
    )

    class Meta:
        model = Tienda
        fields = [
            'tienda_enlace',
            'tienda_nombre',
            'tienda_descripcion',
            'tienda_imagen'
        ]

    def clean_tienda_enlace(self):
        enlace = self.cleaned_data.get('tienda_enlace', '')
        if enlace and not enlace.startswith(('http://', 'https://')):
            enlace = 'http://' + enlace
        return enlace


# ------------------------------------------ CRUD DESTACADOS ----------------------------------------------------------#
class DestacadoForm(forms.Form):
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label='Selecciona productos destacados'
    )

class cotizacionForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo electrónico'})
    )
    telefono = forms.CharField(
        label='Teléfono',
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu número de teléfono'})
    )
    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'})
    )