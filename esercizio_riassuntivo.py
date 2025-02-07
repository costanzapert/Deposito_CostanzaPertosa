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

#post2= PostoVIP(4,10)
#post2.prenota()       
#print(post2.servizi_extra)
        
class PostoStandard:
    def __init__(self, numero, fila, costo, occupato = False ):
        super().__init__(self, numero, fila, occupato = False )
        self.costo = costo
        
    def prenota(self):
        