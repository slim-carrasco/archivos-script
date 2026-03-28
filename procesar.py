
import json
import os

def leer_csv(archivo):
    filas=[]
    with open(f'{archivo}', 'r') as f:
                
            for linea in f:
                linea=linea.strip()
                lista=linea.split(",")
                filas.append(lista)
    return(filas)
def procesar_ruta(ruta):
    resultados=[]
    carpeta=os.listdir(ruta)
    for archivo in carpeta:
        if archivo.endswith(".csv"):
             resultados.append(leer_csv(f"{ruta}/{archivo}"))
    return(resultados)
def filtrar_criticos(filas):
    critico=[]
    for lineas in filas:
        for linea in lineas[1:]:
            if len(linea) < 5:
                continue
            elif int(linea[2]) > 80:
                critico.append(linea)
            elif linea[4]=="down":
                 critico.append(linea)
    return(critico)
def generar_reporte(critico):
    with open("reportes/reporte.txt", "w") as f:
    
        for fila in critico:
            f.write(f"{','.join(fila)}\n")
            
    columnas="timestamp", "servidor", "cpu", "memoria", "status"
    reportes=[]
    
    for fila in critico:
        reportes.append(dict(zip(columnas, fila)))
    with open ("reportes/reporte.json", "w") as f:
        f.write(json.dumps(reportes))
dir = input("Ingresa la ruta a procesar: ")
ruta = dir if dir != "" else "./data"
datos = procesar_ruta(ruta) if os.path.exists(ruta) else print("La ruta no existe")
datos_filtrados=filtrar_criticos(datos)
print("exito")
