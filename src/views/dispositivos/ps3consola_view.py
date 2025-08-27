from src.views.base.base_dispositivo_window import BaseDispositivoWindow
from src.model.dispositivo_model.ps3consola_model import PS3ConsolaModel

class PS3ConsolaWindow(BaseDispositivoWindow):
    def __init__(self, numero_serie, estado, cliente_id):
        dispositivo = PS3ConsolaModel(numero_serie, estado, cliente_id)
        super().__init__(dispositivo, titulo="Consola PS3")
