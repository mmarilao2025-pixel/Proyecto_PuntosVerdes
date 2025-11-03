from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Producto'

urlpatterns = [
    path("obtener/", views.obtener_todo, name="obtener_Productos"),
    path('',views.inicio, name='inicio'),
]
