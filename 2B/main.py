
"""
Funciones auxiliares de validación
"""
def pedirint(mensaje):
    valor=input(mensaje).strip()
    while not valor.lstrip("-").isdigit():
        print("Error: Entrada no válida. Ingresa un número entero.")
        valor=input(mensaje).strip()
    return int(valor)
 
def pedirtexto(mensaje):
    valor=input(mensaje).strip()
    while not valor:
        print("Error: La entrada no puede estar vacía.")
        valor=input(mensaje).strip()
    return valor
 
def pedirbin(mensaje):
    valor=input(mensaje).strip()
    while valor not in ("0", "1"):
        print("Error: Solo se permite 0 o 1.")
        valor=input(mensaje).strip()
    return int(valor)
 
 
def menu():
    print("===========================")
    print("Menú principal")
    print("===========================")
    print("1. Registrar sensor")
    print("2. Capturar lecturas")
    print("3. Mostrar lecturas")
    print("4. Generar reporte")
    print("5. Salir")
 
class Sensores:
    def __init__(self):
        self.sensores=[] #(id_sensor, nombre, tipo)
        self.lecturas=[] #{"id_sensor": id, "lecturas": []}
 
    def buscar(self, id_sensor):
        return next((s for s in self.sensores if s[0]==id_sensor), None)
 
    def registrar(self):
        print("\n-- Registrar sensor ---")
        id_sensor=pedirint("ID del sensor (Int): ")
        if self.buscar(id_sensor):
            print(f"Ya existe un sensor con el ID {id_sensor}.\n")
            return
        nombre=pedirtexto("Nombre del sensor: ")
        tipo=pedirtexto("Tipo de sensor: ")
        self.sensores.append((id_sensor, nombre, tipo))
        print(f"Sensor registrado: ({id_sensor}, {nombre}, {tipo})\n")
 
    def capturar(self):
        print("\n --- Capturar lecturas ---")
        id_sensor=pedirint("ID del sensor a capturar: ")
        if not self.buscar(id_sensor):
            print(f"No existe ningún sensor con el ID {id_sensor}.\n")
            return
        cantidad=pedirint("Cantidad de lecturas a capturar: ")
        while cantidad<=0:
            cantidad=pedirint("La cantidad debe ser mayor a cero. Intenta de nuevo: ")
        valores=[pedirbin(f"Lectura {i}/{cantidad}(0/1): ") for i in range(1, cantidad+1)]
        self.lecturas.append({"id_sensor": id_sensor, "lecturas": valores})
        print(f"Lecturas capturadas para el sensor {id_sensor}: {valores}\n")
 
    def mostrar(self):
        print("\n--- Mostrar lecturas --")
        if not self.lecturas:
            print("No hay lecturas registradas todavía.\n")
            return
        for registro in self.lecturas:
            datos=registro["lecturas"]
            print(f"Sensor ID: {registro['id_sensor']}")
            print(f"Lecturas: {datos}")
            print(f"Eventos activos (1): {datos.count(1)}")
            print(f"Reposo (0): {datos.count(0)}")
 
    def reporte(self):
        print("\n--- Reporte general ---")
        print("Sensores registrados: ")
        for id_sensor, nombre, tipo in self.sensores:
            print(f"\tID {id_sensor}\t{nombre}\t{tipo}")
        if not self.sensores:
            print("No hay sensores registrados")
        print(f"\nLecturas registradas:")
        for registro in self.lecturas:
            print(f"Sensor {registro['id_sensor']}: {registro['lecturas']}")
        if not self.lecturas:
            print("No hay lecturas registradas")
        print()
 
 
def main():
    a=0
    sistema=Sensores()
    menu()
    while (a!=5):
        a=pedirint("Selecciona una opción: ")
        if (a==1):
            sistema.registrar()
        if (a==2):
            sistema.capturar()
        if (a==3):
            sistema.mostrar()
        if (a==4):
            sistema.reporte()
        if (a!=1 and a!=2 and a!=3 and a!=4 and a!=5):
            print("Opción no válida")
        if (a!=5):
            menu()
    print("Finalizando el programa...")
 
if __name__ == "__main__":
    main()