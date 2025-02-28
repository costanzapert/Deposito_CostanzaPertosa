#Trova un numero con più di 5 divisori. Stampa i divisori di ogni numero in input,  se ne ha più di 5 fermati.

#if, range, for , while, liste, variabili, print, strighe
divisori = []
while len(divisori) < 5:
    divisori = []
    n = int(input("Inserisci numero: "))
    for i in range(1,n+1, 1):
        if n % i == 0:
            divisori.append(i)             
    print(divisori)


#trasforma le liste in tuple
    

# ho scoperto cose su tuple che non funzionano    
#divisori_tupla= (*divisori) NOOOOOOOOOOOOO
#print(divisori_tupla)

#modo barbaro. Non capisco perchè alla fine tolga la virgola
divisori_tupla = ()
for i in divisori:
    divisori_tupla = divisori_tupla + (i,)
print(divisori_tupla)

#nuova_lista= tuple([])

#  splat

#trasforma tupla in  lista e controllo tutto funzioni
divisori_lista = [*divisori_tupla] # uso splat
if divisori_lista == divisori:
    print("Tutto funziona")
else: 
    print("Stai sbagliando qualcosa")


#booleani
# conto quante volte sono nel ciclo
print("Contiamo quante volte entra nel ciclo")
conteggio = True
numero_ciclo = 0
while conteggio:
    numero_ciclo += 1
    scelta = input("Sei nel while. Se vuoi uscire scrivi: esci ")
    if scelta == "esci":
        print("numero cicli totali: ", numero_ciclo)    
        conteggio = False
        

#Mancanti: break, pass, continue
