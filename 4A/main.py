import os
import pandas as pd
import serial

from funciones import pedirint
from captura import capturar_muestras
from procesamiento import procesar_senial, FS
from visualizacion import (
    graficar_original,
    graficar_filtrada,
    graficar_anomalias,
    graficar_fft,
)

PUERTO="/dev/ttyACM0" #Para Linux el puerto sería diferente que para Windows
BAUDRATE = 115200
CARPETA_DATOS = "datos"
ARCHIVO_CSV = "mediciones.csv"


def construir_dataframe(muestras, fs=FS):
    n=len(muestras)
    return pd.DataFrame({
        "muestra": range(n),
        "tiempo": [i / fs for i in range(n)],
        "valor": muestras,
    })


def guardar_csv(df):
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    ruta=os.path.join(CARPETA_DATOS, ARCHIVO_CSV)
    df.to_csv(ruta, index=False)
    print(f"Datos guardados en '{ruta}'.\n")

def main():
    print("=== Sistema híbrido - Laptop/Raspberry Pi Pico ===\n")
    n_muestras=pedirint("Cantidad de muestras a capturar (mínimo 1000): ")
    while n_muestras<1000:
        n_muestras=pedirint("Debe ser al menos 1000. Intenta de nuevo: ")
    print("\nComunicación serial")
    try: #Se usa try porque la conexión con el puerto puede quebrar el programa si es incorrecta.
        muestras = capturar_muestras(PUERTO, BAUDRATE, n_muestras)
    except serial.SerialException as error:
        print(f"No se pudo establecer comunicación con la Raspberry Pi Pico: {error}")
        print(f"Verifica que esté conectada y que el puerto ('{PUERTO}') sea el correcto.")
        return
    df=construir_dataframe(muestras)
    guardar_csv(df)
    print("El csv se guardó correctamente")
    print("Tratamiento de señales con SciPy")
    resultados=procesar_senial(df)
    print(f"Picos detectados: {len(resultados['picos'])}")
    print(f"Anomalías detectadas: {len(resultados['anomalias'])}\n")
    print("Creación de gráficas")
    graficar_original(df)
    graficar_filtrada(df, resultados["filtrada"])
    graficar_anomalias(df, resultados["filtrada"], resultados["picos"], resultados["anomalias"])
    graficar_fft(resultados["frecuencias"], resultados["magnitudes"])
    print("Gráficas guardadas en la carpeta 'resultados/'.\n")
    print("Proceso finalizado.")


if __name__ == "__main__":
    main()
