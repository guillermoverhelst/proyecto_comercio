from django.http import HttpResponse
from django.shortcuts import render
from tienda.models import usuario, producto
from tienda.forms import UsuarioForm

def productos(request):
    productos = producto.objects.all()
    productos_EA = []; productos_WE = []; productos_SP = []
    for i in productos:
        if "EA" in i.sku:
            productos_EA.append(i)

        if "WE" in i.sku:
            productos_WE.append(i)
        
        if "SP" in i.sku:
            productos_SP.append(i)

    return render(request, "productos.html",{"producto_EA":productos_EA, "producto_WE":productos_WE, "producto_SP":productos_SP})

def registro(request):
    formulario = {'form': UsuarioForm()}
    if request.method == 'POST':
        datos = UsuarioForm(data = request.POST)
        if datos.is_valid():
            datos.save()
        
    return render(request, "registro.html",formulario)
    
def plt_inicio_sesion(request):
    return render(request,"inicio_sesion.html")

def carrito(request):
    return render(request, "carrito.html")