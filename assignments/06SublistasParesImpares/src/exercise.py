def main():
    #escribe tu código abajo de esta línea

    # CODIGO ############################

    # Listando pares e impares -----------------------------
    # Autor: ricardo.quintero@tec.mx

    fin=False
    lista=[]

    while not fin:
        numero=input()

        if numero == "*":
            break
        lista.append(int(numero))

    lp=[]
    li=[]

    for e in lista:
        if int(e) % 2 == 0:
            lp.append(int(e))
        else:
            li.append(int(e))

    print("PARES")
    print(lp)
    print("IMPARES")
    print(li)

    # FIN CODIGO ########################

    pass

if __name__=='__main__':
    main()
