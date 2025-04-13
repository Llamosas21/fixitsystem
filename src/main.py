import sys
import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from src.model.client_model import ClienteModel

from views.login import LoginWindow

#from src.views.add_date import UpdateWindow  #Pantalla para agregar un dispositivo
#from src.views.dispositivos.computadora_view import BaseComputadoraWindow

cliente_model = ClienteModel() # Crear la base de datos y la tabla 'clientes' si no existen

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def borrar_base_datos(nombre_archivo):
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
    icon_path = os.path.join(os.path.dirname(__file__), "resources/icons/FixiSystem_logo.png")
    app.setWindowIcon(QIcon(icon_path))
    os.system('clear')
    #borrar_base_datos("src/database/fixitsystem.db")     #Borra la base de datos 
    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())