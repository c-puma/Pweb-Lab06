from django.db import models

# Create your models here.
class Persona(models.Model):
nombre = models.CharField(nax_length = 100)
apellidos = models.CharField(nax_Length = 100)
edad = models.IntegerField()