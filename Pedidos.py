from Cliente import Cliente
from Restaurante import Restaurante
from Producto import Producto

class Pedidos:
    def __init__(self, cliente: Cliente, restaurante: Restaurante, productos_pedidos: list, metodo_pago: str):

        self._cliente = cliente 
        self._restaurante = restaurante
        self._productos_pedidos = productos_pedidos 
        self._estado = "pendiente"
        self._total_a_pagar = 0.0
        self._total_a_pagar = self._calcular_total()
        self._metodo_pago = metodo_pago

    def _calcular_total(self):
        total = 0.0
        for producto in self._productos_pedidos:

            total += producto.get_precio()
        return total
    
    def get_metodo_pago(self):
        return self._metodo_pago
    
    def set_estado(self, nuevo_estado: str):
        self._estado = nuevo_estado

    def get_cliente(self):
        return self._cliente

    def get_restaurante(self):
        return self._restaurante

    def get_productos_pedidos(self):
        return self._productos_pedidos
    
    def get_estado(self):
        return self._estado
    
    def get_total_a_pagar(self):
        return self._total_a_pagar