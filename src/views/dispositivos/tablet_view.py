from src.views.base.base_dispositivo_window import BaseDispositivoWindow
from src.model.dispositivo_model.tablet_model import TabletModel

class TabletWindow(BaseDispositivoWindow):
    def __init__(self, marca, modelo, numero_serie, estado, cliente_id):
        dispositivo = TabletModel(marca, modelo, numero_serie, estado, cliente_id)
        super().__init__(dispositivo, titulo=f"Tablet {marca} {modelo}")
