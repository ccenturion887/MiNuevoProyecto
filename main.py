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
    print("3. Salir")
    print("===============================")

def mostrar_menu_restaurantes():
    print("\n===============================")
    print("      RESTAURANTES")
    print("===============================")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Atrás")
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
    catalogo_productos = []
    
    
    print("\n--- Carga de Productos al Catálogo ---")
    
    while True:
        prod_nombre = input("Nombre del producto (o 'fin' para terminar): ")
        if prod_nombre.lower() == 'fin': 
            break
            
        try:
            prod_precio = float(input(f"Precio de '{prod_nombre}': $"))
            prod_categoria = input(f"Categoría (ej: Hamburguesa, Bebida): ")
            
            nuevo_producto = Producto(prod_nombre, prod_precio, prod_categoria)
            
            catalogo_productos.append(nuevo_producto)
            print(f"   -> Producto '{prod_nombre}' añadido a la lista.")
             
            
        except ValueError:
            print("Error: El precio debe ser un número.")
        return catalogo_productos
    
def actualizar_estado_pedido(sistema, restaurante_logeado):
    
    pedidos_activos_sistema = sistema.listar_pedidos_activos() 
    
    pedidos_restaurante = []
    for pedido in pedidos_activos_sistema:
        if pedido.get_restaurante() == restaurante_logeado: 
            pedidos_restaurante.append(pedido)

    if not pedidos_restaurante:
        print("\n--- No hay pedidos activos pendientes para este restaurante. ---")
        return

    print("\n--- 🧾 Pedidos Activos para", restaurante_logeado.get_nombre_comercial(), "---")
    
    for i, pedido in enumerate(pedidos_restaurante):
        cliente_nombre = pedido.get_cliente().get_nombre()
        total = pedido.get_total_a_pagar()
        estado = pedido.get_estado()
        print(f"[{i + 1}] Cliente: {cliente_nombre} | Total: ${total:.2f} | Estado actual: {estado}")
        
    print("------------------------------------------------------------")
    
    try:
        seleccion = input("Seleccione el NÚMERO del pedido a actualizar (o 'fin'): ")
        if seleccion.lower() == 'fin':
            return
            
        indice = int(seleccion) - 1
        
        if 0 <= indice < len(pedidos_restaurante):
            pedido_a_modificar = pedidos_restaurante[indice]
            
            estados_validos = ["en preparación", "en camino", "entregado", "cancelado"]
            print("\nEstados posibles:", estados_validos)
            nuevo_estado = input("Ingrese el NUEVO estado del pedido: ").lower()
            
            if nuevo_estado in estados_validos:
                pedido_a_modificar.set_estado(nuevo_estado) 
                print(f"\n✅ Pedido de {pedido_a_modificar.get_cliente().get_nombre()} actualizado a: '{nuevo_estado}'")
            else:
                print("Estado no válido. Intente de nuevo.")
        else:
            print("Número de pedido inválido.")
            
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

