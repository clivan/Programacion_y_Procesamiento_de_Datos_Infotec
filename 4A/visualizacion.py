"""
Visualización.
* Original
* Original/filtrada
* Anomalías
* FFT
"""
import os
import matplotlib.pyplot as plt

CARPETA_RESULTADOS = "resultados"

def _ruta(nombre_archivo):
    os.makedirs(CARPETA_RESULTADOS, exist_ok=True)
    return os.path.join(CARPETA_RESULTADOS, nombre_archivo)

def graficar_original(df):
    plt.figure(figsize=(10, 4))
    plt.plot(df["tiempo"], df["valor"], color="tab:blue")
    plt.title("Señal original")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.savefig(_ruta("senal_original.png"), dpi=150)
    plt.close()

def graficar_filtrada(df, filtrada):
    plt.figure(figsize=(10, 4))
    plt.plot(df["tiempo"], df["valor"], color="tab:blue", alpha=0.5, label="Original")
    plt.plot(df["tiempo"], filtrada, color="tab:red", linewidth=2, label="Filtrada")
    plt.title("Señal original vs. señal filtrada")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor")
    plt.legend()
    plt.tight_layout()
    plt.savefig(_ruta("senal_filtrada.png"), dpi=150)
    plt.close()


def graficar_anomalias(df, filtrada, picos, anomalias):
    plt.figure(figsize=(10, 4))
    plt.plot(df["tiempo"], df["valor"], color="tab:blue", alpha=0.4, label="Señal original")
    plt.plot(df["tiempo"], filtrada, color="tab:gray", linewidth=1.5, label="Señal filtrada")
    if len(picos) > 0:
        plt.scatter(df["tiempo"].iloc[picos], filtrada[picos],
                    color="tab:green", marker="^", label="Picos detectados", zorder=5)
    if len(anomalias) > 0:
        plt.scatter(df["tiempo"].iloc[anomalias], df["valor"].iloc[anomalias],
                    color="tab:red", marker="x", s=80, label="Anomalías", zorder=6)
    plt.title("Anomalías detectadas")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Valor")
    plt.legend()
    plt.tight_layout()
    plt.savefig(_ruta("anomalias.png"), dpi=150)
    plt.close()

def graficar_fft(frecuencias, magnitudes):
    plt.figure(figsize=(10, 4))
    plt.plot(frecuencias, magnitudes, color="tab:purple")
    plt.title("Espectro de frecuencias (FFT)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.tight_layout()
    plt.savefig(_ruta("fft.png"), dpi=150)
    plt.close()
