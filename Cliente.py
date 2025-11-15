class Cliente:
    # 1. Constructor: Los atributos de la instancia (self.X) son privados
    def __init__(self, nombre, direccion_entrega, metodo_pago):
        self._nombre = nombre
        self._direccion_entrega = direccion_entrega
        self._metodo_pago = metodo_pago

    # 2. Getters: Acceden al atributo privado
    def get_nombre(self):
        return self._nombre

    def get_direccion_entrega(self):
        return self._direccion_entrega

    def get_metodo_pago(self):
        return self._metodo_pago