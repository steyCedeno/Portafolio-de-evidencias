""" Se desea crear un programa que identifique la temperatura promedio de las personas que
ingresan por día a un establecimiento, como no se sabe la cantidad, cada persona ingresa,
digita su nombre y también digita su temperatura. Esto se debe realizar para cada día de la
semana laboral, es decir de lunes a viernes. El programa mostrará:
● Temperatura promedio de las personas para cada día.
● La persona con la temperatura más alta y menos alta por cada día con su respectivo
nombre.
Para realizar los ingresos, el programa consulta cual día desea ingresar, se selecciona uno de
ellos por ejemplo:
Seleccione el dia que desea ingresar
[1] Lunes
[2] Martes
[3] Miercoles
[4] Jueves
[5] Viernes
[6] Mostrar resultados y salir
Por cada uno de los días, se ingresarán los datos que se requieran, sin un límite específico.
Resultados esperados.
Una vez que se ingresan los resultados y se selecciona la opción 6, entonces el programa
deberá mostrar algo similar a:
Lunes
- Temperatura promedio: 37
- Temperatura máxima: 38 | Francisco Leiva
- Temperatura minima: 36 | Francisco Arroyo
Martes
- Temperatura promedio: 37
- Temperatura máxima: 39 | Marta Juarez
- Temperatura minima: 36 | Tobias Ferrera
Hasta luego. """

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
while True:
    nombre = input("Ingrese su nombre ( si quiere salir, digite 'salir'): ")
        
    if nombre.lower() == 'salir':
        break

    apellido = input("Ingrese su apellido: ")
    temperatura_persona = float(input("Ingrese la temperatura de hoy: "))
    dia = int(input("Ingrese el número del día en que estuvo en el establecimiento: ")) 

    if 0 <= dia < len(dias_semana):
        dia = dias_semana[dia]
        print("La temperatura de ", nombre, apellido, "es de ",temperatura_persona)
    else:
        print("Número de día no válido.")

























