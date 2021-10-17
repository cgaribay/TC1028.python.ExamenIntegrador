def diagonal_principal (matriz):
    vector_diagonal = []
    # len(matriz) - cantidad de renglones
    # len(matriz[0]) - cantidad de columnas
    for x  in range(len(matriz[0])):
        vector_diagonal.append(matriz[x][x])
    return vector_diagonal

def leer (ren, col):
    matriz = []
    for x in range (ren):
        lista = []
        for y in range(col):
            valor = int(input())
            lista.append(valor)
        matriz.append(lista)
    return matriz

def main():
    ren = int(input())
    col = int(input())
    if (ren != col):
        print ("La matriz no es cuadrada")
    else:
        matriz = leer (ren, col)
        vector_diagonal = diagonal_principal(matriz)
        print (vector_diagonal)


if __name__=='__main__':
    main()
