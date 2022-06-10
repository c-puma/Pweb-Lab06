from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myHoneView(*args, **kwargs):
    return HttpResponse('<hl>Hola Mundo desde Dlango</hi>')