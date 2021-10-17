def main():
    #escribe tu código abajo de esta línea
    
    # CODIGO ###############

    # Contando pares e impares -----------------------------
    # Autor: ricardo.quintero@tec.mx

    fin=False
    lista=[]

    while not fin:
        numero=input()

        if numero == "*":
            break
        lista.append(int(numero))

    cp=0
    ci=0

    for e in lista:
        if e % 2 == 0:
            cp=cp+1
        else:
            ci=ci+1

    print("PARES="+str(cp))
    print("IMPARES="+str(ci))

    # FIN CODIGO ######################
    
    pass

if __name__=='__main__':
    main()
