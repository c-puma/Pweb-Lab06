from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 100, blank = False)
    apellidos = models.CharField(max_length = 100, blank = True)
    edad = models.IntegerField()
    donador = models.BooleanField(default = True)