class Producto:
    def __init__(self, nombre, precio, categoria):
        self._nombre = nombre
        self._precio = precio
        self._categoria = categoria
        
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_categoria(self):
        return self._categoria
