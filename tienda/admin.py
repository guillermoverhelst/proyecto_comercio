from django.contrib import admin
from tienda.models import usuario,producto
# Register your models here.

class usuario_admin(admin.ModelAdmin):
    list_display=("nombre","correo","clave")
    search_fields=("nombre","correo")

class producto_admin(admin.ModelAdmin):
    list_display=("sku","nombre","unidades_disponibles","precio_unitario")
    search_fields=("sku","nombre","unidades_disponibles","precio_unitario")

admin.site.register(usuario,usuario_admin)
admin.site.register(producto,producto_admin) 