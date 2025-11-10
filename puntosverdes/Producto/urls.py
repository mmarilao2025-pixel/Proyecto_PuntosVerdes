from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('obtener-todo/', views.obtener_todo, name='obtener_todo'), 
    path('obtener-todo/<int:id>/', views.porId, name='productos_porId'),
    path('eliminar/<int:id>/', views.EliminarId, name='productos_eliminar'),
    path('actualizar/<int:id>/', views.ActualizarId, name='productos_actualizar')
]