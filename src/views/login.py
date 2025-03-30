import os
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtGui import QFont, QFontDatabase, QPixmap  # Importar QPixmap para manejar imágenes
from PySide6.QtCore import Qt
from views.start import StartWindow
#from src.controllers.auth import verificar_usuario

class LoginWindow(QWidget): #Se construye la ventana de inicio de sesión
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FixItSystem - Login")
        self.showMaximized()
        self.setStyleSheet(
            "QWidget {"
            "background-color: #0d0d0d;"
            "}"
        )

        # Cargar la fuente personalizada
        font_path = os.path.join(os.path.dirname(__file__), '../resources/fonts/SongMyung-Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            correct_font_name = font_families[0]
            custom_font = QFont(correct_font_name)  
            custom_font.setBold(True)
        else:
            print("❌ Error: No se encontró la familia de fuentes. Usando fuente predeterminada.")
            custom_font = QFont("Arial")  # Fuente predeterminada

        # Crear un QFrame para contener los widgets
        self.frame = QFrame(self)
        self.frame.setFixedSize(500, 700)
        self.frame.setStyleSheet(
            "QFrame {"
            "background-color: #3084f2; "
            "border: 2px solid white; "  
            "border-radius: 15px;"
            "}"
        )
        self.frame.setLayout(QVBoxLayout())
        self.frame.layout().setContentsMargins(20, 20, 20, 20) 

        # Layout principal para la ventana
        layout = QVBoxLayout(self)
        layout.addWidget(self.frame, alignment=Qt.AlignCenter) # Añadir el frame al layout principal

        # Ruta de la imagen
        image_path = os.path.join(os.path.dirname(__file__), '../resources/icons/FixiSystem_logo.png')
        self.label_imagen = QLabel(self)
        pixmap = QPixmap(image_path)

        # Redimensionar la imagen
        pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_imagen.setPixmap(pixmap)
        self.label_imagen.setAlignment(Qt.AlignCenter)

        # Quitar el borde blanco
        self.label_imagen.setStyleSheet("border: none;")

        # Añadir la imagen y el título al layout principal
        self.label_titulo = QLabel("FixItSystem")
        self.label_titulo.setFont(custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 35px; border: None")
        self.frame.layout().insertWidget(0, self.label_titulo, alignment=Qt.AlignHCenter)
        self.frame.layout().insertWidget(0, self.label_imagen, alignment=Qt.AlignHCenter)

        # Estilo de los inputs 
        self.input_usuario = QLineEdit()
        self.input_usuario.setPlaceholderText("Usuario")
        self.input_usuario.setFont(custom_font)
        self.input_usuario.setStyleSheet(
            "QLineEdit {"
            "background-color: #102540; color: #fff; border-radius: 10px; font-size: 15px; "
            "border: 2px solid white; " 
            "height: 40px; width: 300px;"
            "}"
        )

        self.input_contraseña = QLineEdit()
        self.input_contraseña.setPlaceholderText("Contraseña")
        self.input_contraseña.setEchoMode(QLineEdit.Password)
        self.input_contraseña.setFont(custom_font)
        self.input_contraseña.setStyleSheet(
            "QLineEdit {"
            "background-color: #102540; color: #fff; border-radius: 10px; font-size: 15px;"
            "border: 2px solid white; " 
            "height: 40px; width: 300px;"
            "}" 
        )

        self.input_contraseña.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # BOTONES DE NAVEGACIÓN
        boton_estilo = """
            QPushButton {
                background-color: #102540;
                color: white;
                border-radius: 10px;
                border: 2px solid white;  
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #2a4a75;
            }
        """

        self.boton_ingresar = QPushButton("Ingresar")
        self.boton_ingresar.setFont(custom_font)
        self.boton_ingresar.setFixedSize(100, 35) 
        self.boton_ingresar.setStyleSheet(boton_estilo)
        self.boton_ingresar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.boton_ingresar.clicked.connect(self.abrir_inicio)

        # Crear un frame sin color para contener los elementos
        self.contenedor_frame = QFrame(self.frame)
        self.contenedor_frame.setStyleSheet("QFrame { background: transparent;border: none; }")
        self.contenedor_frame.setLayout(QVBoxLayout()) 
        self.contenedor_frame.setFixedHeight(400) 
        self.contenedor_frame.setFixedWidth(280)
    

        # Añadir widgets al contenedor_frame
        self.frame.layout().addWidget(self.contenedor_frame, alignment=Qt.AlignCenter)

        # Asegurar que los widgets dentro del contenedor están centrados
        self.contenedor_frame.layout().addWidget(self.input_usuario, alignment=Qt.AlignCenter)
        self.contenedor_frame.layout().addWidget(self.input_contraseña, alignment=Qt.AlignCenter)
        self.contenedor_frame.layout().addWidget(self.boton_ingresar, alignment=Qt.AlignCenter) 

    """def iniciar_sesion(self):
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()

        if verificar_usuario(usuario, contraseña):
            self.abrir_inicio()
        else:
            self.label_usuario.setText("❌ Usuario incorrecto")
    """
    
    def abrir_inicio(self):
        self.inicio = StartWindow()
        self.inicio.show()
        self.close()