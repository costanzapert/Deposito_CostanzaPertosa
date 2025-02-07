# simulare un teatro

class Posto:
    #overloading
    def __init__(self, numero, fila, occupato = False ):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = occupato
        
    def prenota(self):
        if self.__occupato == False:
            self.__occupato = True 
            print("Il posto",self.__numero , "in fila ", self.__fila, "è appena stato occupato" )
        elif self.__occupato == True:
            print("Il posto",self.__numero , "in fila ", self.__fila, "è già occupato")

#post1= Posto(4,10)
#post1.prenota() 
#post1.prenota() 
#me perchè me li stampa i privati?
    
    def libera(self):
        if self.__occupato == True:
            self.__occupato = False 
            print("Il posto",self.__numero , "in fila ", self.__fila, "è libero adesso" )
        elif self.__occupato == False:
            print("Il posto",self.__numero , "in fila ", self.__fila, "è non era prenotato")

    def get_numero(self):
        return self.__numero
    
    def get_fila(self):
        return self.__fila
    
    def get_occupato(self):
        return self.__occupato
    
#post1= Posto(4,10)
#post1.prenota() 
#post1.libera()

class PostoVIP(Posto):
    
    servizi_extra = []
    def __init__(self, numero, fila, occupato=False):
        super().__init__(numero, fila, occupato)
        self.servizi_extra = []
    
    def prenota(self):
        super().prenota()
        self.servizi_extra = ["Accesso al lounge", "Servizio in posto"]
    
        
    def __str__(self):
        return "PostoVip(" + str(self.get_numero()) + ", " + str(self.get_fila()) + ")"


#post2= PostoVIP(4,10)
#post2.prenota()       
#print(post2.servizi_extra)
        
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo,  occupato = False ):
        super().__init__( numero, fila, occupato  )
        self.costo = costo
       
        
        
    def prenota(self):
        super().prenota()
        print("Il prezzo è di ", self.costo)
        
    def __str__(self):
        return "PostoStandard(" + str(self.get_numero()) + ", " + str(self.get_fila()) + ")"

#post3= PostoStandard(4,10,30)
#post3.prenota() 

class Teatro:
    
    def __init__(self):
        self._posti = []
    
    def aggiungi_posto(self):
        # Controlla le ripetizioni prima di aggiungere un nuovo posto
        scelta = int(input("1) Posto Vip 2) Posto Standard: "))
        num = int(input("Numero posto: "))
        fil = int(input("Numero fila: "))

        for p in self._posti:
            if p.get_numero() == num and p.get_fila() == fil:
                print("Posto già presente")

        if scelta == 1:
            pv = PostoVIP(num, fil, False)
            self._posti.append(pv)
        elif scelta == 2:
            costo = int(input("Costo: "))
            st = PostoStandard(num, fil, costo, False)
            self._posti.append(st)

    # #NON FUNZIONA
    # def aggiungi_posto(self):
    # # non sto usando posto!!!!!
    # # controlla le ripetizioni
    #     scelta = int(input("1) Posto Vip 2)  Posto Standard"))
    #     if scelta == 1:
    #         num  = int(input("Numero posto: "))
    #         fil = int(input("Numero fila: "))
            
    #         pv = PostoVIP(num, fil, False)
    #         print(self._posti)
    #         if pv in self._posti:   #occhio non funziona perchè pv mi dà la posizione dell'oggetto!!!! funziona così per valori base
    #             print("Posto già presente")
    #         else:
    #             self._posti.append(pv)
                
            
    #     elif scelta == 2:
    #         num  = int(input("Numero posto: "))
    #         fil = int(input("Numero fila: "))
    #         costo = int(input("Costo: "))
    #         st = PostoStandard(num, fil, costo, False)
    #         if st not in self._posti:
    #             self._posti.append(st)
    #         else:
    #             print("Posto già presente")
    

    def prenota_posto(self, numero,fila):
         #controlla che non sia gia prenotato
        for x in self._posti:
            if numero == x.get_numero() and fila ==x.get_fila():
                x.prenota()
            elif x.get_occupato() == False:
                print("Posto occupato")
            else:
                print("Errore posto e fila")
    
    
    def stampa_posti_occupati(self):
        for x in self._posti:
            if x.get_occupato() == True:
                print(x)

    
 


t1=Teatro()
t1.aggiungi_posto()
t1.aggiungi_posto()

t1.prenota_posto(3,4)
t1.stampa_posti_occupati()
#t1.stampa_posti_occupati()




