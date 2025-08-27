from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class BaseDispositivoWindow(QWidget):
    def __init__(self, dispositivo, titulo="Información del dispositivo"):
        super().__init__()
        self.dispositivo = dispositivo
        self.setWindowTitle(titulo)
        self.layout = QVBoxLayout()
        self._configurar_interfaz()
        self.setLayout(self.layout)

    def _configurar_interfaz(self):
        for key, value in self.dispositivo.to_dict().items():
            self.layout.addWidget(QLabel(f"{key.capitalize()}: {value}"))

    # Métodos comunes para todos los dispositivos pueden agregarse aquí
