from weasyprint import HTML

def generar_pdf(nombre_archivo: str, html_content: str):
    """
    Genera un PDF a partir de un contenido HTML.

    :param nombre_archivo: Ruta completa del archivo PDF de salida.
    :param html_content: Código HTML con el contenido del PDF.
    """
    try:
        HTML(string=html_content).write_pdf(nombre_archivo)
        print(f"📄 PDF generado exitosamente: {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error al generar el PDF: {e}")
