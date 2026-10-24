import os
from multiprocessing import Process, Queue

import pandas as pd

from analisis import SENSORES, proceso_sensor
from funciones import pedirint
from graficas import generar_graficas

BASE=os.path.dirname(os.path.abspath(__file__))
DIR_DATOS=os.path.join(BASE, "datos")
RUTA_REPORTE=os.path.join(BASE, "reporte_final.csv")
DIR_GRAFICAS=BASE


def ejecutar_analisis():
    cola_resultados=Queue()
    procesos=[]
    for sensor, archivo, nombre in SENSORES:
        ruta=os.path.join(DIR_DATOS, archivo)
        p=Process(target=proceso_sensor, args=(sensor, ruta, nombre, cola_resultados),
                    name=nombre)
        procesos.append(p)
        p.start()
    print("\nCorriendo los 4 procesos en paralelo...\n")
    resultados={}
    errores=[]
    for _ in procesos:
        estado, pid, nombre, contenido=cola_resultados.get()
        if estado=="ok":
            print(f"  [PID {pid}] {nombre}: terminado")
            resultados[contenido["Sensor"]]=contenido
        else:
            print(f"  [PID {pid}] {nombre}: ERROR -> {contenido}")
            errores.append(contenido)
    for p in procesos:
        p.join()
    if errores:
        print("\nErrores .")
        return
    reporte=pd.DataFrame([resultados[sensor] for sensor, _, _ in SENSORES])
    reporte.to_csv(RUTA_REPORTE, index=False, encoding="utf-8")
    print("\n" + reporte.to_string(index=False))
    print(f"\nReporte guardado en '{os.path.basename(RUTA_REPORTE)}'.")

def opcion_graficas():
    try:
        creados=generar_graficas(DIR_DATOS, RUTA_REPORTE, DIR_GRAFICAS)
    except FileNotFoundError as error:
        print(f"\n{error}")
        return
    print("\nGráficas generadas:")
    for archivo in creados:
        print(f"  - {archivo}")


def mostrar_menu():
    print("\n=================================")
    print(" Centro de Análisis de Señales")
    print("=================================\n")
    print("1. Ejecutar análisis")
    print("2. Generar gráficas")
    print("3. Salir\n")


def main():
    while True:
        mostrar_menu()
        opcion=pedirint("Seleccione una opción: ")
        if opcion==1:
            ejecutar_analisis()
        elif opcion==2:
            opcion_graficas()
        elif opcion==3:
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
