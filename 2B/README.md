Instrucciones:

Desarrollar un programa en Python que simule un sistema embebido encargado de registrar sensores digitales y capturar sus lecturas (0 o 1). El programa deberá almacenar la información utilizando tuplas, listas y diccionarios, y mostrar reportes básicos del comportamiento de los sensores. El programa deberá mostrar un menú principal como se muestra a continuación:

----- MENÚ PRINCIPAL -----

1. Registrar sensor

2. Capturar lecturas

3. Mostrar lecturas

4. Generar reporte

5. Salir



Selecciona una opción: 

Dependiendo la opción seleccionada, el sistema deberá realizar los procesos siguientes:

Opción 1. Registrar sensor

Cada sensor se representará como una tupla:
(id_sensor, nombre, tipo)
id_sensor: valor numérico (1, 2, 3, etc)
nombre: nombre de la entrada (puerta 1)
tipo: Botón
Los sensores se almacenarán en una lista de tuplas global.
Validar que el ID sea numérico.


Opción 2. Capturar lecturas

El sistema debe solicitar el ID del sensor para comenzar la captura.
Si el ID no existe, el sistema deberá indicarlo a través de un mensaje por consola.
Si el ID existe, el sistema debe solicitar la cantidad de lecturas digitales a capturar.
Las lecturas se guardarán en un diccionario. Ejemplo:
{ “id_sensor”: 1, “lecturas”: [0, 1, 1, 0] }
Cada registro se almacenará en una lista global de lecturas.


Opción 3. Mostrar lecturas

Para cada sensor con lecturas registradas, mostrar:

ID del sensor.
Lista completa de lecturas.
Cantidad de valores 1 (eventos activos).
Cantidad de valores 0 (estado de reposo).


Ejemplo:

Sensor ID: 1

Lecturas: [1, 0, 1]

Eventos activos (1): 2

Reposo (0): 1

 

Sensor ID: 2

Lecturas: [1]

Eventos activos (1): 1

Reposo (0): 0

 

4. Generar reporte

El reporte deberá incluir:

Lista de sensores registrados
Lecturas capturadas por cada sensor


Ejemplo:

Lecturas registradas:

Sensor 1: [1, 0, 1]

Sensor 2: [1]

Sensor 3: [1]

 

5. Salir

Finaliza la ejecución del programa.

Requisitos técnicos:
Utilizar Python 3.
Implementar obligatoriamente:
Listas
Tuplas
Diccionarios
Utilizar funciones para organizar la lógica del programa.
Incluir comentarios que describan las secciones principales del código.
El programa deberá ejecutarse sin errores.
Se deberá validar el tipo de dato ingresado para evitar cierres inesperados.


Entregables:
Código fuente
Archivo(s) .py debidamente comentados
Reporte técnico
Documento en formato PDF que incluya:
Portada
Objetivo de la práctica
Pseudocódigo de la solución
Capturas de pantalla de la ejecución
Conclusiones
