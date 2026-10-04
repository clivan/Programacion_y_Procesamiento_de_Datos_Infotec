"""
Comunicación serial.
Establece la conexión con el puerto serial. Esto permite la comunicación con la Raspberry Pi Pico mediante PySerial.
"""
import serial
from funciones import es_float

def capturar_muestras(puerto, baudrate, n_muestras, timeout=2):
    """
    Establece la conexión con el puerto serial y captura n muestras (válidas) tomadas por la Raspberry Pi Pico. Si no es numérica, se descarta, pero la lectura continúa.
    Retorna una lista de floats con las muestras capturadas.
    """
    muestras=[]
    descartadas=0
    print(f"Conectando a {puerto} @ {baudrate} baudios...")
    with serial.Serial(puerto, baudrate, timeout=timeout) as conexion:
        conexion.reset_input_buffer()
        while len(muestras)<n_muestras:
            crudo=conexion.readline()
            linea=crudo.decode("utf-8", errors="ignore").strip()
            if not linea:
                continue
            if not es_float(linea):
                descartadas+=1
                continue
            muestras.append(float(linea))
            if len(muestras)%100==0:
                print(f"  {len(muestras)}/{n_muestras} muestras capturadas...")

    print(f"Captura completa: {len(muestras)} muestras válidas, "
          f"{descartadas} descartadas por no ser numéricas.\n")
    return muestras
