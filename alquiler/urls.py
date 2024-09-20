from django.urls import path
from . import views
urlpatterns = [
    path("",views.alquileres,name="alquileres"),
    path("crear_alquiler/",views.crear_alquiler,name="crear_alquiler"),

]
