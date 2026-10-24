"""
Hilo 2: Procesamiento de la señal.
"""
import queue
import time
from datetime import datetime

import numpy as np
from scipy.fft import rfft, rfftfreq

TAMANO_BLOQUE=255
RETARDO_PROCESAMIENTO=0.5

def calcular_frecuencia_dominante(valores, fs):
    señal_ac=valores-np.mean(valores)
    magnitudes=np.abs(rfft(señal_ac))
    frecuencias=rfftfreq(len(señal_ac), d=1 / fs)
    indice_pico=np.argmax(magnitudes[1:]) + 1
    return frecuencias[indice_pico]

def procesar_bloque(muestras):
    timestamps=np.array([m[0] for m in muestras])
    valores=np.array([m[1] for m in muestras], dtype=float)

    duracion=timestamps[-1]-timestamps[0]
    fs_estimada=(len(valores)-1) / duracion if duracion > 0 else 100.0
    promedio=np.mean(valores)
    maximo=np.max(valores)
    minimo=np.min(valores)
    rms=np.sqrt(np.mean(valores ** 2))
    desviacion=np.std(valores)
    frecuencia_dominante=calcular_frecuencia_dominante(valores, fs_estimada)
    return {
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "promedio": round(float(promedio), 2),
        "maximo": int(maximo),
        "minimo": int(minimo),
        "rms": round(float(rms), 2),
        "desviacion": round(float(desviacion), 2),
        "frecuencia_dominante": round(float(frecuencia_dominante), 2),
        "fs_estimada": round(float(fs_estimada), 2),
    }

def procesamiento(cola_muestras, cola_resultados, evento_parada):
    while not evento_parada.is_set():
        bloque=[]
        try:
            while len(bloque) < TAMANO_BLOQUE:
                bloque.append(cola_muestras.get(timeout=1))
        except queue.Empty:
            continue
        resultado=procesar_bloque(bloque)
        print(f"[Procesamiento] {resultado['fecha_hora']} | "
              f"Prom={resultado['promedio']} Max={resultado['maximo']} "
              f"Min={resultado['minimo']} RMS={resultado['rms']} "
              f"Std={resultado['desviacion']} | "
              f"Frecuencia dominante ≈ {resultado['frecuencia_dominante']} Hz "
              f"(fs≈{resultado['fs_estimada']} Hz)")
        cola_resultados.put(resultado)
        time.sleep(RETARDO_PROCESAMIENTO)
    print("[Procesamiento] Finalizado.")
