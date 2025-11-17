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

    def ver_menu_restaurante(self):

        print(f"\n--- Menú de {self.get_nombre_comercial()} ---")
    
        if not self._catalogo:
            print("El catálogo está vacío.")
            return

        # Iterar sobre la lista de objetos Producto
        for i, producto in enumerate(self._catalogo):
            # Usamos los Getters del objeto Producto para acceder a sus datos
            nombre = producto.get_nombre()
            precio = producto.get_precio()
            categoria = producto.get_categoria()
        
            print(f"[{i + 1}] {nombre} ({categoria}) - ${precio:.2f}")
    
        print("---------------------------------------")