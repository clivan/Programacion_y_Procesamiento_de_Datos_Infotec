Formen equipos con un máximo de tres integrantes. Solo un miembro del equipo deberá subir los entregables solicitados. 

Desarrollen un programa orientado a objetos que modele cuatro tipos de sensores (temperatura, humedad, presión, gas). El programa deberá simular la lectura de valores de sensores y realizar cálculos derivados según el tipo de sensor. Se deben implementar cuatro clases de sensores, todas heredando de una clase base llamada Sensor. Cada sensor deberá

Solicitar un valor al usuario.
Validar que el valor ingresado sea numérico.
Guardar el valor solo si es válido.
Implementar un método calcular() sobreescrito en cada clase hija.
Aplicar el cálculo aritmético correspondiente según el tipo de sensor.
El programa deberá contar con un menú como se observa a continuación:

========================

Menú Principal

========================

1- Capturar valores

2- Calcular resultados

3- Mostrar valores capturados

4- Salir



Seleccione una opción:

Cuando el usuario seleccione alguna de las opciones del menú, se deberán realizar las operaciones siguientes:

Opción 1. Capturar valores

El programa deberá solicitar el valor de cada uno de los sensores mencionados anteriormente (temperatura, humedad, presión y gas). Ejemplo:

Ingrese el valor para Temperatura:
Ingrese el valor para Humedad:
Ingrese el valor para Presión:
Ingrese el valor para Gas MQ:


En caso de que algún valor no sea válido (flotante), se deberá imprimir en consola:

Error: debe ingresar un número válido


Opción 2. Calcular resultados

El programa deberá realizar cálculos de acuerdo con el tipo de sensor capturado:

Sensor de Temperatura:
Debe convertir grados Celsius a:
F = C*9/5+32
K = C+273.15
Imprimir en consola el resultado. Ejemplo:
Temperatura: 20.0°C -> 68.0°F, 293.15K
Sensor de humedad:
Debe convertir el valor a porcentaje, considerando que el valor máximo es 4095:
porcentaje = (valor/4095)*100
Imprimir en consola el resultado. Ejemplo:
Humedad: 2.44% de humedad
Sensor de presión:
Debe obtener la altitud aproximada:
relacion = valor / 1013.25
potencia = relacion ** 0.1903
altitud = 44330 * (1 - potencia)
Imprimir en consola el resultado. Ejemplo:
Presión: 12.0 hPa -> Altitud: 25271.96 m
Sensor de Gas MQ:
Debe obtener la concentración aproximada de ppm:
relacion = valor / 10
ppm = 20 * (relacion ** -1.5)
Imprimir en consola el resultado. Ejemplo:
Gas MQ: Rs=12.0 -> 15.21 ppm


Opción 3. Mostrar valores capturados

El programa deberá imprimir en consola los valores capturados de los sensores de Temperatura, Humedad, Presión y Gas. Ejemplo:

Temperatura capturada: 20.0
Humedad capturada: 100.0
Presión capturada: 12.0
Gas Rs capturado: 12.0


Opción 4. Salir

El programa deberá finalizar su ejecución.

Requisitos técnicos:
Python 3
Clases y objetos
Constructores
Herencia
Polimorfismo
Sobreescritura de métodos
Validación de datos
Manejo de excepciones
Operaciones aritméticas
Menú especificado
No utilizar bibliotecas externas o cualquier otro tema no visto en clase.
