#Andare a creare un sistema ripetibile che si occupa di gestire 
# la lunghezza delle stringhe e salvarle, l'utente potrà continuare
# a inserire dati finché la stringa inserita e più lunga della precedente, 
# alla fine stamperà l'insieme delle stringhe date in input divise da virgole
# e quante stringhe ha inserito.

lunghezza_s_iniziale = -1
lunghezza_s_attuale = 0
conteggio_s = 0
insieme_s = []
while lunghezza_s_iniziale < lunghezza_s_attuale:
    lunghezza_s_iniziale = lunghezza_s_attuale
    stringa = input("Inserisci stringa: ")
    lunghezza_s_attuale = len(stringa)
    insieme_s = insieme_s + [stringa]
    conteggio_s +=1
    print("Hai inserito:", conteggio_s, "stringhe,", "le stringhe sono", insieme_s )

