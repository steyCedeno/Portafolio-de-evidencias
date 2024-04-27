#Ejercicio 1
""" def notas():
    notas = []
    for i in range(3):
        grupo = []
        print("Ingrese las notas del grupo", i+1)
        for j in range(5):
            nota = float(input("Ingrese la nota del estudiante {}: ".format(j+1)))
            grupo.append(nota)
        notas.append(grupo)
    return notas

def suma(notas):
    suma = 0
    for grupo in notas:
        for nota in grupo:
            suma += nota
    return suma

def promedio(notas):
    total_estudiantes = suma(notas)
    total_notas = sum(len(grupo) for grupo in notas)
    return total_estudiantes / total_notas

def promedio_grupo(notas):
    promedios = []
    for grupo in notas:
        suma_grupo = sum(grupo)
        promedio_grupo = suma_grupo / len(grupo)
        promedios.append(promedio_grupo)
    return promedios

def aprobados(notas):
    aprobados = []
    for grupo in notas:
        cantidad_aprobados = sum(1 for nota in grupo if nota >= 70)
        aprobados.append(cantidad_aprobados)
    return aprobados

def nota_mayor_menor(grupo):
    mayor = menor = grupo[0]
    for nota in grupo:
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menor = nota
    return mayor, menor

def resultados(notas):
    resultados = []
    for grupo in notas:
        mayor, menor = nota_mayor_menor(grupo)
        resultados.append((sum(grupo), sum(grupo) / len(grupo), mayor, menor))
    return resultados

def mostrar_resultados(notas, resultados):
    print("Notas ingresadas:")
    for i in range(len(notas)):
        print("Grupo", i+1, ":", notas[i])

    print("Promedio total de todas las notas:", promedio(notas))

    promedios = promedio_grupo(notas)
    for i, promedio in enumerate(promedios):
        print("Promedio del grupo", i+1, ":", promedio)

    aprobados_list = aprobados(notas)
    for i, cantidad in enumerate(aprobados_list):
        print("Cantidad de aprobados en el grupo", i+1, ":", cantidad)

    for i, (suma, promedio, mayor, menor) in enumerate(resultados):
        print("Grupo", i+1, ": Suma:", suma, ", Promedio:", promedio, ", Nota mayor:", mayor, ", Nota menor:", menor)

notas_list = notas()
resultados_list = resultados(notas_list)
mostrar_resultados(notas_list, resultados_list) """

#Ejercicio 2
""" def datos():
    pasajeros = []
    for dia in range(5):
        dia_servicio = [0] * 4
        pasajeros.append(dia_servicio)
    for dia in range(5):
        for servicio in range(4):
            while True:
                pasajeros_servicio = input("Ingrese la cantidad de pasajeros para el servicio {} del día {}: ".format(servicio + 1, dia + 1))
                if pasajeros_servicio.isdigit() and 0 <= int(pasajeros_servicio) <= 60:
                    pasajeros[dia][servicio] = int(pasajeros_servicio)
                    break
                else:
                    print("Entrada inválida. Por favor, ingrese un número válido entre 0 y 60.")
    return pasajeros

def sumar(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

def promedios(pasajeros):
    promedios_dia = [0] * 5
    for dia in range(5):
        promedios_dia[dia] = sumar(pasajeros[dia]) / 4
    promedio_general = sumar(sum(fila) for fila in pasajeros) / (5 * 4)
    return promedios_dia, promedio_general

def concurrido(pasajeros):
    servicios_concurridos = [0] * 4
    for dia in range(5):
        for servicio in range(4):
            servicios_concurridos[servicio] += pasajeros[dia][servicio]
    mayor = 0
    indice_mayor = 0
    for servicio in range(len(servicios_concurridos)):
        if servicios_concurridos[servicio] > mayor:
            mayor = servicios_concurridos[servicio]
            indice_mayor = servicio
    return indice_mayor + 1

def menos_concurrido(pasajeros):
    minimo = 9999
    minimo_servicio = 0
    minimo_dia = 0
    for dia in range(5):
        for servicio in range(4):
            if pasajeros[dia][servicio] < minimo:
                minimo = pasajeros[dia][servicio]
                minimo_servicio = servicio + 1
                minimo_dia = dia + 1
    return minimo_servicio, minimo_dia

pasajeros = datos()
promedios_dia, promedio_general = promedios(pasajeros)

for dia in range(5):
    print("Promedio de pasajeros para el día {}: {}".format(dia + 1, promedios_dia[dia]))
print("Promedio general de pasajeros: {}".format(promedio_general))
print("Servicio más concurrido: {}".format(concurrido(pasajeros)))
servicio_menos, dia_menos = menos_concurrido(pasajeros)
print("Servicio menos concurrido: {}, día {}".format(servicio_menos, dia_menos))"""

