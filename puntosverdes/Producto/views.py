from django.shortcuts import render, HttpResponse
from urllib import request
from .models import Producto

def Producto(request):
    return HttpResponse('<h1>Hola Mundo/</h1>')

def obtener_todo(request):
    productos = []
    context = {"nombre": "Pan",
               "cantidad": 1
               }
    return render(request, 'productos/obtener_producto.html')

def inicio(request):
    return render(request, 'productos/inicio.html')