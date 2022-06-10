from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myHoneView(*args, **kwargs):
    return HttpResponse('<hl>Hola Mundo desde Dlango</hi>')
def anotherView(request):
    return HttpResponse('<hl>Solo es otra pagina desde Dlango</hi>')
def testView(request):
    return HttpResponse("Probando mas vistas!")
