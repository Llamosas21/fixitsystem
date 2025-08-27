from src.views.base.base_dispositivo_window import BaseDispositivoWindow
from src.model.dispositivo_model.celular_model import CelularModel

class CelularWindow(BaseDispositivoWindow):
    def __init__(self, marca, modelo, numero_serie, estado, cliente_id):
        dispositivo = CelularModel(marca, modelo, numero_serie, estado, cliente_id)
        super().__init__(dispositivo, titulo=f"Celular {marca} {modelo}")
