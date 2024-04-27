#Ejercicio 1
""" def no_num(matriz, letra):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == letra:
                return fila, columna
    return None


matriz = [[70, 80, 60, 100],
          [65, 70, 55, 90],
          [90, 100, 'o', 80],
          [92, 85, 70, 75],
          [93, 88, 75, 60]]

buscar_o = 'o'
ubicacion = no_num(matriz, buscar_o)
if ubicacion:
    fila, columna = ubicacion
    print("La letra {} se encontro en la posicion: {}, {} ". format(
        buscar_o, fila, columna))
else:
    print("La letra {} no se encontro en la matriz". format(buscar_o))"""

#Ejercicio 2
""" def calcular_nf(calificaciones):
    nota_final = sum(calificaciones) / len(calificaciones)
    return nota_final

calificaciones = []

for i in range(5):
    print("Ingrese las calificaciones para el estudiante {}:".format(i+1))
    calificaciones_estudiante = []
    for j in range(4):  
        calificacion = float(input("Calificación {}:".format(j+1)))
        calificaciones_estudiante.append(calificacion)
    calificaciones.append(calificaciones_estudiante)

notas_finales = []
for nota in calificaciones:
    nota_final = calcular_nf(nota)
    notas_finales.append(nota_final)

for i in range(len(notas_finales)):
    print("La nota final del estudiante {} es: {}".format(i+1, notas_finales[i]))"""

#Ejercicio 3
""" microbus = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def mostrar_asientos():
    print("Estado actual de los asientos:")
    for i in range(len(microbus)):
        for j in range(len(microbus[i])):
            print("Fila {}, Asiento {}: {}".format(i + 1, j + 1, 'Disponible' if microbus[i][j] == 0 else 'Reservado'))

def reservar_asiento(fila, columna):
    if microbus[fila][columna] == 0:
        microbus[fila][columna] = 1
        print("¡Has reservado el asiento en la fila {}, asiento {}!".format(fila + 1, columna + 1))
    else:
        print("Lo siento, este asiento no está disponible.")

print("Bienvenido al sistema de reserva de espacios en la microbús.")
while True:
    opcion = input("¿Desea reservar un asiento? (si/no): ").lower()
    if opcion == 'si':
        mostrar_asientos()
        fila = int(input("Ingrese el número de fila del asiento que desea reservar: ")) - 1
        columna = int(input("Ingrese el número de asiento de la fila que desea reservar: ")) - 1
        if 0 <= fila < len(microbus) and 0 <= columna < len(microbus[0]):
            reservar_asiento(fila, columna)
        else:
            print("La fila o el asiento ingresado no son válidos.")
        mostrar_asientos()
    elif opcion == 'no':
        print("Gracias por usar nuestro servicio de reserva. ¡Buen viaje!")
        break
    else:
        print("Opción no válida. Por favor, ingrese 'si' para reservar un asiento o 'no' para salir.") """


