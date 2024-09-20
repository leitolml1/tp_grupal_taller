from django.db import models
from plataforma.models import plataforma
from genero.models import genero

# Create your models here.
class videojuego(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=200)
    plataforma = models.ForeignKey(plataforma,on_delete=models.CASCADE)
    genero = models.ForeignKey(genero,on_delete=models.CASCADE)
    stock = models.IntegerField() #ver esto
    