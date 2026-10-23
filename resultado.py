import argparse
import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from extraccion import normalizar

ARCHIVO = Path("servicios_LAFISE.csv")

def guardar_csv(ruta, datos, fecha):  
    with open(ruta, "w", encoding="utf-8-sig", newline="") as archivo: 
        escritor = csv.writer(archivo)  
        escritor.writerow(["fecha_consulta", "pais", "categoria", "servicio"])  
        for pais, categoria, servicio in datos:  
            escritor.writerow([fecha, pais, categoria, servicio])  


def procesar_resultados(datos):  
    parser = argparse.ArgumentParser(description="Servicios públicos de LAFISE")  
    parser.add_argument("--pais", default="")  
    parser.add_argument("--categoria", default="")  
    args = parser.parse_args() 

    if not datos:  # Comprueba que la extracción haya encontrado información.
        print("No se encontraron servicios. No se modificó el CSV anterior.")  # Evita guardar un CSV vacío.
        return  # Termina esta función sin continuar.

    anteriores = None  
    if ARCHIVO.exists():  
        with ARCHIVO.open(encoding="utf-8-sig", newline="") as archivo:  
            anteriores = {  
                (fila["pais"], fila["categoria"], fila["servicio"])  
                for fila in csv.DictReader(archivo)  
            }

    fecha = datetime.now(ZoneInfo("America/Managua")).isoformat(timespec="seconds")  
    guardar_csv(ARCHIVO, datos, fecha) 
        