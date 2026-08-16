Algoritmo Sensores
    Definir tempC, tempF, tempK Como Real
    Definir humedad, porcentajeHumedad Como Real
    Definir hpa, relacionPresion, potencia, altitud Como Real
    Definir valorGas, relacionGas, ppm Como Real
    Definir a Como Entero
    tempC <- 0
    tempF <- 0
    tempK <- 0
    humedad <- 0
    porcentajeHumedad <- 0
    hpa <- 0
    relacionPresion <- 0
    potencia <- 0
    altitud <- 0
    valorGas <- 0
    relacionGas <- 0
    ppm <- 0
    a <- 0
    Menu
    Mientras a <> 4 Hacer
        Leer a
        Si a = 1 Entonces
            CapturarTemperatura(tempC)
            CapturarHumedad(humedad)
            CapturarPresion(hpa)
            CapturarGas(valorGas)
        SiNo
            Si a = 2 Entonces
                CalcularTemperatura(tempC, tempF, tempK)
                CalcularHumedad(humedad, porcentajeHumedad)
                CalcularPresion(hpa, relacionPresion, potencia, altitud)
                CalcularGas(valorGas, relacionGas, ppm)
            SiNo
                Si a = 3 Entonces
                    Escribir "Temperatura capturada: ", tempC
                    Escribir "Humedad capturada: ", humedad
                    Escribir "Presion capturada: ", hpa
                    Escribir "Gas Rs capturado: ", valorGas
                SiNo
                    Si a <> 4 Entonces
                        Escribir "Opcion no valida"
                    FinSi
                FinSi
            FinSi
        FinSi
        Si a <> 4 Entonces
            Menu
        FinSi
    FinMientras	
FinAlgoritmo

SubAlgoritmo Menu
    Escribir "==========================="
    Escribir "Menu principal"
    Escribir "==========================="
    Escribir "1. Capturar valores"
    Escribir "2. Calcular resultados"
    Escribir "3. Mostrar valores capturados"
    Escribir "4. Salir"
FinSubAlgoritmo

SubAlgoritmo CapturarTemperatura(tempC Por Referencia)
    Definir aux Como Cadena
    Escribir "Temperatura en Celsius: "
    Leer aux
    Si EsFloat(aux) Entonces
        tempC <- ConvertirANumero(aux)
    SiNo
        tempC <- 0
    FinSi
FinSubAlgoritmo

SubAlgoritmo CalcularTemperatura(tempC, tempF Por Referencia, tempK Por Referencia)
    tempF <- tempC * 9 / 5 + 32
    tempK <- tempC + 273.15
    Escribir "Temperatura: ", tempC, " C -> ", tempF, " F, ", tempK, " K"
FinSubAlgoritmo


SubAlgoritmo CapturarHumedad(humedad Por Referencia)
    Definir aux Como Cadena
    Escribir "Humedad: "
    Leer aux
    Si EsFloat(aux) Entonces
        humedad <- ConvertirANumero(aux)
    SiNo
        humedad <- 0
    FinSi
FinSubAlgoritmo

SubAlgoritmo CalcularHumedad(humedad, porcentaje Por Referencia)
    porcentaje <- (humedad * 100) / 4095
    Escribir "Humedad: ", porcentaje, " % de humedad"
FinSubAlgoritmo

SubAlgoritmo CapturarPresion(hpa Por Referencia)
    Definir aux Como Cadena
    Escribir "Presion: "
    Leer aux
    Si EsFloat(aux) Entonces
        hpa <- ConvertirANumero(aux)
    SiNo
        hpa <- 0
    FinSi
FinSubAlgoritmo

SubAlgoritmo CalcularPresion(hpa, relacion Por Referencia, potencia Por Referencia, altitud Por Referencia)
    relacion <- hpa / 1013.25
    potencia <- relacion ^ 0.1903
    altitud <- 44330 * (1 - potencia)
    Escribir "Presion: ", hpa, " hPa -> Altitud: ", altitud, " m"
FinSubAlgoritmo

SubAlgoritmo CapturarGas(valorGas Por Referencia)
    Definir aux Como Cadena
    Escribir "Gas: "
    Leer aux
    Si EsFloat(aux) Entonces
        valorGas <- ConvertirANumero(aux)
    SiNo
        valorGas <- 0
    FinSi
FinSubAlgoritmo

SubAlgoritmo CalcularGas(valorGas, relacion Por Referencia, ppm Por Referencia)
    Si valorGas = 0 Entonces
        relacion <- 0
        ppm <- 0
    SiNo
        relacion <- valorGas / 10
        ppm <- 20 * (relacion ^ (-1.5))
    FinSi
    Escribir "Gas MQ: Rs = ", valorGas, " -> ", ppm, " ppm"	
FinSubAlgoritmo

Funcion resultado <- EsFloat(num)
    Definir i, inicio, puntos Como Entero
    Definir caracter Como Caracter
    resultado <- Verdadero
    puntos <- 0
    inicio <- 1
    Si Longitud(num) = 0 Entonces
        resultado <- Falso
    SiNo
        Si Subcadena(num, 1, 1) = "-" Entonces
            inicio <- 2
        FinSi
        Si inicio > Longitud(num) Entonces
            resultado <- Falso
        SiNo
            Para i <- inicio Hasta Longitud(num) Hacer
                caracter <- Subcadena(num, i, i)
                Si caracter = "." Entonces
                    puntos <- puntos + 1
                    Si puntos > 1 Entonces
                        resultado <- Falso
                    FinSi
                SiNo
                    Si caracter < "0" O caracter > "9" Entonces
                        resultado <- Falso
                    FinSi
                FinSi
            FinPara
        FinSi
    FinSi
FinFuncion