from EntidadNombrable import EntidadNombrable
from Producto import Producto
class Restaurante:

    def __init__(self, nombre_comercial, direccion_fisica, catalogo=None):
        super().__init__(nombre_comercial)
        self._direccion_fisica = direccion_fisica

        if catalogo is None:
            self._catalogo = []
        else:
            self._catalogo = catalogo
        
    def get_nombre_comercial(self):
        return super().get_nombre()

    def get_direccion_fisica(self):
        return self._direccion_fisica
    
    def get_catalogo(self):
        return self._catalogo

    def dar_alta_producto(self, producto):
        self._catalogo.append(producto)

    def ver_menu_restaurante(self):

        print(f"\n--- Menú de {self.get_nombre_comercial()} ---")
    
        if not self._catalogo:
            print("El catálogo está vacío.")
            return

        for i, producto in enumerate(self._catalogo):

            nombre = producto.get_nombre()
            precio = producto.get_precio()
            categoria = producto.get_categoria()
        
            print(f"[{i + 1}] {nombre} ({categoria}) - ${precio:.2f}")
    
        print("---------------------------------------")
