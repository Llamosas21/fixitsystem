from PySide6.QtWidgets import QMessageBox, QInputDialog, QLineEdit

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
    
""" Alerta no funcional 
def pedir_id_cliente(titulo="Editar Cliente", mensaje="Ingresá el ID del cliente a editar"):
    id_cliente, ok = QInputDialog.getText(None, titulo, mensaje, QLineEdit.Normal)
    if ok and id_cliente.strip():
        return id_cliente.strip()
    else:
        return None
"""