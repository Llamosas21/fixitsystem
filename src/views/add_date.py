import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QGridLayout, QLineEdit, QComboBox, QTextEdit, QDateEdit,QSpinBox,QStyle
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QDate, Signal, QSize
from utils.resource_finder import cargar_fuente_predeterminada

class UpdateWindow(QWidget):
    closed = Signal()
    def __init__(self, dispositivo_inicial="Personalizado"):
        super().__init__()
        self.dispositivo_inicial = dispositivo_inicial
        self.campos = {}
        self.setWindowTitle("FixItSystem - Actualizar Datos")
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.setStyleSheet("QWidget {background-color: #0d0d0d;}")
        self.custom_font = cargar_fuente_predeterminada()
        self.modificado = False
        self._crear_interfaz()
       
    def _crear_interfaz(self):
        self.frame = QFrame(self)
        self.frame.setFixedSize(1200, 700)
        self.frame.setStyleSheet("QFrame {background-color: #3084f2; border-radius: 15px;}")

        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setSpacing(20)

        # TÍTULO
        self.label_titulo = QLabel("FixItSystem", self)
        self.label_titulo.setFont(self.custom_font)
        self.label_titulo.setStyleSheet("color: #102540; font-size: 40px; padding-top: 20px;")
        self.label_titulo.setAlignment(Qt.AlignHCenter)

        # FRAME CONTENEDOR
        self.frame_contenedor = QFrame(self.frame)
        self.frame_contenedor.setFixedSize(1000, 500)
        self.frame_contenedor.setStyleSheet("QFrame {background-color: #102540; border-radius: 20px;}")

        # GRID LAYOUT dentro del contenedor
        self.grid_layout = QGridLayout()
        self.grid_layout.setVerticalSpacing(10)

        # ComboBox para elegir dispositivo
        self.campo_dispositivo = QComboBox()
        self.campo_dispositivo.addItems(["Personalizado", "Computadora", "Impresora", "Notebook", "Consola", "Celular", "Tablet"])
        self.campo_dispositivo.setCurrentText(self.dispositivo_inicial)
        self.campo_dispositivo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")
        self.campo_dispositivo.currentIndexChanged.connect(self.actualizar_campos_por_dispositivo)

        # Insertar el ComboBox al grid layout en la posición (0, 0)
        self.grid_layout.addWidget(self.campo_dispositivo, 0, 0, 1, 2)

        # Frame contenedor con layout que incluye el grid
        frame_contenedor_layout = QVBoxLayout(self.frame_contenedor)
        frame_contenedor_layout.addLayout(self.grid_layout)

        # Mostrar campos personalizados o del dispositivo inicial
        self.actualizar_campos_por_dispositivo()

        # BOTONES (Editar, Agregar, Eliminar, Imprimir)
        boton_estilo = """
            QPushButton {
                background-color: #102540;
                color: white;
                border-radius: 10px;
                padding: 8px 20px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #2a4a75;
            }
        """

        self.boton_editar = QPushButton("Editar", self)
        self.boton_agregar = QPushButton("Agregar", self)
        self.boton_eliminar = QPushButton("Eliminar", self)
        self.boton_imprimir = QPushButton("Imprimir", self)

        for boton in [self.boton_editar, self.boton_agregar, self.boton_eliminar, self.boton_imprimir]:
            boton.setStyleSheet(boton_estilo)
            boton.setFixedSize(120, 35)

        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.boton_editar)
        botones_layout.addWidget(self.boton_agregar)
        botones_layout.addWidget(self.boton_eliminar)
        botones_layout.addWidget(self.boton_imprimir)
        botones_layout.setAlignment(Qt.AlignCenter)

        # Acciones
        self.boton_editar.clicked.connect(self.editar)
        self.boton_agregar.clicked.connect(self.agregar)
        self.boton_eliminar.clicked.connect(self.eliminar)
        self.boton_imprimir.clicked.connect(self.imprimir)

        # Agregar al frame layout
        frame_layout.addWidget(self.label_titulo, alignment=Qt.AlignHCenter | Qt.AlignTop)
        frame_layout.addWidget(self.frame_contenedor, alignment=Qt.AlignCenter)
        frame_layout.addLayout(botones_layout)

        # LAYOUT PRINCIPAL
        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.frame, alignment=Qt.AlignCenter)
        self.setLayout(layout_principal)

        # BOTÓN RETROCESO (posición fija, fuera del layout)
        self.arrow_button = QPushButton(self.frame)
        arrow = os.path.join(os.path.dirname(__file__), '../resources/icons/icons8-sort-left-30.png')
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

    #DEDICADO AL MANEJO DEL FORMULARIO
    def limpiar_grid_layout(self):
        """Limpia todos los widgets del grid_layout excepto el QComboBox."""
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget and widget != self.campo_dispositivo:
                widget.hide()  # En vez de eliminarlo, solo lo ocultamos
                #widget.deleteLater()  # Elimina el widget de manera segura
           
    def actualizar_campos_por_dispositivo(self):
        """Actualiza los campos según el dispositivo seleccionado."""
        self.limpiar_grid_layout()  # Limpiar campos previos del layout
        
        # Obtiene el dispositivo seleccionado
        dispositivo = self.campo_dispositivo.currentText()
        
        # Determina el método adecuado para mostrar los campos según el dispositivo seleccionado
        metodo = getattr(self, f"mostrar_campos_{dispositivo.lower()}", self.mostrar_campos_personalizado)
        
        # Llama al método correspondiente
        metodo()

    def mostrar_campos_personalizado(self):
        etiquetas = [
            "fecha_de_ingreso", "Procesador", "tarjeta_grafica", "Nombre", "garantia",
            "Memoria", "Placa", "telefono", "Modelo", "Fuente", 
            "Pantalla", "Correo", "sistema_operativo", "Ram", "Estado"]
        self._agregar_campos(etiquetas)
       
    def mostrar_campos_impresora(self):
        etiquetas = [
            "fecha_de_ingreso", "estado_general", "tipo_impresora", "Nombre", "garantia",
            "Marca", "Placa", "telefono", "Modelo", "Conectividad",
            "tipo_tinta", "Correo", "numero_serie", "uso_estimado", "Estado", "precio"
        ]
        self._agregar_campos(etiquetas)
        self.cargar_datos_genericos_impresora()


    def mostrar_campos_computadora(self):
        etiquetas = [
            "fecha_de_ingreso", "Procesador", "tarjeta_grafica", "Nombre", "garantia",
            "Memoria", "Placa", "telefono", "Modelo", "Fuente", 
            "Pantalla", "Correo", "sistema_operativo", "Ram", "Estado", "precio"]
        self._agregar_campos(etiquetas)
        self.cargar_datos_genericos()  # Cargar datos genericos

    def mostrar_campos_notebook(self):
        etiquetas = [
            "fecha_de_ingreso", "Estado Cargador", "tarjeta_grafica", "Nombre", "garantia",
            "Procesador", "Placa", "telefono", "Modelo", "Memoria", 
            "Pantalla", "Correo", "TIM", "Ram", "Estado"]
        self._agregar_campos(etiquetas)

    def mostrar_campos_consola(self):
        etiquetas = [
            "fecha_de_ingreso", "Procesador", "Cantidad Mandos", "Nombre", "garantia",
            "Memoria", "Mandos estado", "telefono", "Modelo", "Pantalla", 
            "Correo", "sistema_operativo", "Ram", "Estado", "TIM"]
        self._agregar_campos(etiquetas)

    def mostrar_campos_celular(self):
        etiquetas = [
            "fecha_de_ingreso", "Estado Cargador", "Bateria", "Nombre", "garantia",
            "Memoria", "Placa", "telefono", "Modelo", "Pantalla", 
            "Correo", "sistema_operativo", "Ram", "Estado"]
        self._agregar_campos(etiquetas)

    def mostrar_campos_tablet(self):
        etiquetas = [
            "fecha_de_ingreso", "Estado Cargador", "Bateria", "Nombre", "garantia",
            "Memoria", "Placa", "telefono", "Modelo", "Pantalla", 
            "Correo", "sistema_operativo", "Ram", "Estado"]
        self._agregar_campos(etiquetas)

    def _agregar_campos(self, etiquetas):
        try:
            columnas = 4
            for i, texto in enumerate(etiquetas):
                label = QLabel(texto, self)
                label.setStyleSheet("color: white; font-size: 12px; font-weight: bold;")
                label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                # Campos especiales para "fecha_de_ingreso" y "garantia"
                if texto in ["fecha_de_ingreso", "garantia"]:
                    campo = QDateEdit(self)
                    campo.setDate(QDate.currentDate())  
                    campo.setDisplayFormat("dd-MM-yyyy")  
                    campo.setCalendarPopup(True)  
                    campo.setFixedSize(130, 30) 
                    campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

                # Campo especial para "Estado"
                elif texto == "Estado" or texto == "Mandos estado" or texto == "Estado Cargador":
                    campo = QComboBox(self)
                    campo.addItems(["New", "Used", "Refurbished"])
                    campo.setFixedSize(130, 30)
                    campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

                # Campo especial para "Cantidad Mandos"
                elif texto == "Cantidad Mandos":
                    campo = QSpinBox(self)
                    campo.setRange(1, 10)  # Establece el rango de valores permitidos (1 a 10)
                    campo.setFixedSize(130, 30)
                    campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

                # Campo genérico (QLineEdit)
                else:
                    campo = QLineEdit(self)
                    campo.setFixedSize(130, 30)
                    campo.setStyleSheet("background-color: #2a4a75; color: white; border-radius: 5px; padding-left: 5px;")

                self.campos[texto.lower()] = campo  # Asegúrate de no duplicar claves
                fila, columna = divmod(i, columnas)
                self.grid_layout.addWidget(label, fila + 1, columna * 2)
                self.grid_layout.addWidget(campo, fila + 1, columna * 2 + 1)

            # Añadir QTextEdit "Notas" debajo de los campos
            fila_actual = (len(etiquetas) // columnas) + 1
            if len(etiquetas) % columnas != 0:
                fila_actual += 1

            self.nota = QTextEdit()
            self.nota.setFixedHeight(200)
            self.nota.setPlaceholderText("Notas")
            self.nota.setStyleSheet("""
                background-color: #2a4a75;
                color: white;
                border-radius: 5px;
                padding: 5px;
                margin: 10px;
                font-weight: bold;
            """)
            self.grid_layout.addWidget(self.nota, fila_actual, 0, 1, columnas * 2)
            self.campos["notas"] = self.nota
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")


    def cargar_datos_genericos(self): #PARA HACER TEST EN CASO DE NO USARSE COMENTAR 
        genericos = {
            "nombre": "Juan Pérez",
            "telefono": "123456789",
            "modelo": "Modelo X",
            "placa": "ABC123",
            "pantalla": "15.6 pulgadas",
            "correo": "ejemplo@correo.com",
            "sistema_operativo": "Windows 11",
            "ram": "16GB",
            "procesador": "Intel i7",
            "memoria": "512GB SSD",
            "fuente": "500W",
            "tarjeta_grafica": "NVIDIA GTX 1650",
            "garantia": QDate.currentDate(),
            "fecha_de_ingreso": QDate.currentDate(),
            "precio": "5.000.000",
            "estado": "New"}

        for clave, valor in genericos.items():
            widget = self.campos.get(clave)
            if isinstance(widget, QLineEdit):
                widget.setText(valor)
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(valor)
            elif isinstance(widget, QComboBox):
                index = widget.findText(valor)
                if index != -1:
                    widget.setCurrentIndex(index)
            elif isinstance(widget, QDateEdit) and isinstance(valor, QDate):
                widget.setDate(valor)
        #print("Se Agregan los datos genericos")

    def cargar_datos_genericos_impresora(self):  # PARA HACER TEST EN CASO DE NO USARSE COMENTAR
        genericos = {
            "nombre": "María López",
            "telefono": "0987654321",
            "modelo": "Epson L3150",
            "correo": "maria@example.com",
            "estado_general": "Funciona correctamente",
            "tipo_impresora": "Multifunción",
            "conectividad": "Wi-Fi",
            "tipo_tinta": "Tinta continua",
            "uso_estimado": "Uso doméstico moderado",
            "garantia": QDate.currentDate(),
            "fecha_de_ingreso": QDate.currentDate(),
            "precio": "3.500.000",
            "estado": "En revisión",
            "marca": "Epson",
            "placa": "XYZ456",
            "numero_serie": "SN-987654321"
        }
           

        for clave, valor in genericos.items():
            widget = self.campos.get(clave.lower().replace(" ", "_")) or self.campos.get(clave)
            if isinstance(widget, QLineEdit):
                widget.setText(valor)
            elif isinstance(widget, QTextEdit):
                widget.setPlainText(valor)
            elif isinstance(widget, QComboBox):
                index = widget.findText(valor)
                if index != -1:
                    widget.setCurrentIndex(index)
            elif isinstance(widget, QDateEdit) and isinstance(valor, QDate):
                widget.setDate(valor)


#MÉTODOS PARA CARGAR LOS DATOS DESDE celda_clickeada (data_base_client.py)
    def cargar_datos_editar(self, cliente_seleccionado, dispositivos):
        self.id_cliente = cliente_seleccionado.get("ID Cliente")
        self.cliente_info = cliente_seleccionado             # Guardar cliente
        self.dispositivo_info = dispositivos[0]              # Guardar dispositivo

        tipo_dispositivo = cliente_seleccionado.get("Dispositivo")

        self.campo_dispositivo.blockSignals(True)
        self.campo_dispositivo.setCurrentText(tipo_dispositivo)
        self.campo_dispositivo.blockSignals(False)

        if tipo_dispositivo == "Computadora":
            self.mostrar_campos_computadora()
            self.cargar_datos_dispositivo(self.dispositivo_info)
        elif tipo_dispositivo == "Impresora":
            self.mostrar_campos_impresora()
            self.cargar_datos_dispositivo(self.dispositivo_info)
        elif tipo_dispositivo == "Notebook":
            self.mostrar_campos_notebook(self.dispositivo_info)
        elif tipo_dispositivo == "Consola":
            self.mostrar_campos_consola(self.dispositivo_info)
        elif tipo_dispositivo == "Celular":
            self.mostrar_campos_celular(self.dispositivo_info)
        elif tipo_dispositivo == "Tablet":
            self.mostrar_campos_tablet(self.dispositivo_info)
        else:
            self.mostrar_campos_personalizado()

    def cargar_datos_dispositivo(self, dispositivo):
        for clave, widget in self.campos.items():
            valor = dispositivo.get(clave)

            if valor is None:
                continue  # El campo no está presente en los datos del dispositivo

            if isinstance(widget, QLineEdit):
                widget.setText(str(valor))

            elif isinstance(widget, QTextEdit):
                widget.setPlainText(str(valor))

            elif isinstance(widget, QComboBox):
                index = widget.findText(str(valor))
                if index != -1:
                    widget.setCurrentIndex(index)

            elif isinstance(widget, QSpinBox):
                try:
                    widget.setValue(int(valor))
                except ValueError:
                    widget.setValue(1)  # Valor por defecto

            elif isinstance(widget, QDateEdit):
                if isinstance(valor, QDate):
                    widget.setDate(valor)
                elif isinstance(valor, str):
                    fecha = QDate.fromString(valor, "dd-MM-yyyy")
                    if fecha.isValid():
                        widget.setDate(fecha)

#MÉTODOS DE: VOLVER, REFRESCAR EDITAR, AGREGAR, ELIMINAR 
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

    def refrescar(self, cliente_info, dispositivo_info):
        from views.data_base_client import BaseDateWindow

        try:
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()
                #print("🔄 Conexión cerrada para refrescar.")
        except Exception as e:
            print(f"⚠️ Error al cerrar la conexión: {e}")

        self.base = BaseDateWindow(cliente_info=cliente_info, dispositivo_info=dispositivo_info)
        self.base.show()
        self.close()

    def editar(self):
        from src.controllers.client_controller import ClientController
        from utils.alertas import mostrar_confirmacion,mostrar_alerta

        if not hasattr(self, 'id_cliente') or not self.id_cliente:
            mostrar_alerta("Error", "No se ha seleccionado un cliente.", 300, 200)
            self.volver()
            return

        valor = mostrar_confirmacion(
            "Confirmar edición",
            "¿Estás seguro de que querés guardar los cambios de este cliente y su dispositivo?",
            400, 400
        )

        if not valor:
            return

        # Obtener fecha de ingreso
        fecha_widget = self.campos.get("fecha_de_ingreso")
        if isinstance(fecha_widget, QDateEdit):
            fecha_ingreso = fecha_widget.date().toString("yyyy-MM-dd")
        else:
            print("⚠️ Error: El campo 'fecha_de_ingreso' no es un QDateEdit.")
            return

        id_cliente = self.id_cliente  

        # Datos del cliente
        datos_cliente = {
            "id_cliente": id_cliente,
            "nombre": self.campos["nombre"].text().strip(),
            "telefono": self.campos["telefono"].text().strip(),
            "correo": self.campos["correo"].text().strip(),
            "fecha_ingreso": fecha_ingreso,
        }

        # Validación básica
        if not datos_cliente["nombre"] or not datos_cliente["telefono"] or not datos_cliente["correo"]:
            print("⚠️ Error: Nombre, teléfono y correo son obligatorios")
            return

        # === Actualizar datos del cliente ===
        controller = ClientController()
        try:
            controller.editar_cliente(datos_cliente)
        except Exception as e:
            print("❌ Error al editar cliente:", e)
            import traceback
            traceback.print_exc()
            return

        # === Editar datos del dispositivo ===
        dispositivos_controladores = {
            "Computadora": ("src.controllers.dispositivo_controller.computadora_controller", "ComputadoraController", "editar_computadora"),
            "Impresora": ("src.controllers.dispositivo_controller.impresora_controller", "ImpresoraController", "editar_impresora"),
            "Notebook": ("src.controllers.dispositivo_controller.notebook_controller", "NotebookController", "editar_notebook"),
            "Consola": ("src.controllers.dispositivo_controller.consola_controller", "ConsolaController", "editar_consola"),
            "Celular": ("src.controllers.dispositivo_controller.celular_controller", "CelularController", "editar_celular"),
            "Tablet": ("src.controllers.dispositivo_controller.tablet_controller", "TabletController", "editar_tablet"),
            "Personalizado": ("src.controllers.dispositivo_controller.personalizado_controller", "PersonalizadoController", "editar_personalizado"),
        }

        dispositivo = self.campo_dispositivo.currentText()
        modulo_path, clase_nombre, metodo_editar = dispositivos_controladores.get(dispositivo, (None, None, None))

        if not modulo_path:
            print(f"⚠️ No se encontró un controlador para el dispositivo: {dispositivo}")
            return

        # Importar dinámicamente el controlador del dispositivo
        try:
            modulo = __import__(modulo_path, fromlist=[clase_nombre])
            clase_controlador = getattr(modulo, clase_nombre)
            controlador = clase_controlador()
        except Exception as e:
            print(f"❌ Error al instanciar el controlador '{clase_nombre}': {e}")
            import traceback
            traceback.print_exc()
            return

        # Extraer campos del formulario
        campos_dispositivo = {}
        for etiqueta, widget in self.campos.items():
            clave = etiqueta.lower().replace(" ", "_")

            if hasattr(widget, "text"):
                campos_dispositivo[clave] = widget.text().strip()
            elif isinstance(widget, QDateEdit):
                campos_dispositivo[clave] = widget.date().toString("yyyy-MM-dd")
            elif isinstance(widget, QComboBox):
                campos_dispositivo[clave] = widget.currentText()

        # Agregar notas si existen
        if hasattr(self, "nota"):
            campos_dispositivo["notas"] = self.nota.toPlainText().strip()

        # Relacionar con el cliente
        campos_dispositivo["id_cliente"] = id_cliente

        # Llamar método de edición del controlador
        try:
            metodo = getattr(controlador, metodo_editar)
            metodo(**campos_dispositivo)
        except Exception as e:
            print(f"❌ Error al editar datos del dispositivo ({dispositivo}):", e)
            import traceback
            traceback.print_exc()

        # Se agrega dispositivo al diccionario de cliente
        datos_cliente["dispositivo"] = dispositivo

        self.cliente_info = datos_cliente
        self.dispositivo_info = campos_dispositivo
        self.modificado = True

    def agregar(self):
        from src.controllers.client_controller import ClientController
        from utils.alertas import mostrar_confirmacion,mostrar_alerta
        import uuid

        valor = mostrar_confirmacion("Confirmar alta de cliente","¿Estás seguro de que querés agregar este nuevo cliente a la base de datos?",400, 400)

        if valor == True:
            # Extraer los valores del formulario
            fecha_widget = self.campos.get("fecha_de_ingreso")
            if isinstance(fecha_widget, QDateEdit):
                fecha_ingreso = fecha_widget.date().toString("yyyy-MM-dd")
            else:
                mostrar_alerta("⚠️ Error", "El campo 'fecha_de_ingreso' no es un QDateEdit.", 300, 150)
                return

            id_cliente = uuid.uuid4().hex[:16]  # 16 caracteres únicos 


            datos = {
                "id_cliente": id_cliente,
                "nombre": self.campos["nombre"].text().strip(),
                "dispositivo": self.campo_dispositivo.currentText(),
                "telefono": self.campos["telefono"].text().strip(),
                "correo": self.campos["correo"].text().strip(),
                "fecha_ingreso": fecha_ingreso,
            }

            # Validaciones básicas
            if not datos["nombre"] or not datos["telefono"] or not datos["correo"]:
                mostrar_alerta("⚠️ Error", "El campo Nombre, telefono y Correo son obligatorios.", 300, 150)
                return

            # Enviar datos al controlador
            controller = ClientController()
            resultado = controller.agregar_cliente(datos)

            if not resultado:
                print("Error al agregar cliente")
                return
            #else: print("📦 Datos preparados:", datos)

            # Si se agregó el cliente con éxito, agregar el dispositivo correspondiente
            dispositivos_controladores = {
                "Computadora": ("src.controllers.dispositivo_controller.computadora_controller", "ComputadoraController", "agregar_computadora"),
                "Impresora": ("src.controllers.dispositivo_controller.impresora_controller", "ImpresoraController", "agregar_impresora"),
                "Notebook": ("src.controllers.dispositivo_controller.notebook_controller", "NotebookController", "agregar_notebook"),
                "Consola": ("src.controllers.dispositivo_controller.consola_controller", "ConsolaController", "agregar_consola"),
                "Celular": ("src.controllers.dispositivo_controller.celular_controller", "CelularController", "agregar_celular"),
                "Tablet": ("src.controllers.dispositivo_controller.tablet_controller", "TabletController", "agregar_tablet"),
                "Personalizado": ("src.controllers.dispositivo_controller.personalizado_controller", "PersonalizadoController", "agregar_personalizado"),
            }

            dispositivo = datos["dispositivo"]
            modulo_path, clase_nombre, metodo_agregar = dispositivos_controladores.get(dispositivo, (None, None, None))

            if modulo_path:
                modulo = __import__(modulo_path, fromlist=[clase_nombre])
                clase_controlador = getattr(modulo, clase_nombre)
                try:
                    controlador = clase_controlador()
                except Exception as e:
                    print(f"❌ Error al instanciar el controlador '{clase_nombre}': {e}")
                    import traceback
                    traceback.print_exc()
                    return

                # Extraer campos del formulario según el dispositivo
                campos_dispositivo = {}
                for etiqueta, widget in self.campos.items():
                    clave = etiqueta.lower().replace(" ", "_")

                    try:
                        if isinstance(widget, QLineEdit):
                            campos_dispositivo[clave] = widget.text().strip()

                        elif isinstance(widget, QDateEdit):
                            campos_dispositivo[clave] = widget.date().toString("yyyy-MM-dd")

                        elif isinstance(widget, QComboBox):
                            campos_dispositivo[clave] = widget.currentText()

                        elif isinstance(widget, QSpinBox):
                            campos_dispositivo[clave] = widget.value()

                        elif isinstance(widget, QTextEdit):
                            campos_dispositivo[clave] = widget.toPlainText().strip()

                    except RuntimeError as e:
                        print(f"❌ Error al acceder al campo '{clave}': {e}")
                        continue


            # Agregar notas si el campo existe
            if hasattr(self, "nota"):
                campos_dispositivo["notas"] = self.nota.toPlainText().strip()

            # Relaciona con el cliente creado
            campos_dispositivo["id_cliente"] = id_cliente

            # Llamar al método específico del controlador
            metodo = getattr(controlador, metodo_agregar)
            metodo(**campos_dispositivo)

        else: 
            print("Operación cancelada por el usuario.")

    def eliminar(self):
        from src.controllers.client_controller import ClientController
        from utils.alertas import mostrar_confirmacion, mostrar_alerta

        # Validar que haya un cliente seleccionado
        if not hasattr(self, 'id_cliente') or not self.id_cliente:
            mostrar_alerta("Error", "No se ha seleccionado un cliente para eliminar.", 300, 200)
            return

        # Confirmación del usuario
        valor = mostrar_confirmacion("Confirmar eliminación de cliente","¿Estás seguro de que quieres eliminar este cliente de la base de datos?",400,400)

        if valor is not True:
            return

        # === Eliminar cliente ===
        controller = ClientController()
        resultado = controller.eliminar_cliente(self.id_cliente)

        if not resultado:
            print("❌ Error al eliminar cliente")
            return

        # === Eliminar dispositivo correspondiente ===
        dispositivos_controladores = {
            "Computadora": ("src.controllers.dispositivo_controller.computadora_controller", "ComputadoraController", "eliminar_computadora"),
            "Impresora": ("src.controllers.dispositivo_controller.impresora_controller", "ImpresoraController", "eliminar_impresora"),
            "Notebook": ("src.controllers.dispositivo_controller.notebook_controller", "NotebookController", "eliminar_notebook"),
            "Consola": ("src.controllers.dispositivo_controller.consola_controller", "ConsolaController", "eliminar_consola"),
            "Celular": ("src.controllers.dispositivo_controller.celular_controller", "CelularController", "eliminar_celular"),
            "Tablet": ("src.controllers.dispositivo_controller.tablet_controller", "TabletController", "eliminar_tablet"),
            "Personalizado": ("src.controllers.dispositivo_controller.personalizado_controller", "PersonalizadoController", "eliminar_personalizado"),
        }

        # Extraer tipo de dispositivo desde el comboBox o su valor actual
        dispositivo = None
        if hasattr(self, "campo_dispositivo"):
            dispositivo = self.campo_dispositivo.currentText()
        elif "dispositivo" in self.campos:
            dispositivo = self.campos["dispositivo"].currentText()

        if not dispositivo:
            print("⚠️ No se pudo determinar el tipo de dispositivo.")
            return

        modulo_path, clase_nombre, metodo_eliminar = dispositivos_controladores.get(dispositivo, (None, None, None))

        if modulo_path and clase_nombre and metodo_eliminar:
            try:
                modulo = __import__(modulo_path, fromlist=[clase_nombre])
                clase_controlador = getattr(modulo, clase_nombre)
                controlador = clase_controlador()
                getattr(controlador, metodo_eliminar)(self.id_cliente)
            except Exception as e:
                print(f"❌ Error al eliminar el dispositivo '{dispositivo}': {e}")
                import traceback
                traceback.print_exc()
                return
        else:
            print(f"⚠️ No se encontró un controlador válido para el tipo de dispositivo: {dispositivo}")

        # Mensaje de éxito
        mostrar_alerta("Eliminación exitosa", "El cliente y su dispositivo han sido eliminados correctamente.", 400, 300)
        self.volver()

    def imprimir(self):
        from src.views.exports.boleta.view_boleta import ViewBoleta
        from src.utils.alertas import mostrar_alerta, mostrar_confirmacion
        """ SE VERIFCA EL ESTADO DE LOS DATOS
        print("Datos del Cliente (add_date.py imprimir):")
        print(self.cliente_info)
        print("Datos del Dispositivo:")
        print(self.dispositivo_info)
        """
        #print(f"Estado de modificado después de editar: {self.modificado}") 
        # Verifica si los datos están disponibles
        if not hasattr(self, 'cliente_info') or not hasattr(self, 'dispositivo_info') or not self.cliente_info or not self.dispositivo_info:
            # Muestra la alerta si los datos no están definidos o son vacíos
            mostrar_alerta("Error", "No se seleccionó ningún dato.", 400, 200)
            return  # Detiene la ejecución si no hay datos

        # Verifica si los datos han sido modificados
        if hasattr(self, 'modificado') and not self.modificado:
            valor = mostrar_confirmacion(
                "Confirmar cambios",
                "¿Quieres guardar los cambios antes de imprimir?",
                400, 200
            )
            
            if valor:
                self.editar()  # esto guarda, y también actualiza cliente_info y dispositivo_info
                self.boleta = ViewBoleta(self.cliente_info, self.dispositivo_info)
                self.boleta.show()
                self.close()
            else:
                return
        else:
            return

    def closeEvent(self, event):
            self.closed.emit()  # Emitir señal al cerrar
            super().closeEvent(event)