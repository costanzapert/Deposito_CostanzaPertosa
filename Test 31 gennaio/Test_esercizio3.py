#Andare a creare una funzioni che si occupi di salvare i dati
# dell'utente, andare a creare una funzione che si occupi di 
# fare il login dell'utente, Andare a creare un funzioni che 
# modifichi i dati dell'utente solo se questi sono già stati creati
# / salvati e solo dopo il login.  Andare a creare un menu che 
# concateni le tre funzioni precedenti e permetta di ripetere il ciclo
# a più utenti diversi.


#non funziona :'(
nome = ""
password = ""
def dati():
    nome = input("Inserisci nome: ")
    password = input("Inserisci password: ")
    return nome, password
def login():
    if nome != "" and password != "":
        nome_l = input("Inserisci nome per login: ")
        password_l = input("Inserisci password per login: ")
        if [nome_l , password_l] == [dati()]:
            print("Login effettuato correttamente")
            return True
    
def mod():
    if nome != "" and password != "":
        log()
        scelta = int(input("se vuoi cambiare nome digita 1, password 2, niente 3)"))
        if scelta == 1:
            nome = input ("Inserisci nome nuovo: ")
        elif scelta == 2:
            password = input ("Inserisci pass nuovo: ")
        else: 
            pass
    
def menu():
    dati()
    login()
    mod()
    
menu()


# non funziona