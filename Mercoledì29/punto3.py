lista = []
lunghezza_lista = int(input("Quanti elementi della lista vuoi?"))
while len(lista) < lunghezza_lista:
    numero_lista = int(input("Che numero vuoi inserire nella lista?"))
    lista.append(numero_lista)
for x in lista: 
    print(x**2)
    