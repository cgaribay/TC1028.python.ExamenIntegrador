
from pathlib import Path
import src.productos
import src.vendedores
import src.ventas

lista_productos = []

lista_vendedores = []

lista_ventas = []

# print_matriz
# matriz: la matriz que quieres desplegar en la terminal
# nombre_columnas: una lista con los nombres de cada columna de la matriz
def print_matriz(matriz, nombre_columnas):
    bigger_size = []
    for nombre in nombre_columnas:
        bigger_size.append(len(nombre))
    
    for idx, fila in enumerate(matriz):
        for element in fila:
            if len(str(element)) > bigger_size[idx]:
                bigger_size[idx] = len(str(element))

    for i in range(len(nombre_columnas)):
        print(nombre_columnas[i].center(bigger_size[i] + 2), end = "")
    print()
    
    for i in range(len(matriz[0])):
        for j in range(len(nombre_columnas)):
            print(str(matriz[j][i]).title().center(bigger_size[j] + 2), end = "")
        print()

# buscar_elemento
# matriz: la tabla en la que deseas buscar
# columna: la columna de la tabla en la que deseas buscar
# valor: el valor que deseas buscar
# return: el indice del valor en la tabla o -1 si no esta
#              lista_vendedores, 1, mariana lopez
def buscar_elemento(matriz, columna, valor):
    if valor in matriz[columna]:
        return matriz[columna].index(valor)
    else:
        return -1

# obtener_id
# matriz: la tabla en la que deseas encontrar el identificador
# indice: el indice del elemento del que deseas encontrar el identificador o -1 si el indice es incorrecto
def obtener_id(matriz, indice):
    if indice < len(matriz[0]) and indice >= -len(matriz[0]):
        return matriz[0][indice]
    else:
        return -1

# Abrir el archivo de productos, leer su informacion y carga la informacion en lista_productos
def cargar_productos():
    ruta_productos = Path('assignments/ExamenIntegrador/src/archivos', 'productos.csv')
    archivo_productos = open(ruta_productos)
    contenido_productos = archivo_productos.readlines()
    for line in contenido_productos:
        lista_productos.append(line.strip().split(','))
    archivo_productos.close()

# Abrir el archivo de vendedores, leer su informacion y carga la informacion en lista_vendedores
def cargar_vendedores():
    ruta_vendedores = Path('assignments/ExamenIntegrador/src/archivos', 'vendedores.csv')
    archivo_vendedores = open(ruta_vendedores)
    contenido_vendedores = archivo_vendedores.readlines()
    for line in contenido_vendedores:
        lista_vendedores.append(line.strip().split(','))
    archivo_vendedores.close()

# Abrir el archivo de ventas, leer su informacion y carga la informacion en lista_ventas
def cargar_ventas():
    ruta_ventas = Path('assignments/ExamenIntegrador/src/archivos', 'ventas.csv')
    archivo_ventas = open(ruta_ventas)
    contenido_ventas = archivo_ventas.readlines()
    for line in contenido_ventas:
        lista_ventas.append(line.strip().split(','))
    archivo_ventas.close()

#revisar_metas
#Pregunta al usuario el nombre del vendedor, revisa las ventas de ese vendedor e imprimir el mensaje correspondiente
def revisar_metas():
        pass

def main():
    cargar_productos()
    cargar_vendedores()
    cargar_ventas()

    revisar_metas()

if __name__=='__main__':
    main()
