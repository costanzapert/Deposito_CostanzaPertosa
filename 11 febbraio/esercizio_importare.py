#Scrivete un programma che genera 5 numeri casuali e li salva su un file, 
#l’utente dovrà cercare di indovinarne almeno 2 oppure avrà perso

# from random import randint


# numeri = [str(randint(0, 100)) for x in range(5)]
# contenuto = ",".join(numeri)
# with open("prova.txt", "w") as mioFile:
#     mioFile.write(contenuto)


# with open("prova.txt", "r") as mioFile:
#     numeri_salvati = mioFile.read().split(",")
# numeri_salvati = list(map(int,numeri_salvati))

# tentativi = 5
# indovinati = 0

# print("indovina almeno 2 numeri")
# for x in range(tentativi):
#     try:
#         numero_utente = int(input("inserisci un numero tra 0 e 100: "))
#         if numero_utente in numeri_salvati:
#             print("hai indovinato un numero.")
#             indovinati += 1
#         else:
#             print("sbagliato!")
#     except ValueError:
#         print("numero non valido.")

#         if indovinati >= 2:
#             print("hai vinto!")
#         else:
#             print("hai perso. i numeri erano:", numeri_salvati)
            
            
            
            
from random import randint

# Genera 5 numeri casuali e li salva su un file
numeri = [str(randint(0, 100)) for _ in range(5)]
contenuto = ",".join(numeri)

with open("prova.txt", "w") as mioFile:
    mioFile.write(contenuto)

# Legge i numeri dal file
with open("prova.txt", "r") as mioFile:
    numeri_salvati = mioFile.read().split(",")
numeri_salvati = list(map(int, numeri_salvati))

tentativi = 5
indovinati = 0

print("Indovina almeno 2 numeri!")

for _ in range(tentativi):
    try:
        numero_utente = int(input("Inserisci un numero tra 0 e 100: "))
        if numero_utente in numeri_salvati:
            print("Hai indovinato un numero.")
            indovinati += 1
        else:
            print("Sbagliato!")
    except ValueError:
        print("Numero non valido.")

# Verifica il risultato
if indovinati >= 2:
    print("Hai vinto!")
else:
    print("Hai perso. I numeri erano:", numeri_salvati)