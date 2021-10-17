def suma_matrices(matriz1, matriz2):
    matriz_suma=[]
    for i in range(len(matriz1)):
        renglon=[]
        for j in range(len(matriz1[0])):
            suma_valores=matriz1[i][j]+matriz2[i][j]
            renglon.append(suma_valores)
        matriz_suma.append(renglon)
    return matriz_suma

def lee_matriz_por_renglon():
    matriz=[]
    datos_renglon=input()
    while datos_renglon:     
        renglon_lista_string=datos_renglon.split()
        renglon_lista_int=[]
        for elem in renglon_lista_string:
            renglon_lista_int.append(int(elem))          
        matriz.append(renglon_lista_int)
        datos_renglon = input()
    return matriz

def main():
    matriz1=lee_matriz_por_renglon()
    matriz2=lee_matriz_por_renglon()
    if (len(matriz1) != len(matriz2) or
        len(matriz1[0]) != len(matriz2[0])):
        print("Las matrices no son del mismo tamaño")
    else:
        print(suma_matrices(matriz1,matriz2))


if __name__=='__main__':
    main()
