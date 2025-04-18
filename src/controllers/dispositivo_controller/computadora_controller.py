from src.model.dispositivo_model.computadora_model import ComputadoraModel

class ComputadoraController:
    def __init__(self):
        self.modelo = ComputadoraModel()

    def obtener_computadoras(self):
        rows = self.modelo.obtener_computadoras()  # delegamos al modelo
        return rows 

    def obtener_por_cliente_id(self, cliente_id):
        return self.modelo.obtener_por_cliente_id(cliente_id)
    
    def agregar_computadora(self, **kwargs):
        #print("🧩 Datos recibidos en agregar_computadora:", kwargs)
        self.modelo.agregar_computadora(**kwargs)

    def editar_computadora(self, **kwargs):
        self.modelo.editar_computadora(**kwargs)

    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
