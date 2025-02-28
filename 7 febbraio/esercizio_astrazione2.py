from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self,nome, cognome, stipendio_b):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_b = stipendio_b

    @abstractmethod
    def calcola_stipendio(self):
        pass
    

class ImpiegatoFisso(Impiegato):
    def __init__(self, nome, cognome, stipendio_b):
        super().__init__(nome, cognome, stipendio_b)
    
    def calcola_stipendio(self):
        return self.stipendio_b

class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_b, vendite):
        super().__init__(nome, cognome, stipendio_b)
        self.vendite = vendite
    
    def calcola_stipendio(self):
        return self.stipendio_b + self.vendite * 0.1
    
    
def info(impiegat):
    if type(impiegat) == ImpiegatoFisso:
        print("Impiegato Fisso",impiegat.nome,impiegat.cognome, "stipendio: " ,impiegat.calcola_stipendio())
        
    elif type(impiegat) == ImpiegatoAProvvigione:
        print("Impiegato A Provvigione", impiegat.nome,impiegat.cognome , "stipendio: " ,impiegat.calcola_stipendio())
        
i1=ImpiegatoFisso("andrea", "L", 100)
info(i1)
i2=ImpiegatoAProvvigione("marco", "M", 100, 20)
info(i2)

