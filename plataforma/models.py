from django.db import models

# Create your models here.}
class plataforma(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)