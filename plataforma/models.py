from django.db import models

# Create your models here.
id = models.IntegerField(primary_key=True)
nombre = models.CharField(max_length=200)