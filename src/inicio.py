from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFrame
from PySide6.QtGui import QFont, QFontDatabase
import os
from PySide6.QtCore import Qt


class InicioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Inicio")

        # Hacer que la ventana sea de tamaño fijo después de maximizar
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)

        self.showMaximized()  # Maximizar la ventana al iniciar

        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")

       
        font_path = os.path.join(os.path.dirname(__file__), 'resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            correct_font_name = font_families[0]
            custom_font = QFont(correct_font_name)  
            custom_font.setBold(True)
        else:
            print("❌ Error: No se encontró la familia de fuentes.")

        # Crear un QFrame centrado
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border: none; border-radius: 15px;}")
        self.frame.setLayout(QVBoxLayout())

        # Layout principal para centrar el frame
        layout = QVBoxLayout(self)
        layout.addWidget(self.frame, alignment=Qt.AlignCenter)

        # Widgets dentro del frame
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 30px;")
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.boton_salir = QPushButton("Cerrar")
        self.boton_salir.clicked.connect(self.close)

        self.frame.layout().addWidget(self.label_titulo)
        self.frame.layout().addWidget(self.boton_salir)

        self.setLayout(layout)

    def resizeEvent(self, event):
        """Evita que la ventana se redimensione."""
        self.showMaximized()
