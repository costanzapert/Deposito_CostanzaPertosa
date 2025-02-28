class Ristorante:

    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.lista_piatti = []
        self.lista_prezzi = []
        self.aperto = False
    
    
    # aperto = False
    # lista_piatti = []
    # lista_prezzi = []
    
    def descrivi_ristorante(self):
        print("Il nome del ristorante è ", self.nome,"ed è specializzato nel tipo di cucina ", self.tipo_cucina)
    
    def stato_di_apertura(self):
        if self.aperto == True:
            print("Il ristorante è aperto")
        else: 
            print("Il ristorante è chiuso")
    
    def apri_ristorante(self):
            self.aperto = True
            print("Il ristorante è ora aperto")
        
    def chiudi_ristorante(self):
            self.aperto = False
            print("Il ristorante è ora chiuso")
    
    def aggiungi_al_menu(self):
        nome_piatto = input("Inserisci nome piatto: ")
        prezzo_piatto = int(input("Inserisci prezzo piatto: "))
        self.lista_piatti.append(nome_piatto)
        self.lista_prezzi.append(prezzo_piatto)
    
    def togli_dal_menu(self):
        togli_piatto = input("Dimmi che piatto vuoi togliere: ")
        count = -1
        for x in self.lista_piatti:
            count += 1
            if x == togli_piatto:
                self.lista_piatti.remove(togli_piatto)
                self.lista_prezzi.remove(self.lista_prezzi[count])
                
    def stampa(self):
        print( "Lista ristorante: ",risto1.lista_piatti)
        print("Lista prezzi: ",risto1.lista_prezzi)
    
    

risto1 = Ristorante("L'essenza", "Giapponese")
#risto1.descrivi_ristorante() 
#risto1.apri_ristorante()  
#risto1.stato_di_apertura()

risto1.chiudi_ristorante()  
risto1.stato_di_apertura()
risto1.aggiungi_al_menu()
risto1.aggiungi_al_menu()
risto1.aggiungi_al_menu()
risto1.aggiungi_al_menu()
risto1.stampa()
risto1.togli_dal_menu()
risto1.stampa()
