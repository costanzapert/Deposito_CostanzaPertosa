# class Libro:
#     def __init__(self, titolo, autore, pagine):
#         self.titolo = titolo
#         self.autore = autore
#         self.pagine = pagine
    
#     def descrizione(self):
#         print("Il libro è: ", self.titolo, ", è stato scritto da: ", self.autore, "ed ha", self.pagine, "pagine")

# libro1 = Libro("L'ombra del vento", "Zafon" ,300)
# libro1.descrizione()     


class Libro:
    autore = ""
    numero_pag=0
    titolo=""
    
    def __init__(self, autore, numero_pag, titolo):
        self.autore = autore
        self.numero_pag=numero_pag
        self.titolo = titolo
        
    def stampa_dati(self):
        print(
            self.autore, self.numero_pag, self.titolo
        )
        

class Biblioteca:
    
    lista_libri=[]
    
    def crea_libro(self):
        
        autore = input("autore:")
        numero_pag = int(input("nr pag"))
        titolo = input("titolo")
        
        aggiunta = Libro(autore,numero_pag,titolo) #parametri 
        self.lista_libri.append(aggiunta)
        
    def stampa_libro(self):
        for x in self.lista_libri:
            x.stampa_dati()


biblio = Biblioteca()

while True:
    
    biblio.crea_libro()
    biblio.stampa_libro()
    
    scelta = input("vuoi continuare? si/no")
    if scelta=="no":
        break