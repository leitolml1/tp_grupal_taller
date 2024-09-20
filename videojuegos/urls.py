from django.urls import path
from . import views

urlpatterns = [
    path('',views.videojuego_lista, name="videojuego"),
    path('agregar_videojuego/', views.agregar_videojuego, name='agregar_videojuego'),
]
