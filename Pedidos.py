from Cliente import Cliente
from Restaurante import Restaurante
from Producto import Producto
class Pedidos:
    def __init__(self, cliente: Cliente, restaurante: Restaurante, productos_pedidos: list):
        # Aplicando Encapsulamiento
        self._cliente = cliente 
        self._restaurante = restaurante
        self._productos_pedidos = productos_pedidos 
        self._estado = "pendiente" # Estado inicial por defecto
        self._total_a_pagar = 0.0 # Se calcula con un método de abstracción

    # --- Getters (Encapsulamiento) ---
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