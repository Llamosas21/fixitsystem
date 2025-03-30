import sys
import os
from PySide6.QtGui import QIcon

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication
from src.views.login import LoginWindow
"""
#Temporal
from database.logic_data_base.db_logic import DatabaseCliente
db=DatabaseCliente()
db.conectar()
db.crear_tablas()
db.insertar_cliente(
    id_cliente=None,
    nombre="Juan Perez",
    dispositivo="Laptop",
    correo="ana.lopez@example.com",
    telefono="987654321",
    fecha_ingreso="2025-03-29"
)
print("✅ Cliente insertado correctamente.")
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon_path = os.path.join(os.path.dirname(__file__), "resources/icons/FixiSystem_logo.png")
    app.setWindowIcon(QIcon(icon_path))

    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())