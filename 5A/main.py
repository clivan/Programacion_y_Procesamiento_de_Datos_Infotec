import os
import queue
import threading
import time
from adquisicion import adquisicion
from procesamiento import procesamiento
from registro import registro

PUERTO="/dev/ttyACM1" # Ajustar de acuerdo al puerto usado
BAUDRATE=115200
RUTA_CSV=os.path.join("resultados", "vibracion.csv")

def main():
    print("=== Monitoreo de vibración - Raspberry Pi Pico ===\n")
    cola_muestras=queue.Queue()
    cola_resultados=queue.Queue()
    evento_parada=threading.Event()
    hilo_adquisicion = threading.Thread(
        target=adquisicion,
        args=(PUERTO, BAUDRATE, cola_muestras, evento_parada),
        name="Adquisicion",
        daemon=True,
    )
    hilo_procesamiento = threading.Thread(
        target=procesamiento,
        args=(cola_muestras, cola_resultados, evento_parada),
        name="Procesamiento",
        daemon=True,
    )
    hilo_registro = threading.Thread(
        target=registro,
        args=(cola_resultados, evento_parada, RUTA_CSV),
        name="Registro",
        daemon=True,
    )
    hilo_adquisicion.start()
    hilo_procesamiento.start()
    hilo_registro.start()
    print("Sistema corriendo. Presiona Ctrl+C para detenerlo.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo hilos...")
        evento_parada.set()
    hilo_adquisicion.join(timeout=5)
    hilo_procesamiento.join(timeout=5)
    hilo_registro.join(timeout=5)
    print(f"\nResultados guardados en '{RUTA_CSV}'.")
    print("Programa finalizado.")

if __name__ == "__main__":
    main()
