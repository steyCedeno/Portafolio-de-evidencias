#Ejercicio 1

##print ("ejercicio 1")
##a = 30
##b = 45
##c = 67
##d = 78
##
##print (d, c, b, a)
##
###Funcion input
##
##a = input ("Ingrese el valor a:")
##b = input ("Ingrese el valor b:")
##c = input ("Ingrese el valor c:")
##d = input ("Ingrese el valor d:")
##
##print (d, c, b, a)

#Ejercicio 2
##
##print ("ejercicio 2")
##
##edad = input("Ingrese su edad: ")
##
##suma = int (edad+5)
##
##print ("Dentro de 5 anhos tendra: ", suma)

#Ejercicio 3
##a = input ("Ingrese un numero entero para calcular resultado: ")
##b = input ("Ingrese un numero entero para calcular resultado: ")
##
##resultado = int (a+b)*2/3
##
##print ("El resultado es: ", resultado)

#Ejercicio 4

##num = int(input ("Ingrese un numero entero para calcular resultado: "))

##result1 = num * 2
##result2 = num * 3

##print ("El cuadrado de su numero es: ", result1, "y su cubo es de ", result2)

#Ejercicio 5

##base = int(input ("Ingrese la base de su rectangulo para calcular el area: "))
##altura = int(input ("Ingrese la altura de su rectangulo para calcular el area: "))

##area = base*altura
##perimetro = base*4

##print ("El area de su cuadrado es de ", area, "y el perimetro es de ", perimetro)

#Ejercicio 6

##distancia = float(input("Ingrese la distancia de su casa a la universidad en kilómetros: "))
##costo_por_km = float(input("Ingrese el costo por kilómetro: "))
##dias_semana = int(input("Ingrese la cantidad de días a la semana que va a la universidad: "))

##costo_total_cuatrimestre = distancia * costo_por_km * 2 * dias_semana * 15

##print("El costo total de traslado por cuatrimestre es:", costo_total_cuatrimestre)

#Ejercicio 7

##total_edades = 0

##for i in range(5):
##edad = int(input("Ingrese la edad de la persona: "))
##total_edades += edad

##promedio = total_edades / 5

##print("El promedio de edad es:", promedio)

#Ejercicio 8

##horas = float(input("Horas por semana: "))
##precio = float(input("Precio por hora: "))

##salario_semanal = horas * precio
##salario_mensual = salario_semanal * 4.2

##cargas_sociales = salario_mensual * 0.105
##ded_asociacion = salario_mensual * 0.05
##deducciones = salario_mensual - cargas_sociales - ded_asociacion

##print("Salario mensual después de deducciones:", deducciones)

#Ejercicio 9

##ingresos = float(input("Ingrese sus ingresos mensuales: "))
##gastos_alim = float(input("Ingrese sus gastos mensuales en alimentación: "))

##porcentaje_alim = (gastos_alim / ingresos) * 100
##porcentaje_disp = 100 - porcentaje_alim

##print("Porcentaje de gastos en alimentación:", porcentaje_alim, "%")
##print("Porcentaje disponible para otros rubros:", porcentaje_disp, "%")

