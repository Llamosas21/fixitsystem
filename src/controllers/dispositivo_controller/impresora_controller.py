from src.model.dispositivo_model.impresora_model import ImpresoraModel

class ImpresoraController:
    def __init__(self):
        self.modelo = ImpresoraModel()

    def obtener_impresoras(self):
        return self.modelo.obtener_impresoras()

    def obtener_por_cliente_id(self, cliente_id):
        return self.modelo.obtener_por_cliente_id(cliente_id)
    
    def agregar_impresora(self, **kwargs):
        self.modelo.agregar_impresora(**kwargs)

    def editar_impresora(self, **kwargs):
        self.modelo.editar_impresora(**kwargs)

    def eliminar_impresora(self, id_cliente):
        try:
            self.modelo.eliminar_por_id_cliente(id_cliente)
            return True
        except Exception as e:
            print(f"❌ Error al eliminar impresora: {e}")
            return False

    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
