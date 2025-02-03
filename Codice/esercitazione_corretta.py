# Per entrare nel menu
while True:
    scelta = input("Vuoi entrare nel meni? Si/No ")
    if scelta == "Si":
        
        # Controllo se il numero positivo
        numero = 0
        while numero <= 0:
            numero = int(input("Inserisci un numero positivo"))
        
        # Somma dei numeri pari da 1 al numero
        somma_p=0
        for x in range(0, numero+1, 2 ):
            somma_p += x
        print("Somma pari da 1 a", numero,":" , somma_p)
        
        # Somma dei numeri dispari da 1 al numero
        somma_d=0
        for x in range(1, numero+1, 2 ):
            somma_d += x
        print("Somma dispari da 1 a", numero,":", somma_d)

        # Controllo se il numero è primo
        for x in range(2, numero, 1):
            if numero % x != 0:
                continue
            else:
                print("Il numero ", numero , "è non è primo")
                break
        print("Il numero", numero , "è primo")
    elif scelta == "No":
        break
    else: 
        print("Errore nella scrittura di Si/No, ripeti")
        
    