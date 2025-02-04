class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
    
#casco1 = Prodotto( "casco", 12, 20)
#print(casco1.calcola_profitto())

class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

#cellulare1 = Elettronica( "cellulare", 70, 200, 1)
#print(cellulare1.calcola_profitto())

class Abbigliamento: 
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

#gonna1 = Abbigliamento("gonna", 3, 40, "jeans")
#print(gonna1.calcola_profitto())

class Fabbrica:
    inventario = {}
    lista_prod_generico= []
    lista_prod_elettrinica = []
    lista_prod_abbigliamento = []
    
    
    def descrizione(self):
        print()
    
        
    
    def aggiungi_prodotto_gen(self):
        nome = input("dammi il nome del prodotto: ")
        prezzo_v = int(input("dammi il prezzo di vendita del prodotto: "))
        prezzo_p = int(input("dammi il prezzo di produzione del prodotto: "))
        gen1 = Prodotto( nome, prezzo_v, prezzo_p)
        self.lista_prod_generico.append(gen1)
        self.inventario["prod_gen"] = self.lista_prod_generico  
        
    
    def aggiungi_prodotto_ele(self):
        nome = input("dammi il nome del prodotto: ")
        prezzo_v = int(input("dammi il prezzo di vendita del prodotto: "))
        prezzo_p = int(input("dammi il prezzo di produzione del prodotto: "))
        garanzia = input("dammi la garanzia del prodotto: ")
        gen1 = Elettronica( nome, prezzo_v, prezzo_p, garanzia)
        self.lista_prod_elettrinica.append(gen1)
        self.inventario["prod_ele"] = self.lista_prod_generico  
    
    def aggiungi_prodotto_ele(self):
        nome = input("dammi il nome del prodotto: ")
        prezzo_v = int(input("dammi il prezzo di vendita del prodotto: "))
        prezzo_p = int(input("dammi il prezzo di produzione del prodotto: "))
        materiale = input("dammi il materiale del prodotto: ")
        gen1 = Abbigliamento( nome, prezzo_v, prezzo_p, materiale)
        self.lista_prod_generico.append(gen1)
        self.inventario["prod_abb"] = self.lista_prod_generico  
    
    def vendi_prodotto_gen(self):
        scelta = int(input( "Dimmi di che tipo di prodotto è: 1) Prodotto gen 2) Elettronica 3) Abbigliamento: "))
        if scelta == 1 :
            nome = input("dammi il nome dell' oggetto: ")
            for x in self.lista_prod_generico:
                if x == nome:
                    self.lista_prod_generico.remove(x)
                    
                
        if scelta == 2 :
            nome = input("dammi il nome dell' oggetto: ")
            for x in self.lista_prod_elettrinica:
                if x == nome:
                    self.lista_prod_generico.remove(x)
                    
        if scelta == 3 :
            nome = input("dammi il nome dell' oggetto: ")
            for x in self.lista_prod_abbigliamento:
                if x == nome:
                    self.lista_prod_generico.remove(x)
           
        
                
# Nel tempo a disposizione uletriore ho preferito non continuare questo, ma rivedere quello fatto da Mirko
    

    
    
        
#fabb1 = Fabbrica()
#fabb1.aggiungi_prodotto_ele()
         
        

        
        
    