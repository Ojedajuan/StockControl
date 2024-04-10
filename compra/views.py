# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, ProveedorForm
from .models import Producto
from .models import Proveedor

def agregar_editar_producto(request, id=None):
    if id:
        producto = get_object_or_404(Producto, id=id)
    else:
        producto = None   
    if request.method == 'POST':
    
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos') 
    else:       
        form = ProductoForm(instance=producto)
    return render(request, 'agregar_editar_producto.html', {'form': form})


def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'agregar_editar_producto.html', {'form': form})
