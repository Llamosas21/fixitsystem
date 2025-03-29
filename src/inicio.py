import os
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt
from base_de_datos import BaseDateWindow

class InicioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Inicio")

        # Configurar la ventana maximizada
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")

        # Cargar la fuente personalizada
        font_path = os.path.join(os.path.dirname(__file__), 'resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            correct_font_name = font_families[0]
            custom_font = QFont(correct_font_name)
            custom_font.setBold(True)
        else:
            print("Error: No se encontró la familia de fuentes.")

        # FRAME PRINCIPAL 
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border: none; border-radius: 15px;}")
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(15)

        # Título del programa 
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 30px; padding-top: 20px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)

        # Frame contenedor 
        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setFixedSize(1000, 500)
        self.frame_contenedor.setStyleSheet("QFrame {background-color: #102540; border: none; border-radius: 20px;}")
        frame_contenedor_layout = QVBoxLayout(self.frame_contenedor)
        frame_contenedor_layout.setSpacing(15)

        # Barra de busqueda
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

        # Se definen los frames internos 
        self.frame_arriba = QFrame(self.frame_contenedor)
        self.frame_arriba.setFixedSize(900, 170)
        self.frame_arriba.setStyleSheet("QFrame {background-color: #1e3f69; border-radius: 10px;}")

        self.frame_abajo = QFrame(self.frame_contenedor)
        self.frame_abajo.setFixedSize(900, 170)
        self.frame_abajo.setStyleSheet("QFrame {background-color: #1e3f69; border-radius: 10px;}")

        # Agregar elementos al frame interno
        frame_contenedor_layout.addWidget(self.input_busqueda)
        frame_contenedor_layout.addWidget(self.frame_arriba, alignment=Qt.AlignHCenter)
        frame_contenedor_layout.addWidget(self.frame_abajo, alignment=Qt.AlignHCenter)
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

        self.boton_usuarios = QPushButton("Usuarios")
        self.boton_usuarios.setStyleSheet(boton_estilo)
        self.boton_usuarios.clicked.connect(self.abrir_base)

        self.boton_Editar = QPushButton("Editar")
        self.boton_Editar.setStyleSheet(boton_estilo)
       
        self.boton_Eliminar = QPushButton("Eliminar")
        self.boton_Eliminar.setStyleSheet(boton_estilo)


        # Establecer el mismo tamaño para todos los botones
        for boton in [self.boton_usuarios, self.boton_Eliminar, self.boton_Editar]:
            boton.setFixedSize(120, 35) 

        # Layout horizontal para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_usuarios)
        botones_layout.addWidget(self.boton_Editar)
        botones_layout.addWidget(self.boton_Eliminar)
        botones_layout.setAlignment(Qt.AlignCenter)

        # ORGANIZAR ELEMENTOS
        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)

        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

    def abrir_base(self):
            self.usuario = BaseDateWindow()
            self.usuario.show()
            self.close()

    def resizeEvent(self, event):
        """Evita que la ventana se redimensione."""
        self.showMaximized()
