def main():
    #escribe tu código abajo de esta línea

    #CODIGO ######################

    # codigo que cuenta los numeros pares e impares de una lista cuyos elementos fueron introducidos por el usuario
    # autor: -
    cuantos=int(input())
    lista=[]

    for num in range(cuantos):
        lista.append(int(input()))

    for cont in range(len(lista)):
        if lista[cont] % 2 == 0:
            print("pos "+ str(cont) + ", valor "+ str(lista[cont]))

    # FIN CODIGO ################

    pass

if __name__=='__main__':
    main()
