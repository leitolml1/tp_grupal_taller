from django.shortcuts import render

# Create your views here.

def videojuegos(request):
    return render(request,"videojuegos.html",{
        
    })