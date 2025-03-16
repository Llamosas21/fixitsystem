from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class InicioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Inicio")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_titulo = QLabel("Bienvenido a FixItSystem")
        self.boton_salir = QPushButton("Cerrar")
        self.boton_salir.clicked.connect(self.close)

        layout.addWidget(self.label_titulo)
        layout.addWidget(self.boton_salir)

        self.setLayout(layout)
