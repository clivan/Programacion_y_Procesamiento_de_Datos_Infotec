import os
import pandas as pd

SENSORES=[
    ("TEMP", "temperatura.csv", "Proceso 1: Análisis de temperatura"),
    ("HUM", "humedad.csv", "Proceso 2: Análisis de humedad"),
    ("PRES", "presion.csv", "Proceso 3: Análisis de presión"),
    ("VIB", "vibracion.csv", "Proceso 4: Análisis de vibración"),
]

FACTOR_ANOMALIA=2

def limites_anomalia(valores):
    promedio=valores.mean()
    desviacion=valores.std()
    return promedio-FACTOR_ANOMALIA*desviacion, promedio+FACTOR_ANOMALIA*desviacion

def calcular_estadisticas(sensor, ruta_csv):
    datos=pd.read_csv(ruta_csv)
    valores=datos["Valor"]
    inferior, superior=limites_anomalia(valores)
    anomalias=int(((valores < inferior) | (valores > superior)).sum())
    return {
        "Sensor": sensor,
        "Muestras": int(valores.count()),
        "Min": round(float(valores.min()), 3),
        "Max": round(float(valores.max()), 3),
        "Promedio": round(float(valores.mean()), 3),
        "Mediana": round(float(valores.median()), 3),
        "Desv. Estándar": round(float(valores.std()), 3),
        "Anomalías": anomalias,
    }

def proceso_sensor(sensor, ruta_csv, nombre_proceso, cola_resultados):
    try:
        resultado = calcular_estadisticas(sensor, ruta_csv)
        cola_resultados.put(("ok", os.getpid(), nombre_proceso, resultado))
    except Exception as error:
        cola_resultados.put(("error", os.getpid(), nombre_proceso, f"{sensor}: {error}"))
