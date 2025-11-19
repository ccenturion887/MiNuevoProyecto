from Cliente import Cliente
from Restaurante import Restaurante
from Pedidos import Pedidos

class SistemaPedidos:
    
    def __init__(self)
        self._clientes = []
        self._restaurantes = []
        self._pedidos = []
    
    def dar_alta_cliente(self, cliente: Cliente):
        self._clientes.append(cliente)

    def dar_alta_restaurante(self, restaurante: Restaurante):
        self._restaurantes.append(restaurante)
        
    def dar_alta_pedido(self, pedido: Pedidos):
        self._pedidos.append(pedido)

    def buscar_cliente_por_nombre(self, nombre_buscado: str):
        """Busca y retorna un objeto Cliente para la función login()."""
        for cliente in self._clientes:
            if cliente.get_nombre().lower() == nombre_buscado.lower():
                return cliente
        return None
    
    def buscar_restaurante_por_nombre(self, nombre_buscado: str):
        for restaurante in self._restaurantes:
            if restaurante.get_nombre_comercial().lower() == nombre_buscado.lower():
                return restaurante
        return None
        
    def listar_restaurantes_disponibles(self):
        """Muestra y retorna todos los restaurantes disponibles para que el cliente elija."""
        if not self._restaurantes:
            print("No hay restaurantes registrados en el sistema.")
            return []
            
        print("\n--- Restaurantes Disponibles ---")
        for i, restaurante in enumerate(self._restaurantes):
            print(f"[{i+1}] {restaurante.get_nombre_comercial()} - Dirección: {restaurante.get_direccion_fisica()}")
            
        return self._restaurantes
        
    def listar_pedidos_activos(self):
        """Lista pedidos que no fueron entregados (Abstracción)."""
        activos = [p for p in self._pedidos if p.get_estado() != "entregado" and p.get_estado() != "cancelado"]
        return activos
