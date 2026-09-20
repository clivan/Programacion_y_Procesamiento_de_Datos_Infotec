import pandas as pd
import matplotlib.pyplot as plt
from funciones import pedirint

ARCHIVO_CSV = "clima_2023.csv"
COLUMNAS_REQUERIDAS = {"fecha", "temperatura", "humedad", "precipitacion"}


def menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Cargar datos")
    print("2. Exploración inicial")
    print("3. Indexamiento")
    print("4. Filtrado y agrupamiento")
    print("5. Series de tiempo")
    print("6. Gráficas")
    print("7. Salir")


class ClimaPandas:
    def __init__(self):
        self.df = None

    def hay_datos(self):
        """Verifica que ya se hayan cargado datos antes de operar sobre ellos."""
        if self.df is None:
            print("Primero debes cargar los datos (opción 1).\n")
            return False
        return True

    def indice_fecha(self):
        """Convierte la columna 'fecha' en índice datetime, solo si aún no lo es."""
        if not isinstance(self.df.index, pd.DatetimeIndex):
            self.df = self.df.set_index("fecha").sort_index()

    # Opción 1: Cargar datos
    def cargar_datos(self):
        print("\n--- Cargar datos ---")
        try:
            df = pd.read_csv(ARCHIVO_CSV)
        except FileNotFoundError:
            print(f"No se encontró el archivo '{ARCHIVO_CSV}'.")
            return
        except pd.errors.EmptyDataError:
            print(f"El archivo '{ARCHIVO_CSV}' está vacío.\n")
            return

        if not COLUMNAS_REQUERIDAS.issubset(df.columns):
            print(f"El archivo no tiene las columnas esperadas {COLUMNAS_REQUERIDAS}.")
            print(f"Columnas encontradas: {list(df.columns)}\n")
            return

        df["fecha"] = pd.to_datetime(df["fecha"])
        df["mes"] = df["fecha"].dt.month
        self.df = df
        print(f"Datos cargados correctamente: {len(self.df)} registros.\n")

    # Opción 2: Exploración inicial
    def exploracion(self):
        print("\n--- Exploración inicial ---")
        if not self.hay_datos():
            return

        print("Primeras 10 filas:")
        print(self.df.head(10))
        print("\nInformación general:")
        self.df.info()
        print("\nEstadísticas descriptivas:")
        print(self.df.describe())
        print()

    # Opción 3: Indexamiento
    def indexamiento(self):
        print("\n--- Indexamiento ---")
        if not self.hay_datos():
            return

        print("Columna de temperatura:")
        print(self.df["temperatura"])
        print("\nFilas del día 50 al 70:")
        print(self.df.iloc[49:70])
        print("\nTemperatura y humedad de los primeros 100 registros:")
        print(self.df[["temperatura", "humedad"]].head(100))
        print(f"\nTemperatura del día 120: {self.df.iloc[119]['temperatura']}")
        print(f"Humedad del día 200: {self.df.iloc[199]['humedad']}\n")

    # Opción 4: Filtrado y agrupamiento
    def filtrado_agrupamiento(self):
        print("\n--- Filtrado y agrupamiento ---")
        if not self.hay_datos():
            return

        calidos = self.df[self.df["temperatura"] > 30]
        print(f"Días con temperatura mayor a 30° ({len(calidos)} registros):")
        print(calidos)
        secos = self.df[self.df["humedad"] < 40]
        print(f"\nDías con humedad menor a 40% ({len(secos)} registros):")
        print(secos)
        ordenado = self.df.sort_values("temperatura", ascending=False)
        print("\nDataFrame ordenado por temperatura (mayor a menor):")
        print(ordenado)
        agrupado = self.df.groupby("mes").agg(
            temperatura_promedio=("temperatura", "mean"),
            humedad_promedio=("humedad", "mean"),
            precipitacion_total=("precipitacion", "sum"),
        )
        print("\nAgrupamiento por mes:")
        print(agrupado)
        print()

    # Opción 5: Series de tiempo
    def series_tiempo(self):
        print("\n--- Series de tiempo ---")
        if not self.hay_datos():
            return

        self.indice_fecha()
        print("Registros de junio de 2023:")
        print(self.df.loc["2023-06"])
        print("\nPrimer trimestre del año (enero-marzo 2023):")
        print(self.df.loc["2023-01":"2023-03"])
        promedio_semanal = self.df["temperatura"].resample("W").mean()
        print("\nPromedio semanal de temperatura:")
        print(promedio_semanal)
        print()

    # Opción 6: Gráficas
    def graficas(self):
        print("\n--- Gráficas ---")
        if not self.hay_datos():
            return
 
        self.indice_fecha()
        fig, (ax_linea, ax_barras, ax_hist) = plt.subplots(1, 3, figsize=(16, 4.5))
        fig.suptitle("Análisis de Datos Climáticos - 2023")

        ax_linea.plot(self.df.index, self.df["temperatura"], color="tab:red")
        ax_linea.set_title("Temperatura diaria")
        ax_linea.set_xlabel("Fecha")
        ax_linea.set_ylabel("Temperatura (°C)")
        ax_linea.tick_params(axis="x", rotation=45)
 
        precipitacion_mensual = self.df.groupby("mes")["precipitacion"].sum()
        ax_barras.bar(precipitacion_mensual.index, precipitacion_mensual.values, color="tab:blue")
        ax_barras.set_title("Precipitación total por mes")
        ax_barras.set_xlabel("Mes")
        ax_barras.set_ylabel("Precipitación (mm)")
        ax_barras.set_xticks(range(1, 13))

        ax_hist.hist(self.df["temperatura"], bins=20, color="tab:green", edgecolor="black")
        ax_hist.set_title("Distribución de temperaturas")
        ax_hist.set_xlabel("Temperatura (°C)")
        ax_hist.set_ylabel("Frecuencia")
        plt.tight_layout()
        plt.show()


def main():
    opcion = 0
    clima = ClimaPandas()
    menu()
    while opcion != 7:
        opcion = pedirint("Selecciona una opción: ")
        if opcion == 1:
            clima.cargar_datos()
        elif opcion == 2:
            clima.exploracion()
        elif opcion == 3:
            clima.indexamiento()
        elif opcion == 4:
            clima.filtrado_agrupamiento()
        elif opcion == 5:
            clima.series_tiempo()
        elif opcion == 6:
            clima.graficas()
        elif opcion != 7:
            print("Opción no válida\n")
        if opcion != 7:
            menu()
    print("Finalizando el programa...")

if __name__ == "__main__":
    main()