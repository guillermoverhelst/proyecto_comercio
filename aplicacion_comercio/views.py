from django.http import HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render
#from usuarios import usuario
def productos(request):
    return render(request, "productos.html")

def registro(request):
    return render(request, "registro.html")


    
def inicio_sesion(request):
    return render(request,"inicio_sesion.html")