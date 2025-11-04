from django.shortcuts import render, HttpResponse
from urllib import request
from .models import Producto


def obtener_todo(request):
    productos = Producto.objects.all()
    context = {"nombre": "Pan",
               "cantidad": 1
               }
    return render(request, 'productos/obtener_producto.html', 
                  {'productos': productos})

def inicio(request):
    return render(request, 'productos/inicio.html')