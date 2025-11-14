class cliente:
    def __init__(self, nombre, direccion_entrega, metodo_pago_preferido):
        self._nombre = nombre
        self._direccion_entrega = direccion_entrega
        self._metodo_pago_preferido = metodo_pago_preferido

n = input("¿Cual es tu nombre? ")
d = input("¿Cual es su direccion? ")
m = input("Añada un metodo de pago")
nombre = cliente(f"nombre: {n}", "hola", "adios")