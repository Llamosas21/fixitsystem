# src/controllers/dispositivo_controller/notebook_controller.py
from src.model.dispositivo_model.notebook_model import NotebookModel

class NotebookController:
    def __init__(self):
        self.modelo = NotebookModel()

    def obtener_notebooks(self):
        return self.modelo.obtener_notebooks()

    def obtener_por_cliente_id(self, cliente_id):
        return self.modelo.obtener_por_cliente_id(cliente_id)

    def agregar_notebook(self, **kwargs):
        self.modelo.agregar_notebook(**kwargs)

    def editar_notebook(self, **kwargs):
        self.modelo.editar_notebook(**kwargs)

    def eliminar_notebook(self, id_cliente):
        try:
            self.modelo.eliminar_por_id_cliente(id_cliente)
            return True
        except Exception as e:
            print(f"❌ Error al eliminar notebook: {e}")
            return False

    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
