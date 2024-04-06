"""
URL configuration for StockControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from compra import views


urlpatterns = [
    path('', views.listar_productos, name='inicio'), 
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    path('listar-proveedores/', views.listar_proveedores, name='listar_proveedores'),
]