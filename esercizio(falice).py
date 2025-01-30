#controllo divisore più piccolo
def div_m(n):
    if n%2 == 0:
        return 2
    else:
        for i in range(3,n+1,2):
            if n%i == 0:
                return i
                
#print(div_m(4))
#print(div_m(10))
#print(div_m(17))

#funzione primo o no
lista_primi=[]
def primo_o_no(n):
    for x in range(2, n, 1):
        if n % x != 0:
            continue
        else:
            print(n,"sta nel divisore più piccolo, cioè: ", div_m(n), "questo numero di volte",n//div_m(n) )
            return False
    lista_primi.append(n)
    print(lista_primi) # in più
    return True

#primo_o_no(3)

#menu che mi chiede in inuput valore
def menu():
    while True:
        n = int(input("scegli un numero: "))
        primo_o_no(n)

#richiamo funzione menu        
menu()


