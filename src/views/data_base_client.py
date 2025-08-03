import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QLineEdit, QSizePolicy, QScrollArea
)
from src.controllers.client_controller import ClientController
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from utils.resource_finder import cargar_fuente_predeterminada
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class BaseDateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Base de Datos")
        self.controller = ClientController()
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
        frame_contenedor_layout.setContentsMargins(30, 30, 30, 30)

        # BARRA DE BÚSQUEDA
        self.input_busqueda = QLineEdit()
        self.input_busqueda.setPlaceholderText("Buscar")
        self.input_busqueda.setFixedHeight(40)
        self.input_busqueda.setStyleSheet("""
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

        # SCROLL DE TARJETAS
        self.scroll_area = QScrollArea(self.frame_contenedor)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("QScrollArea { border: none; }")
        self.scroll_area.viewport().setStyleSheet("background: #102540;")
        self.tarjetas_container = QWidget()
        self.tarjetas_layout = QVBoxLayout(self.tarjetas_container)
        self.tarjetas_layout.setSpacing(18)
        self.tarjetas_layout.setContentsMargins(10, 10, 10, 10)
        self.tarjetas_container.setLayout(self.tarjetas_layout)
        self.scroll_area.setWidget(self.tarjetas_container)
        frame_contenedor_layout.addWidget(self.scroll_area)
        self.frame_contenedor.setLayout(frame_contenedor_layout)

        # BOTONES DE NAVEGACIÓN
        boton_estilo = """
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
        self.boton_Modificar = QPushButton("Agregar")
        self.boton_Modificar.setStyleSheet(boton_estilo)
        self.boton_Modificar.setFixedSize(120, 35)
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_Modificar)
        botones_layout.setAlignment(Qt.AlignCenter)
        self.boton_Modificar.clicked.connect(self.abrir_actualizar_base)

        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)

        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

        # BOTÓN RETROCESO
        self.arrow_button = QPushButton(self.frame)
        arrow = os.path.join(os.path.dirname(__file__), '../resources/icons/icons8-sort-left-30.png')
        icon = QIcon(arrow)
        icon_size = icon.actualSize(QSize(50, 50))
        self.arrow_button.setIcon(icon)
        self.arrow_button.setStyleSheet("QPushButton {background-color: transparent; border: none;}")
        self.arrow_button.setIconSize(icon_size)
        self.arrow_button.setFixedSize(icon_size.width(), icon_size.height())
        self.arrow_button.move(20, 40)
        self.arrow_button.clicked.connect(self.volver_al_inicio)

    def _cargar_datos(self):
        datos = self.controller.obtener_clientes()
        for i in reversed(range(self.tarjetas_layout.count())):
            widget = self.tarjetas_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        if not datos:
            return

        for row_data in datos:
            tarjeta = QFrame(self.tarjetas_container)
            tarjeta.setStyleSheet("""
                QFrame {
                    background-color: #1e3f69; /* Color base de la tarjeta */
                    border-radius: 16px;
                }
            """)
            tarjeta.setMinimumHeight(130)
            tarjeta.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            # Efecto sombra
            sombra = QGraphicsDropShadowEffect()
            sombra.setBlurRadius(20)
            sombra.setXOffset(0)
            sombra.setYOffset(4)
            sombra.setColor(Qt.black)
            tarjeta.setGraphicsEffect(sombra)

            tarjeta_layout = QHBoxLayout(tarjeta)
            tarjeta_layout.setContentsMargins(20, 15, 20, 15)
            tarjeta_layout.setSpacing(15)

            # INFO CLIENTE
            info_widget = QWidget(tarjeta)
            info_widget.setStyleSheet("background-color: #1e3f69;")  # Forzar fondo sólido
            info_layout = QVBoxLayout(info_widget)
            info_layout.setSpacing(5)  # Separación uniforme entre líneas
            info_layout.setContentsMargins(0, 0, 0, 0)

            # Nombre destacado
            label_nombre = QLabel(row_data[1])  # Nombre
            label_nombre.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
            info_layout.addWidget(label_nombre)

            # Datos secundarios en una sola línea
            label_info = QLabel(f"ID: {row_data[0]} | Dispositivo: {row_data[2]} | Fecha: {row_data[5]}")
            label_info.setStyleSheet("color: #90caf9; font-size: 12px; background-color: #1e3f69;")
            info_layout.addWidget(label_info)

            # Contacto (correo y teléfono)
            label_contacto = QLabel(f"{row_data[3]}   |   {row_data[4]}")
            label_contacto.setStyleSheet("color: #e3f2fd; font-size: 13px; background-color: #1e3f69;")
            info_layout.addWidget(label_contacto)

            info_widget.setLayout(info_layout)
            tarjeta_layout.addWidget(info_widget)

            # Imagen
            imagen_frame = QFrame(tarjeta)
            imagen_frame.setFixedSize(200, 100)
            imagen_frame.setStyleSheet("""
                QFrame {
                    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.7, stop:0 #42a5f5, stop:1 #2a4a75);
                    border-radius: 12px;
                    border: 2px solid #90caf9;
                }
            """)
            tarjeta_layout.addWidget(imagen_frame)

            tarjeta.setLayout(tarjeta_layout)
            self.tarjetas_layout.addWidget(tarjeta)

            tarjeta.mousePressEvent = lambda event, row=row_data: self.tarjeta_clickeada(row)

    def volver_al_inicio(self):
        from utils.alertas import mostrar_alerta
        mostrar_alerta("En desarrollo", "Esta función todavía no está disponible. Estamos trabajando en ello.", 400, 300)

    def abrir_actualizar_base(self):
        from views.add_date import UpdateWindow
        self.actualizar = UpdateWindow()
        self.actualizar.show()
        self.actualizar.closed.connect(self._cargar_datos)
        self.close()

    def tarjeta_clickeada(self, row_data):
        headers = ["ID Cliente", "Nombre", "Dispositivo", "Correo", "telefono", "fecha_de_ingreso"]
        fila_datos = {headers[i]: str(row_data[i]) for i in range(len(row_data))}
        self.datos_cliente_seleccionado = fila_datos
        self.buscar_datos_dispositivo()

    def buscar_datos_dispositivo(self):
        cliente_id = self.datos_cliente_seleccionado.get("ID Cliente")
        tipo_dispositivo = self.datos_cliente_seleccionado.get("Dispositivo")

        if not cliente_id or not tipo_dispositivo:
            print("❌ Falta el ID Cliente o el tipo de dispositivo.")
            return

        controlador = None
        if tipo_dispositivo == "Computadora":
            from src.controllers.dispositivo_controller.computadora_controller import ComputadoraController
            controlador = ComputadoraController()
        elif tipo_dispositivo == "Impresora":
            from src.controllers.dispositivo_controller.impresora_controller import ImpresoraController
            controlador = ImpresoraController()

        if controlador:
            dispositivos = controlador.obtener_por_cliente_id(cliente_id)
            self.datos_dispositivo = dispositivos
            from src.views.add_date import UpdateWindow
            self.ventana_update = UpdateWindow()
            self.ventana_update.show()
            self.ventana_update.cargar_datos_editar(self.datos_cliente_seleccionado, dispositivos)
            self.close()
        else:
            print("❌ Tipo de dispositivo no reconocido.")

    def closeEvent(self, event):
        self.controller.cerrar_conexion()
        super().closeEvent(event)

    def resizeEvent(self, event):
        self.showMaximized()
