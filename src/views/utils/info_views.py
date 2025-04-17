from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton


class DialogoNotas(QDialog):
    def __init__(self, parent, nota):
        super().__init__(parent)
        self.setWindowTitle("Notas")
        self.setFixedSize(625, 404)  # Tamaño fijo

        layout = QVBoxLayout(self)

        self.caja_texto = QTextEdit()
        self.caja_texto.setReadOnly(True)
        
        nota_limpia = nota.strip() if nota and nota.strip() else "(Sin notas)"
        self.caja_texto.setText(nota_limpia)

        self.caja_texto.setStyleSheet("""
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
        self.move(
            parent.geometry().center() - self.rect().center()
        )


        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.clicked.connect(self.accept)
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

        layout.addWidget(self.caja_texto)
        layout.addWidget(boton_cerrar)

        self.setStyleSheet("QDialog { background-color: #1F3F68; }")

def mostrar_popup_notas(parent, table_widget, lista_computadoras, fila, columna):
    nombre_columna = table_widget.horizontalHeaderItem(columna).text()
    if nombre_columna.lower() == "notas":
        id_cliente = table_widget.item(fila, 1).text()

        nota_completa = ""
        for computadora in lista_computadoras:
            if computadora["id_cliente"] == id_cliente:
                nota_completa = computadora.get("notas", "")
                break

        dialogo = DialogoNotas(parent, nota_completa)
        dialogo.exec()