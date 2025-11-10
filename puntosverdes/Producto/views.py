from django.shortcuts import render, HttpResponse
from urllib import request
from .models import Producto
from django.shortcuts import get_object_or_404


def obtener_todo(request):
    productos = Producto.objects.all()
    context = {"nombre": "Pan",
               "cantidad": 1
               }
    return render(request, 'productos/obtener_producto.html', 
                  {'productos': productos})

def inicio(request):
    return render(request, 'productos/inicio.html')

def porId(request, id):
   # print(id)
   # producto = Producto.object.get (id=id)
    producto = get_object_or_404(Producto, id=id)  
    context = {'producto':producto}
    return render(request, 'productos/obtener_producto.html', context)
    