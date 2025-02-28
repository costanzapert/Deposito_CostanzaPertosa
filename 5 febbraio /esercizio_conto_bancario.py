class ContoBancario:
    def __init__(self, tit , sal ):
        self.__titolare = tit 
        self.__saldo = sal
        
    def get_sal(self):
        return self.__saldo 
    
    def set_sal(self, sal2):
        self.__saldo = sal2

    def get_titolare(self):
        if self.__titolare!= "":
            return self.__titolare
        else: 
            print("Errore")
    
    def set_tit(self, tit2):
        self.__titolare = tit2


        
#c1= ContoBancario("c", 12)
#print(c1.__titolare)

    def deposita(self , importo):
        if importo>0:
            return self.__saldo + importo
        else: 
            print("Metti importo positivo")
    
#c1= ContoBancario("c", 12)
#print(c1.deposita(10))
      
    def preleva(self , importo):
        if importo > 0 and self.__saldo >= importo:
            self.__saldo = self.__saldo - importo
        else:
            print("Errore: Metti importo positivo oppure importo troppo grande")

    def visualizza_saldo(self):
        return self.get_sal()


#c1= ContoBancario("c", 12)
#print(c1.visualizza_saldo())

