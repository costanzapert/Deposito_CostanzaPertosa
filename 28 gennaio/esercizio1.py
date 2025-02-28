nome_utente_reg = " "
password_reg = " "
bool_reg = False

# registrazione
if nome_utente_reg == " " and password_reg == " ":
    nome_utente_reg = input("Scegli nome utente ")
    password_reg = input ("Scegli password ")
    
# login
nome_utente = input("Inserisci nome utente ")
password = input ("Inserisci password ")
if nome_utente.lower() == nome_utente_reg.lower() and password == password_reg:
    print("Benvenuto", nome_utente + "!")
    bool_reg = True
else:
    print("Ritenta, nome utente o password scorretti.")

if bool_reg:
# cambio nome o pass
    print("Se vuoi cambiare nome utente digita 1, se vuoi cambiare password 2")
    modifica = int(input(" 1 o 2: "))
    if modifica == 1 :
        nome_utente_reg = input("Scegli nome utente ")
    elif modifica == 2 :
        password_reg = input ("Scegli password ")
    else:
        pass


    print("Inserisci tra A e B per scegliere tra domande segrete: A) Colore preferito? B) Animale preferito?")
    scelta = input ("A/B: ")
    if scelta.upper() == "A":
        risposta = input( "Risposta:" )
        print(" Scelta domanda A, risposta", risposta)
    elif scelta.upper() == "B":
        risposta = input( "Risposta:" )
        print(" Scelta domanda B, risposta", risposta)
    else: 
        "Errore"


else:
    print("Non sei registrato!")


