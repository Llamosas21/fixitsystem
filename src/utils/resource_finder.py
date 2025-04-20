import sys,os,re
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


def get_ruta_base():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def get_ruta_arch_exportados():
    return os.path.join(get_ruta_base(), "arch_exportados")

def crear_directorio_cliente(nombre_completo, id_cliente):
    # Sanitizar nombre (quitar espacios, tildes, símbolos raros, etc.)
    nombre_limpio = re.sub(r'\W+', '', nombre_completo.replace(" ", "_"))

    # Construir nombre de carpeta
    carpeta = f"Cliente_{nombre_limpio}_ID_{id_cliente}"

    # Ruta base del proyecto (asume que estás parado en src o más profundo)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))  # Sube desde /src/views/exports
    ruta_exports = os.path.join(base_dir, "arch_exportados")
    ruta_cliente = os.path.join(ruta_exports, carpeta)

    # Crear carpeta si no existe
    os.makedirs(ruta_cliente, exist_ok=True)

    print(f"📁 Ruta de exportación: {ruta_cliente}")
    return ruta_cliente