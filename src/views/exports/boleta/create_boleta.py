
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

            <!-- Campos dinámicos -->
            {campos_impresora}

            <p><strong>Estado:</strong> {estado}</p>
            <p><strong>Garantía hasta:</strong> {garantia}</p>

            <p class="precio">Precio estimado: ${precio}</p>
            <hr>
            {div_notas}
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
    background: #0D0D0D;
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
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.notas.impresora {
    min-height: 105mm;
}

.notas.computadora {
    min-height: 95mm;
}

.campos_impresora {
    margin-top: 15px;
    font-size: 9pt;
}

.campos_impresora p {
    margin: 5px 0;
    font-weight: normal;
    font-size: 9pt;
}
"""

def campo_html(label, valor):
    return f"<p><strong>{label}:</strong> {valor}</p>" if valor else ""

def generar_html_boleta(cliente, dispositivo):
    tipo_dispositivo = cliente.get("dispositivo", "").lower()
    es_impresora = tipo_dispositivo == "impresora"

    datos_comunes = {
        "nombre": cliente.get("nombre", dispositivo.get("nombre", "")),
        "correo": cliente.get("correo", dispositivo.get("correo", "")),
        "telefono": cliente.get("telefono", dispositivo.get("telefono", "")),
        "fecha_ingreso": cliente.get("fecha_ingreso", dispositivo.get("fecha_ingreso", "")),
        "dispositivo": cliente.get("dispositivo", ""),
        "modelo": dispositivo.get("modelo", ""),
        "estado": dispositivo.get("estado", ""),
        "garantia": dispositivo.get("garantia", ""),
        "precio": dispositivo.get("precio", ""),
        "notas": dispositivo.get("notas", "")
    }

    campos_html = ""

    if es_impresora:
        campos_html += f"""
        <div class="campos_impresora">
            {campo_html("Tipo de Impresora", dispositivo.get("tipo_impresora", ""))}
            {campo_html("Marca", dispositivo.get("marca", ""))}
            {campo_html("Conectividad", dispositivo.get("conectividad", ""))}
            {campo_html("Tipo de Tinta", dispositivo.get("tipo_tinta", ""))}
            {campo_html("Uso Estimado", dispositivo.get("uso_estimado", ""))}
            {campo_html("Número de Serie", dispositivo.get("numero_serie", ""))}
        </div>
        """
    else:
        campos_html += f"""
            {campo_html("Procesador", dispositivo.get("procesador", ""))}
            {campo_html("RAM", dispositivo.get("ram", ""))}
            {campo_html("Almacenamiento", dispositivo.get("memoria", ""))}
            {campo_html("Tarjeta Gráfica", dispositivo.get("tarjeta_grafica", ""))}
            {campo_html("Fuente", dispositivo.get("fuente", ""))}
            {campo_html("Pantalla", dispositivo.get("pantalla", ""))}
            {campo_html("Sistema Operativo", dispositivo.get("sistema_operativo", ""))}
        """

    div_clase_notas = '<div class="notas impresora">' if es_impresora else '<div class="notas computadora">'
    return plantilla_html.format(css=estilos_css, campos_impresora=campos_html, div_notas=div_clase_notas, **datos_comunes)

def vista_previa_boleta(cliente, dispositivo):
    nombre_completo = cliente.get("nombre")
    id_cliente = cliente.get("id_cliente")

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
    nombre_completo = cliente.get("nombre")
    id_cliente = cliente.get("id_cliente")

    if not nombre_completo or not id_cliente:
        print("⚠️ Falta el nombre completo o el ID del cliente. Cancelando exportación.")
        return None

    html = generar_html_boleta(cliente, dispositivo)
    ruta_cliente = crear_directorio_cliente(nombre_completo, id_cliente)

    path_pdf = os.path.join(ruta_cliente, nombre_archivo)
    generar_pdf(path_pdf, html)
    return path_pdf
