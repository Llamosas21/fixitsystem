import sqlite3

class ComputadoraModel:
 
    def __init__(self, db_path="src/database/fixitsystem.db", marca=None, modelo=None, numero_serie=None, estado=None, cliente_id=None):
        if marca is not None:
            # Instancia para visualización rápida
            self.marca = marca
            self.modelo = modelo
            self.numero_serie = numero_serie
            self.estado = estado
            self.cliente_id = cliente_id
        else:
            # Instancia para acceso a base de datos
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
           CREATE TABLE IF NOT EXISTS computadoras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente TEXT NOT NULL,
            fecha_ingreso TEXT,
            procesador TEXT,
            tarjeta_grafica TEXT,
            nombre TEXT,
            garantia TEXT,
            memoria TEXT,
            placa TEXT,
            telefono TEXT,
            modelo TEXT,
            fuente TEXT,
            pantalla TEXT,
            correo TEXT,
            sistema_operativo TEXT,
            ram TEXT,
            estado TEXT,
            precio  TEXT,     
            notas TEXT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id))""")
        self.connect.commit()

    def agregar_computadora(self, **kwargs):
        datos = (
            kwargs['id_cliente'],
            kwargs['fecha_de_ingreso'],
            kwargs['procesador'],
            kwargs['tarjeta_grafica'],
            kwargs['nombre'],
            kwargs['garantia'],
            kwargs['memoria'],
            kwargs['placa'],
            kwargs['telefono'],
            kwargs['modelo'],
            kwargs['fuente'],
            kwargs['pantalla'],
            kwargs['correo'],
            kwargs['sistema_operativo'],
            kwargs['ram'],
            kwargs['estado'],
            kwargs ['precio'],
            kwargs.get('notas', '') 
        )
        self.cursor.execute("""
            INSERT INTO computadoras (
                id_cliente, fecha_ingreso, procesador, tarjeta_grafica,
                nombre, garantia, memoria, placa, telefono, modelo, fuente,
                pantalla, correo, sistema_operativo, ram, estado, precio, notas
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, datos)
        self.connect.commit()

    def obtener_computadoras(self):
        self.cursor.execute("SELECT * FROM computadoras")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def obtener_por_cliente_id(self, cliente_id):
        self.cursor.execute("SELECT * FROM computadoras WHERE id_cliente = ?", (cliente_id,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]  # Por si un cliente tiene más de una computadora

    def editar_computadora(self, **kwargs):
        datos = (
            kwargs['fecha_de_ingreso'],
            kwargs['procesador'],
            kwargs['tarjeta_grafica'],
            kwargs['nombre'],
            kwargs['garantia'],
            kwargs['memoria'],
            kwargs['placa'],
            kwargs['telefono'],
            kwargs['modelo'],
            kwargs['fuente'],
            kwargs['pantalla'],
            kwargs['correo'],
            kwargs['sistema_operativo'],
            kwargs['ram'],
            kwargs['estado'],
            kwargs ['precio'],
            kwargs.get('notas', ''),  # opcional
            kwargs['id_cliente']  # condición del WHERE
        )

        self.cursor.execute("""
            UPDATE computadoras SET
                fecha_ingreso = ?, procesador = ?, tarjeta_grafica = ?, nombre = ?, garantia = ?,
                memoria = ?, placa = ?, telefono = ?, modelo = ?, fuente = ?, pantalla = ?,
                correo = ?, sistema_operativo = ?, ram = ?, estado = ?, precio = ?, notas = ?
            WHERE id_cliente = ?
        """, datos)
        self.connect.commit()

    def eliminar_por_id_cliente(self, id_cliente):
        self.cursor.execute("DELETE FROM computadoras WHERE id_cliente = ?", (id_cliente,))
        self.connect.commit()

    def cerrar_conexion(self):
        self.connect.close()
