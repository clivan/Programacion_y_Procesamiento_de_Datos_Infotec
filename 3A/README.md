Desarrollen un programa en Python que permita analizar un conjunto de datos climáticos utilizando la biblioteca Pandas y generar visualizaciones con Matplotlib. Recuerda que debes instalar las librerías antes de iniciar la práctica:

pip3 install pandas
pip3 install matplotlib


El programa deberá contar con un menú principal con las opciones siguientes:

===== MENÚ PRINCIPAL =====

1. Cargar datos

2. Exploración inicial

3. Indexamiento

4. Filtrado y agrupamiento

5. Series de tiempo

6. Gráficas

7. Salir



Selecciona una opción:

Si el usuario selecciona alguna de las opciones existentes, se deberá ejecutar el proceso correspondiente:



Opción 1. Cargar datos

Se trabajará con el archivo clima_2023.csv, así que da clic y descárgalo. Esta opción deberá:

Leer el archivo clima_2023.csv.
Convertir la columna fecha a tipo datetime.
Agregar la columna mes a partir de la fecha convertida anteriormente.
Retornar o almacenar el DataFrame generado, ya que se utilizará posteriormente.


Opción 2. Exploración inicial

El sistema deberá mostrar por consola:

Las primeras 10 filas.
Información general del DataFrame (info).
Estadísticas descriptivas (describe).


Opción 3. Indexamiento

El programa deberá mostrar por consola:

La columna de temperatura.
Las filas del día 50 al 70.
Las columnas temperatura y humedad de los primeros 100 registros.
El valor de temperatura del día 120.
El valor de humedad del día 200.


Opción 4. Filtrado y agrupamiento

El programa deberá mostrar por consola:

Filtrado de días con temperatura mayor a 30°
Filtrado de días con humedad menor a 40%
Ordenamiento del DataFrame por temperatura de mayor a menor.
Agrupamiento por mes para obtener:
Temperatura promedio
Humedad promedio
Precipitación total


Opción 5. Series de tiempo

Establecer la columna fecha como índice del DataFrame
Mostrar por consola:
Todos los registros de junio de 2023
El primer trimestre del año
El promedio semanal de temperatura usando resample(“W”)


Opción 6. Gráficas

El programa deberá generar y mostrar las siguientes gráficas:

Temperatura diaria (gráfica de línea).
Precipitación total por mes (gráfica de barras).
Histograma de temperaturas.


Cada gráfica deberá incluir:

Título.
Etiqueta de ejes.
Colores adecuados.


Requisitos técnicos:
Utilizar Python 3.
Pandas.
Matplotlib.
Funciones para organizar todo el código.


No se permite utilizar herramientas externas de análisis de datos (Power BI, Tableau, Excel para realizar los cálculos, etc.). Todo el procesamiento deberá realizarse mediante código Python.

Entregables:
1. Código fuente:

Archivo(s) .py debidamente comentados.

2. Reporte técnico:
a. Documento en formato PDF que incluya:
b. Portada.
c. Objetivo de la práctica.
d. Pseudocódigo de la solución implementada
e. Capturas de pantalla de la ejecución y de las gráficas generadas.
f. Responder a las preguntas siguientes:

¿Qué ventajas ofrece convertir la columna fecha en un DatetimeIndex al trabajar con series de tiempo en Pandas, y qué operaciones del programa dependen directamente de esta conversión?
Después de analizar los datos agrupados por mes, ¿qué patrones observaste en la temperatura, humedad o precipitación? Explica al menos una tendencia que identifiques y cómo la obtuviste.
De las tres gráficas generadas (temperatura diaria, precipitación mensual e histograma de temperaturas), ¿cuál consideras que aporta más información útil y por qué? Describe qué interpretación concreta puedes obtener de esa gráfica.
g. Conclusiones generales del equipo