def cargar_producto_a_restaurante(restaurante_logeado):
    print(f"\n--- Añadir Productos a {restaurante_logeado.get_nombre_comercial()} ---")
    
    while True:
        prod_nombre = input("Nombre del nuevo producto (o 'fin' para terminar): ")
        if prod_nombre.lower() == 'fin':
            break

        try:
            prod_precio = float(input(f"Precio de '{prod_nombre}': $"))
            prod_categoria = input("Categoría (ej: Postre, Adicional): ")
            
            nuevo_producto = Producto(prod_nombre, prod_precio, prod_categoria)
            
            restaurante_logeado.dar_alta_producto(nuevo_producto)
            
            print(f"-> Producto '{prod_nombre}' añadido al catálogo.")
            print(f"Total de productos ahora: {len(restaurante_logeado.get_catalogo())}")

        except ValueError:
            print("Error: El precio debe ser un número válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    print("\n--- Terminada la carga de productos ---")
    
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
    

    restaurante_encontrado = sistema.buscar_restaurante_por_nombre(nombre_ingresado)
    
    if restaurante_encontrado:
        print(f"¡Bienvenido/a al Panel, {restaurante_encontrado.get_nombre_comercial()}!")

        menu_restaurante_logeado(sistema, restaurante_encontrado)
        return restaurante_encontrado
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

def mostrar_pedidos_activos_restaurante(sistema, restaurante_logeado):

    pedidos_activos_sistema = sistema.listar_pedidos_activos()
    
    pedidos_restaurante = []
    for pedido in pedidos_activos_sistema:
        if pedido.get_restaurante() == restaurante_logeado: 
            pedidos_restaurante.append(pedido)

    if not pedidos_restaurante:
        print("\n--- No hay pedidos activos pendientes para este restaurante. ---")
        return

    print("\n=======================================================")
    print(f"       PEDIDOS ACTIVOS PENDIENTES: {restaurante_logeado.get_nombre_comercial()}")
    print("=======================================================")
    

    for i, pedido in enumerate(pedidos_restaurante):
        cliente = pedido.get_cliente()
        productos = pedido.get_productos_pedidos()
        
        print(f"\n[PEDIDO #{i + 1}]")
        print(f"  - Cliente: {cliente.get_nombre()}")
        print(f"  - Dirección de Entrega: {cliente.get_direccion_entrega()}")
        print(f"  - Estado: {pedido.get_estado()}")
        print(f"  - Pago: {pedido.get_metodo_pago()}")
        print(f"  - Total: ${pedido.get_total_a_pagar():.2f}")
        print("  --- Detalle de Productos ---")
        
        for producto in productos:
            print(f"    -> {producto.get_nombre()} (${producto.get_precio():.2f})")
            
        print("-------------------------------------------------------")
        
    input("\nPresione Enter para volver al menú principal del restaurante...")

def ver_estado_pedido_cliente(sistema, cliente_logeado):
    
    pedidos_activos_sistema = sistema.listar_pedidos_activos()
    

    mis_pedidos = []
    for pedido in pedidos_activos_sistema:
    
        if pedido.get_cliente() == cliente_logeado: 
            mis_pedidos.append(pedido)

    if not mis_pedidos:
        print("\n--- No has realizado ningún pedido todavía. ---")
        return

    print(f"\n======== ESTADO DE TUS PEDIDOS ({cliente_logeado.get_nombre()}) ========")
    
    for i, pedido in enumerate(mis_pedidos):
        restaurante = pedido.get_restaurante()
        estado = pedido.get_estado()
        total = pedido.get_total_a_pagar()
        
        print(f"[{i + 1}] Restaurante: {restaurante.get_nombre_comercial()}")
        print(f"    -> Estado: **{estado.upper()}**")
        print(f"    -> Total: ${total:.2f}")
        print("-------------------------------------------------------")
        
    input("\nPresione Enter para volver al menú principal del cliente...")

def seleccionar_y_ver_menu(sistema, cliente_logeado):
    
    print("\n--- SELECCIÓN DE RESTAURANTE ---")

    restaurantes_disponibles = sistema.listar_restaurantes_disponibles() 
    
    if not restaurantes_disponibles:
        print("Lo sentimos, no hay restaurantes registrados en el sistema.")
        return None 

    while True:
        nombre_ingresado = input("\nIngrese el nombre del restaurante para ver el menú (o 'fin'): ")
        
        if nombre_ingresado.lower() == 'fin':
            return None
        
        restaurante_seleccionado = sistema.buscar_restaurante_por_nombre(nombre_ingresado)
        
        if restaurante_seleccionado:
            print(f"\n--- 📖 Menú de {restaurante_seleccionado.get_nombre_comercial()} ---")
            
            restaurante_seleccionado.ver_menu_restaurante()
            carrito  = []
            monto_total = 0.0
            catalogo = restaurante_seleccionado.get_catalogo()

            
            print("\n--- SELECCIÓN DE PRODUCTOS ---")
        print("Ingrese el número de producto que desea añadir (o 'fin' para terminar).")

        while True:
            seleccion = input(f"Añadir producto (1 a {len(catalogo)}, o 'fin'): ")
            
            if seleccion.lower() == 'fin':
                break
            
            try:

                indice_producto = int(seleccion) - 1 
                
                if 0 <= indice_producto < len(catalogo):
                    producto_elegido = catalogo[indice_producto]
                    

                    carrito.append(producto_elegido)
                    

                    monto_total += producto_elegido.get_precio()
                    
                    print(f"Añadido: {producto_elegido.get_nombre()}. Total parcial: ${monto_total:.2f}")
                else:
                    print("Número fuera del rango del menú.")
            except ValueError:
                print("Ingrese un número válido o 'fin'.")


        return {
            'restaurante': restaurante_seleccionado,
            'carrito': carrito,
            'monto_total': monto_total
        }
    else:
        return None

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
        
        elif opcion == '3':
            print("Muchas gracias por elegirnos!")
            sys.exit()
    
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
        
        elif opcion == '3':
            opciones_menu(sistema)
        
        else:
            print("Opción invalida.")

def menu_cliente_logueado(sistema, cliente_encontrado):
    while True:
        print("\n===============================")
        print("1. Hace tu pedido")
        print("2. Ver estado")
        print("3. Cerrar Sesión")
        print("===============================")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            print("\n--- INICIO DE PEDIDO ---")
            
            datos_pedido = seleccionar_y_ver_menu(sistema, cliente_encontrado)
            
            if datos_pedido and datos_pedido['monto_total'] > 0:
                
                restaurante = datos_pedido['restaurante']
                carrito = datos_pedido['carrito']
                metodo_pago_cliente = cliente_encontrado.get_metodo_pago()

                pedido_nuevo = Pedidos(
                    cliente = cliente_encontrado,
                    restaurante = restaurante,
                    productos_pedidos = carrito,
                    metodo_pago = metodo_pago_cliente

                )
                
                monto = pedido_nuevo.get_total_a_pagar()

                sistema.dar_alta_pedido(pedido_nuevo)
                
                print("\n================ TICKET DE PEDIDO ===============")
                print(f"Cliente: {cliente_encontrado.get_nombre()}")
                print(f"Restaurante: {restaurante.get_nombre_comercial()}")
                print(f"Estado: {pedido_nuevo.get_estado()}")
                print(f"MÉTODO DE PAGO: {pedido_nuevo.get_metodo_pago()}")
                print("-------------------------------------------------")
                
                for producto in carrito:
                    print(f"  - {producto.get_nombre()} | ${producto.get_precio():.2f}")
                
                print("-------------------------------------------------")
                print(f"MONTO TOTAL A PAGAR: ${monto:.2f}")
                print("=================================================")
                print(f"✅ Restaurante seleccionado: {restaurante.get_nombre_comercial()}.")
                
                print("\n¡Pedido creado y registrado en el sistema!")
                
                print("\n✅ ¡Pedido creado y registrado en el sistema!")
                

            elif datos_pedido:
                print("\nEl carrito está vacío. No se generó ningún pedido.")
        
        elif opcion == '2':
            ver_estado_pedido_cliente(sistema, cliente_encontrado)
        
        elif opcion == '3':
            break

        else:
            print("Opción invalida.")


def menu_restaurante_logeado(sistema, restaurante_logeado):
    while True:
        print("\n===============================")
        print("1. Ver Pedidos Activos")
        print("2. Actualizar Estado de un Pedido")
        print("3. Ver catálogo")
        print("4. Añadir Producto(s)")
        print("5. Cerrar Sesión")
        print("===============================")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            mostrar_pedidos_activos_restaurante(sistema, restaurante_logeado)

        elif opcion == '2':
            actualizar_estado_pedido(sistema, restaurante_logeado)

        elif opcion == '3':
            restaurante_logeado.ver_menu_restaurante()

        elif opcion == '4':
            cargar_producto_a_restaurante(restaurante_logeado)

        elif opcion == '5':
            break

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
 