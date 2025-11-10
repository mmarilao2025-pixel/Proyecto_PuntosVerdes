from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('obtener-todo/', views.obtener_todo, name='obtener_todo'),
    path('obtener/<int:id>')
]