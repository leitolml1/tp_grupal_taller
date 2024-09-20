from django.shortcuts import render, redirect
from .models import videojuego
from .forms import VideojuegoForm

# Create your views here.

def videojuego_lista(request):
    juegos = videojuego.objects.all()
    return render(request, 'videojuegos.html', {'juegos': juegos})

def agregar_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('videojuegos')
    else:
        return render(request,"agregar_videojuego.html",{
            "form":VideojuegoForm()
        })

