class EntidadNombrable:
    def __init__(self, nombre: str):
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre