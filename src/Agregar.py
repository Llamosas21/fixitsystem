import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QGridLayout, QLineEdit, QTextEdit
)
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt

class UpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Actualizar Datos")
        self._configurar_ventana()
        self._cargar_fuente_personalizada()
        self._crear_interfaz()

    def _configurar_ventana(self):
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")

    def _cargar_fuente_personalizada(self):
        font_path = os.path.join(os.path.dirname(__file__), 'resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            self.custom_font = QFont(font_families[0], 14)
            self.custom_font.setBold(True)
        else:
            print("Error: No se encontró la familia de fuentes.")
            self.custom_font = QFont()

    def _crear_interfaz(self):
        # FRAME PRINCIPAL
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border: none; border-radius: 15px;}")
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(10)

        # TÍTULO
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(self.custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 24px; padding-top: 15px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)

        # FRAME CONTENEDOR OSCURO
        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setFixedSize(1000, 500)
        self.frame_contenedor.setStyleSheet("QFrame {background-color: #102540; border: none; border-radius: 20px;}")
        frame_contenedor_layout = QVBoxLayout(self.frame_contenedor)

        # GRID PARA LOS CAMPOS DE ENTRADA
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        etiquetas = [
            "Producto", "Fecha ingreso", "Precio", "ID",
            "Garantía fecha", "Garantías", "Modelo", "S.O.",
            "Procesador", "Memoria", "Fuente", "Ram",
            "Nombre", "Teléfono", "Domicilio", "Correo"
        ]

        self.entradas = {}

        for i, texto in enumerate(etiquetas):
            label = QLabel(texto)
            label.setStyleSheet("color: white; font-size: 12px;")
            campo = QLineEdit()
            campo.setFixedSize(150, 30)
            campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")
            grid_layout.addWidget(label, i // 4, (i % 4) * 2)
            grid_layout.addWidget(campo, i // 4, (i % 4) * 2 + 1)
            self.entradas[texto] = campo

        # CAMPOS DE TEXTO MULTILÍNEA
        self.observaciones = QTextEdit()
        self.observaciones.setFixedSize(320, 80)
        self.observaciones.setPlaceholderText("Observaciones")
        self.observaciones.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding: 5px;")

        self.nota = QTextEdit()
        self.nota.setFixedSize(320, 80)
        self.nota.setPlaceholderText("Nota")
        self.nota.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding: 5px;")

        grid_layout.addWidget(QLabel("Observaciones"), 4, 0, 1, 2)
        grid_layout.addWidget(self.observaciones, 5, 0, 1, 4)
        grid_layout.addWidget(QLabel("Nota"), 4, 4, 1, 2)
        grid_layout.addWidget(self.nota, 5, 4, 1, 4)

        frame_contenedor_layout.addLayout(grid_layout)
        self.frame_contenedor.setLayout(frame_contenedor_layout)

        # BOTONES DE ACCIÓN
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

        self.boton_volver = QPushButton("Volver")
        self.boton_historial = QPushButton("Historial")
        self.boton_aceptar = QPushButton("Aceptar")

        for boton in [self.boton_volver, self.boton_historial, self.boton_aceptar]:
            boton.setStyleSheet(boton_estilo)
            boton.setFixedSize(120, 40)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_volver)
        botones_layout.addWidget(self.boton_historial)
        botones_layout.addWidget(self.boton_aceptar)
        botones_layout.setAlignment(Qt.AlignCenter)

        # ORGANIZAR ELEMENTOS
        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)

        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

    def resizeEvent(self, event):
        """Evita que la ventana se redimensione."""
        self.showMaximized()
