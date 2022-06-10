from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myHoneView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def anotherView(request):
    return render(request, "otroTemplate.html")
def testView(request):
    return HttpResponse("Probando mas vistas!")
