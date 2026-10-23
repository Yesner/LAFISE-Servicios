import requests
from descarga import descargar_html
from extraccion import extraer_servicios
from resultado import procesar_resultados

if __name__ == "__main__":
    try:
        html = descargar_html()
        datos=extraer_servicios(html)
        procesar_resultados(datos)
    except requests.RequestException as error:
        print(f"No se pudo consultar LAFISE {error}")