from django.http import HttpResponse
from django.template import Template,Context,loader

def productos(request):
    documento = loader.get_template('productos.html')
    documento = documento.render()
    return HttpResponse(documento)

def registro(request):
    documento = loader.get_template('registro.html')
    documento = documento.render()
    return HttpResponse(documento)

def inicio_sesion(request):
    documento = loader.get_template('inicio_sesion.html')
    documento = documento.render()
    return HttpResponse(documento)