Proceso SimuladorSensores
	Definir opcion, i, j, idBuscado, cantidad, pos, activos, reposo Como Entero
	Definir contSensores, contLecturas Como Entero
	Definir nombre, tipo Como Caracter
	Definir encontrado Como Logico
	Definir idSensor Como Entero
	Definir nombreSensor, tipoSensor Como Caracter
	Dimension idSensor[50]
	Dimension nombreSensor[50]
	Dimension tipoSensor[50]
	Definir idLecturaSensor, cantLecturas Como Entero
	Definir lecturas Como Entero
	Dimension idLecturaSensor[50]
	Dimension cantLecturas[50]
	Dimension lecturas[50,100]
	contSensores <- 0
	contLecturas <- 0
	opcion <- 0
	Repetir
		Escribir ""
		Escribir "----- MENU PRINCIPAL -----"
		Escribir "1. Registrar sensor"
		Escribir "2. Capturar lecturas"
		Escribir "3. Mostrar lecturas"
		Escribir "4. Generar reporte"
		Escribir "5. Salir"
		Escribir "Selecciona una opcion: "
		Leer opcion
		Segun opcion Hacer
			1:
				// -----------------------------------------------
				// Opcion 1: Registrar sensor
				// -----------------------------------------------
				Escribir "--- Registrar sensor ---"
				Escribir "ID del sensor (numerico): "
				Leer idBuscado
				encontrado <- Falso
				Para i <- 1 Hasta contSensores Con Paso 1
					Si idSensor[i] = idBuscado Entonces
						encontrado <- Verdadero
					FinSi
				FinPara
				Si encontrado Entonces
					Escribir "Ya existe un sensor con el ID ", idBuscado
				SiNo
					Escribir "Nombre del sensor (ej. Puerta 1): "
					Leer nombre
					Escribir "Tipo de sensor (ej. Boton): "
					Leer tipo
					contSensores <- contSensores + 1
					idSensor[contSensores] <- idBuscado
					nombreSensor[contSensores] <- nombre
					tipoSensor[contSensores] <- tipo
					Escribir "Sensor registrado correctamente."
				FinSi
			2:
				// -----------------------------------------------
				// Opcion 2: Capturar lecturas
				// -----------------------------------------------
				Escribir "--- Capturar lecturas ---"
				Escribir "ID del sensor a capturar: "
				Leer idBuscado
				pos <- 0
				Para i <- 1 Hasta contSensores Con Paso 1
					Si idSensor[i] = idBuscado Entonces
						pos <- i
					FinSi
				FinPara
				Si pos = 0 Entonces
					Escribir "No existe ningun sensor con el ID ", idBuscado
				SiNo
					Escribir "Cantidad de lecturas a capturar: "
					Leer cantidad
					Mientras cantidad <= 0 Hacer
						Escribir "La cantidad debe ser mayor a cero. Intenta de nuevo: "
						Leer cantidad
					FinMientras
					contLecturas <- contLecturas + 1
					idLecturaSensor[contLecturas] <- idBuscado
					cantLecturas[contLecturas] <- cantidad
					Para i <- 1 Hasta cantidad Con Paso 1
						Escribir "Lectura ", i, "/", cantidad, " (0/1): "
						Leer lecturas[contLecturas, i]
						Mientras lecturas[contLecturas,i] <> 0 Y lecturas[contLecturas,i] <> 1 Hacer
							Escribir "Valor invalido. Solo se permite 0 o 1: "
							Leer lecturas[contLecturas, i]
						FinMientras
					FinPara
					Escribir "Lecturas capturadas para el sensor ", idBuscado
				FinSi
			3:
				// -----------------------------------------------
				// Opcion 3: Mostrar lecturas
				// -----------------------------------------------
				Escribir "--- Mostrar lecturas ---"
				Si contLecturas = 0 Entonces
					Escribir "No hay lecturas registradas todavia."
				SiNo
					Para i <- 1 Hasta contLecturas Con Paso 1
						activos <- 0
						reposo <- 0
						Para j <- 1 Hasta cantLecturas[i] Con Paso 1
							Si lecturas[i,j] = 1 Entonces
								activos <- activos + 1
							SiNo
								reposo <- reposo + 1
							FinSi
						FinPara
						Escribir "Sensor ID: ", idLecturaSensor[i]
						Escribir Sin Saltar "Lecturas: ["
						Para j <- 1 Hasta cantLecturas[i] Con Paso 1
							Si j > 1 Entonces
								Escribir Sin Saltar ", "
							FinSi
							Escribir Sin Saltar lecturas[i,j]
						FinPara
						Escribir "]"
						Escribir "Eventos activos (1): ", activos
						Escribir "Reposo (0): ", reposo
						Escribir ""
					FinPara
				FinSi
			4:
				// -----------------------------------------------
				// Opcion 4: Generar reporte
				// -----------------------------------------------
				Escribir "--- Reporte general ---"
				Escribir "Sensores registrados:"

				Si contSensores = 0 Entonces
					Escribir "  (sin sensores registrados)"
				SiNo
					Para i <- 1 Hasta contSensores Con Paso 1
						Escribir "  ID ", idSensor[i], " - ", nombreSensor[i], " (", tipoSensor[i], ")"
					FinPara
				FinSi

				Escribir ""
				Escribir "Lecturas registradas:"

				Si contLecturas = 0 Entonces
					Escribir "  (sin lecturas registradas)"
				SiNo
					Para i <- 1 Hasta contLecturas Con Paso 1
						Escribir Sin Saltar "  Sensor ", idLecturaSensor[i], ": ["
						Para j <- 1 Hasta cantLecturas[i] Con Paso 1
							Si j > 1 Entonces
								Escribir Sin Saltar ", "
							FinSi
							Escribir Sin Saltar lecturas[i,j]
						FinPara
						Escribir "]"
					FinPara
				FinSi
			5:
				Escribir "Finalizando el programa..."
			De Otro Modo:
				Escribir "Opcion invalida. Selecciona un numero del 1 al 5."
		FinSegun
	Hasta Que opcion = 5
FinProceso
