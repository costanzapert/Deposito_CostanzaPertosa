  
numero = int(input("Inserisci numero")) 
numerilista = range(numero)

for x in numerilista:
    if x == 0: 
        max = len(numerilista)
    print(numerilista[max-1])
    max -=1

    