from descarga import descargar_html
from bs4 import BeautifulSoup, Tag

sopa = BeautifulSoup(descargar_html(), "html.parser")

paises = ["Nicaragua", "Panamá", "Costa Rica", "Honduras", "República Dominicana"]

for i, nombre in enumerate(paises, 1):
    print(f"{i}. {nombre}")

respuesta = input("País (nombre o número): ").strip()
pais = paises[int(respuesta)-1] if respuesta.isdigit() and 1<=int(respuesta) <= len(paises) else respuesta

boton = next((e for e in sopa.find_all("button")
              if e.get_text(" ", strip=True).casefold()== pais.casefold()), None)
if not boton:
    raise SystemExit("No se encontro ese país en el HTML")

grupos = []
for etiqueta in boton.next_elements:
    if not isinstance(etiqueta, Tag):
        continue
    if etiqueta.name=="button" and etiqueta.get_text(" ", strip=True).casefold() in [p.casefold() for p in paises]:
        break
    if etiqueta.name=="h2":
        grupos.append([etiqueta, None])
    elif etiqueta.name in("ul", "ol") and grupos and grupos[-1][1] is None:
        if not etiqueta.find_parent(["ul", "ol"]):
             grupos[-1][1]=etiqueta

grupos= [(titulo, lista) for titulo, lista in grupos if lista is not None]

while True:
    print(f"\n País: {pais} -> <{boton.name}>")
    print("Grupos disponibles: ")
    for i, (titulo, _) in enumerate(grupos, 1):
        print(f"{i}. {titulo.get_text(' ', strip=True)} -> <{titulo.name}>")

    opcion = input(" Grupo (0 para salir)").strip()
    if opcion =="0":
        break
    if not opcion.isdigit() or not 1<=int(opcion) <=len(grupos):
        print("Elige un numero valido")
        continue

    titulo, lista = grupos[int(opcion)-1]
    print(f"\n {titulo.get_text(' ', strip=True)} -> <{titulo.name}>")
    print("Lista de servicios -> <{lista.name}>")

    for servicio in lista.find_all("li", recursive=False):
        print(f" {servicio.get_text(' ', strip=True)} -> <{servicio.name}>")
        if input("  Enter = siguiente <li> | s = otro grupo: ").strip().lower() =="s":
            break

