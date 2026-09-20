"""
Reciclaje de funciones que se han usado anteriormente.
V1.0
"""
def pedirint(mensaje):
    """
    Validar si la entrada es de tipo entero. Arroja error si no se cumple.
    """
    valor=input(mensaje).strip()
    while not valor.lstrip("-").isdigit():
        print("Error: Entrada no válida. Ingresa un número entero.")
        valor=input(mensaje).strip()
    return int(valor)

def pedirfloat(mensaje):
    """
    Validar si la entrada es de tipo flotante. Arroja error si no se cumple
    """
    valor=input(mensaje).strip()
    while not isfloat(valor):
        print("Error: Entrada no válida. Ingresa un número (acepta decimales).")
        valor=input(mensaje).strip()
    return float(valor)

def pedirtexto(mensaje):
    """
    Validar que la entrada de texto no esté vacía
    """
    valor=input(mensaje).strip()
    while not valor:
        print("Error: La entrada no puede estar vacía.")
        valor=input(mensaje).strip()
    return valor
 
def pedirbin(mensaje):
    """
    Validar que los enteros ingresados sean sólo 0 o 1
    """
    valor=input(mensaje).strip()
    while valor not in ("0", "1"):
        print("Error: Solo se permite 0 o 1.")
        valor=input(mensaje).strip()
    return int(valor)

def isfloat(cadena):
    """
    Validar que los datos ingresados son tipo float.
    """
    try:
        float(cadena)
        return True
    except ValueError:
        return False