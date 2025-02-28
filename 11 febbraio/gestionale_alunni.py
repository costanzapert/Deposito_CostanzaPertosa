def inizio():
    fileT = False
    try:
        with open("dbAl.txt","r") as dbFile:
            contenuto = dbFile.read()
        fileT = True
    except:
        contenuto= "nome,cognome,voto1,voto2,voto3"
    righe = contenuto.split("\n")
    tabella = [riga.split(",") for riga in righe]
    return tabella, fileT

def scriviFile(tabella):
    righe = [",".join(riga) for riga in tabella]
    contenuto = "\n".join(righe)
    with open("dbAl.txt","w") as dbFile:
        dbFile.write(contenuto)
    print("file scritto!")

    


def inserisciAlunno(tabella):
    nuovoAl =[]
    nome = input("inserisci il nome dell'alunno: ")
    nuovoAl.append(nome)
    cognome = input("inserisci il cognome dell'alunno: ")
    nuovoAl.append(cognome)
    for n in range(3):
        voto = input("inserisci un voto: ")
        nuovoAl.append(voto)
    tabella.append(nuovoAl)
    scriviFile(tabella)
    return tabella, True

tabella, fileT = inizio()
tabella, fileT = inserisciAlunno(tabella)

print(tabella)