#Ejercicio 3
""" def pedir_salarios(cantidad_jugadores):
    salarios = []
    for _ in range(cantidad_jugadores):
        salario = int(input("Ingrese el salario del futbolista: "))
        salarios.append(salario)
    return salarios

def desglose(salario, denominacion):
    cantidad_billetes = salario // denominacion
    return cantidad_billetes, salario - cantidad_billetes * denominacion

def total(salarios):
    desglose_total = [0] * 11
    for salario in salarios:
        billetes = [50000, 20000, 10000, 5000, 2000, 1000, 500, 100, 25, 10, 5]
        for i in range(len(billetes)):
            cantidad_billetes, salario_restante = desglose(salario, billetes[i])
            desglose_total[i] += cantidad_billetes
            salario = salario_restante
    return desglose_total

cantidad_jugadores = int(input("Ingrese la cantidad de jugadores: "))
salarios = pedir_salarios(cantidad_jugadores)
desglose_total = total(salarios)

billetes = [50000, 20000, 10000, 5000, 2000, 1000, 500, 100, 25, 10, 5]
print("Denominación   Cantidad   Monto")
for i in range(len(desglose_total)):
    monto = billetes[i] * desglose_total[i]
    print("{:<14} {:<10} {}".format(billetes[i], desglose_total[i], monto)) """

#Ejercicio 4
""" import os

def cargar_personas(ruta_archivo):
    personas = []
    with open(ruta_archivo, "r") as file:
        for linea in file:
            personas.append(linea.strip())
    return personas

def guardar_personas(ruta_archivo, personas):
    with open(ruta_archivo, "w") as file:
        for persona in personas:
            file.write(persona + "\n")

def registro_ingreso(personas):
    if len(personas) >= 10:
        return "El abastecedor está lleno. No se permite ingresar más personas."

    nombre = input("Ingrese el nombre de la persona que ingresa: ")
    if not nombre:
        return "Nombre inválido. Por favor, ingrese un nombre válido."
    personas.append(nombre)
    guardar_personas(ruta_archivo, personas)
    return "Se ha registrado el ingreso de {}.".format(nombre)

def registro_salida(personas):
    if not personas:
        return "No hay personas dentro del abastecedor para la persona que sale."

    nombre = input("Ingrese el nombre de la persona que sale: ")
    if not nombre:
        return "Nombre inválido. Por favor, ingrese un nombre válido."

    if nombre in personas:
        personas.remove(nombre)
        guardar_personas(ruta_archivo, personas)
        return "Se ha registrado el egreso de {}.".format(nombre)
    else:
        return "La persona {} no se encuentra dentro del abastecedor.".format(nombre)

ruta_archivo = r"C:\Users\Hewlett Packard\Documents\Universidad 2024\Programación básica\Portafolio de evidencias\Duodécima clase\aforo.txt"

abastecedor = cargar_personas(ruta_archivo)

while True:
    opcion = input("Seleccione una opción: 1.Registrar ingreso, 2.Registrar salida, 3.Salir. Ingrese el número de la opción: ")
    if opcion == '1':
        resultado = registro_ingreso(abastecedor)
        print(resultado)
    elif opcion == '2':
        resultado = registro_salida(abastecedor)
        print(resultado)
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")"""
        
        