from django import forms
from .models import alquiler  # Asegúrate de que el nombre del modelo esté en mayúscula

class FormAlquiler(forms.ModelForm):
    fecha_alquiler = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))#en ambos le determino que el input sea de tipo  fecha
    fecha_devolucion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))#por que si no, solo sale un entry xd
    class Meta:
        model = alquiler  # Asegúrate de que el nombre del modelo esté en mayúscula
        fields = ["cliente", "videojuego", "fecha_alquiler", "fecha_devolucion"]
