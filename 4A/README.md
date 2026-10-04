Una empresa dedicada al monitoreo de maquinaria industrial desea analizar continuamente las lecturas provenientes de sensores instalados en sus equipos.

Debido a interferencias eléctricas y variaciones ambientales, las señales recibidas contienen ruido y eventos anómalos que dificultan identificar el comportamiento real del sistema.

El departamento de ingeniería ha desarrollado un dispositivo basado en Raspberry Pi Pico que transmite continuamente las lecturas de un sensor mediante comunicación serial.

Su equipo ha sido contratado para desarrollar una herramienta capaz de:

Capturar los datos enviados por la Pico.
Almacenar las mediciones.
Analizar la señal.
Filtrar el ruido.
Detectar anomalías.
Generar visualizaciones para apoyar la toma de decisiones.


Instrucciones:

Formen equipos con un máximo de tres integrantes.

Desarrollen una solución que permita adquirir las señales generadas por la Raspberry Pi Pico mediante comunicación serial y aplicar técnicas de procesamiento digital utilizando SciPy para obtener información útil a partir de los datos recibidos. El programa para la Raspberry Pi Pico se puede descargar en el link proporcionado, con el nombre generador_senial.py, también se proporciona un script de ejemplo para comprobar la generación de señales de la raspberry con el código en python llamado lectura_serial.py

Recuerda instalar las librerías a utilizar antes de ejecutar el código:

pip3 install numpy.
pip3 install scipy.
pip3 install pyserial.
pip3 install pandas.
La solución se dividirá de acuerdo con los puntos siguientes:

 
Parte 1. Comunicación serial
Desarrollar un programa en Python que:

Establezca comunicación con la Raspberry Pi Pico mediante PySerial.
Reciba al menos 1000 muestras.
Valide que los datos recibidos sean numéricos (en caso contrario, desecharlo pero continuar con la obtención de muestras).
Almacene la información para su procesamiento posterior.
 

Parte 2. Almacenamiento de datos
Crear un DataFrame de Pandas que contenga los siguiente campos:

Muestra: número consecutivo de la medición iniciando en 0. Ejemplo:
0, 1, 2, 3...999
Tiempo: instante en segundos en el que se tomó la muestra, calculado a partir de la frecuencia de muestreo (FS = 10). Ejemplo:
0.0, 0.1, 0.2, 0.3…0.9
Se calcula a partir del número de la muestra entre la frecuencia, por la cantidad total de datos:
tiempo = i/frecuencia
tiempo = 0/10 = 0
tiempo = 1/10 = 0.1
…
Valor: valores obtenidos de la Raspberry Pi Pico. Ejemplo:
50.2, 51.4, 48.8…


Guardar los datos en un archivo CSV con el nombre mediciones.csv. Ejemplo del contenido esperado:

muestra,tiempo,valor

0,0.0,63.53

1,0.1,60.23

2,0.2,61.27

3,0.3,61.52

 
Parte 3. Tratamiento de señales con SciPy
Aplicar las siguientes técnicas de procesamiento de señales (teniendo en cuenta que la frecuencia de muestreo son 10 muestras por segundo, FS=10):

Filtro pasa bajas.
Detección de picos en la señal filtrada.
FFT en la señal filtrada
 
Parte 4. Visualización
Generar las siguientes gráficas:

Gráfica 1: Señal original:
Generar un archivo de imagen llamado senal_original.png
Gráfica 2: Comparación entre señal original y filtrada:
Generar un archivo de imagen llamado senal_filtrada.png
Gráfica 4: Anomalías detectadas:
Generar un archivo de imagen llamado anomalias.png
Gráfica 5: Espectro de frecuencias (FFT):
Generar un archivo de imagen llamado fft.png


Sugerencia de organización del proyecto:

Practica4A/

├── datos/

│ └── mediciones.csv

├── resultados/

│ ├── senal_original.png

│ ├── senal_filtrada.png

│ ├── fft.png

│ └── anomalias.png 

├── captura.py

├── procesamiento.py

├── visualizacion.py

├── main.py


Requisitos técnicos:
Utilizar Python 3.
SciPy.
Pandas.
Matplotlib.
PySerial.
No está permitido modificar el programa cargado en la Raspberry Pi Pico. El sistema deberá trabajar exclusivamente con la señal recibida mediante el puerto serial.


Entregables:
1. Código fuente:

Archivo(s) .py debidamente comentados.

2. Reporte técnico:

a. Documento en formato PDF que incluya:

Portada.
Objetivo de la práctica.
Descripción de la solución implementada.
Metodología (descripción de las operaciones realizadas sobre los datos).
Capturas de pantalla de la ejecución y de las gráficas generadas.
Conclusiones generales del equipo.