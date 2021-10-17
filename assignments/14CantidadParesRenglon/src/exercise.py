def matParesCol (matriz):
    
    vectorPares= []
    for ren  in range(len(matriz)):
        contPares = 0
        for col in range(len(matriz[0])):
            if (matriz[ren][col] % 2 == 0):
                contPares += 1
                
        vectorPares.append(contPares)        
       
    return vectorPares

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

    matriz = leer (ren, col)
    vectorPares = matParesCol(matriz)
    print (vectorPares)


if __name__=='__main__':
    main()
