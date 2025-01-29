conteggio_pari=0
pari=[]
while conteggio_pari<5:
    numero = int(input("Inserisci numero: ")) 
    if numero % 2 == 0:
        print("Il numero è primo")
        pari.append(numero)
        conteggio_pari += 1
    else:
        print("Il numero non è primo")
print(pari)