import requests #Solicitando navegación a la pag web desde Py

URL = "https://www.lafise.com/bancanet/lafiservicios/index.html"

def descargar_html():
    respuesta = requests.get(URL, timeout=25)
    respuesta.raise_for_status()
    respuesta.encoding = respuesta.apparent_encoding or "utf-8"
    return respuesta.text