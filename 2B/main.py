import numpy as np
from funciones import pedirint, pedirfloat #Funciones recicladas de tareas anteriores

N_LECTURAS=10  # cantidad de lecturas (días) por variable

def menu():
    print("===========================")
    print(" Análisis de Datos Climáticos")
    print("===========================")
    print("1. Capturar datos")
    print("2. Imprimir datos")
    print("3. Calcular estadísticas")
    print("4. Indexamiento y filtrado")
    print("5. Álgebra lineal")
    print("6. Funciones especiales")
    print("7. Salir")


class Clima:
    def __init__(self):
        self.temperatura=[]
        self.humedad=[]
        self.viento=[]

    def novacio(self):
        return len(self.temperatura) > 0

    # Opción 1: Capturar datos
    def capturar(self):
        print(f"\n--- Capturar datos ({N_LECTURAS} lecturas) ---")
        temperatura, humedad, viento=[], [], []
        for i in range(1, N_LECTURAS + 1):
            print(f"-- Día {i} --")
            temperatura.append(pedirfloat(f"  Temperatura día {i}: "))
            humedad.append(pedirfloat(f"  Humedad día {i}: "))
            viento.append(pedirfloat(f"  Viento día {i}: "))
        self.temperatura=temperatura
        self.humedad=humedad
        self.viento=viento
        print("Datos capturados correctamente.\n")

    # Opción 2: Imprimir datos
    def imprimir(self):
        print("\n--- Datos capturados ---")
        if not self.novacio():
            print("No hay datos capturados todavía.\n")
            return
        print(f"Temperaturas: {self.temperatura}")
        print(f"Humedades:    {self.humedad}")
        print(f"Vientos:      {self.viento}\n")

    # Opción 3: Calcular estadísticas
    def estadisticas(self):
        print("\n--- Estadísticas ---")
        if not self.novacio():
            print("No hay datos capturados todavía.\n")
            return
        variables={
            "Temperatura": np.array(self.temperatura),
            "Humedad": np.array(self.humedad),
            "Viento": np.array(self.viento),
        }
        for nombre, arreglo in variables.items():
            print(f"{nombre}:")
            print(f"  Media:               {arreglo.mean():.2f}")
            print(f"  Máximo:              {arreglo.max():.2f}")
            print(f"  Mínimo:              {arreglo.min():.2f}")
            print(f"  Desviación estándar: {arreglo.std():.2f}")
        print()

    # Opción 4: Indexamiento y filtrado
    def filtrado(self):
        print("\n--- Indexamiento y filtrado ---")
        if not self.novacio():
            print("No hay datos capturados todavía.\n")
            return
        temp=np.array(self.temperatura)
        hum=np.array(self.humedad)
        vien=np.array(self.viento)
        promedio_temp=temp.mean()
        dias_temp_alta=np.where(temp>promedio_temp)[0] + 1
        print(f"Promedio de temperatura: {promedio_temp:.2f}")
        print(f"Días con temperatura mayor al promedio: {dias_temp_alta.tolist()}")
        print(f"  Valores: {temp[temp > promedio_temp].tolist()}")
        dias_humedad_baja = np.where(hum < 40)[0] + 1
        print(f"\nDías con humedad menor a 40: {dias_humedad_baja.tolist()}")
        print(f"  Valores: {hum[hum < 40].tolist()}")
        mascara_combo = (temp > 30) & (vien > 20)
        dias_combo = np.where(mascara_combo)[0] + 1
        print(f"\nDías con temperatura > 30 y viento > 20: {dias_combo.tolist()}")
        print(f"  Temperaturas: {temp[mascara_combo].tolist()}")
        print(f"  Vientos:      {vien[mascara_combo].tolist()}\n")

    # Opción 5: Álgebra lineal
    def algebra(self):
        print("\n--- Álgebra lineal ---")
        if not self.novacio():
            print("No hay datos capturados todavía.\n")
            return
        temp=np.array(self.temperatura)
        hum=np.array(self.humedad)
        vien=np.array(self.viento)

        def normalizar(vector):
            norma = np.linalg.norm(vector)
            return vector / norma if norma != 0 else vector

        temp_norm=normalizar(temp)
        hum_norm=normalizar(hum)
        vien_norm=normalizar(vien)
        print("Vectores normalizados:")
        print(f"  Temperatura: {np.round(temp_norm, 3)}")
        print(f"  Humedad:     {np.round(hum_norm, 3)}")
        print(f"  Viento:      {np.round(vien_norm, 3)}")
        dot_temp_hum=np.dot(temp_norm, hum_norm)
        dot_temp_vien=np.dot(temp_norm, vien_norm)
        print(f"\nProducto punto Temperatura-Humedad: {dot_temp_hum:.4f}")
        print(f"Producto punto Temperatura-Viento:  {dot_temp_vien:.4f}")
        matriz=np.vstack([temp_norm, hum_norm, vien_norm])  # matriz 3x10
        print(f"\nMatriz 3x{N_LECTURAS} de datos normalizados:")
        print(np.round(matriz, 3))
        corr=np.corrcoef(matriz)
        print("\nMatriz de correlación 3x3 (Temperatura, Humedad, Viento):")
        print(np.round(corr, 3))
        print()

    # Opción 6: Funciones especiales
    def funciones_especiales(self):
        print("\n--- Funciones especiales ---")
        if not self.novacio():
            print("No hay datos capturados todavía.\n")
            return
        temp=np.array(self.temperatura)
        hum=np.array(self.humedad)
        indice_termico=temp*np.exp(hum/100)
        print("Índice térmico simulado (IT = temperatura * exp(humedad/100)):")
        print(f"Primeros 5 valores: {np.round(indice_termico[:5], 3)}\n")

def main():
    a=0
    clima=Clima()
    menu()
    while a!=7:
        a=pedirint("Opción: ")
        if a==1:
            clima.capturar()
        elif a==2:
            clima.imprimir()
        elif a==3:
            clima.estadisticas()
        elif a==4:
            clima.filtrado()
        elif a==5:
            clima.algebra()
        elif a==6:
            clima.funciones_especiales()
        elif a!=7:
            print("Opción no válida\n")
        if a!=7:
            menu()
    print("Finalizando el programa...")

if __name__ == "__main__":
    main()