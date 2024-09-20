from django.shortcuts import render,redirect,get_object_or_404
from .models import alquiler
from .forms import FormAlquiler
from videojuegos.models import videojuego
# Create your views here.

def alquileres(request):
    alquileres=alquiler.objects.all()
    return render(request,"alquileres.html",{
        "alquileres":alquileres,
    })

def crear_alquiler(request):
    if request.method=="POST":
        form_nuevo_alquiler=FormAlquiler(request.POST)
        if form_nuevo_alquiler.is_valid():
            nuevo_alquiler=form_nuevo_alquiler.save(commit=False)
            nuevo_alquiler.estado="Alquilado"
            nuevo_alquiler.save()
            nuevo_alquiler.videojuego.stock-= 1
            nuevo_alquiler.videojuego.save()
            return redirect("alquileres")

    else:
        return render(request,"crear_alquiler.html",{
            "form":FormAlquiler()
        })
def concretar_alquilar(request,id):
    alquilerr=get_object_or_404(alquiler,id=id)
    if request.method=="POST":
        print("HOLA")
        alquilerr.estado="Concretado"
        alquilerr.videojuego.stock +=1

        alquilerr.videojuego.save()
        alquilerr.save()
        return redirect("alquileres")
