# Controlador para consolas PS3
from src.model.dispositivo_model.ps3consola_model import PS3ConsolaModel

class PS3ConsolaController:
    def __init__(self):
        self.consolas = []

    def agregar_ps3consola(self, numero_serie, estado, cliente_id):
        consola = PS3ConsolaModel(numero_serie, estado, cliente_id)
        self.consolas.append(consola)
        return consola

    def obtener_todas(self):
        return self.consolas

    def buscar_por_serie(self, numero_serie):
        for consola in self.consolas:
            if consola.numero_serie == numero_serie:
                return consola
        return None

    # Métodos para actualizar, eliminar, etc. pueden agregarse aquí
