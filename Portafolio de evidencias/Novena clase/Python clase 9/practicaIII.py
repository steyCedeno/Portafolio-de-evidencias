""" La pulpería de su comunidad tiene a la venta múltiples productos que son parte de su oferta
semanal, esta oferta puede ser cambiada ya sea porque se agrega un producto nuevo o porque
se elimina uno de ellos. En estos productos se encuentran los siguiente grupos:
● Articulos enlatados.
● Productos de limpieza.
● Carnes.
● Granos. (Arroz, frijoles, entre otros)
Donde cada grupo indica los nombres de los productos. El administrador debe poder
seleccionar alguno de los grupos realizar las siguientes acciones:
- Agregar productos.
- Eliminar uno de los productos.
- Actualizar uno de los productos.
El programa debe ser capaz de mostrar todos los elementos de la lista, de la siguiente manera:
- Producto 1: <producto>
- Producto 2: <producto>
- ...
- Producto n: <producto>
Donde n, es el último producto del conjunto.
Los productos deben mostrarse en las siguientes circunstancias:
- Antes de eliminar un producto.
- Después de eliminar un producto.
- Después de agregar un producto.
- Después de actualizar un producto.
Ahora bien, si el producto que se desea agregar, ya existe en el conjunto, entonces no se
agrega y se muestra un mensaje:
El producto ya existe. """

""" # Definimos las listas para cada grupo de productos
articulos_enlatados = ["Atún", "Maíz", "Sardinas"]
productos_limpieza = ["Detergente", "Desinfectante", "Limpiavidrios"]
carnes = ["Pollo", "Res", "Cerdo"]
granos = ["Arroz", "Frijoles", "Lentejas"]

# Lista que contendrá todas las listas de productos
productos = [articulos_enlatados, productos_limpieza, carnes, granos]

# Función para mostrar todos los productos
def mostrar_productos():
    for grupo in productos:
        for producto in grupo:
            print(producto)
        print()

# Mostrar productos antes de realizar cualquier acción
mostrar_productos()

# Agregar un producto
productos[0].append("Champiñones")
mostrar_productos()

# Eliminar un producto
productos[2].remove("Pollo")
mostrar_productos()

# Actualizar un producto
productos[3][2] = "Garbanzos"
mostrar_productos()

profe este fue mi primer intento y quise dejarlo, no haga caso
"""

# Lista que contendrá todas las listas de productos
productos = []

# Función para ingresar productos para un grupo específico
def ingresar_productos(grupo, cantidad):
    productos_grupo = []
    for i in range(cantidad):
        producto = input(f"Ingrese el producto para el grupo de {grupo}: ")
        productos_grupo.append(producto)
    return productos_grupo

# Pedir al usuario que ingrese los productos para cada grupo
cantidad_articulos = int(input("¿Cuántos productos desea ingresar para el grupo de Artículos enlatados? "))
productos.append(ingresar_productos("Articulos enlatados", cantidad_articulos))

cantidad_limpieza = int(input("¿Cuántos productos desea ingresar para el grupo de Productos de limpieza? "))
productos.append(ingresar_productos("Productos de limpieza", cantidad_limpieza))

cantidad_carnes = int(input("¿Cuántos productos desea ingresar para el grupo de Carnes? "))
productos.append(ingresar_productos("Carnes", cantidad_carnes))

cantidad_granos = int(input("¿Cuántos productos desea ingresar para el grupo de Granos? "))
productos.append(ingresar_productos("Granos", cantidad_granos))

# Función para mostrar todos los productos
def mostrar_productos():
    for grupo in productos:
        print(grupo)

# Mostrar productos antes de realizar cualquier acción
print("Productos antes de realizar cualquier acción:")
mostrar_productos()
print()

# Agregar un producto
grupo_agregar = int(input("Ingrese el grupo donde desea agregar un producto (0 para Articulos enlatados, 1 para Productos de limpieza, 2 para Carnes, 3 para Granos): "))
producto_agregar = input("Ingrese el producto que desea agregar: ")
productos[grupo_agregar].append(producto_agregar)
print("Productos después de agregar un producto:")
mostrar_productos()
print()

# Eliminar un producto
grupo_eliminar = int(input("Ingrese el grupo donde desea eliminar un producto (0 para Articulos enlatados, 1 para Productos de limpieza, 2 para Carnes, 3 para Granos): "))
producto_eliminar = input("Ingrese el producto que desea eliminar: ")
productos[grupo_eliminar].remove(producto_eliminar)
print("Productos después de eliminar un producto:")
mostrar_productos()
print()

# Actualizar un producto
grupo_actualizar = int(input("Ingrese el grupo donde desea actualizar un producto (0 para Articulos enlatados, 1 para Productos de limpieza, 2 para Carnes, 3 para Granos): "))
actualizar = int(input("Ingrese cual es el producto que desea actualizar: "))
producto_nuevo = input("Ingrese el nuevo producto: ")
productos[grupo_actualizar][actualizar] = producto_nuevo
print("Productos después de actualizar un producto:")
mostrar_productos()

