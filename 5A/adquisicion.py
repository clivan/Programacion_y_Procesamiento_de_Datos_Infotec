"""
Hilo 1: Adquisición de datos.
"""
import time
import serial

def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def adquisicion(puerto, baudrate, cola_muestras, evento_parada, timeout=2):
    descartadas=0
    print(f"[Adquisición] Conectando a {puerto} @ {baudrate} baudios...")
    with serial.Serial(puerto, baudrate, timeout=timeout) as conexion:
        conexion.reset_input_buffer()
        print("[Adquisición] Conectado. Leyendo muestras...")
        while not evento_parada.is_set():
            linea = conexion.readline().decode("utf-8", errors="ignore").strip()
            if not linea:
                continue
            if not es_numero(linea):
                descartadas += 1
                continue
            cola_muestras.put((time.time(), float(linea)))
    print(f"[Adquisición] Finalizada. Muestras descartadas (no numéricas): {descartadas}")
