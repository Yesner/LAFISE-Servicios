import unicodedata 
from bs4 import BeautifulSoup

paises = ["Nicaragua", "Panamá", "Costa Rica", "Honduras", "República Dominicana"]


def normalizar(texto): 
    texto = unicodedata.normalize("NFKD", texto)  
    return "".join(c for c in texto if not unicodedata.combining(c)).casefold().strip()  


def extraer_servicios(html):  
    sopa = BeautifulSoup(html, "html.parser")  
    pais = grupo = None  
    datos = []  

    for etiqueta in sopa.find_all(["button", "h2", "ul"]): 
        texto = etiqueta.get_text(" ", strip=True)  

        if etiqueta.name == "button" and texto in paises:  
            pais, grupo = texto, None  
        elif etiqueta.name == "h2":  
            if "todo en una sola aplicacion" in normalizar(texto):  
                break  
            if pais:  
                grupo = texto  
        elif etiqueta.name == "ul" and pais and grupo:  
            for li in etiqueta.find_all("li", recursive=False):  
                servicio = li.get_text(" ", strip=True)  
                if servicio:  
                    datos.append((pais, grupo, servicio))  
            grupo = None  

    return list(dict.fromkeys(datos))  