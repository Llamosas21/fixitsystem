from PySide6.QtGui import QIcon

from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton
from PySide6.QtCore import Qt

def mostrar_popup_notas(parent, table_widget, lista_computadoras, fila, columna):
    nombre_columna = table_widget.horizontalHeaderItem(columna).text()
    if nombre_columna.lower() == "notas":
        id_cliente = table_widget.item(fila, 1).text()

        nota_completa = ""
        for computadora in lista_computadoras:
            if computadora["id_cliente"] == id_cliente:
                nota_completa = computadora.get("notas", "")
                break

        dialogo = QDialog(parent)
        dialogo.setWindowTitle("Notas")
        dialogo.setMinimumSize(400, 300)

        layout = QVBoxLayout(dialogo)

        caja_texto = QTextEdit()
        caja_texto.setReadOnly(True)
        caja_texto.setText(nota_completa or "(Sin notas)")

        # Asegurar scroll automático
        caja_texto.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        caja_texto.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        caja_texto.setStyleSheet("""
            QTextEdit {
                background-color: #1F3F68;
                color: white;
                font-size: 14px;
                border: none;
            }

            QScrollBar:vertical {
                background: #102540;
                width: 12px;
                border: 1px solid #1e3f69;
            }

            QScrollBar::handle:vertical {
                background: #4682B4;
                min-height: 20px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
                border: none;
                height: 0px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
        """)





        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.clicked.connect(dialogo.accept)
        boton_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #102540;
                color: white;
                padding: 6px 12px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #1c3a5e;
            }""")

        layout.addWidget(caja_texto)
        layout.addWidget(boton_cerrar)

        dialogo.setStyleSheet("QDialog { background-color: #1F3F68; }")

        dialogo.exec()