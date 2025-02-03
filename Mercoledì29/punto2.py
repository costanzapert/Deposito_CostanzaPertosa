# punto 2
condizione = True
n = int (input("Inserisci un numero: "))
while condizione:
    for x in range(n, -1, -1):
        print(x)
    scelta = input("Vuoi continuare? Si/No ")
    if scelta == "Si":
        n = int (input("Inserisci un numero: "))
    elif scelta == "No":
        condizione = False
    else:
        print("Inserimento errato")

    