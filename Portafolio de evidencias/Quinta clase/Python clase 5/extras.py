#Ejercicio 1
""" total_pagado = 0

for i in range(1, 11):
    salario = float(input("Ingrese el salario del colaborador: "))
    salario_neto = salario - (salario * 0.09)
    total_pagado += salario_neto

print("Total pagado por la empresa por concepto de salarios:", total_pagado)"""

#Ejercicio 2
""" suma_pares = 0

for i in range(1, 11):
    valor = int(input("Ingrese el valor: "))
    if valor % 2 == 0:
        suma_pares += valor

print("La suma de los números pares es:", suma_pares) """

#Ejercicio 3
""" numero = int(input("Ingrese un número entero: "))

# Convertir a binario
binario = 0
exp = 1
temp = numero
while temp > 0:
    residuo = temp % 2
    binario += residuo * exp
    exp *= 10
    temp //= 2

# Convertir a octal
octal = 0
exp = 1
temp = numero
while temp > 0:
    residuo = temp % 8
    octal += residuo * exp
    exp *= 10
    temp //= 8

# Convertir a hexadecimal
hexadecimal = 0
exp = 1
temp = numero
while temp > 0:
    residuo = temp % 16
    hexadecimal += residuo * exp
    exp *= 100
    temp //= 16

print("Número en binario:", binario)
print("Número en octal:", octal)
print("Número en hexadecimal:", hexadecimal) """
