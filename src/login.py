import os
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt
from src.inicio import InicioWindow
from src.controllers.auth import verificar_usuario

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Login")
        self.showMaximized()
        self.setStyleSheet(
            "QWidget {"
            "background-color: #0d0d0d;"
            "}"
        )

        # Cargar la fuente personalizada
        font_path = os.path.join(os.path.dirname(__file__), 'resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            correct_font_name = font_families[0]
            custom_font = QFont(correct_font_name)  
            custom_font.setBold(True)
        else:
            print("❌ Error: No se encontró la familia de fuentes.")

        # Crear un QFrame para contener los widgets
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 700)
        self.frame.setStyleSheet(
            "QFrame {background-color: #3084f2; "
            "border: none; "
            "border-radius: 15px;}"
        )
        self.frame.setLayout(QVBoxLayout())

        # Layout principal para la ventana
        layout = QVBoxLayout(self)
        layout.addWidget(self.frame, alignment=Qt.AlignCenter)  # Añadir el frame al layout principal

        # Widgets
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 40px;")
        self.label_titulo.setContentsMargins(0, 50, 0, 50)  # Ajustar márgenes

        self.input_usuario = QLineEdit()
        self.input_usuario.setPlaceholderText("Usuario")
        self.input_usuario.setFont(custom_font)
        self.input_usuario.setStyleSheet(
            "QLineEdit {background-color: #102540; color: #fff; border-radius: 10px; padding: 15px; margin: 10px;}"
        )

        self.input_contraseña = QLineEdit()
        self.input_contraseña.setPlaceholderText("Contraseña")
        self.input_contraseña.setEchoMode(QLineEdit.Password)
        self.input_contraseña.setFont(custom_font)
        self.input_contraseña.setStyleSheet(
            "QLineEdit {background-color: #102540; color: #fff; border-radius: 10px; padding: 15px; margin: 10px;}"
        )

        self.boton_ingresar = QPushButton("Ingresar")
        self.boton_ingresar.setFont(custom_font)
        self.boton_ingresar.setStyleSheet(
            "QPushButton {background-color: #102540; color: #fff; border-radius: 10px; padding: 15px; margin: 20px;}"
        )
        self.boton_ingresar.clicked.connect(self.abrir_inicio)

        # Añadir widgets al layout del frame
        self.frame.layout().addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.frame.layout().addWidget(self.input_usuario)
        self.frame.layout().addWidget(self.input_contraseña)
        self.frame.layout().addWidget(self.boton_ingresar)

    def abrir_inicio(self):
        self.inicio = InicioWindow()
        self.inicio.show()
        self.close()