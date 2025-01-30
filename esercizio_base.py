def indovina(n_prog):
    controllo = True
    while True:
        n_ut = int(input("Indovina il numero da 1 a 100 randomico: "))
        if n_ut > n_prog:
            print("Numero maggiore")
        elif n_ut < n_prog:
            print("Numero inferiore")
        else:
            print("Numero indovinato")
            controllo = False
            break


indovina(7)