from django import forms
from .models import videojuego

class videojuegoForm(forms.ModelForm):
    class Meta:
        models = videojuego
        fiels = ('titulo','plataforma','genero','stock')
            