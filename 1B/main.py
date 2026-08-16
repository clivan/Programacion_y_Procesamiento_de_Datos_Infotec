def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        print("Error: debe ingresar un número válido")
        return False

def menu():
    print("===========================")
    print("Menú principal")
    print("===========================")
    print("1. Capturar valores")
    print("2. Calcular resultados")
    print("3. Mostrar valores capturados")
    print("4. Salir")
    
class Sensor:
    """Clase padre"""
    def __init__(self, sensor, valor, calculo):
        self.sensor=sensor
        self.valor=valor
        self.calculo=calculo
    def getValor(self):
        return "Valor"
    def calcular(self):
        return "Resultado"

class SensorTemperatura(Sensor):
    """Clase hija que hereda de Sensor"""
    def __init__(self, sensor, valor, calculo):
        super().__init__(sensor, valor, calculo)
        self.celsius=0.0
        self.kelvin=0.0
        self.farenheit=0.0
    def getValor(self):
        print(f"Temperatura en Celsius: ")
        aux=input()
        if isfloat(aux):
            self.celsius = float(aux)
        else:
            self.celsius = 0.0
    def calcular(self):
        self.farenheit=self.celsius*9.0/5.0+32.0
        self.kelvin=self.celsius+273.15
        print(f"Temperatura: {self.celsius: .2f}°C -> {self.farenheit: .2f}°F, {self.kelvin: .2f}K")

class SensorHumedad(Sensor):
    """Clase hija que hereda de Sensor"""
    def __init__(self, sensor, valor, calculo):
        super().__init__(sensor, valor, calculo)
        self.valorHumedad=0.0
        self.porcentaje=0.0
    def getValor(self):
        print(f"Humedad: ")
        aux=input()
        if isfloat(aux):
            self.valorHumedad=float(aux)
        else:
            self.valorHumedad=0.0
    def calcular(self):
        self.porcentaje=(self.valorHumedad*100)/4095
        print(f"Humedad: {self.porcentaje: .2f}% de humedad")

class SensorPresion(Sensor):
    """Clase hija que hereda de Sensor"""
    def __init__(self, sensor, valor, calculo):
        super().__init__(sensor, valor, calculo)
        self.hpa=0.0
        self.relacion=0.0
        self.potencia=0.0
        self.altitud=0.0
    def getValor(self):
        print(f"Presión: ")
        aux=input()
        if isfloat(aux):
            self.hpa=float(aux)
        else:
            self.hpa=0.0
    def calcular(self):
        self.relacion=self.hpa/1013.25
        self.potencia=self.relacion**0.1903
        self.altitud=44330*(1-self.potencia)
        print(f"Presión: {self.hpa: .2f} hPa -> Altitud: {self.altitud: .2f} m")

class SensorGas(Sensor):
    """Clase hija que hereda de Sensor"""
    def __init__(self, sensor, valor, calculo):
        super().__init__(sensor, valor, calculo)
        self.valorgas=0.0
        self.relacion=0.0
        self.ppm=0.0
    def getValor(self):
        print(f"Gas: ")
        aux=input()
        if isfloat(aux):
            self.valorgas=float(aux)
        else:
            self.valorgas=0.0
    def calcular(self):
        if self.valorgas==0.0:
            self.relacion=0.0
        else:
            self.relacion=self.valorgas/10
        self.ppm=20*(self.relacion**-1.5)
        print(f"Gas MQ: Rs={self.valorgas: .2f} -> {self.ppm: .2f}ppm")

if __name__ == "__main__":
    temp=SensorTemperatura("DHT22", 0, None)
    hum=SensorHumedad("DHT22", 0, None)
    pres=SensorPresion("BMP180", 0, None)
    gas=SensorGas("MQ-2", 0, None)
    a=0
    menu()
    while (a!=4):
        a=int(input())
        if (a==1):
            temp.getValor()
            hum.getValor()
            pres.getValor()
            gas.getValor()
        if (a==2):
            temp.calcular()
            hum.calcular()
            pres.calcular()
            gas.calcular()
        if (a==3):
            print(f"Temperatura capturada: {temp.celsius: .2f}")
            print(f"Humedad capturada: {hum.valorHumedad: .2f}")
            print(f"Presión capturada: {pres.hpa: .2f}")
            print(f"Gas Rs capturado: {gas.valorgas: .2f}")
        if (a!=1 and a!=2 and a!=3 and a!=4):
            print("Opción no válida")
        menu()

    
   


