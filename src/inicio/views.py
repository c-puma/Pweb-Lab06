from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myHoneView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<hl>Hola mundo desde Dlango</hi>')

def anotherView(request):
    return HttpResponse('<hl>Solo es otra pagina desde Dlango</hi>')
def testView(request):
    return HttpResponse("Probando mas vistas!")
