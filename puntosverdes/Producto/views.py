from django.shortcuts import render, HttpResponse, get_object_or_404, redirect # ¡Añadir 'redirect'!
from urllib import request # Aunque no se usa en las vistas mostradas, se mantiene
from .models import Producto 
# La importación de get_object_or_404 se puede remover si ya está arriba


def obtener_todo(request):
    productos = Producto.objects.all()
    context = {"nombre": "Pan",
               "cantidad": 1
               }
    return render(request, 'productos/obtener_producto.html', 
                  {'productos': productos})

def inicio(request):
    return render(request, 'productos/inicio.html')

# ... (otras funciones como obtener_todo e inicio)

def porId(request, id):
    # Usa 'producto' en minúscula
    producto = get_object_or_404(Producto, id=id)  
    context = {'producto': producto}
    return render(request, 'productos/obtener_producto.html', context)

def EliminarId(request, id):
    # Usa 'producto' en minúscula
    producto = get_object_or_404(Producto, id=id) 
    producto.delete()
    # Cambia 'lista_productos' al nombre de la URL que muestra toda la lista.
    # Si quieres que redirija a 'obtener-todo/' que tienes en urls.py, el name es: 'obtener_todo'
    return redirect('obtener_todo') # Asumiendo que 'obtener_todo' es tu lista

def ActualizarId(request, id):
    # Usa 'producto' en minúscula
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.cantidad = request.POST.get('cantidad')
        producto.save()
        
        # Redirige a la vista del producto individual, pasando el ID de la instancia
        # ¡IMPORTANTE!: Usa producto.id, no solo producto
        return redirect('productos_porId', id=producto.id) 
    else:
        context = {'producto': producto}
        # Asegúrate de que esta plantilla exista y tenga el formulario
        return render(request, 'productos/productos_actualizar.html', context) # Cambié el nombre del template para ser más específico
    
def agregarProducto(request):
    # Esta función está incompleta, pero ya no debería causar el error de importación.
    producto = {}