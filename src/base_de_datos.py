import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QLineEdit
)
from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtCore import Qt, QSize
from agregar import UpdateWindow


class BaseDateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Base de Datos")
        self._configurar_ventana()
        self._cargar_fuente_personalizada()
        self._crear_interfaz()
    
    def _configurar_ventana(self):
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")

    # DEDICADO AL TIPO DE LETRA   
    def _cargar_fuente_personalizada(self):
        font_path = os.path.join(os.path.dirname(__file__), 'resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        
        if font_families:
            self.custom_font = QFont(font_families[0])
            self.custom_font.setBold(True)
        else:
            print("Error: No se encontró la familia de fuentes.")
            self.custom_font = QFont()

    # FRAME PRINCIPAL
    def _crear_interfaz(self):
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border: none; border-radius: 15px;}")
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(20)
        
        # TÍTULO
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(self.custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 30px; padding-top: 20px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)
        
        # FRAME CONTENEDOR
        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setFixedSize(1000, 500)
        self.frame_contenedor.setStyleSheet("QFrame {background-color: #102540; border: none; border-radius: 20px;}")
        frame_contenedor_layout = QVBoxLayout(self.frame_contenedor)
        frame_contenedor_layout.setSpacing(15)
        frame_contenedor_layout.setContentsMargins(0, 20, 0, 0)
        
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
            """
        )
        frame_contenedor_layout.addWidget(self.input_busqueda)
        
        # BASE DE DATOS
        self.frame_fondo_db = QFrame(self.frame_contenedor)
        self.frame_fondo_db.setFixedSize(917, 400)
        self.frame_fondo_db.setStyleSheet("QFrame {background-color: #1e3f69; border-radius: 15px;}")
        frame_contenedor_layout.addWidget(self.frame_fondo_db, alignment=Qt.AlignCenter)
        
        self.frame_contenedor.setLayout(frame_contenedor_layout)
        
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
            """
        )
        
        self.boton_Agregar = QPushButton("Agregar")
        self.boton_Editar = QPushButton("Editar")
        self.boton_Eliminar = QPushButton("Eliminar")
        
        for boton in [self.boton_Agregar, self.boton_Editar, self.boton_Eliminar]:
            boton.setStyleSheet(boton_estilo)
            boton.setFixedSize(120, 35)
        
        # LAYOUT DE BOTONES
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_Agregar)
        botones_layout.addWidget(self.boton_Editar)
        botones_layout.addWidget(self.boton_Eliminar)
        botones_layout.setAlignment(Qt.AlignCenter)

        # ACCIONES DE LOS BOTONES
        self.boton_Agregar.clicked.connect(self.abrir_actualizar_base)
        
        # ORGANIZAR ELEMENTOS
        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)
        
        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

        # BOTÓN RETROCESO
        self.arrow_button = QPushButton(self.frame)  # Agrega el botón directamente al frame
        arrow = os.path.join(os.path.dirname(__file__), 'resources/icons/icons8-sort-left-30.png')
        icon = QIcon(arrow)  # Crea un objeto QIcon a partir de la ruta
        icon_size = icon.actualSize(QSize(50, 50))  # Tamaño máximo permitido para el ícono
        self.arrow_button.setIcon(icon)

        # ESTILO DEL BOTÓN
        self.arrow_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;  
                border: none;  
            }
            """
        )

        # Ajustar el tamaño del botón
        self.arrow_button.setIconSize(icon_size)
        self.arrow_button.setFixedSize(icon_size.width(), icon_size.height()) 
        self.arrow_button.move(20, 20) 

        # Acción del botón
        self.arrow_button.clicked.connect(self.volver_al_inicio)    



    def volver_al_inicio(self):
        from inicio import InicioWindow
        self.login = InicioWindow()
        self.login.show()
        self.close()

    def abrir_actualizar_base(self):
        self.actualizar = UpdateWindow()
        self.actualizar.show()
        self.close()
    
    def resizeEvent(self, event):# En un futuro se deberá quitar
        """Evita que la ventana se redimensione."""
        self.showMaximized()