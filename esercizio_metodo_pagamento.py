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

p1 = GestorePagamento
p1.metodo_pagamento() 
   
    