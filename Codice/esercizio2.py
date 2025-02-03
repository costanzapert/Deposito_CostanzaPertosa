class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
        print("Il libro è: ", self.titolo, ", è stato scritto da: ", self.autore, "ed ha", self.pagine, "pagine")

libro1 = Libro("L'ombra del vento", "Zafon" ,300)
libro1.descrizione()     


    