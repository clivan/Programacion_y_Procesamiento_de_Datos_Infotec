Instrucciones:

Desarrolla un programa en consola que permita capturar y analizar datos de temperatura mediante un menú interactivo. El sistema deberá validar los datos ingresados, almacenar valores, detectar anomalías y calcular estadísticas básicas.

El programa deberá mostrar continuamente el siguiente menú hasta que el usuario elija salir:

===========================

Análisis de datos de temperatura

===========================

1. Capturar datos

2. Ejecutar análisis

3. Salir

opción:

De acuerdo con el tipo de opción seleccionada, se deberán ejecutar los siguientes procesos:

 

Opción 1. Capturar datos

Al seleccionar la opción 1 del menú, el sistema deberá:
Solicitar 5 valores numéricos flotantes (almacenarlas en variables individuales ya definidas de manera global)
Validar que cada dato ingresado sea realmente un número flotante
Si el valor ingresado no es un número flotante, el sistema deberá continuar con el flujo normal (solicitar los valores siguientes)
Cada valor deberá almacenarse en una variable distinta:
Temperatura1
Temperatura2
Temperatura3
Temperatura4
Temperatura5
Cuando el usuario ingrese un dato inválido (texto, vacío, etc), la variable correspondiente deberá marcarse como inválida (puede asignarse None o un indicador similar), ya que estos valores no serán utilizados en los cálculos posteriores.
 

Opción 2. Ejecutar análisis

Al seleccionar la opción 2 del menú, el sistema deberá analizar los 5 valores capturados, de acuerdo con los puntos siguientes:

1. Validaciones previas: si alguna variable contiene un valor inválido, el sistema deberá:

a. Mostrar un mensaje indicando qué valor es inválido.
b. Continuar el análisis con los valores restantes.

2. Cálculos requeridos: con los valores válidos (flotantes), el sistema deberá calcular:

i. Rango válido: 20° a 50°
ii. Cualquier valor menor a 20° o mayor a 50° se considera fuera de rango
a. Promedio
b. Valor mínimo
c. Valor máximo
d. Cantidad de valores inválidos (anomalías)
e. Cantidad de valores fuera de rango, considerando:

i. Rango válido: 20° a 50°
ii. Cualquier valor menor a 20° o mayor a 50° se considera fuera de rango


f. El sistema deberá mostrar todos estos resultados por consola de forma clara.

 

Opción 3. Salir

Al seleccionar la opción 3 del menú, el programa deberá finalizar su ejecución.