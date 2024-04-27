""" La asociación de desarrollo de su comunidad desea iniciar un nuevo recurso para la obtención de
ingresos, esto mediante rifas con premios donados a la Asociación. En estos participan todas las
personas que asisten a las reuniones semanales y que realizan un aporte. Los premios de cada rifa
puede variar según el aporte que realiza el miembro. Esta es la cantidad de dinero de los aportes que
se pueden realizar y los premios posibles para cada uno:
Aporte Premio
500 colones Hamburguesa con papas y gaseosa.
1000 colones Cupon cena para 2 personas.
2000 colones Un día en el parque de diversiones con
transporte y comida pago para 3 personas.
5000 colones Fin de semana todo incluido en hotel
paradisiaco para 2 personas.
El secretario de la asociación debe seleccionar un número ganador por semana, esto para 4
semanas. El número debe estar entre 1 y 100, teniendo un máximo de participantes para la rifa de
100 personas por semana. Una vez que el secretario configura todos los números ganadores para
las semanas. Se selecciona la semana que se hará la reunión y los miembros ingresan sus datos.
- El miembro de la sesión ingresa su nombre, cédula y el monto que aportó.
- Se debe verificar si el numero de ingreso corresponde al número ganador para esa semana.
- Si el número de ingreso es el mismo que el número ganador, entonces se guardan los datos
del miembro ganador.
- Una vez que se completan los 100 ingresos, el programa muestra el nombre de la persona
ganadora, el número de cédula y el premio que obtuvo, basado en el monto aportado.
- También se debe mostrar cuál fue el monto total recaudado para esa semana. """

# Definición de listas para aportes y premios
aportes = [500, 1000, 2000, 5000]
premios = ["Hamburguesa con papas y gaseosa", "Cupon cena para 2 personas","Un día en el parque de diversiones con transporte y comida para 3 personas","Fin de semana todo incluido en hotel paradisiaco para 2 personas"]
monto_total = 0
numeros_ganadores = []


#Bucle para los numeros ganadores de las 4 semanas
for i in range(4):
    while True:  #se empiza con el valor verdaero, por ende mientras no cambie el valor va a seguirse ejecutando
        numero_ganador = int(input("Número ganador semana: "))
        if 1 <= numero_ganador <= 100:  # Verificación de rango del número ganador
            numeros_ganadores.append(numero_ganador)
            break #rompe el bucle while 
        else:
            print("Ese número está fuera de rango. Por favor, inténtelo de nuevo.")

numero_de_participantes = int(input("Ingrese la cantidad de personas que participaron en esta rifa: "))

#rifa segun los participantes ingresados
for i in range(numero_de_participantes):
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    aporte = int(input("Monto aportado 500, 1000, 2000, 5000: "))

    numero_rifa = int(input("Número de la rifa 1 al 100: "))
    if numero_rifa in numeros_ganadores:
        premio_ganador = premios[aportes.index(aporte)]  # Se busca en la lista de premios segun el aporte dado
        print("¡Felicidades!", nombre, "con el número de cédula", cedula, "ganó", premio_ganador)
        monto_total += aporte 

# Mostrar el monto total recaudado
print("Monto total recaudado:", monto_total, "colones")
