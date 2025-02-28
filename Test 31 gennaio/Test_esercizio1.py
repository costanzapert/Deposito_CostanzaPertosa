#Crea un sistema ripetibile che si occupi di dividere su tre possibili liste 
# i tipi basilari di dato che riceve in entrata. Deve poter stampare una lista singola o tutte.  
# Si deve ripetere X volte definite all'inizio dall'utente

X = int(input( "Quante volte vuoi ripetere? " ))
conteggio = 1
lista_n = []
lista_s = []
lista_b = []
while conteggio <= X:
    print("Che tipo di dato vuoi inserire? 1) int 2)float 3) char o stringa 4) booleano")
    i = int(input("1/2/3/4"))
    if i ==1:
        n = int(input("Inserici int: ")) 
        lista_n.append(n)
        conteggio +=1
    elif i == 2:
        n = float(input("Inserici float: ")) 
        lista_n.append(n)
        conteggio +=1
    elif i==3:
        s =  input("Inserici char o str: ")
        lista_s.append(s)
        conteggio +=1

    elif i ==4:
        b = bool( input("Inserici booleano: "))
        lista_b.append(b)
        conteggio +=1

    else:
        print("errore selezione")
            
print("Quali liste vuoi stampare? 1) Lista numerica 2) Lista semantica 3) Lista Booleani 4) Tutte")
a = int(input("1/2/3/4"))
if a ==1:
    print(lista_n)
elif a ==2:
    print(lista_s)
elif a ==3:
    print(lista_b)
elif a ==4: 
   print(lista_n,lista_s,lista_b)
else: 
    print("errore selezione")
          
    
        
        
        