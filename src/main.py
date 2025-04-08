import sys
import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
#from src.views.add_date import UpdateWindow  #
from views.login import LoginWindow

from src.model.client_model import ClienteModel

# Crear la base de datos y las tablas si no existen
cliente_model = ClienteModel()
cliente_model.inicializar_base()

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

"""#Temporal
from controllers.db_logical_client import DatabaseCliente
db=DatabaseCliente()
db.conectar()
db.crear_tablas()
db.insertar_cliente(
    id_cliente=None,
    dispositivo="Laptop",
    nombre="Juan Perez",
    telefono="987654321",
    correo="ana.lopez@example.com",
    fecha_ingreso="2025-03-29"
)
print("✅ Cliente insertado correctamente.")
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon_path = os.path.join(os.path.dirname(__file__), "resources/icons/FixiSystem_logo.png")
    app.setWindowIcon(QIcon(icon_path))

    #ventana = UpdateWindow()
    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())