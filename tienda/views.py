from django.http import JsonResponse
from django.shortcuts import render, redirect
from tienda.models import usuario, producto
from tienda.forms import UsuarioForm, InicioSesionForm
from tienda import functions as f
import json

global productos_carrito

def llenar_producto():
    producto.objects.all().delete()
    with open('tienda/archivos/productos.json','r') as f:
        jsonproductos = json.load(f)
    for i in jsonproductos:
        produc, created = producto.objects.get_or_create(
            sku=i["sku"],
            defaults={
                "nombre": i["nombre"],
                "descripcion": i["descripcion"],
                "unidades_disponibles": i["unidades_disponibles"],
                "precio_unitario": i["precio_unitario"]
            }
        )       

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

def productos(request):
    llenar_producto()
    productos = producto.objects.all()
    productos_EA = []; productos_WE = []; productos_SP = []
    for i in productos:
        if "EA" in i.sku:
            productos_EA.append(i)

        if "WE" in i.sku:
            productos_WE.append(i)
        
        if "SP" in i.sku:
            productos_SP.append(i)

    if 'productos_carrito' in globals():
        for i in productos_carrito:
            for j in productos_EA:
                if j.sku == i['sku']:
                    j.unidades_disponibles -= i['cantidad']
                    j.color = "red" if i['cantidad'] != 0 else ""

            for k in productos_WE:
                if k.sku == i['sku']:
                    k.unidades_disponibles -= (i['cantidad']/1000)
                    k.color = "red" if i['cantidad'] != 0 else ""

            for z in productos_SP:
                if z.sku == i['sku']:
                    z.unidades_disponibles -= i['cantidad']
                    z.color = "red" if i['cantidad'] != 0 else ""
                    
    return render(request, "productos.html",{"producto_EA":productos_EA, "producto_WE":productos_WE, "producto_SP":productos_SP})

def agregar_a_carrito(request):
    global productos_carrito
    if request.method == 'POST':
        json_data = request.POST.get('data')
        lista_diccionarios = json.loads(json_data)

        if 'productos_carrito' in globals():
            for i in lista_diccionarios:
                
                diccionario_buscado = next((diccionario for diccionario in productos_carrito if dict(diccionario)['sku'] == i['sku']), None)
                
                if diccionario_buscado:
                    diccionario_buscado['cantidad'] = int(diccionario_buscado['cantidad']) + int(i['cantidad'])
                else:
                    productos_carrito.append(i) 
        else:
            productos_carrito = lista_diccionarios

        productos_carrito = f.limpiar_lista(productos_carrito)          

        return JsonResponse({'status': 'ok', 'url': "/mostrar_carrito/"})

def mostrar_carrito(request):
    total = 0
    productos = producto.objects.all()
    productos_EA = []; productos_WE = []; productos_SP = []
    for j in productos_carrito:
        for i in productos:
            if "EA" in i.sku and i.sku == j['sku']:
                i.unidades_disponibles = j['cantidad']
                i.valor = i.precio_unitario * j['cantidad']
                total += i.valor
                productos_EA.append(i)

            if "WE" in i.sku and i.sku == j['sku']:
                i.unidades_disponibles = j['cantidad']
                i.valor = i.precio_unitario * j['cantidad']
                total += i.valor
                productos_WE.append(i)
        
            if "SP" in i.sku and i.sku == j['sku']:
                i.unidades_disponibles = j['cantidad']
                if (j['cantidad'] < 3):
                    i.valor = i.precio_unitario * j['cantidad']
                else:
                    if (j['cantidad'] < 6):
                        i.valor = (i.precio_unitario * j['cantidad']) - ((i.precio_unitario * j['cantidad'])* 0.2)
                    else:
                        if(j['cantidad'] < 9):
                            i.valor = (i.precio_unitario * j['cantidad']) - ((i.precio_unitario * j['cantidad'])* 0.4)
                        else:
                            i.valor = (i.precio_unitario * j['cantidad']) - ((i.precio_unitario * j['cantidad'])* 0.5)

                total += i.valor
                productos_SP.append(i)

    return render(request, "carrito.html",{"producto_EA":productos_EA, "producto_WE":productos_WE, "producto_SP":productos_SP, "total":f.valor_moneda(total)})

def eliminar_de_carrito(request):
    global productos_carrito
    if request.method == 'POST':
        json_data = request.POST.get('data')
        lista_diccionarios = json.loads(json_data)

        productos_carrito = f.eliminar_elementos_carrito(lista_diccionarios, productos_carrito)

        return JsonResponse({'status': 'ok', 'url': "/productos/"})
    
def pagar_carrito(request):
    global productos_carrito
    objeto_restar_stock = 0

    if request.method == 'POST':
        json_data = request.POST.get('data')
        valor = request.POST.get('valor')
        lista_diccionarios = json.loads(json_data)
        productos_carrito = f.limpiar_lista(productos_carrito)

        productos_carrito = f.eliminar_elementos_carrito(lista_diccionarios, productos_carrito)

        for i in productos_carrito:
            objeto_restar_stock = producto.objects.get(sku=i['sku'])
            objeto_restar_stock.unidades_disponibles -= (i['cantidad']/1000) if ("WE") in i['sku'] else i['cantidad']
            
            objeto_restar_stock.save()

        del(productos_carrito)

        f.actualizar_json()
        f.actualizar_total_tienda(int((valor.split(":")[1][2:]).replace(",", "")))

        return JsonResponse({'status': 'ok', 'url': "/productos/"})