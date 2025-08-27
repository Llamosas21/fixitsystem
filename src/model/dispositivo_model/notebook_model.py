# src/model/dispositivo_model/notebook_model.py
import sqlite3

class NotebookModel:
    def __init__(self, db_path="src/database/fixitsystem.db", marca=None, modelo=None, numero_serie=None, estado=None, cliente_id=None):
        if marca is not None:
            self.marca = marca
            self.modelo = modelo
            self.numero_serie = numero_serie
            self.estado = estado
            self.cliente_id = cliente_id
        else:
            self.connect = sqlite3.connect(db_path)
            self.connect.row_factory = sqlite3.Row
            self.cursor = self.connect.cursor()
            self.crear_tabla()

    def to_dict(self):
        if hasattr(self, 'marca'):
            return {
                'marca': self.marca,
                'modelo': self.modelo,
                'numero_serie': self.numero_serie,
                'estado': self.estado,
                'cliente_id': self.cliente_id
            }
        return {}

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notebooks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente TEXT NOT NULL,
                fecha_ingreso TEXT,
                estado_cargador TEXT,
                tarjeta_grafica TEXT,
                nombre TEXT,
                garantia TEXT,
                procesador TEXT,
                placa TEXT,
                telefono TEXT,
                modelo TEXT,
                memoria TEXT,
                pantalla TEXT,
                correo TEXT,
                tim TEXT,
                ram TEXT,
                estado TEXT,
                notas TEXT,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id)
            )
        """)
        self.connect.commit()

    def agregar_notebook(self, **kwargs):
        datos = (
            kwargs['id_cliente'],
            kwargs['fecha_de_ingreso'],
            kwargs.get('estado_cargador', ''),
            kwargs.get('tarjeta_grafica', ''),
            kwargs.get('nombre', ''),
            kwargs.get('garantia', ''),
            kwargs.get('procesador', ''),
            kwargs.get('placa', ''),
            kwargs.get('telefono', ''),
            kwargs.get('modelo', ''),
            kwargs.get('memoria', ''),
            kwargs.get('pantalla', ''),
            kwargs.get('correo', ''),
            kwargs.get('tim', ''),
            kwargs.get('ram', ''),
            kwargs.get('estado', ''),
            kwargs.get('notas', '')
        )
        self.cursor.execute("""
            INSERT INTO notebooks (
                id_cliente, fecha_ingreso, estado_cargador, tarjeta_grafica, nombre, garantia,
                procesador, placa, telefono, modelo, memoria, pantalla, correo, tim, ram, estado, notas
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, datos)
        self.connect.commit()

    def obtener_notebooks(self):
        self.cursor.execute("SELECT * FROM notebooks")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def obtener_por_cliente_id(self, cliente_id):
        self.cursor.execute("SELECT * FROM notebooks WHERE id_cliente = ?", (cliente_id,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def editar_notebook(self, **kwargs):
        datos = (
            kwargs['fecha_de_ingreso'],
            kwargs.get('estado_cargador', ''),
            kwargs.get('tarjeta_grafica', ''),
            kwargs.get('nombre', ''),
            kwargs.get('garantia', ''),
            kwargs.get('procesador', ''),
            kwargs.get('placa', ''),
            kwargs.get('telefono', ''),
            kwargs.get('modelo', ''),
            kwargs.get('memoria', ''),
            kwargs.get('pantalla', ''),
            kwargs.get('correo', ''),
            kwargs.get('tim', ''),
            kwargs.get('ram', ''),
            kwargs.get('estado', ''),
            kwargs.get('notas', ''),
            kwargs['id_cliente']
        )
        self.cursor.execute("""
            UPDATE notebooks SET
                fecha_ingreso=?, estado_cargador=?, tarjeta_grafica=?, nombre=?, garantia=?,
                procesador=?, placa=?, telefono=?, modelo=?, memoria=?, pantalla=?, correo=?, 
                tim=?, ram=?, estado=?, notas=?
            WHERE id_cliente=?
        """, datos)
        self.connect.commit()

    def eliminar_por_id_cliente(self, id_cliente):
        self.cursor.execute("DELETE FROM notebooks WHERE id_cliente=?", (id_cliente,))
        self.connect.commit()

    def cerrar_conexion(self):
        self.connect.close()
