from django.shortcuts import render, redirect
from .models import plataforma
from .forms import PlataformaForm

# Create your views here.

def agregar_plataforma(request):
    plataformas = plataforma.objects.all()
    return render(request,'plataformas.html',{'plataforma': plataformas})

def agregar_plataforma(request):
    if request.method == 'POST':
        form = PlataformaForm()
        if form.is_valid():
            plataforma.save()
            return redirect('plataformas')
    else:
        return render(request,'agregar_plataforma.html',{'form':PlataformaForm})
        