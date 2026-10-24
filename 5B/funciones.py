"""
Funciones auxiliares de validación (reciclado de tareas anteriores).
"""

def pedirint(mensaje):
    valor = input(mensaje).strip()
    while not valor.lstrip("-").isdigit():
        print("Error: Entrada no válida. Ingresa un número entero.")
        valor = input(mensaje).strip()
    return int(valor)


def pedirfloat(mensaje):
    valor = input(mensaje).strip()
    while not es_float(valor):
        print("Error: Entrada no válida. Ingresa un número (acepta decimales).")
        valor = input(mensaje).strip()
    return float(valor)


def pedirtexto(mensaje):
    valor = input(mensaje).strip()
    while not valor:
        print("Error: La entrada no puede estar vacía.")
        valor = input(mensaje).strip()
    return valor


def es_float(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
