class MetodoPagamento:
    def effettua_pagamento(self,importo):
        print("Hai effettiato il pagamento del seguente importo", importo)

class C(MetodoPagamento):
    def effettua_pagamento(self,importo):
            print("Hai effettiato tramite la carta di credito il pagamento del seguente importo: ", importo)
        
#c1=CartaDiCredito()
#c1.effettua_pagamento(5)

class PayPal(MetodoPagamento):
    def effettua_pagamento(self,importo):
        print("Hai effettiato tramite PayPal il pagamento del seguente importo: ", importo)

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self,importo):
        print("Hai effettiato tramite bonifico barncario il pagamento del seguente importo: ", importo)


class GestorePagamento:
    def metodo_pagamento():
        importo = int(input("importo: "))
        scelta = int(input("1. CartaDiCredito 2. PayPal 3.BonificoBancario: "))
        if scelta ==1:
            g1=BonificoBancario()
        elif scelta ==2:
            g1 = PayPal()
        elif scelta ==3:
            g1 = BonificoBancario()
        else:
            print("Errore selezione")
            
        g1.effettua_pagamento(importo)

#p1 = GestorePagamento
#p1.metodo_pagamento() 
   
#Crea l'oggetto banca che accetti un conto e un utente e dopo il controllo delle credenziali gli di accesso alle funzioni del conto
class Banca:
    def __init__(self, conto, utente,  password):
        self.conto = conto
        self.utente = utente
        self.__password = password
    
    def login(self, uten1, pass1):
        if uten1 == self.utente and pass1 ==  self.__password:
            g1=GestorePagamento
            g1.metodo_pagamento() 
        else:
            print("Errore login")
            
#b1= Banca(123, "Gino", "abc")
#b1.login("Gino", "abc")

b2= Banca(123, "Gino", "abc")
b2.login("Gino", "acb")




###### DI MIRKO
# class gestore:
# def pagamento(self, metodo_di_pagamento):
# imp = int(input("€"))
# metodo_di_pagamento.effetua_pagamento(imp)

# @staticMethod
# def pagamento2(self, metodo_di_pagamento):
# imp = int(input("€"))
# metodo_di_pagamento.effetua_pagamento(imp)

# metodo = carta_di_credito()
# gest = gestore()
# gest.pagamento(metodo)
# gestore.pagamento2(metodo)