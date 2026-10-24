"""
Hilo 3: Registro de resultados.

Toma los resultados calculados por el hilo de procesamiento y los guarda
en un archivo CSV, una fila por cada bloque procesado.
"""
import csv
import os
import queue

CAMPOS_CSV = ["FechaHora", "Promedio", "Maximo", "Minimo", "RMS", "DesviacionEstandar"]


def _escribir_fila(escritor, resultado):
    escritor.writerow([
        resultado["fecha_hora"],
        resultado["promedio"],
        resultado["maximo"],
        resultado["minimo"],
        resultado["rms"],
        resultado["desviacion"],
    ])


def registro(cola_resultados, evento_parada, ruta_csv):
    carpeta = os.path.dirname(ruta_csv)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    archivo_nuevo = not os.path.exists(ruta_csv)

    with open(ruta_csv, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if archivo_nuevo:
            escritor.writerow(CAMPOS_CSV)
            archivo.flush()

        while not evento_parada.is_set():
            try:
                resultado = cola_resultados.get(timeout=1)
            except queue.Empty:
                continue

            _escribir_fila(escritor, resultado)
            archivo.flush()
            print(f"[Registro] Bloque guardado en '{ruta_csv}'.")

        # Al detenerse, vaciamos lo que haya quedado pendiente en la cola
        while True:
            try:
                resultado = cola_resultados.get_nowait()
            except queue.Empty:
                break
            _escribir_fila(escritor, resultado)
        archivo.flush()

    print("[Registro] Finalizado.")
