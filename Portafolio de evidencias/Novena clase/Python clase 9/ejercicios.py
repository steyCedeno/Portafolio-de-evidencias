""" Eduardo es un joven ciclista, cada semana debe reportar a su
entrenador la cantidad de kilómetros recorridos en sus prácticas. Haga
un programa que le permita almacenar para cada día los kilómetros
recorridos y luego al final de la semana muestre por cada día, junto con
el total de la semana. Para la solución, utilice arreglos y ciclos. """

""" kilometros = [0] * 7

semanas_entrenamiento = int(input("Ingrese la cantidad de semanas de entrenamiento: "))

for semana in range(1, semanas_entrenamiento + 1):
    print("Semana", semana)
    for dia in range(7):
        kilometro = float(input("Ingrese los kilómetros recorridos el día: "))
        kilometros[dia] += kilometro

for i in range(7):
    print("Día", i + 1, ":", kilometros[i], "kilómetros")

total_semana = sum(kilometros)
print("Total de la semana:", total_semana, "kilómetros") """

""" En una sala de teatro se requiere almacenar los nombres de las personas
que ocuparán las butacas de una fila, cada fila tiene 10 butacas. Cree
un programa que almacena los nombres en las posiciones que le van
indicando, por ejemplo: Ana Jiménez, 4 (el cuatro indica el número de
butaca)."""

""" butacas = []
for _ in range(10):
    butacas.append([])

while True:
    nombre = input("Ingrese el nombre de la persona (o escriba 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    
    num_butaca = int(input("Ingrese el número de butaca (de 1 a 10): ")) - 1
    if 0 <= num_butaca < 10:
        butacas[num_butaca].append(nombre)
    else:
        print("Número de butaca inválido. Inténtelo de nuevo.")

print("Nombres almacenados en las butacas:")

for num_fila in range(1, 11):
    fila = butacas[num_fila - 1]
    print("Fila", num_fila, "butacas:", fila) """


""" Se requiere un programa que imprima una palabra al revés, debe
funcionar para cualquier palabra, por lo cual debe utilizar instrucciones
de lectura. En la solución utilice ciclos. """

""" palabra = input("Ingrese una palabra: ")
palabra_al_reves = ""

for letra in palabra:
    palabra_al_reves = letra + palabra_al_reves

print("Palabra al revés:", palabra_al_reves) """

""" Jimena es una joven que trabaja para pagarse sus estudios. Se ha
inscrito en una de las plataformas de entrega de comida y otros.
Haga un programa que le permita a Jimena registrar el monto ganado
en cada día, al finalizar la semana le mostrará el total y le indicará el día
que ganó menos dinero. """

""" dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

total_ganado = 0
monto_ganado = float(input("Ingrese el monto ganado el: "))
menor_ganancia = monto_ganado
dia_menor_ganancia = dias_semana[0]

for dia in dias_semana[1:]:
    monto_ganado = float(input("Ingrese el monto ganado el: "))
    total_ganado += monto_ganado
    
    if monto_ganado < menor_ganancia:
        menor_ganancia = monto_ganado
        dia_menor_ganancia = dia

print("Total ganado en la semana:", total_ganado)
print("Día con menor ganancia:", dia_menor_ganancia) """

