from PySide6.QtWidgets import QPushButton, QVBoxLayout, QFrame, QLabel, QWidget
from src.utils.resource_finder import cargar_fuente_predeterminada
from PySide6.QtCore import Qt, QSize
from src.views.exports.boleta.create_boleta import vista_previa_boleta
from PySide6.QtGui import QIcon
import os 



class ViewBoleta(QWidget):
    def __init__(self, cliente_info, dispositivo_info):
        super().__init__()
        self.setWindowTitle("Vista Previa Boleta")
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")
        self.showMaximized()
        self.custom_font = cargar_fuente_predeterminada()
        self.cliente_info = cliente_info
        self.dispositivo_info = dispositivo_info
        """
        print("Datos del Cliente (mostrar_vista_previa):")
        print(cliente_info)
        
        print("Datos del Dispositivo (mostrar_vista_previa):")
        print(dispositivo_info)
        """
        self._crear_interfaz()

    def _crear_interfaz(self):
        # Frame principal con estilo
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 700)
        self.frame.setStyleSheet("""
            QFrame {
                background-color: #3084f2;
                border-radius: 15px;
            }
        """)

        # Layout interno del frame
        frame_layout = QVBoxLayout()
        frame_layout.setSpacing(20)
        frame_layout.setContentsMargins(20, 20, 20, 20)
        self.frame.setLayout(frame_layout)

        # Título
        self.label_titulo = QLabel("Vista Previa de Boleta", self)
        self.label_titulo.setFont(self.custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 32px; padding-top: 10px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)
        frame_layout.addWidget(self.label_titulo)

       # Estilo para ambos botones
        boton_estilo_vertical = """
            QPushButton {
                background-color: #102540;
                color: white;
                border-radius: 10px;
                padding: 10px 35px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2a4a75;
            }
        """

        # Crear botones
        self.boton_previa = QPushButton("Vista Previa", self)
        self.boton_descargar = QPushButton("Descargar", self)

        # Aplicar estilo
        self.boton_previa.setStyleSheet(boton_estilo_vertical)
        self.boton_descargar.setStyleSheet(boton_estilo_vertical)

        # Conexión de señales
        self.boton_previa.clicked.connect(self.mostrar_vista_previa)
        self.boton_descargar.clicked.connect(self.imprimir)

        # Layout para los botones (vertical)
        botones_layout_vertical = QVBoxLayout()
        botones_layout_vertical.setAlignment(Qt.AlignHCenter)
        botones_layout_vertical.setSpacing(40)  # Espacio entre los botones

        botones_layout_vertical.addWidget(self.boton_previa)
        botones_layout_vertical.addWidget(self.boton_descargar)

        # Insertar el layout dentro del contenedor principal
        frame_layout.addStretch()
        frame_layout.addLayout(botones_layout_vertical)
        frame_layout.addStretch()

        # Layout principal de la ventana (centrado)
        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(self.frame, alignment=Qt.AlignCenter)
        layout.addStretch()
        self.setLayout(layout)

         # BOTÓN RETROCESO (posición fija, fuera del layout)
        self.arrow_button = QPushButton(self.frame)
        arrow = os.path.join(os.path.dirname(__file__), '../../../resources/icons/icons8-sort-left-30.png')
        icon = QIcon(arrow)
        self.arrow_button.setIcon(icon)
        self.arrow_button.setIconSize(QSize(50, 50))
        self.arrow_button.setFixedSize(30, 30)
        self.arrow_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 5px;
            }
        """)
        self.arrow_button.move(20, 40)  # Posición absoluta, como en la segunda interfaz
        self.arrow_button.clicked.connect(self.volver)        
    #Lista de datos ficticios (cliente_info y dispositivo_info)
    def cargar_datos_prueba_computadora(self):
            cliente_info = {
                'ID Cliente': '90a2670d3e48434c',
                'Nombre': 'Juan Pérez',
                'Dispositivo': 'Computadora',
                'Correo': 'ejemplo@correo.com',
                'telefono': '123456789',
                'fecha_de_ingreso': '2025-04-19'
            }

            dispositivo_info = {
                'id': 1,
                'id_cliente': '90a2670d3e48434c',
                'fecha_ingreso': '19-04-2025',
                'procesador': 'Intel i7',
                'tarjeta_grafica': 'NVIDIA GTX 1650',
                'nombre': 'Juan Pérez',
                'garantia': '19-04-2025',
                'memoria': '512GB SSD',
                'placa': 'ABC123',
                'telefono': '123456789',
                'modelo': 'Modelo X',
                'fuente': '500W',
                'pantalla': '15.6 pulgadas',
                'correo': 'ejemplo@correo.com',
                'sistema_operativo': 'Windows 11',
                'ram': '16GB',
                'estado': 'New',
                'precio': '5.000.000',
                'notas': 'Lorem Lorem Lorem Lorem Lorem...'
            }

            return cliente_info, dispositivo_info

    def imprimir(self):
        from src.views.exports.boleta.create_boleta import generar_boleta_pdf
        from src.utils.alertas import mostrar_info
        """
        # En caso de querer usar el genérico descomentar
        # Recupera los datos
        cliente_info, dispositivo_info = self.cargar_datos_prueba_computadora()
        # Pasa los datos recuperados al método generar_boleta_pdf
        generar_boleta_pdf(cliente_info, dispositivo_info)
        """
        generar_boleta_pdf(self.cliente_info, self.dispositivo_info)
        mostrar_info("Boleta generada", "La boleta fue guardada correctamente en la carpeta de destino.", 600, 300)
       
    def mostrar_vista_previa(self):
        """
        # En caso de querer usar el genérico descomentar
        # Recupera los datos
        cliente_info, dispositivo_info = self.cargar_datos_prueba_computadora()
        # Pasa los datos recuperados al método generar_boleta_pdf
        vista_previa_boleta(cliente_info, dispositivo_info)
        """
        vista_previa_boleta(self.cliente_info, self.dispositivo_info)

    def volver(self):
        from views.data_base_client import BaseDateWindow

        try:
            # Si existe una conexión abierta en esta ventana, cerrala
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()
                print("✅ Conexión a base de datos cerrada desde la vista actual.")
        except Exception as e:
            print(f"⚠️ Error al cerrar la conexión: {e}")

        self.base = BaseDateWindow()
        self.base.show()
        self.close()