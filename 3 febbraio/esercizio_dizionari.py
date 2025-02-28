while True:
    lista= []
    b = input("Inserisci True/False: ")
    lista.append(b)
    n = int(input("Inserisci un intero: "))
    lista.append(n)
    s = input("Inserisci una stringa: ")
    lista.append(s)

    dizionario = {}
    dizionario["tipididato"] = lista 
    print(dizionario)
    
    scelta = input("Se vuoi uscire scrivi: esci")
    if scelta == "esci":
        break
    