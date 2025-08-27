from src.views.base.base_dispositivo_window import BaseDispositivoWindow
from src.model.dispositivo_model.playstation_model import PlayStationModel

class PlayStationWindow(BaseDispositivoWindow):
    def __init__(self, modelo, numero_serie, estado, cliente_id):
        dispositivo = PlayStationModel(modelo, numero_serie, estado, cliente_id)
        super().__init__(dispositivo, titulo=f"PlayStation {modelo}")
