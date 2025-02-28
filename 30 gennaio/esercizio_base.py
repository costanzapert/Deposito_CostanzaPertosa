def indovina():
    while True: 
        n_temp = int(input("Inserisci un numero: 1 a 9 "))
        if n_temp >=1 and n_temp <=9:
            n_prog = n_temp * n_temp # numero randomico da indovinare
            controllo = True
            while controllo:
                n_ut = int(input("Indovina il numero da 1 a 100 randomico: "))
                if n_ut > n_prog:
                    print("Numero maggiore")
                elif n_ut < n_prog:
                    print("Numero inferiore")
                else:
                    print("Numero indovinato")
                    controllo = False
                    break
        else: 
            print("Inseriemnto errato")


indovina()