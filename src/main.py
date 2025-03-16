from PySide6.QtWidgets import QApplication
from src.login import LoginWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())