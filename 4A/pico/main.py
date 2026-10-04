from machine import Timer
import math
import random
import time

muestra = 0

while True:

    # Tiempo simulado
    t = muestra * 0.1

    # Señal principal
    senal = 50 + 10 * math.sin(2 * math.pi * 0.1 * t)

    # Tendencia lenta
    tendencia = t * 0.02

    # Ruido
    ruido = random.uniform(-2, 2)

    # Señal final
    valor = senal + tendencia + ruido

    # Evento anómalo ocasional
    if muestra % 120 == 0 and muestra != 0:
        valor += random.uniform(15, 25)

    print(round(valor, 2))

    muestra += 1

    time.sleep(0.1)