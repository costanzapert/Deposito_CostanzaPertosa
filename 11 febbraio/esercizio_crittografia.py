# Scrivete un programma che utilizza il cifrario di Cesare per criptare una
# parola o decriptarla.

# Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
# ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
# sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
# di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
# una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
# Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
# conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
# di posti corrispondente alla chiave.

alfabeto = "abcdefghijklmnopqrstuvwxyz"
punteggiatura = " .,!'?:;"

def cripta(frase, chiave):
    nuova_frase=""
    for x in frase.lower():
        if x in punteggiatura:
            nuova_frase+= x
        else:
            x = alfabeto[(alfabeto.index(x)+chiave)%len(alfabeto)]
            nuova_frase+=x
    return nuova_frase
        
        
def decripta(frase, chiave):
    nuova_frase=""
    for x in frase.lower():
        if x in punteggiatura:
            nuova_frase+= x
        else:
            x = alfabeto[(alfabeto.index(x)-chiave)%len(alfabeto)]
            nuova_frase+=x
    return nuova_frase
      
    
criptata=cripta(" Ciao! ", 5)
decriptata = decripta(criptata,5)
print(f"criptata: {criptata} decriptata : {decriptata}" )