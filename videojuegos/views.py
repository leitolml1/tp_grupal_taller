from django.shortcuts import render, redirect
from .models import videojuego
from .forms import videojuegoform

# Create your views here.

def videojuego_lista(request):
    juegos = videojuego.objects.all()
    return render(request, 'videojuegos.html', {'juegos': juegos})

def agregar_videojuego(request):
    if request.method == 'POST':
        form = videojuegoform(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('videojuegos')
    else:
        form = videojuegoform()
    return render(request,'videojuego/agregar_videojuego.html',{'form': form})
        
