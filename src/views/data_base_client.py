import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView
)
from src.controllers.client_controller import ClientController
from PySide6.QtGui import  QIcon
from PySide6.QtCore import Qt, QSize
from views.utils.resource_finder import cargar_fuente_personalizada


class BaseDateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Base de Datos")
        self.controller = ClientController()
        self._configurar_ventana()
        self.custom_font = cargar_fuente_personalizada()
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
        
        # TÍTULO
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(self.custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 40px; padding-top: 20px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)
        
        # FRAME CONTENEDOR
        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setFixedSize(1000, 500)
        self.frame_contenedor.setStyleSheet("QFrame {background-color: #102540; border: none; border-radius: 20px;}")
        frame_contenedor_layout = QVBoxLayout(self.frame_contenedor)
        frame_contenedor_layout.setSpacing(15)
        frame_contenedor_layout.setContentsMargins(0, 30, 0, 0)
        
        # BARRA DE BÚSQUEDA
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
                margin-right: 30px;
            }
            """)
        frame_contenedor_layout.addWidget(self.input_busqueda)
        
        # BASE DE DATOS
        self.frame_fondo_db = QFrame(self.frame_contenedor)
        self.frame_fondo_db.setFixedSize(917, 360)
        self.frame_fondo_db.setStyleSheet("QFrame {background-color: #1e3f69; border-radius: 15px;}")
        frame_contenedor_layout.addWidget(self.frame_fondo_db, alignment=Qt.AlignCenter)

        # TABLA CON LOS DATOS
        self.table_widget = QTableWidget(self.frame_fondo_db)
        self.table_widget.setColumnCount(6)  # Número total de columnas en la tabla 'clientes'
        self.table_widget.setHorizontalHeaderLabels([
            "ID Cliente", "Nombre", "Dispositivo", "Correo", "telefono",
            "fecha_de_ingreso"
        ])
        self.table_widget.setStyleSheet("""
        QTableWidget {
            background-color: #1e3f69;
            color: white;
            border: 2px solid #2a4a75;  /* Agrega un borde alrededor de la tabla */
            border-radius: 1px;  /* Bordes redondeados */}
        QHeaderView::section {
            background-color: #2a4a75;
            color: white;
            border: 2px solid #2a4a75;}
        QHeaderView::section:vertical {
            background-color: #2a4a75;  /* Cambia el color del encabezado vertical */
            color: white;
            border: 2px solid #2a4a75;}""")
        
        self.table_widget.setGeometry(10, 10, self.frame_fondo_db.width() - 20, self.frame_fondo_db.height() - 20)
        self.table_widget.horizontalHeader().setStretchLastSection(True)  # Ajusta la última columna
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Ajusta todas las columnas
        self.table_widget.verticalHeader().setVisible(False)
        self.frame_contenedor.setLayout(frame_contenedor_layout)
        self.table_widget.cellClicked.connect(self.celda_clickeada)
      
        # BOTONES DE NAVEGACIÓN
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
            """)
        
        
        # Solo un botón, renombrado a "Modificar"
        self.boton_Modificar = QPushButton("Modificar")
        self.boton_Modificar.setStyleSheet(boton_estilo)
        self.boton_Modificar.setFixedSize(120, 35)

        # LAYOUT DE BOTÓN
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_Modificar)
        botones_layout.setAlignment(Qt.AlignCenter)

        # ACCIÓN DEL BOTÓN "Modificar"
        self.boton_Modificar.clicked.connect(self.abrir_actualizar_base)
        
        # ORGANIZAR ELEMENTOS
        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)
        
        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

        # BOTÓN RETROCESO
        self.arrow_button = QPushButton(self.frame) 
        arrow = os.path.join(os.path.dirname(__file__), '../resources/icons/icons8-sort-left-30.png')
        icon = QIcon(arrow) 
        icon_size = icon.actualSize(QSize(50, 50))  
        self.arrow_button.setIcon(icon)

        # ESTILO DEL BOTÓN
        self.arrow_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;  
                border: none;  
            }""")

        # Ajustar el tamaño del botón
        self.arrow_button.setIconSize(icon_size)
        self.arrow_button.setFixedSize(icon_size.width(), icon_size.height()) 
        self.arrow_button.move(20, 20) 

        # Acción del botón
        self.arrow_button.clicked.connect(self.volver_al_inicio)    
    
    def _cargar_datos(self):
        datos = self.controller.obtener_clientes()

        if not datos:  
                #print("⚠️ No se encontraron clientes en la base de datos.")
                self.table_widget.setRowCount(0)
                return

        # Configurar el número de filas en el QTableWidget
        self.table_widget.setRowCount(len(datos))

        # Insertar los datos en el QTableWidget
        for row_index, row_data in enumerate(datos):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table_widget.setItem(row_index, col_index, item)

    def volver_al_inicio(self):
        from views.start import StartWindow
        self.login = StartWindow()
        self.login.show()
        self.close()

    def abrir_actualizar_base(self):
        from views.add_date import UpdateWindow
        self.actualizar = UpdateWindow()
        self.actualizar.show()
        self.actualizar.closed.connect(self._cargar_datos)
        self.close()
    
    def celda_clickeada(self, row, column):
        if self.table_widget.horizontalHeaderItem(column).text() == "Dispositivo":
            dispositivo = self.table_widget.item(row, column).text().lower()  # Convertir a minúsculas

            # Diccionario de dispositivos y vistas asociadas
            vistas_dispositivos = {
                "computadora": ("computadora_view", "BaseComputadoraWindow"),
                "notebook": ("notebook_view", "BaseNotebookWindow"),
                "consola": ("consola_view", "BaseConsolaWindow"),
                "celular": ("celular_view", "BaseCelularWindow"),
                "tablet": ("tablet_view", "BaseTabletWindow"),
                "personalizado": ("personalizado_view", "BasePersonalizadoWindow"),
            }

            clase_view = vistas_dispositivos.get(dispositivo)
            #print(clase_view)  # Verifica el nombre del archivo a importar

            if clase_view:
                nombre_modulo, nombre_clase = clase_view
                self.abrir_vista_dinamica(nombre_modulo, nombre_clase)
            else:
                print(f"⚠️ Vista no definida para el dispositivo: {dispositivo}")

    def abrir_vista_dinamica(self, nombre_modulo, nombre_clase):
        try:
            modulo = __import__(f"src.views.dispositivos.{nombre_modulo}", fromlist=[nombre_clase])
            clase = getattr(modulo, nombre_clase)
            self.vista = clase()
            self.vista.show()
            self.close()
        except Exception as e:
            print(f"❌ Error al abrir la vista {nombre_modulo}: {e}")

            
    def closeEvent(self, event):
        self.controller.cerrar_conexion()
        super().closeEvent(event)

    def resizeEvent(self, event):# En un futuro se deberá quitar
        """Evita que la ventana se redimensione."""
        self.showMaximized()