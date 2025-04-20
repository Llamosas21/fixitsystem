import os
import webbrowser
from utils.arch_generator import generar_pdf
from src.utils.resource_finder import crear_directorio_cliente 


# Plantilla HTML
plantilla_html = """
<html>
    <head>
        <meta charset="utf-8">
        <style>
            {css}
        </style>
    </head>
    <body>
        <div class="hoja_pdf_A4">
            <h1>Fixitsystem - Reparación</h1>
            <p><strong>Cliente:</strong> {nombre}</p>
            <p><strong>Correo:</strong> {correo}</p>
            <p><strong>Teléfono:</strong> {telefono}</p>
            <p><strong>Fecha de ingreso:</strong> {fecha_ingreso}</p>
            <hr>
            <p><strong>Dispositivo:</strong> {dispositivo}</p>
            <p><strong>Modelo:</strong> {modelo}</p>
            <p><strong>Procesador:</strong> {procesador}</p>
            <p><strong>RAM:</strong> {ram}</p>
            <p><strong>Almacenamiento:</strong> {memoria}</p>
            <p><strong>Tarjeta Gráfica:</strong> {tarjeta_grafica}</p>
            <p><strong>Fuente:</strong> {fuente}</p>
            <p><strong>Pantalla:</strong> {pantalla}</p>
            <p><strong>Sistema Operativo:</strong> {sistema_operativo}</p>
            <p><strong>Estado:</strong> {estado}</p>
            <p><strong>Garantía hasta:</strong> {garantia}</p>
            <p class="precio">Precio estimado: ${precio}</p>
            <hr>
            <div class="notas">
                <p><strong>Descripción de la reparación:</strong></p>
                <p>{notas}</p>
            </div>

            <div class="footer">
                <p>Gracias por confiar en nosotros.</p>
            </div>
        </div>
    </body>
</html>
"""

# CSS 
estilos_css = """
@page {
    size: A4;
    margin: 0;
    padding: 0;
}

body {
    background: #0D0D0D; /* O blanco si no querés espacio negro */
    margin: 0;
    padding: 0;
}

.hoja_pdf_A4 {
    width: 210mm;
    background: white;
    margin: auto;
    font-family: sans-serif;
    font-size: 9pt;
    box-sizing: border-box;
    padding: 10mm;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
}


h1 {
    color: #007acc;
    text-align: center;
    font-size: 24pt;
    margin: 0px 0 130px 0;
    font-weight: normal;
}

p {
    margin: 5px 0;
    font-size: 9pt;
    font-weight: normal;
}

.precio {
    color: green;
    font-size: 10pt;
    font-weight: bold;
    margin-top: 10px;
}

.footer {
    font-size: 8pt;
    color: #666;
    text-align: center;
    margin-top: 20px;
}

hr {
    margin: 10px 0;
    border: none;
    border-top: 1px solid #ccc;
}
.notas {
    min-height: 95mm;  
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

"""

def generar_html_boleta(cliente, dispositivo):
    """ 
    print("Datos del Cliente (create_boleta.py imprimir):")
    print(cliente)
    print("Datos del Dispositivo:")
    print(dispositivo)
    """
    
    # Continuar con la lógica de generación del HTML
    datos_combinados = {
        "nombre": cliente.get("nombre") or cliente.get("Nombre") or dispositivo.get("nombre", ""),
        "correo": cliente.get("correo") or cliente.get("Correo") or dispositivo.get("correo", ""),
        "telefono": cliente.get("telefono") or dispositivo.get("telefono", ""),
        "fecha_ingreso": cliente.get("fecha_ingreso") or cliente.get("fecha_de_ingreso") or dispositivo.get("fecha_ingreso", ""),
        "dispositivo": cliente.get("dispositivo", ""),
        "modelo": dispositivo.get("modelo", ""),
        "procesador": dispositivo.get("procesador", ""),
        "ram": dispositivo.get("ram", ""),
        "memoria": dispositivo.get("memoria", ""),
        "tarjeta_grafica": dispositivo.get("tarjeta_grafica", ""),
        "fuente": dispositivo.get("fuente", ""),
        "pantalla": dispositivo.get("pantalla", ""),
        "sistema_operativo": dispositivo.get("sistema_operativo", ""),
        "estado": dispositivo.get("estado", ""),
        "garantia": dispositivo.get("garantia", ""),
        "precio": dispositivo.get("precio", ""),
        "notas": dispositivo.get("notas", "")
    }

    return plantilla_html.format(css=estilos_css, **datos_combinados)

def vista_previa_boleta(cliente, dispositivo):
    nombre_completo = cliente.get("Nombre") or cliente.get("nombre")
    id_cliente = cliente.get("id") or cliente.get("id_cliente")


    if not nombre_completo or not id_cliente:
        print("⚠️ No se puede generar vista previa sin nombre completo e ID.")
        return None

    html = generar_html_boleta(cliente, dispositivo)
    ruta_cliente = crear_directorio_cliente(nombre_completo, id_cliente)

    path_html = os.path.join(ruta_cliente, "vista_previa_boleta.html")
    with open(path_html, "w", encoding="utf-8") as f:
        f.write(html)

    webbrowser.open(f"file://{path_html}")
    return path_html


def generar_boleta_pdf(cliente, dispositivo, nombre_archivo="boleta.pdf"):
    # Validación explícita
    nombre_completo = cliente.get("Nombre") or cliente.get("nombre")
    id_cliente = cliente.get("id") or cliente.get("id_cliente")


    if not nombre_completo or not id_cliente:
        print("⚠️ Falta el nombre completo o el ID del cliente. Cancelando exportación.")
        return None

    html = generar_html_boleta(cliente, dispositivo)

    ruta_cliente = crear_directorio_cliente(nombre_completo, id_cliente)
    path_pdf = os.path.join(ruta_cliente, nombre_archivo)
    generar_pdf(path_pdf, html)
    return path_pdf


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                