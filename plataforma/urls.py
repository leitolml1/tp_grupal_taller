from django.urls import path
from . import views

urlpatterns = [
    path('',views.plataforma_lista, name="plataforma"),
    path('agregar_plataforma/', views.agregar_plataforma, name='agregar_plataforma'),
]
