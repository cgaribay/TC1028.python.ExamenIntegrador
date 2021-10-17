def determinante(matriz):
    det=(matriz[0][0] * matriz[1][1]) - (matriz[1][0]*matriz[0][1])
    return det
    
def leer_matriz_por_renglon():
    matriz=[]
    for i in range(2):
        datos_renglon = input()
        renglon_lista_string=datos_renglon.split()
        renglon_lista_int=[]
        for elem in renglon_lista_string:
            renglon_lista_int.append(int(elem))          
        matriz.append(renglon_lista_int)
    return matriz
    
def main():
    matriz = leer_matriz_por_renglon()
    if (len(matriz) != 2 or len(matriz[0])!= 2):
        print("La matriz no es una matriz de 2x2")
    else:
        resultado = determinante(matriz)
        print(resultado)


if __name__=='__main__':
    main()
