""" cantidad_numeros = int(input("Ingrese la cantidad de números que desea convertir: "))
binarios = []
numeros_originales = []

print("")

for i in range(cantidad_numeros):
    binario_actual = []
    
    n_128 = 0
    n_64 = 0
    n_32 = 0
    n_16 = 0
    n_8 = 0
    n_4 = 0
    n_2 = 0
    n_1 = 0
    
    numero_original = int(input("Ingrese el número (máximo 255): "))
    numeros_originales.append(numero_original)
    
    numero = numero_original
    
    if numero >= 128:
        numero -= 128
        n_128 += 1
    if numero >= 64:
        numero -= 64
        n_64 += 1
    if numero >= 32:
        numero -= 32
        n_32 += 1
    if numero >= 16:
        numero -= 16
        n_16 += 1
    if numero >= 8:
        numero -= 8
        n_8 += 1
    if numero >= 4:
        numero -= 4
        n_4 += 1
    if numero >= 2:
        numero -= 2
        n_2 += 1
    if numero >= 1:
        numero -= 1
        n_1 += 1
    
    binario_actual.extend([n_128, n_64, n_32, n_16, n_8, n_4, n_2, n_1])
    binarios.append(binario_actual)
    
    if cantidad_numeros <= 1:
        print("")
        print("El código binario de", numero_original, "es:", binario_actual)

if cantidad_numeros > 1:
    print("")
    print("El código binario completo de", numeros_originales, "es:", binarios)

print("")    
print("")
terminar = input("Presiona enter para finalizar") """


def obtener_binarios(numero):
    digitos_binarios = [0] * 8

    for i in range(7, -1, -1):
        if numero >= 2**i:
            numero -= 2**i
            digitos_binarios[7 - i] += 1
    
    return digitos_binarios

def decimal_binario(numero_decimal):
    digitos_binarios = obtener_binarios(numero_decimal)
    return digitos_binarios

cantidad_numeros = int(input("Ingrese la cantidad de números que desea convertir: "))
codigos_binarios = []
numeros_originales = []

print("")

for _ in range(cantidad_numeros):
    numero_original = int(input("Ingrese el número (máximo 255): "))
    numeros_originales.append(numero_original)
    
    codigo_binario_actual = decimal_binario(numero_original)
    codigos_binarios.append(codigo_binario_actual)
    
    if cantidad_numeros <= 1:
        print("")
        print("El código binario de", numero_original, "es:", codigo_binario_actual)

if cantidad_numeros > 1:
    print("")
    print("El código binario completo de", numeros_originales, "es:", codigos_binarios)

terminar = input("Presiona enter para finalizar")
