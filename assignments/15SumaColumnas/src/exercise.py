def generaMatriz (renglon, columna):
    matriz = []
    for i in range (renglon):
        lista = []
        for j in range(columna):
            valor = int(input())
            lista.append(valor)
        matriz.append(lista)
    return matriz

def sumaColumnas (matriz):
    vectorSuma= []
    for columna  in range(len(matriz[0])):
        suma = 0
        for renglon in range(len(matriz)):
            suma = suma + matriz[renglon][columna]        
        vectorSuma.append(suma)        
    return vectorSuma


def main():
    renglon = int(input())
    columna = int(input())
    if renglon>=1 and columna>=1:
        matriz = generaMatriz (renglon, columna)
        vectorSuma = sumaColumnas(matriz)
        print (vectorSuma)
    else:
        print("Error")



if __name__=='__main__':
    main()
