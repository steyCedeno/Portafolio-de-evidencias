#Ejercicio 1
""" nombre_producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad comprada: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))

sin_iva = cantidad * precio_unitario
iva = sin_iva * 0.13
total_a_pagar = sin_iva + iva

print("Detalle de la compra: ")
print("Producto: ", nombre_producto)
print("Cantidad: ", cantidad)
print("Precio unitario: ", precio_unitario)
print("Total sin IVA: ", sin_iva)
print("IVA (13%): ", iva)
print("Total a pagar:  ", total_a_pagar) """

#Ejercicio 2
""" entrada_horas = int(input("Hora de entrada: "))
salida_horas = int(input("Hora de salida: "))

tiempo_laborado = salida_horas - entrada_horas * 3600

print("El tiempo laborado es:", tiempo_laborado, "segundos.") """

#Ejercicio 3
""" cedula = input("Número de cédula: ")
nombre = input("Nombre del funcionario: ")
salario_bruto = float(input("Salario bruto: "))

ccss = salario_bruto * 0.08
banco_popular = salario_bruto * 0.01
total_deducciones = ccss + banco_popular
salario_neto = salario_bruto - total_deducciones

print("Empleado:", nombre)
print("Identificación:", cedula)
print("Salario bruto:", salario_bruto)
print("CCSS (8%):", ccss)
print("Banco Popular (1%):", banco_popular)
print("Total deducciones:", total_deducciones)
print("Salario neto:", salario_neto) """

#Ejercicio 4
""" producto = input("Nombre del producto: ")
precio_sj = float(input("Precio en San José: "))
precio_h = float(input("Precio en Heredia: "))
precio_a = float(input("Precio en Alajuela: "))

precio_promedio = precio_sj + precio_h + precio_a / 3

print("Nombre del producto:", producto)
print("Precio en San José:", precio_sj)
print("Precio en Heredia:", precio_h)
print("Precio en Alajuela:", precio_a)
print("Precio promedio del producto:", precio_promedio) """

#Ejercicio 5
""" nombre = input("Nombre del vendedor: ")
unidades_vendidas = int(input("Total de unidades vendidas: "))
precio = float(input("Precio del artículo vendido: "))

if precio <= 20000:
    comision = precio * 0.03
elif precio < 50000:
    comision = precio * 0.05
else:
    comision = precio * 0.10

print("Nombre:", nombre)
print("Unidades vendidas:", unidades_vendidas)
print("Precio del artículo:", precio)
print("Comisión:", comision) """
