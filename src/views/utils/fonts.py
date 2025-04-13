import os
from PySide6.QtGui import QFontDatabase, QFont

def cargar_fuente_personalizada():
    ruta_fuente = os.path.join(os.path.dirname(__file__), '../../resources/fonts/SongMyung-Regular.ttf')
    id_fuente = QFontDatabase.addApplicationFont(ruta_fuente)
    familias = QFontDatabase.applicationFontFamilies(id_fuente)

    if familias:
        fuente = QFont(familias[0])
        fuente.setBold(True)
        return fuente
    else:
        print("⚠️ No se pudo cargar la fuente personalizada.")
        return QFont()
