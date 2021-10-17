def menores_a_10(matriz):
    menores=[]
    for renglon in matriz:
        for elem in renglon:
            if elem < 10:
                menores.append(elem)
    return menores
        
def lee_matriz(ren,col):
    matriz=[]
    for i in range(ren):
        renglon=[]
        for j in range(col):
            valor = int(input())
            renglon.append(valor)
        matriz.append(renglon)
    return matriz

def main():
    renglones=int(input())
    columnas=int(input())
    matriz=lee_matriz(renglones,columnas)
    print(menores_a_10(matriz))



if __name__=='__main__':
    main()
