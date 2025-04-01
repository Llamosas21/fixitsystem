import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QGridLayout, QLineEdit, QComboBox, QTextEdit, QDateEdit,QSpinBox
)
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt, QDate

class UpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Actualizar Datos")
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")
        self._cargar_fuente_personalizada()
        self._crear_interfaz()

    def _cargar_fuente_personalizada(self):
        font_path = os.path.join(os.path.dirname(__file__), '../resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        self.custom_font = QFont(font_families[0], 14, QFont.Bold) if font_families else QFont()

    def _crear_interfaz(self):
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border-radius: 15px;}")

        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(10)

        self.label_titulo = QLabel("FixItSystem", self)
        self.label_titulo.setFont(self.custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 40px; padding-top: 15px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)

        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setFixedSize(1000, 500)
        self.frame_contenedor.setStyleSheet("QFrame {background-color: #102540; border-radius: 20px;}")

        self.grid_layout = QGridLayout()
        self.campo_dispositivo = QComboBox()
        self.campo_dispositivo.addItems(["Personalizado", "Computadora", "Notebook", "Consola", "Celular", "Tablet"])
        self.campo_dispositivo.setFixedSize(150, 30)
        self.campo_dispositivo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")
        self.campo_dispositivo.currentIndexChanged.connect(self.actualizar_campos_por_dispositivo)

        self.grid_layout.addWidget(self.campo_dispositivo, 0, 0, 1, 2)
        self.mostrar_campos_personalizado()
        self.grid_layout.setVerticalSpacing(10)  # Reduce el espacio vertical entre filas

        frame_contenedor_layout = QVBoxLayout(self.frame_contenedor)
        frame_contenedor_layout.addLayout(self.grid_layout)

        boton_estilo = """
            QPushButton {
                background-color: #102540;
                color: white;
                border-radius: 10px;
                padding: 8px 20px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #2a4a75;
            }
        """

        self.boton_volver = QPushButton("Volver", self)
        self.boton_historial = QPushButton("Historial", self)
        self.boton_aceptar = QPushButton("Aceptar", self)

        for boton in [self.boton_volver, self.boton_historial, self.boton_aceptar]:
            boton.setStyleSheet(boton_estilo)
            boton.setFixedSize(120, 35)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_volver)
        botones_layout.addWidget(self.boton_historial)
        botones_layout.addWidget(self.boton_aceptar)
        botones_layout.setAlignment(Qt.AlignCenter)

        self.boton_volver.clicked.connect(self.volver)

        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)

        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

    def limpiar_grid_layout(self):
        """Limpia todos los widgets del grid_layout excepto el QComboBox."""
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget and widget != self.campo_dispositivo:
                widget.deleteLater()

    def actualizar_campos_por_dispositivo(self):
        """Actualiza los campos según el dispositivo seleccionado."""
        self.limpiar_grid_layout()
        dispositivo = self.campo_dispositivo.currentText()
        metodo = getattr(self, f"mostrar_campos_{dispositivo.lower()}", self.mostrar_campos_personalizado)
        metodo()

    def mostrar_campos_personalizado(self):
        etiquetas = [
            "Fecha de ingreso", "Procesador", "Tarjeta gráfica", "Nombre", "Garantía",
            "Memoria", "Placa", "Teléfono", "Modelo", "Fuente", 
            "Pantalla", "Correo", "S.O.", "Ram", "Estado"
        ]
        self._agregar_campos(etiquetas)

    def mostrar_campos_computadora(self):
        etiquetas = [
            "Fecha de ingreso", "Procesador", "Tarjeta gráfica", "Nombre", "Garantía",
            "Memoria", "Placa", "Teléfono", "Modelo", "Fuente", 
            "Pantalla", "Correo", "S.O.", "Ram", "Estado"
        ]
        self._agregar_campos(etiquetas)

    def mostrar_campos_notebook(self):
        etiquetas = [
            "Fecha de ingreso", "Estado Cargador", "Tarjeta gráfica", "Nombre", "Garantía",
            "Procesador", "Placa", "Teléfono", "Modelo", "Memoria", 
            "Pantalla", "Correo", "TIM", "Ram", "Estado"
        ]
        self._agregar_campos(etiquetas)

    def mostrar_campos_consola(self):
        etiquetas = [
            "Fecha de ingreso", "Procesador", "Cantidad Mandos", "Nombre", "Garantía",
            "Memoria", "Mandos estado", "Teléfono", "Modelo", "Pantalla", 
            "Correo", "S.O.", "Ram", "Estado", "TIM"
        ]
        self._agregar_campos(etiquetas)

    def mostrar_campos_celular(self):
        etiquetas = [
            "Fecha de ingreso", "Estado Cargador", "Bateria", "Nombre", "Garantía",
            "Memoria", "Placa", "Teléfono", "Modelo", "Pantalla", 
            "Correo", "S.O.", "Ram", "Estado"
        ]
        self._agregar_campos(etiquetas)

    def mostrar_campos_tablet(self):
        etiquetas = [
            "Fecha de ingreso", "Estado Cargador", "Bateria", "Nombre", "Garantía",
            "Memoria", "Placa", "Teléfono", "Modelo", "Pantalla", 
            "Correo", "S.O.", "Ram", "Estado"
        ]
        self._agregar_campos(etiquetas)

    def _agregar_campos(self, etiquetas):
        columnas = 4
        for i, texto in enumerate(etiquetas):
            label = QLabel(texto, self)
            label.setStyleSheet("color: white; font-size: 12px; font-weight: bold;")
            label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            # Campos especiales para "Fecha de ingreso" y "Garantía"
            if texto in ["Fecha de ingreso", "Garantía"]:
                campo = QDateEdit(self)
                campo.setDate(QDate.currentDate())  
                campo.setDisplayFormat("dd-MM-yyyy")  
                campo.setCalendarPopup(True)  
                campo.setFixedSize(130, 30) 
                campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

            # Campo especial para "Estado"
            elif texto == "Estado" or texto == "Mandos estado" or texto == "Estado Cargador":
                campo = QComboBox(self)
                campo.addItems(["New", "Used", "Refurbished"])
                campo.setFixedSize(130, 30)
                campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

            # Campo especial para "Cantidad Mandos"
            elif texto == "Cantidad Mandos":
                campo = QSpinBox(self)
                campo.setRange(1, 10)  # Establece el rango de valores permitidos (1 a 10)
                campo.setFixedSize(130, 30)
                campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

            # Campo genérico (QLineEdit)
            else:
                campo = QLineEdit(self)
                campo.setFixedSize(130, 30)
                campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

            fila, columna = divmod(i, columnas)
            self.grid_layout.addWidget(label, fila + 1, columna * 2)
            self.grid_layout.addWidget(campo, fila + 1, columna * 2 + 1)

        # Añadir QTextEdit "Notas" debajo de los campos
        fila_actual = (len(etiquetas) // columnas) + 1
        if len(etiquetas) % columnas != 0:
            fila_actual += 1

        self.nota = QTextEdit()
        self.nota.setFixedHeight(200)
        self.nota.setPlaceholderText("Notas")
        self.nota.setStyleSheet("""
            background-color: #2a4a75;
            color: white;
            border-radius: 5px;
            padding: 5px;
            margin: 10px;
            font-weight: bold;
        """)
        self.grid_layout.addWidget(self.nota, fila_actual, 0, 1, columnas * 2)

    def volver(self):
        from views.data_base_client import BaseDateWindow
        self.base = BaseDateWindow()
        self.base.show()
        self.close()