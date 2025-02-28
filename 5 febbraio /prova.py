# variabile globale
numero = 10

def funzione_interna():
    #Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_interna (local): ", numero)

    
    def funzione_interna():
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal): ", numero)
    
    funzione_interna()

print("Numero nel main(globale): ", numero)
funzione_esterna()
print("Numero nel main dopo chiamata globale: ", numero)
