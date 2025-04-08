import sqlite3
import os

class ClienteModel:
    def __init__(self, db_path=None):
        # Construir la ruta absoluta de la base de datos
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), "../database/fixitsystem_clientes.db")
        self.db_path = db_path
        self.connection = None

    def conectar(self):
        try:
            db_dir = os.path.dirname(self.db_path)
            if not os.path.exists(db_dir):
                os.makedirs(db_dir)
            self.connection = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"❌ Error al conectar con la base de datos: {e}")

    def cerrar_conexion(self):
        if self.connection:
            self.connection.close()

    def obtener_datos(self, query, params=()):
        if not self.connection:
            print("❌ No hay conexión a la base de datos.")
            return []
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Error al ejecutar la consulta: {e}")
            return []

    def crear_tablas(self):
        """Crea las tablas 'clientes' y 'dispositivos' si no existen."""
        if not self.connection:
            print("❌ No hay conexión a la base de datos.")
            return

        # Tabla de clientes
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
            print(f"❌ Error al crear las tablas: {e}")

    def ejecutar_query(self, query, params=()):
            if not self.connection:
                print("❌ No hay conexión a la base de datos.")
                return
            try:
                cursor = self.connection.cursor()
                cursor.execute(query, params)
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"❌ Error al ejecutar la consulta: {e}")

    def insertar_cliente(self, id_cliente, dispositivo, nombre, telefono, correo, fecha_ingreso):
        if not self.connection:
            print("❌ No hay conexión a la base de datos.")
            return
        query = """
            INSERT INTO clientes (id_cliente, dispositivo, nombre, telefono, correo, fecha_ingreso)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.ejecutar_query(query, (id_cliente, dispositivo, nombre, telefono, correo, fecha_ingreso))
        except sqlite3.Error as e:
            print(f"❌ Error al insertar el cliente: {e}")

    def obtener_clientes(self):
        query = "SELECT id_cliente, nombre, dispositivo, correo, telefono, fecha_ingreso FROM clientes"
        try:
            return self.obtener_datos(query)
        except Exception as e:
            print(f"❌ Error al obtener clientes desde la base de datos: {e}")
            return []
       
    def inicializar_base(self):
            self.conectar()
            self.crear_tablas()
            self.cerrar_conexion()

"""
        # Tabla de dispositivos
        query_dispositivos = 
            CREATE TABLE IF NOT EXISTS dispositivos (
                id_dispositivo TEXT PRIMARY KEY,
                id_cliente INTEGER NOT NULL,
                fecha_ingreso TEXT,
                garantia_fecha TEXT,
                procesador TEXT,
                domicilio TEXT,
                producto TEXT,
                garantias TEXT,
                memoria TEXT,
                precio REAL,
                modelo TEXT,
                fuente TEXT,
                so TEXT,
                ram TEXT,
                nota TEXT,
                observaciones TEXT,
                FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
            )
        
"""