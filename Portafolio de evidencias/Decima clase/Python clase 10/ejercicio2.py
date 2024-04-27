""" Un profesor necesita un programa que calcule la nota final de
sus estudiantes. Tiene 25 estudiantes que realizan 4 actividades
evaluativas (para efectos de esta clase, se reducirá a 5
estudiantes).
Utilice una matriz para almacenar las calificaciones donde
cada fila representará un estudiante y las columnas
almacenarán la información de las actividades evaluativas """

calificaciones = [[70, 80, 60, 100], [50, 70, 80, 90], [100, 60, 70, 50], [40, 60, 70, 80], [10, 60, 20, 10]]

def nota_final(calificaciones):
    notas_finales = []
    for estudiante in calificaciones:
        suma_notas = sum(estudiante)
        nota_final = suma_notas / len(estudiante)
        notas_finales.append(nota_final)
    return notas_finales

print(nota_final(calificaciones))

