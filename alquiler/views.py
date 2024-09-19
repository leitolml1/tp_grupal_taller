from django.shortcuts import render,redirect
from .models import alquiler
from .forms import FormAlquiler
# Create your views here.

def alquileres(request):
    alquileres=alquiler.objects.all()
    return render(request,"alquileres.html",{
        "alquileres":alquileres
    })

def crear_alquiler(request):
    if request.method=="POST":
        form_nuevo_alquiler=FormAlquiler(request.POST)
        if form_nuevo_alquiler.is_valid():
            nuevo_alquiler=form_nuevo_alquiler.save(commit=False)
            nuevo_alquiler.save()
            return redirect("alquileres")

    else:
        return render(request,"crear_alquiler.html",{
            "form":FormAlquiler()
        })