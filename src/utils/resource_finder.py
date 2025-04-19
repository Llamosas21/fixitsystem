import os
from PySide6.QtGui import QFontDatabase, QFont

def cargar_fuente_predeterminada():
    """
    Carga y devuelve la fuente predeterminada del sistema.
    La funcionalidad para cargar una fuente personalizada está comentada.
 
    ruta_fuente = os.path.join(os.path.dirname(__file__), '../resources/fonts/SongMyung-Regular.ttf') # Ya descargada 
    id_fuente = QFontDatabase.addApplicationFont(ruta_fuente)
    familias = QFontDatabase.applicationFontFamilies(id_fuente)
    
    if familias:
        fuente = QFont(familias[0])
        fuente.setBold(True)
        return fuente
    else:
        print("⚠️ No se pudo cargar la fuente personalizada.")
    """
    fuente_predeterminada = QFont()
    """ En caso de querer saber el tipo de fuente 
    print(f"Fuente predeterminada (familia): {fuente_predeterminada.family()}")
    print(f"Fuente predeterminada (tamaño): {fuente_predeterminada.pointSize()}")
    print(f"Fuente predeterminada (es negrita): {fuente_predeterminada.bold()}")
    print(f"Fuente predeterminada (es itálica): {fuente_predeterminada.italic()}")
    """
    return fuente_predeterminada    #La fuente depende de la configuración de sistema
