#Scrivete un programma che chiede all'utente una
#frase e restituisce solo le vocali e l’indice della
#vocale all’interno della frase.

def programma():
    vocali = "aeiou"
    frase = input("Inserisci frase: ")
    for x in range(len(frase)):
        # if frase[x]== "a":
        #     print("a", x)
        # elif frase[x]== "e":
        #      print("e", x)
        # elif frase[x]== "i":
        #      print("i", x)
        # elif frase[x]== "o":
        #      print("o", x)
        # elif frase[x]== "u":
        #      print("u", x)
        if frase[x] in vocali:
            print(frase[x], x)

programma()
        