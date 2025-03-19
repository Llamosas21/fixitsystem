import os
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt

class InicioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Inicio")

        # Configurar la ventana maximizada
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")

        # Cargar la fuente personalizada
        font_path = os.path.join(os.path.dirname(__file__), 'resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            correct_font_name = font_families[0]
            custom_font = QFont(correct_font_name)
            custom_font.setBold(True)
        else:
            print("Error: No se encontró la familia de fuentes.")

        # FRAME PRINCIPAL (Celeste)
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border: none; border-radius: 15px;}")

        # Layout para el frame principal
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(10)


        # Título del programa 
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 30px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)


        # Frame interno (Azul oscuro)
        self.frame_interno = QFrame(self.frame)
        self.frame_interno.setFixedSize(1000, 500)
        self.frame_interno.setStyleSheet("QFrame {background-color: #1e3f69; border: none; border-radius: 20px;}")

        frame_interno_layout = QVBoxLayout(self.frame_interno)
        frame_interno_layout.setSpacing(15)


        # Barra de busqueda
        self.input_busqueda = QLineEdit()
        self.input_busqueda.setPlaceholderText("Buscar")
        self.input_busqueda.setFixedHeight(40)
        self.input_busqueda.setStyleSheet("""
            QLineEdit {
                background-color: #2a4a75;
                border-radius: 10px;
                color: white;
                padding-left: 10px;
            }
        """)

    
        # Se definen los frames internos y externos
        self.frame_arriba = QFrame(self.frame_interno)
        self.frame_arriba.setFixedSize(900, 150)
        self.frame_arriba.setStyleSheet("QFrame {background-color: #1e3f69; border-radius: 10px;}")

        self.frame_abajo = QFrame(self.frame_interno)
        self.frame_abajo.setFixedSize(900, 150)
        self.frame_abajo.setStyleSheet("QFrame {background-color: #1e3f69; border-radius: 10px;}")

        # Agregar elementos al frame interno
        frame_interno_layout.addWidget(self.input_busqueda)
        frame_interno_layout.addWidget(self.frame_arriba, alignment=Qt.AlignHCenter)
        frame_interno_layout.addWidget(self.frame_abajo, alignment=Qt.AlignHCenter)
        self.frame_interno.setLayout(frame_interno_layout)


        # BOTONES DE NAVEGACIÓN
        boton_estilo = """
            QPushButton {
                background-color: #1e3f69;
                color: white;
                border-radius: 10px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #2a4a75;
            }
        """

        self.boton_usuarios = QPushButton("Usuarios")
        self.boton_usuarios.setStyleSheet(boton_estilo)

        self.boton_reportes = QPushButton("Reportes")
        self.boton_reportes.setStyleSheet(boton_estilo)

        self.boton_fichas = QPushButton("Fichas")
        self.boton_fichas.setStyleSheet(boton_estilo)

        # Layout horizontal para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_usuarios)
        botones_layout.addWidget(self.boton_reportes)
        botones_layout.addWidget(self.boton_fichas)
        botones_layout.setAlignment(Qt.AlignCenter)

        # ==========================
        # ORGANIZAR ELEMENTOS
        # ==========================
        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_interno, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)

        # ==========================
        # LAYOUT PRINCIPAL
        # ==========================
        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

    def resizeEvent(self, event):
        """Evita que la ventana se redimensione."""
        self.showMaximized()
