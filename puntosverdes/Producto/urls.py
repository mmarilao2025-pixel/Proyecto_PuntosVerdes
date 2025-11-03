from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("obtener/", views.obtener_todo, name="obtener_producto"),
    path('',views.inicio, name='inicio'),
]
