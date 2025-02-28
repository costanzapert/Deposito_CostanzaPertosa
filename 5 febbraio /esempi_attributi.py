class Persona:
    __nome = "Mirko"
    _cognome = "Campari"

    def get_nome(self):
        return self.__nome
    def set_nome(self, n):
        self.__nome = n 
    
mirko1 = Persona()
#print(mirko1.__nome)    
#print(mirko1._cognome)    
print(mirko1.get_nome())
mirko1.set_nome("Paolo")
print(mirko1.get_nome())


