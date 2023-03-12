from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    clave = models.CharField(max_length=20)  
    
    def agregar_producto_a_carrito(producto,cantidad):
        pass

class producto(models.Model):   
    sku = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    unidades_disponibles = models.IntegerField()
    precio_unitario = models.FloatField()
    
    def hay_unidades(unidades_disponibles):
        return True if unidades_disponibles > 0 else False