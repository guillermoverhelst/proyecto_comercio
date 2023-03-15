from django.core.serializers.json import DjangoJSONEncoder
from tienda.models import producto
import json
import pandas as pd
from io import StringIO

def valor_moneda(valor):
    valor = list(str(int(valor))[::-1])
    nuevo_valor = ""
    
    nuevo_valor = ''.join([valor[i] + ',' if (i+1) % 3 == 0 and i != len(valor)-1 else valor[i] for i in range(len(valor))])
    nuevo_valor = (nuevo_valor.replace(",", "", 1) if nuevo_valor.startswith(",") else nuevo_valor)

    return '$' + nuevo_valor[::-1]

def limpiar_lista(productos_carrito):
    for i in productos_carrito:
        if i['cantidad'] == 0:
            productos_carrito.remove(i)

    return productos_carrito

def eliminar_elementos_carrito(lista_diccionarios, productos_carrito):
    for i in lista_diccionarios:
        diccionario_buscado = next((diccionario for diccionario in productos_carrito if dict(diccionario)['sku'] == i['sku']), None)
                
        if diccionario_buscado:
            diccionario_buscado['cantidad'] = int(diccionario_buscado['cantidad']) - int(i['cantidad'])

    return productos_carrito

def actualizar_json():
    my_objects = producto.objects.all()
    serialized_objects = serialize_objects(my_objects)
    #serialized_objects = serializers.serialize('json', my_objects, use_natural_foreign_keys=True)
    #deserialized_objects = json.loads(serialized_objects)

    with open(r"C:\Users\LENOVO\Desktop\workspace\tienda_enfasis_r\proyecto_comercio\tienda\archivos\productos.json", 'w') as outfile:
        #json.dump(deserialized_objects, outfile)
        outfile.write(serialized_objects)

def serialize_objects(objs):
    # Crear una lista para almacenar los objetos serializados
    serialized_objects = []
    # Iterar sobre los objetos y agregar solo los datos necesarios
    for obj in objs:
        serialized_objects.append({
            'sku': obj.sku,
            'nombre': obj.nombre,
            'descripcion': obj.descripcion,
            'unidades_disponibles': obj.unidades_disponibles,
            'precio_unitario': obj.precio_unitario,

            # Agregar cualquier otro campo necesario
        })
    # Devolver la lista de objetos serializados como una cadena JSON
    return json.dumps(serialized_objects, cls=DjangoJSONEncoder)

def actualizar_total_tienda(nuevo_total):

    with open('tienda/archivos/total.txt', 'r') as file:
        total = int(file.read())
    
    total += nuevo_total

    with open('tienda/archivos/total.txt', 'w') as file:
        file.write('')
        file.write(str(total))