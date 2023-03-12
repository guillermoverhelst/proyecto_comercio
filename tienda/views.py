from django.http import HttpResponse
from django.shortcuts import render
from tienda.models import usuario, producto
from tienda.forms import UsuarioForm
def productos(request):
    productos = producto.objects.all()
    return render(request, "productos.html",{"producto":productos})

def registro(request):
    formulario = {'form': UsuarioForm()}
    if request.method == 'POST':
        datos = UsuarioForm(data = request.POST)
        if datos.is_valid():
            datos.save()
        
    return render(request, "registro.html",formulario)
    
def plt_inicio_sesion(request):
    return render(request,"inicio_sesion.html")