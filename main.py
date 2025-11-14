from Cliente import Cliente

def seleccionar_metodo_pago():
    print("\n--- Métodos de Pago Disponibles ---")
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


print("--- Registro de Nuevo Cliente ---")

nombre_cliente = input("Ingrese el nombre del cliente: ")
direccion_cliente = input("Ingrese la dirección de entrega: ")
metodo_pago_seleccionado = seleccionar_metodo_pago()

cliente_nuevo = Cliente(
    nombre_cliente,
    direccion_cliente,
    metodo_pago_seleccionado
)

print("\nCliente registrado con éxito:")
print(f"Nombre: {cliente_nuevo.get_nombre()}")
print(f"Dirección: {cliente_nuevo.get_direccion_entrega()}")
print(f"Pago Preferido: {cliente_nuevo.get_metodo_pago()}")