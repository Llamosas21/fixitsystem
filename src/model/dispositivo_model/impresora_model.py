import sqlite3

class ImpresoraModel:
 
    def __init__(self, db_path="src/database/fixitsystem.db"):
        self.connect = sqlite3.connect(db_path)
        self.connect.row_factory = sqlite3.Row 
        self.cursor = self.connect.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
           CREATE TABLE IF NOT EXISTS impresoras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente TEXT NOT NULL,
            estado_general TEXT,
            tipo_impresora TEXT,
            conectividad TEXT,
            tipo_tinta TEXT,
            uso_estimado TEXT,
            nombre TEXT,
            garantia TEXT,
            modelo TEXT,
            telefono TEXT,
            correo TEXT,
            fecha_ingreso TEXT,
            marca TEXT,
            estado TEXT,
            precio TEXT,
            notas TEXT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id))
        """)
        self.connect.commit()

    def agregar_impresora(self, **kwargs):
        datos = (
            kwargs['id_cliente'],
            kwargs['estado_general'],
            kwargs['tipo_impresora'],
            kwargs['conectividad'],
            kwargs['tipo_tinta'],
            kwargs['uso_estimado'],
            kwargs['nombre'],
            kwargs['garantia'],
            kwargs['modelo'],
            kwargs['telefono'],
            kwargs['correo'],
            kwargs['fecha_de_ingreso'],
            kwargs['marca'],
            kwargs['estado'],
            kwargs['precio'],
            kwargs.get('notas', '')
        )
        self.cursor.execute("""
            INSERT INTO impresoras (
                id_cliente, estado_general, tipo_impresora, conectividad,
                tipo_tinta, uso_estimado, nombre, garantia, modelo,
                telefono, correo, fecha_ingreso, marca, estado, precio, notas
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, datos)
        self.connect.commit()

    def obtener_impresoras(self):
        self.cursor.execute("SELECT * FROM impresoras")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def obtener_por_cliente_id(self, cliente_id):
        self.cursor.execute("SELECT * FROM impresoras WHERE id_cliente = ?", (cliente_id,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def editar_impresora(self, **kwargs):
        datos = (
            kwargs['estado_general'],
            kwargs['tipo_impresora'],
            kwargs['conectividad'],
            kwargs['tipo_tinta'],
            kwargs['uso_estimado'],
            kwargs['nombre'],
            kwargs['garantia'],
            kwargs['modelo'],
            kwargs['telefono'],
            kwargs['correo'],
            kwargs['fecha_de_ingreso'],
            kwargs['marca'],
            kwargs['estado'],
            kwargs['precio'],
            kwargs.get('notas', ''),
            kwargs['id_cliente']
        )

        self.cursor.execute("""
            UPDATE impresoras SET
                estado_general = ?, tipo_impresora = ?, conectividad = ?, tipo_tinta = ?, uso_estimado = ?,
                nombre = ?, garantia = ?, modelo = ?, telefono = ?, correo = ?,
                fecha_ingreso = ?, marca = ?, estado = ?, precio = ?, notas = ?
            WHERE id_cliente = ?
        """, datos)
        self.connect.commit()

    def eliminar_por_id_cliente(self, id_cliente):
        self.cursor.execute("DELETE FROM impresoras WHERE id_cliente = ?", (id_cliente,))
        self.connect.commit()

    def cerrar_conexion(self):
        self.connect.close()
