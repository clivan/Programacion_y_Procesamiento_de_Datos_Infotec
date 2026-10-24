import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from analisis import SENSORES, limites_anomalia

ETIQUETAS={
    "TEMP": ("Temperatura", "Temperatura (°C)", "temperatura.png"),
    "HUM": ("Humedad", "Humedad (%)", "humedad.png"),
    "PRES": ("Presión", "Presión (kPa)", "presion.png"),
    "VIB": ("Vibración", "Vibración", "vibracion.png"),
}

def _cargar(dir_datos):
    return {sensor: pd.read_csv(os.path.join(dir_datos, archivo))
            for sensor, archivo, _ in SENSORES}

def _grafica_individual(sensor, datos, dir_salida):
    titulo, etiqueta_y, archivo=ETIQUETAS[sensor]
    tiempo, valores=datos["Timestamp"], datos["Valor"]
    inferior, superior=limites_anomalia(valores)
    es_anomalia=(valores < inferior) | (valores > superior)

    fig, ax=plt.subplots(figsize=(11, 4.5))
    ax.plot(tiempo, valores, linewidth=0.6, color="tab:blue", label=titulo)
    ax.scatter(tiempo[es_anomalia], valores[es_anomalia], s=14, color="red",
               zorder=3, label=f"Anomalías ({int(es_anomalia.sum())})")
    ax.axhline(inferior, color="gray", linestyle="--", linewidth=0.8, label="Promedio ± 2σ")
    ax.axhline(superior, color="gray", linestyle="--", linewidth=0.8)
    ax.set_title(f"{titulo} vs Tiempo")
    ax.set_xlabel("Tiempo (Timestamp)")
    ax.set_ylabel(etiqueta_y)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(dir_salida, archivo), dpi=120)
    plt.close(fig)
    return archivo

def _comparativa(todos, dir_salida):
    fig, ejes=plt.subplots(4, 1, figsize=(11, 10), sharex=True)
    for ax, (sensor, datos) in zip(ejes, todos.items()):
        titulo, etiqueta_y, _ = ETIQUETAS[sensor]
        ax.plot(datos["Timestamp"], datos["Valor"], linewidth=0.6)
        ax.set_ylabel(etiqueta_y)
        ax.set_title(titulo, loc="left", fontsize=10)
        ax.grid(alpha=0.3)
    ejes[-1].set_xlabel("Tiempo (Timestamp)")
    fig.suptitle("Comparativa de sensores", fontsize=14)
    fig.tight_layout()
    fig.savefig(os.path.join(dir_salida, "comparativa.png"), dpi=120)
    plt.close(fig)

def _anomalias(ruta_reporte, dir_salida):
    reporte=pd.read_csv(ruta_reporte)
    fig, ax=plt.subplots(figsize=(7, 4.5))
    barras=ax.bar(reporte["Sensor"], reporte["Anomalías"],
                    color=["tab:red", "tab:blue", "tab:green", "tab:orange"])
    ax.bar_label(barras)
    ax.set_title("Cantidad de anomalías por sensor")
    ax.set_xlabel("Sensor")
    ax.set_ylabel("Anomalías")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(dir_salida, "anomalias.png"), dpi=120)
    plt.close(fig)

def generar_graficas(dir_datos, ruta_reporte, dir_salida):
    if not os.path.exists(ruta_reporte):
        raise FileNotFoundError(
            f"No existe '{ruta_reporte}'. Ejecuta primero la opción 1 (Ejecutar análisis).")

    os.makedirs(dir_salida, exist_ok=True)
    todos=_cargar(dir_datos)

    creados=[_grafica_individual(sensor, datos, dir_salida) for sensor, datos in todos.items()]
    _comparativa(todos, dir_salida)
    _anomalias(ruta_reporte, dir_salida)
    creados+=["comparativa.png", "anomalias.png"]
    return sorted(creados)
