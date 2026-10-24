import math
import utime

AMPLITUD = 1500
OFFSET = 2048

t = 0.0
dt = 0.01

inicio = utime.ticks_ms()

while True:

    tiempo = (
        utime.ticks_diff(
            utime.ticks_ms(),
            inicio
        ) / 1000
    )

    ciclo = int(tiempo // 20) % 4

    if ciclo == 0:
        frecuencia = 5

    elif ciclo == 1:
        frecuencia = 10

    elif ciclo == 2:
        frecuencia = 20

    else:
        frecuencia = 40

    valor = int(
        OFFSET +
        AMPLITUD *
        math.sin(
            2 * math.pi * frecuencia * t
        )
    )

    print(valor)

    t += dt

    utime.sleep_ms(10)
