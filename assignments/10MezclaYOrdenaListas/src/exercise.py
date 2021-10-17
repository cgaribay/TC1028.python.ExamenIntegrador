def main():
    #escribe tu código abajo de esta línea

    # CODIGO #####
    # Mezclando y ordenando listas -----------------------------
    # Autor: ricardo.quintero@tec.mx

    l1=[]
    fin=False
    while not fin:
        numero=input()

        if numero == "*":
            break
        l1.append(int(numero))

    l2=[]
    while not fin:
        numero=input()

        if numero == "*":
            break
        l2.append(int(numero))
    
    print("L1=")
    print(l1)
    print("L2=")
    print(l2)
    l3 = []
    l3 = l1
    l3.extend(l2)
    print("LORDENADA=")
    print(sorted(l3))

    # FIN CODIGO #####
    pass

if __name__=='__main__':
    main()
