from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from src.inicio import InicioWindow
from src.controllers.auth import verificar_usuario


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Login")
        self.showMaximized()


        layout = QVBoxLayout()

        self.label_usuario = QLabel("Usuario:")
        self.input_usuario = QLineEdit()

        self.label_contraseña = QLabel("Contraseña:")
        self.input_contraseña = QLineEdit()
        self.input_contraseña.setEchoMode(QLineEdit.Password)

        self.boton_ingresar = QPushButton("Ingresar")
        self.boton_ingresar.clicked.connect(self.iniciar_sesion)

        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_contraseña)
        layout.addWidget(self.input_contraseña)
        layout.addWidget(self.boton_ingresar)

        self.setLayout(layout)

    def iniciar_sesion(self):
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()

        if verificar_usuario(usuario, contraseña):
            self.abrir_inicio()
        else:
            self.label_usuario.setText("❌ Usuario incorrecto")

    def abrir_inicio(self):
        self.inicio = InicioWindow()
        self.inicio.show()
        self.close()
