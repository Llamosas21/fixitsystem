import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication
from inicio import InicioWindow  # Cambiar por la importación correcta # from src.login import LoginWindow
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InicioWindow() # Cambiar por la clase correcta # ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())