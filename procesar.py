import os
def leer_csv(archivo):
    with open(f'{archivo}', 'r') as f:
        for linea in f:
                linea=linea.strip()
                lista=linea.split(",")
                print(lista)
def procesar_ruta(ruta):
    carpeta=os.listdir(ruta)
    for archivo in carpeta:
        if archivo.endswith(".csv"):
             leer_csv(f"{ruta}/{archivo}")
def filtrar_criticos(datos):
    pass
def generar_reporte(filtrado):
    pass

leer_csv("./data/servidor_db1.csv")
