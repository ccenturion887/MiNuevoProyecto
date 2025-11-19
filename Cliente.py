from EntidadNombrable import EntidadNombrable
class Cliente:

    def __init__(self, nombre, direccion_entrega, metodo_pago):
        super().__init__(nombre)
        self._direccion_entrega = direccion_entrega
        self._metodo_pago = metodo_pago

    def get_nombre(self):
        return self._nombre

    def get_direccion_entrega(self):
        return self._direccion_entrega

    def get_metodo_pago(self):
        return self._metodo_pago
