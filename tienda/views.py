from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from tienda.models import usuario, producto
from tienda.forms import UsuarioForm,InicioSesionForm
import json

global productos_carrito

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
    formulario = {'form': InicioSesionForm()}
    usuarios = usuario.objects.all() 
    if request.method == 'POST':
        datos = InicioSesionForm(data = request.POST)
        if datos.is_valid():
            correo = datos.cleaned_data['correo']
            clave = datos.cleaned_data['clave']
            for i in usuarios:
                if correo == i.correo and clave == i.clave:
                    return redirect(to = 'productos')
               
    return render(request,"inicio_sesion.html",formulario)


def agregar_a_carrito(request):
    global productos_carrito
    if request.method == 'POST':
        json_data = request.POST.get('data')
        lista_diccionarios = json.loads(json_data)

        if 'productos_carrito' in globals():
            print("1")
            for i in lista_diccionarios:
                
                diccionario_buscado = next((diccionario for diccionario in productos_carrito if dict(diccionario)['sku'] == i['sku']), None)
                
                if diccionario_buscado:
                    diccionario_buscado['cantidad'] = int(diccionario_buscado['cantidad']) + int(i['cantidad'])
                else:
                    productos_carrito.append(i)
                    
        else:
            print("2")
            productos_carrito = lista_diccionarios        

        for i in productos_carrito:
            print(i)

        return JsonResponse({'status': 'ok', 'url': "/mostrar_carrito/"})

def mostrar_carrito(request):

    productos = producto.objects.all()
    productos_EA = []; productos_WE = []; productos_SP = []
    for j in productos_carrito:
        for i in productos:
            if "EA" in i.sku and i.sku == j['sku']:
                i.unidades_disponibles = j['cantidad']
                productos_EA.append(i)

            if "WE" in i.sku and i.sku == j['sku']:
                i.unidades_disponibles = j['cantidad']
                productos_WE.append(i)
        
            if "SP" in i.sku and i.sku == j['sku']:
                i.unidades_disponibles = j['cantidad']
                productos_SP.append(i)

    return render(request, "carrito.html",{"producto_EA":productos_EA, "producto_WE":productos_WE, "producto_SP":productos_SP})
    