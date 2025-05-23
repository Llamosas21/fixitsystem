import sqlite3
import os

class ClienteModel:
    def __init__(self, db_path=None):
        if db_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(base_dir, "../database/fixitsystem.db")
            db_path = os.path.abspath(db_path)

        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.crear_tabla()

    def _asegurar_conexion(self):
        try:
            self.connection.execute("SELECT 1")
        except sqlite3.ProgrammingError:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()

    def cerrar_conexion(self):
        if self.connection:
            self.connection.close()

    def obtener_datos(self, query, params=()):
        self._asegurar_conexion()
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error al ejecutar la consulta: {e}")
            return []

    def crear_tabla(self):
        query_clientes = """
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente TEXT PRIMARY KEY,
                dispositivo TEXT NOT NULL,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                correo TEXT,
                fecha_ingreso TEXT
            )
        """
        try:
            self.ejecutar_query(query_clientes)
        except sqlite3.Error as e:
            print(f"❌ Error al crear la tabla: {e}")

    def ejecutar_query(self, query, params=()):
        self._asegurar_conexion()
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"❌ Error al ejecutar la consulta: {e}")

    def insertar_cliente(self, id_cliente, dispositivo, nombre, telefono, correo, fecha_ingreso):
        self._asegurar_conexion()
        query = """
            INSERT INTO clientes (id_cliente, dispositivo, nombre, telefono, correo, fecha_ingreso)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.ejecutar_query(query, (id_cliente, dispositivo, nombre, telefono, correo, fecha_ingreso))
        except sqlite3.Error as e:
            print(f"❌ Error al insertar el cliente: {e}")

    def obtener_clientes(self):
        self._asegurar_conexion()
        query = "SELECT id_cliente, nombre, dispositivo, correo, telefono, fecha_ingreso FROM clientes"
        try:
            return self.obtener_datos(query)
        except Exception as e:
            print(f"❌ Error al obtener clientes: {e}")
            return []

    def editar_cliente(self, id_cliente, nombre, telefono, correo, fecha_ingreso):
        self._asegurar_conexion()
        try:
            self.cursor.execute("""
                UPDATE clientes
                SET nombre = ?, telefono = ?, correo = ?, fecha_ingreso = ?
                WHERE id_cliente = ?
            """, (nombre, telefono, correo, fecha_ingreso, id_cliente))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"❌ Error al editar cliente: {e}")
            return False

    def eliminar_cliente(self, id_cliente):
        self._asegurar_conexion()
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM clientes WHERE id_cliente = ?"
            cursor.execute(query, (id_cliente,))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"❌ Error al eliminar cliente: {e}")
            return False
