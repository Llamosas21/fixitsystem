import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from src.controllers.dispositivo_controller.impresora_controller import ImpresoraController
from utils.resource_finder import cargar_fuente_predeterminada
from src.views.base.base_dispositivo_window import BaseDispositivoWindow
from src.model.dispositivo_model.impresora_model import ImpresoraModel


class BaseImpresoraWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Base de Datos Impresora")
        self.controller = ImpresoraController()
        self._configurar_ventana()
        self.custom_font = cargar_fuente_predeterminada()
        self._crear_interfaz()
        self._cargar_datos()
        
    def _configurar_ventana(self):
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")

    def _crear_interfaz(self):
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border: none; border-radius: 15px;}")
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(20)
        
        self.label_titulo = QLabel("Impresoras Registradas")
        self.label_titulo.setFont(self.custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 40px; padding-top: 20px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)

        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setFixedSize(1000, 500)
        self.frame_contenedor.setStyleSheet("QFrame {background-color: #102540; border: none; border-radius: 20px;}")
        frame_contenedor_layout = QVBoxLayout(self.frame_contenedor)
        frame_contenedor_layout.setSpacing(15)
        frame_contenedor_layout.setContentsMargins(0, 30, 0, 0)
        
        self.arrow_button = QPushButton(self.frame)
        arrow = os.path.join(os.path.dirname(__file__), '../../resources/icons/icons8-sort-left-30.png')
        icon = QIcon(arrow)
        self.arrow_button.setIcon(icon)
        self.arrow_button.setIconSize(QSize(30, 30))
        self.arrow_button.setFixedSize(40, 40)
        self.arrow_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 5px;
            }
        """)
        self.arrow_button.move(20, 45)
        self.arrow_button.clicked.connect(self.volver)
        self.arrow_button.raise_()
        self.arrow_button.show()

        self.input_busqueda = QLineEdit()
        self.input_busqueda.setPlaceholderText("Buscar")
        self.input_busqueda.setFixedHeight(40)
        self.input_busqueda.setStyleSheet(
            """
            QLineEdit {
                background-color: #2a4a75;
                border-radius: 10px;
                color: white;
                padding-left: 10px;
                margin-left: 30px;
                margin-right: 30px;}""")
        
        frame_contenedor_layout.addWidget(self.input_busqueda)

        self.frame_fondo_db = QFrame(self.frame_contenedor)
        self.frame_fondo_db.setFixedSize(917, 360)
        self.frame_fondo_db.setStyleSheet("QFrame {background-color: #1e3f69; border-radius: 15px;}")
        frame_contenedor_layout.addWidget(self.frame_fondo_db, alignment=Qt.AlignCenter)

        self.table_widget = QTableWidget(self.frame_fondo_db)
        campos = [
            "ID", "ID Cliente", "Fecha Ingreso", "Marca", "Modelo", "Tipo Impresora",
            "Conectividad", "Tipo Tinta", "Uso Estimado", "Nombre", "Teléfono",
            "Correo", "Garantía", "Estado", "Notas"
        ]
        self.table_widget.setColumnCount(len(campos))
        self.table_widget.setHorizontalHeaderLabels(campos)

        # Estilo visual
        self.table_widget.setStyleSheet("""
            QTableWidget {
                background-color: #1e3f69;
                color: white;
                border: 2px solid #2a4a75;
            }
            QHeaderView::section {
                background-color: #2a4a75;
                color: white;
                border: 2px solid #2a4a75;
            }
            
            QScrollBar:horizontal {
                background: #102540;
                height: 12px;
                border: 1px solid #1e3f69;
            }

            QScrollBar::handle:horizontal {
                background: #4682B4;
            }

            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background: none;
                border: none;
                height: 0px;
            }

            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: none;
            }""")
        self.frame_contenedor.setLayout(frame_contenedor_layout)
        self.table_widget.setGeometry(10, 10,self.frame_fondo_db.width() - 20,self.frame_fondo_db.height() - 20)

        header = self.table_widget.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QHeaderView.Interactive)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setSortingEnabled(False)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.cellClicked.connect(self.handle_cell_click)

        boton_estilo = (
            """
            QPushButton {
                background-color: #102540;
                color: white;
                border-radius: 10px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #2a4a75;
            }
            """
        )

        self.boton_Agregar = QPushButton("Agregar")
        self.boton_Agregar.setStyleSheet(boton_estilo)
        self.boton_Agregar.setFixedSize(120, 35)
        self.boton_Agregar.clicked.connect(self.abrir_formulario_impresora)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_Agregar)
        botones_layout.setAlignment(Qt.AlignCenter)

        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)

        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

    def _cargar_datos(self):
        datos = self.controller.obtener_impresoras()
        self.table_widget.setRowCount(0)

        if not datos:
            return

        campos_a_mostrar = [
            "id", "id_cliente", "fecha_ingreso", "marca", "modelo", "tipo_impresora",
            "conectividad", "tipo_tinta", "uso_estimado", "nombre", "telefono",
            "correo", "garantia", "estado", "notas"
        ]

        self.lista_impresoras_original = datos
        self.table_widget.setColumnCount(len(campos_a_mostrar))
        self.table_widget.setRowCount(len(datos))
        self.table_widget.setHorizontalHeaderLabels(campos_a_mostrar)

        for fila, impresora in enumerate(self.lista_impresoras_original):
            for columna, campo in enumerate(campos_a_mostrar):
                valor = str(impresora.get(campo, ""))

                if campo == "notas":
                    palabras = valor.split()
                    valor = " ".join(palabras[:2]) + ("..." if len(palabras) > 2 else "")

                item = QTableWidgetItem(valor)

                if campo == "notas":
                    item.setToolTip(impresora.get("notas", ""))

                self.table_widget.setItem(fila, columna, item)

    def insertar_en_tabla_dinamica(self, fila):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        for columna, valor in enumerate(fila):
            item = QTableWidgetItem(str(valor))
            item.setTextAlignment(Qt.AlignCenter)
            self.table_widget.setItem(row_position, columna, item)

    def handle_cell_click(self, fila, columna):
        from utils.info_views import mostrar_popup_notas
        mostrar_popup_notas(self, self.table_widget, self.lista_impresoras_original, fila, columna)

    def volver(self):
        from views.data_base_client import BaseDateWindow
        self.base = BaseDateWindow()
        self.base.show()
        self.close()
        
    def abrir_formulario_impresora(self):
        from views.add_date import UpdateWindow
        self.ventana_formulario = UpdateWindow(dispositivo_inicial="Impresora")
        self.ventana_formulario.show()
        self.close()

    def abrir_actualizar_base(self):
        from views.add_date import UpdateWindow
        self.actualizar = UpdateWindow()
        self.actualizar.show()
        self.actualizar.closed.connect(self._cargar_datos)
        self.close()

    def closeEvent(self, event):
        self.controller.cerrar_conexion()
        super().closeEvent(event)


class ImpresoraWindow(BaseDispositivoWindow):
    def __init__(self, marca, modelo, numero_serie, estado, cliente_id):
        dispositivo = ImpresoraModel(marca, modelo, numero_serie, estado, cliente_id)
        super().__init__(dispositivo, titulo=f"Impresora {marca} {modelo}")
