from django import forms
from .models import plataforma

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = plataforma
        fields = ('nombre')