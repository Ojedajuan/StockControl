
from compra import views
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path ('admin/', admin.site.urls),
    path('', views.listar_productos, name='inicio'),  # 
    path('agregar_editar_producto/<int:id>/', views.agregar_editar_producto, name='agregar_editar_producto'),
    path('agregar-proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('listar-proveedores/', views.listar_proveedores, name='listar_proveedores'),
    # Otros patrones de URL
]
