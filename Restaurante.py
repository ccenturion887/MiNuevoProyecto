from Producto import Producto
class Restaurante:
    # Constructor: Los atributos de la instancia (self._X) son privados
    def __init__(self, nombre_comercial, direccion_fisica, catalogo):
        self._nombre_comercial = nombre_comercial
        self._direccion_fisica = direccion_fisica
        self._catalogo = catalogo # Lista de objetos Producto
        

    # Getter para el nombre (Accede a la versión privada)
    def get_nombre_comercial(self):
        return self._nombre_comercial

    # Getter para la dirección física (Accede a la versión privada)
    def get_direccion_fisica(self):
        return self._direccion_fisica
    
    # Getter para el Catálogo (Coherencia y Accede a la versión privada)
    def get_catalogo(self):
        return self._catalogo
    
    # Método de ABSTRACCIÓN clave para gestionar el catálogo
    def dar_alta_producto(self, producto):
        self._catalogo.append(producto)

