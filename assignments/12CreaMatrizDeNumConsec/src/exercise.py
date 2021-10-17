def main():
    #escribe tu código abajo de esta línea

    # CODIGO ######################
    ren=int(input())
    col=int(input())
    if ren>=2 and col>=2:
        matriz=[]
        num=1
        for r in range(ren):
            renglon=[]
            for c in range(col):
                renglon.append(num)
                num+=1
            matriz.append(renglon)
        print(matriz)
    else:
        print("Error")
    # FIN DEL CODIGO ##############

    pass

if __name__=='__main__':
    main()
