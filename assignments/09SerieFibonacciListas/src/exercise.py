def main():
    #escribe tu código abajo de esta línea

    ### CODIGO #####

    # Inicializar la lista
    a = []

    # Leer iN
    iN = int(input())

    # Validar iN
    while iN < 0:
        iN = int(input())

    # Inicializar con fibonacci
    iF1 = 0
    iF2 = 1
    if iN == 1:
        a.append(0)
    elif iN >= 2:
        a.append(0)
        a.append(1)
        for i in range(2,iN):
            a.append(a[i-1] + a[i-2])
            
    # Desplegar la lista
    print(a)

    ### FIN CODIGO #####

    pass

if __name__=='__main__':
    main()
