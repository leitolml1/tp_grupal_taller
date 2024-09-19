from django.db import models

# Create your models here.

class genero(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)