class Persona:
    def __init__(self, nome, età):
        self.__nome = nome
        self.__età = età
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome
        
    def get_età(self):
        return self.__età
    
    def set_nome(self, nuovo_età):
        self.__età = nuovo_età
        
    def presentazione(self):
        print("Il mio nome è", self.get_nome(), "la mia età",self.get_età() )

#pers1 = Persona("Gian", 20)    
#pers1.presentazione() 

class Studente(Persona):
    def __init__(self, nome, età, voti):
        super().__init__(nome, età)
        self.__voti = voti
        
    def get_voti(self):
        return self.__voti
    
    def set_voti(self, nuovi_voti):
        self.__voti = nuovi_voti
    
    def __calcola_media(self):
        somma=0
        for x in self.get_voti():
            somma += x
        return  somma/len(self.get_voti())
    
    def get_calcola_media(self):
        return self.__calcola_media()
    
#stud1= Studente("Andrea", 30, [5,10,2])
#print(stud1.get_calcola_media())

    def presentazione(self):
        print("Il mio nome è", self.get_nome(), "la mia età",self.get_età(), "e la mia media voti è", self.get_calcola_media())

#stud1= Studente("Andrea", 27, [5,10,2])
#stud1.presentazione()


class Professore(Persona):
    def __init__(self, nome, età, materia):
        super().__init__(nome, età)
        self.materia = materia
    
    def presentazione(self):
        #super().presentazione()
        #print("la materia che insegno è", self.materia)
        print("Il mio nome è", self.get_nome(), "la mia età",self.get_età(), "la materia che insegno è", self.materia)

   
#prof1 = Professore("Mirko", 30, "informatica" )
#prof1.presentazione()


class Scuola:
    lista_studenti=[]
    lista_professori = []
    def __init__(self, nome):
        self.nome = nome
        self.lista_studenti=[]
        self.lista_professori = []
    
    def stampa(self):
        print("Il nome della scuola è ", self.nome) 
        print("gli studenti sono:")
        for x in self.lista_studenti:
            x.presentazione()
        print("i professori sono:")
        for x in self.lista_professori:
            x.presentazione()
    
scuola1= Scuola("De rogatis")

                    
    
while True:    
        scelta = int(input( "Digita 1 se vuoi aggiungere uno studente, 2 se professore, 3 se non vuoi aggiungere nulla"))
        if scelta ==1:
            nome = input("Nome: ")
            età = int(input("Età: "))
            numero_voti = int(input("Quanti voti ha lo studente? "))
            voti= []
            for x in range(0,numero_voti, 1):
                voto_singolo=int(input("voto_singolo: "))
                voti.append(voto_singolo)           
            #print(voti)
            stud1 = Studente (nome, età, voti)
            #stud1.presentazione()
            scuola1.lista_studenti.append(stud1)
            
            
        if scelta ==2:
            nome = input("Nome: ")
            età = int(input("Età: "))
            materia = input("Materia: ")
            prof1 = Professore(nome,età,materia)
            scuola1.lista_professori.append(prof1)
            #prof1.presentazione()
        
        if scelta ==3:
            break
    
    

scuola1.stampa()

