#controllo divisore più piccolo
def div_m(n):
    if n%2 == 0:
        return 2
    else:
        for i in range(3,n+1,2):
            if n%i == 0:
                return i

# Test         
#print(div_m(4))
#print(div_m(10))
#print(div_m(17))

#funzione primo o no
nome = input("Come ti chiami? ")
lista_primi=[nome]
def primo_o_no(n):
    for x in range(2, n, 1):
        if n % x != 0:
            continue
        else:
            print(nome, "ha scelto come numero", n,"che sta nel divisore più piccolo, cioè: ", div_m(n),",", "questo numero di volte: ",n//div_m(n) )
            return False
    lista_primi.append(n)
    print("Lista primi: ", lista_primi) # in più
    return True

# Test         
#primo_o_no(3)

#menu che mi chiede in inuput valore
def menu(): 
    n = int(input("scegli un numero: "))
    while primo_o_no(n):
        n = int(input("scegli un numero: "))


#richiamo funzione menu        
menu()


