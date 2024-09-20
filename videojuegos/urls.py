from django.urls import path
from . import views

urlpatterns = [
    path('',views.videojuego_lista, name="videojuego"),
    path('agregar_videojuego/', views.agregar_videojuego, name='agregar_videojuego'),
    path('filtrar_genero',views.filtrar_genero,name="filtrar_genero"),
    path('filtrar_plataforma',views.filtrar_plataforma,name="filtrar_plataforma"),

]
