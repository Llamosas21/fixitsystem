from src.views.base.base_dispositivo_window import BaseDispositivoWindow
from src.model.dispositivo_model.notebook_model import NotebookModel

class NotebookWindow(BaseDispositivoWindow):
    def __init__(self, marca, modelo, numero_serie, estado, cliente_id):
        dispositivo = NotebookModel(marca, modelo, numero_serie, estado, cliente_id)
        super().__init__(dispositivo, titulo=f"Notebook {marca} {modelo}")
