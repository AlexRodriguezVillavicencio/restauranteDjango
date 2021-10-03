from django.shortcuts import render
from .models import Producto, Categoria


def inicio(request):
    categorias = Categoria.objects.filter(estado = True)
    return render(request, "apprestaurante/index.html", {'categorias': categorias})

def categoria(request, slug):
    categorias = Categoria.objects.filter(estado = True)
    objCategoria = Categoria.objects.get(slug=slug)
    context = {
        'categorias': categorias,
        'categoria':objCategoria
    }
    return render(request, "apprestaurante/catalogoProductos.html",context)


def producto(request, slug):
    categorias = Categoria.objects.filter(estado = True)
    objProducto = Producto.objects.get(slug=slug)
    context = {
        'categorias': categorias,
        'producto':objProducto
    }
    return render(request, "apprestaurante/producto.html", context)
