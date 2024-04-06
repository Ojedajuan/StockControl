from django.contrib import admin
from .models import Producto, Proveedor
class ProductoAdmin(admin.ModelAdmin):
    list_display=['id', 'nombre', 'precio','categoria',  'color', 'stock_actual','proveedor' ]
    search_fields=['id', 'nombre', 'precio', 'color', 'stock_actual','proveedor' ]
class ProveedorAdmin(admin.ModelAdmin):
    list_display=['id', 'nombre','apellido', 'dni']
    search_fields=['id', 'nombre','apellido', 'dni', 'mail_contacto']
admin.site.register(Producto)
admin.site.register(Proveedor)
