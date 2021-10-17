def main():
    #escribe tu código abajo de esta línea

    # CODIGO ##############
    
    # Problema de listas --- propuesto por Rocío Villagómez
    tam=int(input())
    lista=[]
    sin_duplicados=[]
    if tam>0:
        for n in range(tam):
            lista.append(input())
        for elemento in lista:
            if elemento not in sin_duplicados:
                sin_duplicados.append(elemento)
        print(lista)
        print(sin_duplicados)
    else:
        print("Error")

    # FIN CODIGO ##########

    pass

if __name__=='__main__':
    main()
