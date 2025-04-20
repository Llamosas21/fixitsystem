import sys
import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

# Modelos
from src.model.client_model import ClienteModel

# Vistas principales
from src.views.login import LoginWindow
from src.views.data_base_client import BaseDateWindow
from src.views.dispositivos.computadora_view import BaseComputadoraWindow
# from src.views.add_date import UpdateWindow  # Pantalla para agregar un dispositivo (opcional)

#vista Secundaria
from src.views.exports.boleta.view_boleta import ViewBoleta

# Inicializa la base de datos (crea tabla si no existe)
cliente_model = ClienteModel()

# Asegura que el directorio raíz del proyecto esté en el PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def borrar_base_datos(nombre_archivo):
    """Elimina el archivo de base de datos si existe."""
    if os.path.exists(nombre_archivo):
        try:
            os.remove(nombre_archivo)
            print(f"🗑️ Base de datos '{nombre_archivo}' eliminada correctamente.")
        except Exception as e:
            print(f"❌ Error al intentar borrar la base de datos: {e}")
    else:
        print(f"⚠️ La base de datos '{nombre_archivo}' no existe, no se eliminó nada.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Icono principal
    icon_path = os.path.join(os.path.dirname(__file__), "resources/icons/FixiSystem_logo.png")
    app.setWindowIcon(QIcon(icon_path))

    os.system('clear')  # Limpia la consola (en sistemas tipo Unix)

    #--- !!CUIDADO BORRAR BASE¡¡ ---
    #borrar_base_datos("src/database/fixitsystem.db")

    # --- Ventanas principales del sistema ---
    #ventana = LoginWindow()                 # Pantalla de login
    #ventana = BaseComputadoraWindow()       # Vista de base de datos de computadoras
    ventana = BaseDateWindow()              # Vista general de base de datos de clientes

    # --- Ventanas Secundarias del sistema ---
    #ventana = ViewBoleta()                 # Vista boleta
    #ventana.mostrar_vista_previa()         # Llama al botón y abre un html (sin hacer nada)
    sys.exit(app.exec())
