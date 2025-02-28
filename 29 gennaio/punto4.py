lista = []
lunghezza_lista = int(input("Quanti elementi della lista vuoi?"))
while len(lista) < lunghezza_lista:
    numero_lista = int(input("Che numero vuoi inserire nella lista?"))
    lista.append(numero_lista)

print("Il numero di elementi nella lista è: ", lunghezza_lista)
if lista == []:
    print("Lista vuota")
else:
    lista.sort()
    massimo = lista[-1]
    print("numero massimo: ", massimo, ";" , "numero elementi: ", lunghezza_lista )       
    