class Squadra:
    lista_giocatori = []
    lista_allenatori  = []
    lista_assinstenti = []
    
    def __init__(self, nome_squadra):
        self.nome_squadra = nome_squadra
        self.lista_giocatori = []
        self.lista_allenatori  = []
        self.lista_assinstenti = []
        
    def stampa_squadra(self):
        for x in self.lista_giocatori:
            print(x)
        for y in self.lista_allenatori:
            print(y)
        for z in self.lista_assinstenti:
            print(z)
        
    
class MembroSquadra:
    def __init__(self, nome, età):
        self.nome =  nome
        self.età = età
    
    def descrivi(self):
        print("Fa parte della squadra")

class Giocatore(MembroSquadra):
    def __init__(self,  nome, età, ruolo, numero_maglia):
        super().__init__(nome, età)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def gioca_partita(self):
        print("Il giocatore cerca di segnare o marcare")
    
    def __str__(self):
        return f"Giocatore({self.nome}, {self.età}, {self.ruolo}, {self.numero_maglia})"

# gioc1 = Giocatore("mario",20,"attaccante", 20)
# print(gioc1)
# gioc1.gioca_partita()


class Allenatore(MembroSquadra):
    def __init__(self,  nome, età, anni_di_esperienza):
        super().__init__(nome,età)
        self.anni_di_esperienza = anni_di_esperienza
    
    def dirige_allenamento(self):
        print("Conduce allenamento con i suoi anni di esperienza, ovvero", self.anni_di_esperienza)

    def __str__(self):
        return f"Allenatore({self.nome}, {self.età}, {self.anni_di_esperienza})"

# all1 = Allenatore("marco", 40, 15)
# all1.dirige_allenamento()
 

class Assistente(MembroSquadra):
    def __init__(self,  nome, età, specializzazione):
        super().__init__(nome,età)
        self.specializzazione = specializzazione
    
    def supporta_team(self):
        print("Supporta la squadra nella seguente specializzazione", self.specializzazione)
    
    def __str__(self):
        return f"Assistente({self.nome}, {self.età}, {self.specializzazione})"

# ass1 = Assistente("Ale", 50, "fisioterapista")
# ass1.supporta_team()


# Costruisco l'oggetto sqd1

sqd1 = Squadra("Juve")
scelta_g = int(input("Quanti giocatori vuoi?"))
for x in range(0,scelta_g,1):
    nome = input("nome: ")
    età = int(input("età: "))
    ruolo = input("ruolo: ")
    numero_maglia = int(input("numero maglia: "))
    aggiunta_g = Giocatore(nome, età, ruolo, numero_maglia)
    sqd1.lista_giocatori.append(aggiunta_g)

scelta_all = int(input("Quanti allenatori vuoi?"))
for x in range(0,scelta_all,1):
    nome = input("nome: ")
    età = int(input("età: "))
    anni_di_esperienza = int(input("numero maglia: "))
    aggiunta_all = Allenatore(nome, età, anni_di_esperienza)
    sqd1.lista_allenatori.append(aggiunta_all)


scelta_ass = int(input("Quanti assistenti vuoi?"))
for x in range(0,scelta_ass,1):
    nome = input("nome: ")
    età = int(input("età: "))
    specializzazione = input("specializzazione: ")
    aggiunta_ass = Assistente(nome, età, specializzazione)
    sqd1.lista_assinstenti.append(aggiunta_ass)

sqd1.stampa_squadra()

