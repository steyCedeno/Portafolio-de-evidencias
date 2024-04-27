#Nombres de los integrantes del grupo: Steilyn Cedeno Garcia y JUAN ANDREY VINDAS MATARRITA 

def agregar_datos(ruta_archivo):
    file = open(ruta_archivo, "w")
    print("Este archivo es para que guardes las ventas de tus empleados")

    num_vendedores = int(input("Ingrese el número de vendedores: "))

    for i in range(num_vendedores):
        nombre_vendedor = input("Digite el nombre del vendedor {}: ".format(i+1))
        monto_venta = input("Digite el monto de venta en dólares: ")

        file.write("{},{}\n".format(nombre_vendedor, monto_venta))

    print("Guardaste todo con exito")
    file.close()

def mostrar_datos(ruta_archivo):
    file = open(ruta_archivo, "r")
    print("Datos de ventas:")
    for linea in file:
        nombre_vendedor, monto_venta = linea.strip().split(',')
        print("Vendedor: {}, Venta de: {} dólares".format(nombre_vendedor, monto_venta))
    file.close()

# Ruta completa del archivo
ruta_archivo = r"C:\Users\Hewlett Packard\Documents\Universidad 2024\Programación básica\Portafolio de evidencias\Duodécima clase\ventas.txt"

# Ejemplo de uso
agregar_datos(ruta_archivo)
mostrar_datos(ruta_archivo)
