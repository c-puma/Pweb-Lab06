from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Animal(models.Model):
    nombres = models.TextField()
    edad = models.IntegerField()
    salvaje = models.BooleanField()
