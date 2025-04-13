from model.client_model import ClienteModel

class ClientController:
    def __init__(self):
        self.db = ClienteModel()

    def agregar_cliente(self, datos):
        """Agrega un cliente a la base de datos."""
        try:
            self.db.insertar_cliente(
                id_cliente=datos["id_cliente"],
                nombre=datos["nombre"],
                dispositivo=datos["dispositivo"],
                telefono=datos["telefono"],
                correo=datos["correo"],
                fecha_ingreso=datos["fecha_ingreso"]
            )
            return True
        except Exception as e:
            print(f"❌ Error al agregar cliente: {e}")
            return False
   
    def obtener_clientes(self):
        try:
            return self.db.obtener_clientes()
        except Exception as e:
            print(f"Error al obtener el cliente: {e}")
            return []

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        self.db.cerrar_conexion()