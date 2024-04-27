""" # Capturar los tiempos de las vueltas
tiempos_vueltas = []
for i in range(10):
    tiempo_vuelta = float(input("Ingrese el tiempo de la vuelta en segundos: "))
    tiempos_vueltas.append(tiempo_vuelta)

# Capturar los tiempos en PITS
tiempos_pits = []
for i in range(10):
    tiempo_pit = float(input("Ingrese el tiempo en PITS en segundos: "))
    tiempos_pits.append(tiempo_pit)

# Calcular el tiempo promedio por vuelta
tiempo_promedio_vuelta = sum(tiempos_vueltas) / 10

# Calcular el tiempo promedio en PITS
tiempo_promedio_pits = sum(tiempos_pits) / 10

# Calcular el porcentaje del tiempo en PITS con respecto al tiempo de recorrido de una vuelta
porcentaje_pits_vuelta = (tiempo_promedio_pits / tiempo_promedio_vuelta) * 100

# Imprimir los resultados
print("Tiempo promedio por vuelta:", tiempo_promedio_vuelta, "segundos")
print("Tiempo promedio en PITS:", tiempo_promedio_pits, "segundos")
print("Porcentaje del tiempo en PITS respecto al tiempo de recorrido de una vuelta: ", porcentaje_pits_vuelta) """

""" # Solicitar la cantidad de niños
N = int(input("Ingrese la cantidad de niños en la escuela: "))

# Inicializar contadores para cada rango de altura y el total de estaturas
alt_menos_de_100 = 0
alt_100_y_120 = 0
alt_121_y_130 = 0
alt_131_y_140 = 0
alt_mas_de_140 = 0
total_estaturas = 0

# Solicitar las estaturas de los niños y calcular estadísticas
for i in range(N):
    estatura = float(input(f"Ingrese la estatura del niño {i + 1} en centímetros: "))
    total_estaturas += estatura
    
    if estatura < 100:
        alt_menos_de_100 += 1
    elif 100 <= estatura <= 120:
        alt_100_y_120 += 1
    elif 121 <= estatura <= 130:
        alt_121_y_130 += 1
    elif 131 <= estatura <= 140:
        alt_131_y_140 += 1
    else:
        alt_mas_de_140 += 1

# Calcular el promedio de estaturas
promedio_estaturas = total_estaturas / N

# Mostrar los resultados
print("Cantidad de niños que miden menos de 100 cm:", alt_menos_de_100)
print("Cantidad de niños que miden entre 100 y 120 cm:", alt_100_y_120)
print("Cantidad de niños que miden entre 121 y 130 cm:", alt_121_y_130)
print("Cantidad de niños que miden entre 131 y 140 cm:", alt_131_y_140)
print("Cantidad de niños que miden más de 140 cm:", alt_mas_de_140)
print("Promedio de estaturas:", promedio_estaturas, "cm")
"""
""" 
# Solicitar al usuario un valor
valor = int(input("Ingrese un valor: "))

# Mostrar los primeros 10 números divisibles entre el valor ingresado
print("Los primeros 10 números divisibles son: ")
contador = 0
numero = valor
while contador < 10:
    if numero % valor == 0:
        print(numero)
        contador += 1
    numero += 1
"""

""" def calcular_dinero_necesario(salarios):
    salario_minimo = 500
    dinero_necesario = 0
    for salario in salarios:
        if salario < salario_minimo:
            diferencia = salario_minimo - salario
            dinero_necesario += diferencia
    return dinero_necesario

salarios = []
for i in range(15):
    salario = float(input("Ingrese su salario: "))
    salarios.append(salario)

dinero_necesario = calcular_dinero_necesario(salarios)
print("Se necesitan $", dinero_necesario, "para que al menos todos ganen $500.") """
