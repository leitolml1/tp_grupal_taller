from django.shortcuts import render, redirect
from .models import videojuego
from .forms import VideojuegoForm
from genero.models import genero
from plataforma.models import plataforma

# Create your views here.

def videojuego_lista(request):
    generos = genero.objects.all()  # Obtén todos los géneros
    juegos = videojuego.objects.all()  # Obtén todos los videojuegos por defecto
    plataformas=plataforma.objects.all()
    return render(request,"videojuegos.html",{
        "generos":generos,
        "juegos":juegos,
        "plataformas":plataformas,
    })
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

def filtrar_genero(request):
    generos = genero.objects.all()  # Obtén todos los géneros
    juegos = videojuego.objects.all()  # Obtén todos los videojuegos por defecto
    plataformas = plataforma.objects.all()  # Obtén todos los géneros

    if request.method == "POST":
        genero_id = request.POST.get('genero')  # Obtén el ID del género seleccionado
        if genero_id and genero_id != "noFiltrar":
        
            juegos=videojuego.objects.filter(genero_id=genero_id)

    context = {
        'plataformas': plataformas,
        'juegos': juegos,
        'generos': generos,
    }
    return render(request, 'videojuegos.html', context)
def filtrar_plataforma(request):
    generos = genero.objects.all()  # Obtén todos los géneros
    plataformas = plataforma.objects.all()  # Obtén todos los géneros
    juegos = videojuego.objects.all()  # Obtén todos los videojuegos por defecto

    if request.method == "POST":
        plataformas_id = request.POST.get('plataforma')  # Obtén el ID del género seleccionado
        if plataformas_id and plataformas_id != "noFiltrar":
        
            juegos=videojuego.objects.filter(plataforma_id=plataformas_id)

    context = {
        'juegos': juegos,
        'generos': generos,
        'plataformas': plataformas,
    }
    return render(request, 'videojuegos.html', context)