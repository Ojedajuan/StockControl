# forms.py

from django import forms
from .models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['id','nombre', 'apellido', 'dni','mail_contacto']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id','nombre', 'precio', 'stock_actual', 'proveedor', 'descripcion']
