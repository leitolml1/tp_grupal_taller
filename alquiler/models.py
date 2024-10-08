from django.db import models
from videojuegos.models import videojuego
# Create your models here.
class alquiler(models.Model):
    id=models.IntegerField(primary_key=True)
    cliente=models.CharField(max_length=100)
    videojuego=models.ForeignKey(videojuego,on_delete=models.CASCADE)
    fecha_alquiler=models.DateTimeField()
    fecha_devolucion=models.DateTimeField(null=True,blank=True)
    estado=models.CharField(max_length=100,null=True,default="Sin estado")