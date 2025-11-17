import sys 
from Cliente import Cliente 
from Restaurante import Restaurante
from Producto import Producto
from SistemaPedidos import SistemaPedidos
from Pedidos import Pedidos

def mostrar_menu():
    print("\n===============================")
    print("      SISTEMA DE PEDIDOS YA")
    print("===============================")
    print("1. Restaurante")
    print("2. Cliente")
    print("3. Salir") # Final de programa
    print("===============================")

def mostrar_menu_restaurantes():
    print("\n===============================")
    print("      RESTAURANTES")
    print("===============================")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Ver catalogo")
    print("4. Atrás")
    print("===============================")

def mostrar_menu_cliente():
    print("\n===============================")
    print("      CLIENTES")
    print("===============================")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Atrás")
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
        return catalogo_productos
    
def alta_restaurante(sistema):
    nombre_comercial = input("Ingrese el nombre del restaurante: ")
    direccion_fisica = input("Introduce la direccion del local: ")
    catalogo = añadir_catalogo()
    
    restaurante_nuevo = Restaurante (
        nombre_comercial,
        direccion_fisica,
        catalogo
    )
    sistema.dar_alta_restaurante(restaurante_nuevo)
    print("\nRestaurante registrado con éxito:")
    print(f"Nombre del restaurante: {restaurante_nuevo.get_nombre_comercial()}")
    print(f"Dirección del local: {restaurante_nuevo.get_direccion_fisica()}")
    restaurante_nuevo.ver_menu_restaurante()
    return menu_restaurante_logeado(sistema, restaurante_nuevo)

def login_restaurante(sistema):
    print("\n--- Inicio de Sesión de Restaurante ---")
    nombre_ingresado = input("Ingrese el nombre del restaurante: ")
    pass
    
    # Abstracción: Uso el método del sistema para buscar
    restaurante_encontrado = sistema.buscar_restaurante_por_nombre(nombre_ingresado)
    
    if restaurante_encontrado:
        print(f"¡Bienvenido/a al Panel, {restaurante_encontrado.get_nombre_comercial()}!")
        # Pasa el control al menú del restaurante
        menu_restaurante_logeado(sistema, restaurante_encontrado)
    else:
        print("Nombre de restaurante no encontrado.")
        return None

def seleccionar_metodo_pago():
    while True:
        print("\n===============================")
        print("      METODOS DE PAGO")
        print("===============================")
        opciones = {
        '1': 'Tarjeta de Crédito',
        '2': 'Tarjeta de Débito',
        '3': 'Efectivo',
        '4': 'Mercado Pago'
    }
    
        for clave, valor in opciones.items():
            print(f"[{clave}] {valor}")
        
        while True:
            eleccion = input("Seleccione el número de su método de pago preferido: ")
            if eleccion in opciones:
                return opciones[eleccion]
            else:
                print("Opción no válida. Intente de nuevo.")


def alta_cliente(sistema):
    print("--- Registro de Nuevo Cliente ---")

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    direccion_cliente = input("Ingrese la dirección de entrega: ")
    metodo_pago_seleccionado = seleccionar_metodo_pago()
    
    cliente_nuevo = Cliente(
        nombre_cliente,
        direccion_cliente,
        metodo_pago_seleccionado
        )
    sistema.dar_alta_cliente(cliente_nuevo)
    print("\nCliente registrado con éxito:")
    print(f"Nombre: {cliente_nuevo.get_nombre()}")
    print(f"Dirección: {cliente_nuevo.get_direccion_entrega()}")
    print(f"Pago Preferido: {cliente_nuevo.get_metodo_pago()}")

def login_cliente(sistema):
    nombre_ingresado = input("Ingrese su nombre de cliente para acceder: ")
    cliente_encontrado = sistema.buscar_cliente_por_nombre(nombre_ingresado)
    
    if cliente_encontrado:
        print(f"¡Bienvenido/a, {cliente_encontrado.get_nombre()}!")
        menu_cliente_logueado(sistema, cliente_encontrado)
    else:
        print("Nombre no encontrado.")
        return None

def opciones_menu(sistema):
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            menu_restaurantes(sistema)

        elif opcion == '2':
            menu_cliente(sistema)
    
        else:
            print("Opcion invalida.")

def menu_restaurantes(sistema):
    while True:
        mostrar_menu_restaurantes()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_restaurante(sistema)

        elif opcion == '2':
            login_restaurante(sistema)
        
        elif opcion == '4':
            opciones_menu(sistema)
        
        else:
            print("Opción invalida.")

def menu_cliente_logueado(sistema, cliente_encontrado):
    while True:
        print("\n===============================")
        print("1. Ver Datos")
        print("2. Hace tu pedido")
        print("3. Ver estado")
        print("4. Cerrar Sesión")
        print("===============================")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            opciones_menu(sistema)
        else:
            print("Error")


def menu_restaurante_logeado(sistema, restaurante_logeado):
    while True:
        print("\n===============================")
        print("1. Ver Pedidos Activos")
        print("2. Actualizar Estado de un Pedido")
        print("3. Ver catalogo")
        print("4. Cerrar Sesión")
        print("===============================")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            opciones_menu(sistema) # Es temporal, hasta que haga la programacion de pedidos y cliente, mostrar_pedidos_activos_restaurante(sistema, restaurante_logeado)

        elif opcion == '2':
            opciones_menu(sistema) # Es temporal, hasta que haga la programacion de pedidos y cliente

        elif opcion == '3':
            restaurante_logeado.ver_menu_restaurante()

        elif opcion == '4':
            opciones_menu(sistema)

        else:
            print("Opción invalida.")

def menu_cliente(sistema):
    while True:
        mostrar_menu_cliente()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_cliente(sistema)
        
        elif opcion == '2':
            login_cliente(sistema)
        
        elif opcion == '3':
            opciones_menu(sistema)

        else:
            print("Opción invalida.")


if __name__ == "__main__":
    sistema_pedidos = SistemaPedidos()
    opciones_menu(sistema_pedidos)
 