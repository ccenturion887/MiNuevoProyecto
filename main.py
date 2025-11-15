import sys 
from Cliente import Cliente 
from Restaurante import Restaurante
from Producto import Producto
from SistemaPedidos import SistemaPedidos

def mostrar_menu():
    print("\n===============================")
    print("      SISTEMA DE PEDIDOS YA")
    print("===============================")
    print("1. Dar de Alta Restaurante (y Productos)")
    print("2. Registrarse")
    print("3. Iniciar Sesión")
    print("4. Salir")
    print("===============================")
    
def ejecutar_app():
    app = SistemaPedidos()
    opciones_menu(app)

def añadir_catalogo():
    """Crea objetos Producto interactuando con el usuario y retorna la lista."""
    catalogo_productos = [] # La lista se inicia aca
    
    
    print("\n--- Carga de Productos al Catálogo ---")
    
    while True:
        prod_nombre = input("Nombre del producto (o 'fin' para terminar): ")
        if prod_nombre.lower() == 'fin': 
            break
            
        try:
            prod_precio = float(input(f"Precio de '{prod_nombre}': $"))
            prod_categoria = input(f"Categoría (ej: Hamburguesa, Bebida): ")
            
            # Crear Objeto Producto
            nuevo_producto = Producto(prod_nombre, prod_precio, prod_categoria)
            
            # Añadir a la lista
            catalogo_productos.append(nuevo_producto)
            print(f"   -> Producto '{prod_nombre}' añadido a la lista.")
            
        except ValueError:
            print("Error: El precio debe ser un número.")
            
    return opciones_menu # Retorna la lista completa de objetos Producto
    
    
    

def alta_restaurante():
    nombre_comercial = input("Ingrese el nombre del restaurante: ")
    direccion_fisica = input("Introduce la direccion del local: ")
    catalogo = añadir_catalogo()

    restaurante_nuevo = Restaurante (
        nombre_comercial,
        direccion_fisica,
        catalogo
    )
    print("\nRestaurante registrado con éxito:")
    print(f"Nombre del restaurante: {restaurante_nuevo.get_nombre_comercial()}")
    print(f"Dirección del local: {restaurante_nuevo.get_direccion_fisica()}")
    

def opciones_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            alta_restaurante()
    
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    opciones_menu()
