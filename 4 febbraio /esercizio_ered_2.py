class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self. eta = eta
    
    def fai_suono(self):
        print("L'animale fa il suono generico")
        

class Leone(Animale):
    colore = "marrone"
    def fai_suono(self):
        print("arg")
    def caccia(self):
        print("Il leone caccia puntando la preda da lontano")

class Giraffa(Animale):
    colore = "giallo"
    def fai_suono(self):
        print("ccab")
    def numero_zampe(self):
        print("Ha quattro zampe") 


class Pinguino(Animale):
    colore = "bianco e nero"
    def fai_suono(self):
        print("abbb")
    def numero_occhi(self):
        print("Ha due occhi")


ping1=Pinguino("ale", 12)
ping1.numero_occhi()
print(ping1.colore)

gir1= Giraffa("girella", 3)
gir1.numero_zampe()
print(gir1.colore)

leo1 = Leone("liam", 5)
print(leo1.colore)
leo1.caccia()




    


        