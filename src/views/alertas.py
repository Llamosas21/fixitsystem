from PySide6.QtWidgets import QMessageBox

def mostrar_confirmacion(titulo, mensaje,ancho,alto):
    msg = QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setText(mensaje)
    msg.setIcon(QMessageBox.Question)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.resize(ancho,alto)
    return msg.exec() == QMessageBox.Yes

def mostrar_alerta(titulo, mensaje,ancho,alto):
    msg = QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setText(mensaje)
    msg.setIcon(QMessageBox.Warning)
    msg.resize(ancho,alto)
    msg.exec()

def mostrar_info(titulo, mensaje,ancho,alto):
    msg = QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setText(mensaje)
    msg.setIcon(QMessageBox.Information)
    msg.resize(ancho,alto)
    msg.exec()


"""
    Método que controla lo que se hace al presionar el registro que contiene
    las notas referidas al producto. Muestra un popup con las notas completas
    del producto seleccionado.
"""