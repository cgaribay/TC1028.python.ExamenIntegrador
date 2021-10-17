def generaMatriz (renglon, columna):
    matriz = []
    for i in range (renglon):
        lista = []
        for j in range(columna):
            valor = int(input())
            lista.append(valor)
        matriz.append(lista)
    return matriz

def cambiaRenglones(matriz):
    renglon1=int(input())-1
    renglon2=int(input())-1
    
    for columna in range(len(matriz[0])):
        elemento=matriz[renglon1][columna]
        matriz[renglon1][columna] = matriz[renglon2][columna]
        matriz[renglon2][columna] = elemento

    return matriz

def main():
    renglon = int(input())
    columna = int(input())
    matriz = generaMatriz (renglon, columna)
    matriz = cambiaRenglones(matriz)
    print(matriz)


if __name__=='__main__':
    main()
