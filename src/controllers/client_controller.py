from controllers.db_logical_client import DatabaseCliente

class ClientController:
    def __init__(self):
        self.db = DatabaseCliente()
        self.db.conectar()

    def obtener_clientes(self):
        """Obtiene todos los clientes de la base de datos."""
        query = "SELECT id_cliente, nombre, dispositivo, correo, telefono, fecha_ingreso FROM clientes"
        return self.db.obtener_datos(query)

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        self.db.cerrar_conexion()