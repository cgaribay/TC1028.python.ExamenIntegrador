def generaMatriz (renglon, columna):
    matriz = []
    for i in range (renglon):
        lista = []
        for y in range(columna):
            valor = int(input())
            lista.append(valor)
        matriz.append(lista)
    return matriz

def centroMatriz(matriz):
    matrizSalida=[]
    for ren in range(len(matriz)-2):
        vector=[]
        for col  in range(len(matriz[0])-2):
            vector.append(matriz[ren+1][col+1])       
        matrizSalida.append(vector)        
    return matrizSalida

def main():
    renglon = int(input())
    columna = int(input())
    matriz = generaMatriz (renglon, columna)
    matriz=centroMatriz(matriz)
    print(matriz)


if __name__=='__main__':
    main()
