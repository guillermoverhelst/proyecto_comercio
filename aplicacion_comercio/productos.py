class producto:

    def __init__(self,sku,nombre,descripcion,unidades_disponible,precio_unitario):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.unidades_disponible = unidades_disponible
        self.precio_unitario = precio_unitario
    
    def hay_unidades(unidades_disponibles):
        return True if unidades_disponibles > 0 else False