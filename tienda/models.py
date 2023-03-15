from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    clave = models.CharField(max_length=20)  
    
    def __str__(self):
        return self.nombre 

class producto(models.Model):   
    sku = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    unidades_disponibles = models.FloatField()
    precio_unitario = models.FloatField()
    
    def __str__(self):
        return self.nombre
    def hay_unidades(unidades_disponibles):
        return True if unidades_disponibles > 0 else False