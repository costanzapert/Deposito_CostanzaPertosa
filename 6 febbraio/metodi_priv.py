class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
        
    def __metodo_privato(self):
        return "Questo è un metodo privato"
    
    def stampa(self):
        print(self.__metodo_privato())
            
obj = MiaClasse()
obj.stampa()
#print(obj._MiaClasse__variabile_privata)