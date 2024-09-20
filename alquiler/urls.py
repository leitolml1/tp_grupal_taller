from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.alquileres,name="alquileres"),
    path("crear_alquiler/",views.crear_alquiler,name="crear_alquiler"),
    path("concretar_alquilar/<int:id>",views.concretar_alquilar,name="concretar_alquilar",)

]
