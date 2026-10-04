"""
Tratamiento de señales con SciPy.
* Filtor pasa-bajas
* Detección de picos
* Detección de anomalías
* Análisis FFT
"""
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks
from scipy.fft import rfft, rfftfreq

FS=10
CORTE_HZ=1.5 
ORDEN_FILTRO=4 #2, 3, 5
UMBRAL_ANOMALIA=3

def filtro_pasa_bajas(valores, fs=FS, corte=CORTE_HZ, orden=ORDEN_FILTRO):
    b, a=butter(orden, corte, btype="low", fs=fs)
    return filtfilt(b, a, valores)

def detectar_picos(senal_filtrada):
    prominencia=np.std(senal_filtrada)*0.5
    indices, _=find_peaks(senal_filtrada, prominence=prominencia)
    return indices

def detectar_anomalias(valores, senal_filtrada, umbral=UMBRAL_ANOMALIA):
    residuo=valores-senal_filtrada
    limite=umbral*np.std(residuo)
    indices=np.where(np.abs(residuo-np.mean(residuo))>limite)[0]
    return indices

def calcular_fft(senal_filtrada, fs=FS):
    n=len(senal_filtrada)
    magnitudes=np.abs(rfft(senal_filtrada)) / n
    frecuencias=rfftfreq(n, d=1/fs)
    return frecuencias, magnitudes

def procesar_senial(df):
    valores=df["valor"].to_numpy()
    filtrada=filtro_pasa_bajas(valores)
    picos=detectar_picos(filtrada)
    anomalias=detectar_anomalias(valores, filtrada)
    frecuencias, magnitudes=calcular_fft(filtrada)
    return {
        "filtrada": filtrada,
        "picos": picos,
        "anomalias": anomalias,
        "frecuencias": frecuencias,
        "magnitudes": magnitudes,
    }
