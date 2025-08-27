# Controlador para dispositivos PlayStation (PS3, PS4, PS5)
from src.model.dispositivo_model.playstation_model import PlayStationModel

class PlayStationController:
    def __init__(self):
        self.dispositivos = []

    def agregar_playstation(self, modelo, numero_serie, estado, cliente_id):
        dispositivo = PlayStationModel(modelo, numero_serie, estado, cliente_id)
        self.dispositivos.append(dispositivo)
        return dispositivo

    def obtener_todos(self):
        return self.dispositivos

    def buscar_por_serie(self, numero_serie):
        for dispositivo in self.dispositivos:
            if dispositivo.numero_serie == numero_serie:
                return dispositivo
        return None

    # Métodos para actualizar, eliminar, etc. pueden agregarse aquí
