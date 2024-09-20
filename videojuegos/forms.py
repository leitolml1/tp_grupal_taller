from django import forms
from .models import videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = videojuego
        fields = ['titulo','plataforma','genero','stock']
            